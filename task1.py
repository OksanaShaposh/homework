#############
# задание 1 #
#############

# напишите цикл, рисующий по
# вертикали фигуры (квадраты
# или другие из ссылки выше)

from drawbot_skia.drawbot import rect, saveImage, oval, newDrawing, line
y= 25
step= 100
for i in range(10):
    rect(500, y, 50, 50)
    y= y+step
saveImage("task-1.pdf")

#############
# задание 2 #
#############

# напишите вложенный (двойной)
# цикл, заполняющий холст фигурами
# полностью, по вертикали и
# горизонтали

newDrawing()
x = 0
y = 0
step = 100
for a in range(10):
    for b in range(10):
        rect(x, y, 50 , 50)
        y = y + step
    y = 0
    x = x + step
saveImage("task-2.pdf")