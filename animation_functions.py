import pygame
import sys
import math
import time
import random

from Vector import Vector


def random_color(min_color=1, max_color=190):
    return (random.randint(min_color, max_color),
            random.randint(min_color, max_color),
            random.randint(min_color, max_color))


def move_around(min_number=0, max_number=100, step=1.0, number=0):
    if min_number <= number + step <= max_number:
        return number + step
    elif min_number > number + step:
        return min_number
    elif max_number < number + step:
        return max_number


def return_electric_force(pos1, pos2, q1, q2):
    distance = return_distance(pos1, pos2)
    value = q1 * q2 / distance ** 2
    return return_direction(pos1, pos2) * value


def return_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 +
                     (pos1[1] - pos2[1]) ** 2)


def return_direction(pos1, pos2):
    return (pos1 - pos2) / return_distance(pos1, pos2)


def return_value(pos):
    return return_distance(pos, (0, 0))


def lighter_color(color, rate):
    white = Vector((255, 255, 255))
    opposite_color = white - Vector(color)
    new_opposite_color = opposite_color * rate
    new_color = white - new_opposite_color
    return (int(new_color[0]),
            int(new_color[1]),
            int(new_color[2])
            )


def in_the_rect(pos, max_width, max_height, min_width=0, min_height=0):
    if pos[0] < min_width:
        bool_x = -1
    elif pos[0] > max_width:
        bool_x = 1
    else:
        bool_x = 0
    if pos[1] < min_height:
        bool_y = -1
    elif pos[1] > max_height:
        bool_y = 1
    else:
        bool_y = 0

    return bool_x, bool_y


def animation(start_time, end_time, current_time,
              start, end):
    if current_time < start_time:
        return start
    elif current_time > end_time:
        return end
    to_one = (current_time - start_time) / (end_time - start_time)
    current = (start + end) / 2 + \
              (end - start) / 2 * \
              math.sin(3.1415 * to_one - 3.1415 / 2)
    return current


def move_animation(start_time, end_time, current_time,
                   start_pos, end_pos):
    x = animation(start_time, end_time, current_time,
                  start_pos[0], end_pos[0])
    y = animation(start_time, end_time, current_time,
                  start_pos[1], end_pos[1])
    return x, y


def arithmetic_progression(
        start_index, end_index, current_index,
        start, end):
    if current_index < start_index:
        return start
    elif current_index > end_index:
        return end
    current = start + (end - start) * \
              (current_index - start_index) / (end_index - start_index)
    return current


def resize_the_image(image, rate=(1, 1)):
    if rate == (1, 1):
        return image
    old_size = image.get_size()
    new_size = (old_size[0] * rate[0],
                old_size[1] * rate[1])
    return pygame.transform.scale(image, new_size)
