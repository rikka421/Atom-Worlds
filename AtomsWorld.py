from Settings import *
from Atom import Atom

from Vector import Vector
import pygame
import sys
import math
import time
import random


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('AtomsWorld!')

        self.settings = {'draw_line': False}

        self.dt = DELTA_TIME

        self.atoms = None
        # 对象初始化

        self.create_balls()

        self.draw_screen()

    def create_balls(self):
        # 对象初始化
        # self.atoms = ATOMS1
        # self.atoms = ATOMS2
        # self.atoms = ATOMS3
        self.atoms = ATOMS4

    def draw_screen(self):
        self.screen.fill(BACKGROUND)

        # self.draw_circles()

        for atom in self.atoms:
            atom.show(surface=self.screen, draw_line=self.settings['draw_line'])

        pygame.display.update()

    def run(self):
        while True:
            start = time.time()
            self.check_event()

            # 将小球的受力归零
            for atom in self.atoms:
                atom.force = Vector((0, 0))
            # 遍历小球, 计算受力
            for atom in self.atoms:
                for ano_atom in self.atoms:
                    if atom is not ano_atom:
                        atom.check_force(ano_atom)
            # 运动
            for atom in self.atoms:
                atom.check_velocity(self.dt)
                atom.move()
                atom.check_pump(PUMP)
            self.draw_screen()

            time.sleep(1 / FRAME_RATE)

    def check_event(self):
        # 按键检测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if self.settings['draw_line']:
                        self.settings['draw_line'] = False
                    else:
                        self.settings['draw_line'] = True


if __name__ == '__main__':
    game = Game()
    game.run()

