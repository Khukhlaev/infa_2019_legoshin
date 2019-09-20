from graph import *

penSize(1)
brushColor("yellow")
circle(250, 250, 200)
brushColor("red")
circle(250-75, 225, 40)
circle(250+75, 225, 25)
brushColor("black")
circle(250-75, 225, 17)
circle(250+75, 225, 17)
penSize(20)
moveTo(125, 225-70)
lineTo(250-75+50, 270-70)
moveTo(250+75-30, 270-60)
lineTo(250+75+30, 225-60)
moveTo(200, 360)
lineTo(300, 360)


run()
