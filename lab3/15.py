from graph import *

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

c = canvas()

c.create_oval(200, 400, 300, 450, outline="black", fill="white")
c.create_oval(300-25, 370+25, 350-25, 400+25, outline="black", fill="white")
c.create_oval(300+15, 370+5, 350+20, 400+10+5, outline="black", fill="white")

run()
