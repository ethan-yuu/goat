from turtle import *


# 绘制正方形
def draw_square(size):
    # 设置笔刷宽度
    width(4)

    # 前进 右转 笔刷颜色默认为黑色
    forward(size)
    right(90)

    pencolor('red')
    forward(size)
    right(90)

    pencolor('blue')
    forward(size)
    right(90)

    pencolor('green')
    forward(size)
    right(90)

    # 调用done() 使得窗口等待关闭，否则将立即关闭窗口
    done()


def draw_star(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading; 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)
    done()


if __name__ == '__main__':
    # 绘制正方形
    # draw_square(400)
    # 绘制五角星
    draw_star(0, 50)
