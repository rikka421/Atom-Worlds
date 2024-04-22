import random

WHITE = (255, 255, 255)
ORANGE = (255, 120, 40)
GREY = (255, 245, 255)
DARK = (100, 100, 100)
LIGHT = (200, 200, 200)
GREEN = (180, 230, 30)
PINK = (255, 170, 200)
RED = (230, 30, 30)
BLUE = (100, 100, 180)
YELLOW = (255, 240, 0)
DEEP_DARK = (40, 40, 50)
BLACK = (0, 0, 0)
PURPLE = (160, 70, 160)

BACKGROUND = WHITE
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1400 // 16 * 9

# 是否有墙壁
PUMP = True
PUMP_RATE = 0.9

# 类似运行速度. 数字越大, 小球会动地越快
DELTA_TIME = 1
# 帧率 不建议改动
FRAME_RATE = 60

# 尾迹的长度
PATH_LENGTH = 70


from Atom import Atom
from Vector import Vector

# 一些预设的小球组合
# 对象初始化
q1 = 15
q2 = 20
q3 = 25
RADIUS = 100
distance = RADIUS * 2
ele_force = (q1 * q2) / distance ** 2
v = (ele_force * RADIUS) * 1

q1, q2, q3 = (q1 * 3, q2 * 3, q3 * 3)

ATOMS1 = [Atom(color=PURPLE,
                   electric_charge=q1, mass=q1,
                   velocity=Vector((0, -v)),
                   pos=Vector((SCREEN_WIDTH // 2 - RADIUS, SCREEN_HEIGHT // 2))),
              Atom(color=GREEN,
                   electric_charge=q1, mass=q1,
                   pos=Vector((SCREEN_WIDTH // 2 + RADIUS, SCREEN_HEIGHT // 2)),
                   velocity=Vector((0, v))),
              Atom(color=RED,
                   electric_charge=q2, mass=q2,
                   pos=Vector((SCREEN_WIDTH // 2 - RADIUS, SCREEN_HEIGHT // 2 - RADIUS)),
                   velocity=Vector((0, 0))),
              Atom(color=BLUE,
                   electric_charge=q3, mass=q3,
                   pos=Vector((SCREEN_WIDTH // 2 + RADIUS, SCREEN_HEIGHT // 2 + RADIUS)),
                   velocity=Vector((0, v))),
              Atom(color=PINK,
                   electric_charge=q3, mass=q3,
                   pos=Vector((SCREEN_WIDTH // 2 - RADIUS, SCREEN_HEIGHT // 2 - RADIUS * 2)),
                   velocity=Vector((0, v)))
              ]

ATOMS2 = [    Atom(color=GREEN,
                   electric_charge=q1, mass=q1,
                   pos=Vector((SCREEN_WIDTH // 2 + RADIUS, SCREEN_HEIGHT // 2)),
                   velocity=Vector((0, v))),
              Atom(color=RED,
                   electric_charge=q2, mass=q2,
                   pos=Vector((SCREEN_WIDTH // 2 - RADIUS, SCREEN_HEIGHT // 2 - RADIUS)),
                   velocity=Vector((0, 0))),
              Atom(color=BLUE,
                   electric_charge=q3, mass=q3,
                   pos=Vector((SCREEN_WIDTH // 2 + RADIUS, SCREEN_HEIGHT // 2 + RADIUS)),
                   velocity=Vector((0, v))),
              Atom(color=PINK,
                   electric_charge=q2, mass=q2,
                   pos=Vector((SCREEN_WIDTH // 2 - RADIUS, SCREEN_HEIGHT // 2 - RADIUS * 2)),
                   velocity=Vector((0, v)))
              ]

N = 5

ATOMS3 = [Atom(   color=(random.randint(10, 250), random.randint(10, 250), random.randint(10, 250)),
                   electric_charge=q2, mass=q2,
                   pos=Vector((SCREEN_WIDTH // 2 + SCREEN_HEIGHT // (N + 2) * (i + 1),
                               SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // (N + 2) * (j + 1))),
                   velocity=Vector((0, 0))) for i in range(- N // 2, N // 2) for j in range(-N // 2, N // 2)]

N = 2
ATOMS4 = [Atom(   color=(random.randint(10, 250), random.randint(10, 250), random.randint(10, 250)),
                   electric_charge=q2, mass=q2,
                   pos=Vector((SCREEN_WIDTH // 2 + SCREEN_HEIGHT // (N + 2) * (i + 1),
                               SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // (N + 2) * (j + 1))),
                   velocity=Vector((0, 0))) for i in range(- N // 2, N // 2) for j in range(-N // 2, N // 2)]
