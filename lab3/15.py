from graph import *


def fish(x, y): # FISH
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


windowSize(1000, 600)


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

def stupidbird(a, x, y):
    polyline([(x+53*a, y+93*a), (x+95*a, y+103*a), (x+121*a, y+124*a), (x+140*a, y+94*a), (x+196*a, y+91*a)])

penColor("White")
brushColor("White")
polyline([(53, 93), (95, 103), (121, 124), (140, 94), (196, 91)])
stupidbird(1.1, 250, 0)
stupidbird(0.9, 100, 100)

c = canvas()
penSize(1)

penColor("Black")
brushColor("White")

polygon([(213, 431), (176, 430), (139, 422), (159, 396), (176, 366), (192, 395), (223, 410)])
polygon([(262, 406), (258, 346), (246, 331), (200, 315), (151, 278), (154, 311), (176, 334), (229, 412)])
polygon([(249, 408), (245, 377), (230, 357), (171, 336), (143, 322), (126, 300), (130, 338), (151, 366), (213, 399), (222, 424)])

penSize(1)
penColor("Black")
brushColor("Orange")
polygon([(280+20, 507), (288+20, 498), (297+20, 495), (306+20, 498), (297+20, 499), (287+20, 505), (294+20, 504), (304+20, 506), (289+20, 510), (300+20, 512), (306+20, 517), (285+20, 513), (274+20, 518), (265+20, 532), (265+20, 516), (292, 509)])
brushColor("White")
polygon([(233+20, 480), (232+20, 488), (239+20, 497), (253+20, 507), (269+20, 512), (284+20, 512), (280+20, 503), (264+20, 492), (246+20, 484)])
brushColor("Orange")
polygon([(280, 507), (288, 498), (297, 495), (306, 498), (297, 499), (287, 505), (294, 504), (304, 506), (289, 510), (300, 512), (306, 517), (285, 513), (274, 518), (265, 532), (265, 516), (272, 509)])
brushColor("White")
polygon([(233, 480), (232, 488), (239, 497), (253, 507), (269, 512), (284, 512), (280, 503), (264, 492), (246, 484)])

c.create_oval(220+20, 485, 245+20, 440, outline="black", fill="white")
c.create_oval(220, 485, 245, 440, outline="black", fill="white")

penColor("black")
brushColor("Orange")
polygon([(357+5, 396+5), (357+5, 396), (375+10, 390),(398+10, 382+4), (398+20, 386+3), (406+18, 398+5)])
polygon([(365, 404), (382, 410), (407, 413), (423, 405), (426, 396), (399, 399), (368, 398)])
c.create_oval(200, 400, 300, 450, outline="black", fill="white")
c.create_oval(300-25, 370+25, 350-25, 400+25, outline="black", fill="white")
c.create_oval(300+15, 370+5, 350+20, 400+10+5, outline="black", fill="white")
c.create_oval(350, 385, 355, 390, outline="black", fill="black")



fish(350, 550)

run()
