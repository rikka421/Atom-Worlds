from Settings import *
from animation_functions import *

from Vector import Vector

import pygame


class Atom:
    def __init__(self, name=None,
                 pos=Vector((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)),
                 velocity=Vector((0, 0)), force=Vector((0, 0)),
                 mass=1, electric_charge=1, color=None):
        self.name = name
        self.pos = pos
        self.color = color
        self.mass = mass
        self.radius = self.mass // 5
        self.velocity = velocity
        self.force = force
        self.electric_charge = electric_charge
        if color is None:
            self.color = random_color()
        else:
            self.color = color

        self.path_max_length = PATH_LENGTH
        self.path = [self.pos] * self.path_max_length

    def check_force(self, other):
        new_pos = Vector(other.pos.content)
        in_rect = in_the_rect(other.pos,
                              self.pos[0] + SCREEN_WIDTH // 2,
                              self.pos[1] + SCREEN_HEIGHT // 2,
                              self.pos[0] - SCREEN_WIDTH // 2,
                              self.pos[1] - SCREEN_HEIGHT // 2
                              )

        if not PUMP:
            if in_rect[0] == 1:
                new_pos[0] -= SCREEN_WIDTH
            elif in_rect[0] == -1:
                new_pos[0] += SCREEN_WIDTH
            else:
                pass
            if in_rect[1] == 1:
                new_pos[1] -= SCREEN_HEIGHT
            elif in_rect[1] == -1:
                new_pos[1] += SCREEN_HEIGHT
            else:
                pass

        distance = return_distance(self.pos, new_pos)
        if distance > 0.1:
            other.force += return_electric_force(self.pos, new_pos,
                                                 self.electric_charge, other.electric_charge)

    def check_velocity(self, dt):
        result = self.force * dt
        value = return_distance(result, Vector((0, 0)))
        if value < 1:
            self.velocity += result
        else:
            self.velocity += result / value

    def check_pump(self, pump=False):
        bool_x, bool_y = in_the_rect(self.pos, SCREEN_WIDTH, SCREEN_HEIGHT)
        if pump:
            if bool_x * self.velocity.content[0] > 0:
                self.velocity = Vector((-self.velocity[0] * PUMP_RATE, self.velocity[1] * PUMP_RATE))
            if bool_y * self.velocity.content[1] > 0:
                self.velocity = Vector((self.velocity[0] * PUMP_RATE, -self.velocity[1] * PUMP_RATE))
        else:
            if bool_x == 1:
                self.pos[0] -= SCREEN_WIDTH
            elif bool_x == -1:
                self.pos[0] += SCREEN_WIDTH
            if bool_y == 1:
                self.pos[1] -= SCREEN_HEIGHT
            elif bool_y == -1:
                self.pos[1] += SCREEN_HEIGHT

    def move(self):
        self.pos += self.velocity
        if len(self.path) >= self.path_max_length:
            self.path.pop(0)
        pos = Vector(self.pos.content)
        self.path.append(pos)

    def show(self, surface, draw_line=False, draw_path=True):
        if self.pos[0] > SCREEN_WIDTH or self.pos[0] < 0 \
                or self.pos[1] > SCREEN_HEIGHT or self.pos[1] < 0:
            return
        surface.lock()
        # 画本体
        pygame.draw.circle(surface, self.color, self.pos.content, self.radius)

        if draw_line:
            # 画受力
            max_force_length = 50
            rate = 100
            if return_value(self.force * rate) < max_force_length:
                pygame.draw.aaline(surface, BLACK, self.pos.content, (self.pos + self.force * rate).content)
            else:
                pygame.draw.aaline(surface, BLACK, self.pos.content,
                                 (self.pos + self.force / return_value(self.force) * max_force_length).content)

            # 画速度
            pygame.draw.line(surface, RED, self.pos.content, (self.pos + self.velocity * 20).content)

        if draw_path:
            # 画轨迹
            for index in range(len(self.path) - 1):
                seen_rate = 0.9
                rate = index / self.path_max_length * seen_rate + (1 - seen_rate)
                new_color = lighter_color(self.color, rate)
                if in_the_rect(self.path[index], SCREEN_WIDTH, SCREEN_HEIGHT) == (0, 0):
                    pygame.draw.line(surface, new_color,
                                       self.path[index].content, self.path[index + 1].content,
                                     width=self.radius // 4)
        surface.unlock()

    def __str__(self):
        return str(("name", str(self.name),
                    "pos:", str(self.pos),
                    "force:", str(self.force),
                    "velocity:", str(self.velocity)
                    ))
