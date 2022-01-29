def TurtleDraw() :
    # turtle.penup()
    turtle.goto(100, 100)
    turtle.goto(100, -100)
    turtle.goto(-100, -100)
    turtle.goto(-100, 100)
    turtle.goto(0, 0)

# 绘制一个心型
def TurTleDrawHeart() :
    turtle.penup()
    turtle.speed(6)
    turtle.goto(-30, 100)
    turtle.pendown()
    # 逆时针旋转90度
    turtle.left(90)
    # 画圆，半径为120， 弧度为180
    turtle.circle(120, 180)
    turtle.circle(360, 70)
    turtle.left(38)
    turtle.circle(360, 70)
    turtle.circle(120, 180)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

# 绘制一个太阳花
def TurtleDrawSunFlower() :
    turtle.color("red", "yellow")
    turtle.speed(10)
    turtle.begin_fill()
    for x in range(50) :
        turtle.forward(200)
        turtle.left(170)
    turtle.end_fill()

# 绘制一个六边形
def TurtleDrawHexagon(intpuPara) :
    turtle.bgcolor("black")
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    sides = int(intpuPara)
    colors = ["red", "yellow", "green", "blue", "orange", "purple"]
    for angle in range(120) :
        turtle.pencolor(colors[angle % 6])
        turtle.forward(angle * 3 / sides + angle)
        turtle.left(360 / sides + 1)
        turtle.width(int(angle * sides / 200))

# 弹出框的使用
def TurtleDrawBox() :
    # 设置画布大小及背景颜色
    turtle.screensize(800, 600, "black")
    studentName = turtle.textinput("pls input your name: ", "the name is :")
    myColor = ["green", "red", "blue", "yellow"]
    for x in range(20) :
        turtle.pencolor(myColor[x % 4])
        turtle.penup()
        turtle.forward(x * 4)
        turtle.down()
        # turtle.write(studentName, font = ('arial', 8, 'normal'))
        turtle.write(studentName, font=("Arial", int((x + 4) / 4), "bold"))
        turtle.left(93)

# 使用python语言做一段玫瑰花--begin
def TurtleDrawRose() :
    turtle.screensize(800, 600, "pink")
    turtle.clear()
    # writing txt
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(130, 50)
    # turtle.pendown()
    turtle.color("blue")
    turtle.write("Tabitha, I am preparing a gift for you ~~~", font=("Times", 18, "bold"))
    time.sleep(2)
    turtle.goto(180, 10)
    turtle.write("Now Begin", font=("Times", 18, "bold"))
    time.sleep(2)
    turtle.goto(200, -20)
    turtle.write("Ready?", font=("Times", 18, "bold"))
    time.sleep(2)
    turtle.goto(215, -50)
    turtle.write("go!", font=("Times", 18, "bold"))
    time.sleep(2)

    # turtle.end_fill()
    # 设置初始位置
    turtle.goto(0, 0)
    turtle.color("black")
    turtle.penup()
    turtle.left(90)
    turtle.forward(200)
    turtle.pendown()
    turtle.right(90)
    # 花蕊
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.circle(25, 110)
    turtle.left(50)
    turtle.circle(60, 45)
    turtle.circle(20, 170)
    turtle.right(24)
    turtle.forward(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.forward(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.forward(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.forward(45)
    turtle.right(165)
    turtle.forward(20)
    turtle.left(155)
    turtle.circle(150, 80)
    turtle.left(50)
    turtle.circle(150, 90)
    turtle.end_fill()
    # 花瓣1
    turtle.left(150)
    turtle.circle(-90, 70)
    turtle.left(20)
    turtle.circle(75, 105)
    turtle.setheading(60)
    turtle.circle(80, 98)
    turtle.circle(-90, 40)
    # 花瓣2
    turtle.left(180)
    turtle.circle(90, 40)
    turtle.circle(-80, 98)
    turtle.setheading(-83)
    # 叶子1
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()
    turtle.right(135)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(85)
    turtle.left(90)
    turtle.forward(80)
    # 叶子2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()
    turtle.left(135)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(60)
    turtle.right(90)
    turtle.circle(200, 60)
    time.sleep(2)
    turtle.penup()
    turtle.color("blue")
    turtle.goto(180, -100)
    turtle.write("~~~", font=("Times", 18, "bold"))
    time.sleep(20)
# 使用python语言做一段玫瑰花--end




# 该模块的main函数入口
def TurtleMain() :
    # TurtleDraw()
    # TurTleDrawHeart()
    # TurtleDrawSunFlower()
    # TurtleDrawHexagon(6)
    TurtleDrawBox()
    TurtleDrawRose()
