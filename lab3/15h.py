# coding=utf-8
from graph import *
import math as m


def wannadie(a, b, x, y):
    '''рисует лебедя'''
    penSize(1)

    penColor("Black")
    brushColor("White")

    polygon([(x + a * b * 213, y + a * 431), (x + a * b * 176, y + a * 430), (x + a * b * 139, y + a * 422),
             (x + a * b * 159, y + a * 396), (x + a * b * 176, y + a * 366), (x + a * b * 192, y + a * 395),
             (x + a * b * 223, y + a * 410)])
    polygon([(x + a * b * 262, y + a * 406), (x + a * b * 258, y + a * 346), (x + a * b * 246, y + a * 331),
             (x + a * b * 200, y + a * 315), (x + a * b * 151, y + a * 278), (x + a * b * 154, y + a * 311),
             (x + a * b * 176, y + a * 334), (x + a * b * 229, y + a * 412)])
    polygon([(x + a * b * 249, y + a * 408), (x + a * b * 245, y + a * 377), (x + a * b * 230, y + a * 357),
             (x + a * b * 171, y + a * 336), (x + a * b * 143, y + a * 322), (x + a * b * 126, y + a * 300),
             (x + a * b * 130, y + a * 338), (x + a * b * 151, y + a * 366), (x + a * b * 213, y + a * 399),
             (x + a * b * 222, y + a * 424)])

    penSize(1)
    penColor("Black")
    brushColor("Orange")
    polygon([(x + a * b * (280 + 20), y + a * 507), (x + a * b * (288 + 20), y + a * 498),
             (x + a * b * (297 + 20), y + a * 495), (x + a * b * (306 + 20), y + a * 498),
             (x + a * b * (297 + 20), y + a * 499), (x + a * b * (287 + 20), y + a * 505),
             (x + a * b * (294 + 20), y + a * 504), (x + a * b * (304 + 20), y + a * 506),
             (x + a * b * (289 + 20), y + a * 510), (x + a * b * (300 + 20), y + a * 512),
             (x + a * b * (306 + 20), y + a * 517), (x + a * b * (285 + 20), y + a * 513),
             (x + a * b * (274 + 20), y + a * 518), (x + a * b * (265 + 20), y + a * 532),
             (x + a * b * (265 + 20), y + a * 516), (x + a * b * (292), y + a * 509)])
    brushColor("White")
    polygon([(x + a * b * (233 + 20), y + a * 480), (x + a * b * (232 + 20), y + a * 488),
             (x + a * b * (239 + 20), y + a * 497), (x + a * b * (253 + 20), y + a * 507),
             (x + a * b * (269 + 20), y + a * 512), (x + a * b * (284 + 20), y + a * 512),
             (x + a * b * (280 + 20), y + a * 503), (x + a * b * (264 + 20), y + a * 492),
             (x + a * b * (246 + 20), y + a * 484)])
    brushColor("Orange")
    polygon([(x + a * b * (280), y + a * 507), (x + a * b * (288), y + a * 498), (x + a * b * (297), y + a * 495),
             (x + a * b * (306), y + a * 498), (x + a * b * (297), y + a * 499), (x + a * b * (287), y + a * 505),
             (x + a * b * 294, y + a * 504), (x + a * b * 304, y + a * 506), (x + a * b * 289, y + a * 510),
             (x + a * b * 300, y + a * 512), (x + a * b * 306, y + a * 517), (x + a * b * 285, y + a * 513),
             (x + a * b * 274, y + a * 518), (x + a * b * 265, y + a * 532), (x + a * b * 265, y + a * 516),
             (x + a * b * 272, y + a * 509)])
    brushColor("White")
    polygon([(x + a * b * 233, y + a * 480), (x + a * b * 232, y + a * 488), (x + a * b * 239, y + a * 497),
             (x + a * b * 253, y + a * 507), (x + a * b * 269, y + a * 512), (x + a * b * 284, y + a * 512),
             (x + a * b * 280, y + a * 503), (x + a * b * 264, y + a * 492), (x + a * b * 246, y + a * 484)])

    c.create_oval(x + a * b * (220 + 20), y + a * 485, x + a * b * (245 + 20), y + a * 440, outline="black",
                  fill="white")
    c.create_oval(x + a * b * 220, y + a * 485, x + a * b * 245, y + a * 440, outline="black", fill="white")

    penColor("black")
    brushColor("Orange")
    polygon([(x + a * b * (357 + 5), y + a * (396 + 5)), (x + a * b * (357 + 5), y + a * 396),
             (x + a * b * (375 + 10), y + a * 390), (x + a * b * (398 + 10), y + a * (382 + 4)),
             (x + a * b * (398 + 20), y + a * (386 + 3)), (x + a * b * (406 + 18), y + a * (398 + 5))])
    polygon([(x + a * b * 365, y + a * 404), (x + a * b * 382, y + a * 410), (x + a * b * 407, y + a * 413),
             (x + a * b * 423, y + a * 405), (x + a * b * 426, y + a * 396), (x + a * b * 399, y + a * 399),
             (x + a * b * 368, y + a * 398)])
    c.create_oval(x + a * b * 200, y + a * 400, x + a * b * 300, y + a * 450, outline="black", fill="white")
    c.create_oval(x + a * b * (300 - 25), y + a * (370 + 25), x + a * b * (350 - 25), y + a * (400 + 25),
                  outline="black", fill="white")
    c.create_oval(x + a * b * (300 + 15), y + a * (370 + 5), x + a * b * (350 + 20), y + a * (400 + 10 + 5),
                  outline="black", fill="white")
    c.create_oval(x + a * b * 350, y + a * 385, x + a * b * 355, y + a * 390, outline="black", fill="black")


def fish(x, y):  # FISH
    brushColor('#ADADC7')
    polygon([(x, y), (x + 30, y - 10), (x, y - 20)])
    c.create_oval(x + 30, y, x + 100, y - 20, fill='#ADADC7', outline='black')
    brushColor("#1E90FF")
    circle(x + 80, y - 10, 5)
    brushColor('black')
    circle(x + 80, y - 10, 2)
    brushColor('white')
    circle(x + 78, y - 12, 2)
    # верхний плавник
    brushColor('#CD5C5C')
    polygon([(x + 80, y - 19), (x + 82, y - 27), (x + 55, y - 29), (x + 65, y - 20)])
    # нижний правый плавник
    polygon([(x + 80, y - 1), (x + 82, y + 8), (x + 69, y + 8), (x + 70, y)])
    # нижний левый плавник
    polygon([(x + 50, y - 1), (x + 49, y + 8), (x + 35, y + 8), (x + 40, y - 2)])


def mew_bird(size, x, y, pensize):
    """x, y - координаты центральной точки чайки, size - радиус кривизны крыла"""
    penSize(pensize)
    for j in range(2):
        wingX = []
        wingX.append(x)
        wingY = []
        wingY.append(y)
        phi = m.pi / 4
        for i in range(1, 3600 // 4, 1):
            # окружность можно представить как правильный многоугольник, здесь мы будем рисовать четверть окружности
            if j == 0:
                wingX.append(wingX[i - 1] - size * m.sin(2 * m.pi / 1800) * m.sin(phi))
            else:
                wingX.append(wingX[i - 1] + size * m.sin(2 * m.pi / 1800) * m.sin(phi))
            wingY.append(wingY[i - 1] - size * m.sin(2 * m.pi / 1800) * m.cos(phi))
            phi += m.pi / 1800
        points = [(k, m) for k, m in zip(wingX, wingY)]
        polyline(points)

windowSize(1000, 600)
canvasSize(1000, 600)
penColor("black")

penSize(100)

penColor(0, 0, 70)
moveTo(0, 50)
lineTo(550, 50)

penSize(60)

penColor(150, 50, 255)
moveTo(0, 130)
lineTo(550, 130)

penSize(80)

penColor(200, 150, 200)
moveTo(0, 190)
lineTo(550, 190)

penSize(100)

penColor(255, 150, 200)
moveTo(0, 280)
lineTo(550, 280)

penSize(60)

penColor(255, 175, 100)
moveTo(0, 310)
lineTo(550, 310)

penSize(950)

penColor(0, 100, 100)
moveTo(0, 810)
lineTo(550, 810)

penSize(5)

penColor("White")
brushColor("White")

mew_bird(30, 100, 100, 5)
mew_bird(10, 200, 200, 1)
mew_bird(10, 300, 300, 1)
mew_bird(30, 150, 150, 3)
mew_bird(15, 50, 20, 2)
mew_bird(5, 124, 140, 1)
mew_bird(5, 178, 120, 1)
mew_bird(5, 500, 200, 1)
mew_bird(5, 400, 200, 1)
mew_bird(10, 350, 100, 2)
mew_bird(20, 290, 300, 6)
mew_bird(5, 470, 250, 1)
mew_bird(20, 500, 90, 7)

c = canvas()
penSize(1)

wannadie(0.5, 1, -70, 70)
wannadie(0.7, -1, 650, 20)
wannadie(1, 1, 0, 35)

fish(350, 550)
fish(200, 600)
fish(100, 500)

run()
