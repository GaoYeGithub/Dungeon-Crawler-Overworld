import turtle

myarr = []
turtle.hideturtle()

f = open("map.txt", "r")

while True:
    tempLine = f.readline()
    if tempLine == "":
        break
    temparr = []
    for t in tempLine:
        temparr.append(t)
    myarr.append(temparr)

f.close()

num_rows = len(myarr)
num_cols = len(myarr[0])

while True:
    try:
        row = int(input("Starting Row: "))
        col = int(input("Starting Column: "))
        if 0 <= row < num_rows and 0 <= col < num_cols and myarr[row][col] == "0":
            myarr[row][col] = "1"
            break
        else:
            print("Invalid starting position. Please choose an empty cell marked with '0'.")
    except ValueError:
        print("Please enter valid integers for row and column.")

side = 20

screen_width = num_cols * side
screen_height = num_rows * side

turtle.screensize(screen_width, screen_height)
turtle.setup(width=screen_width + 50, height=screen_height + 50)

def drawSquare(x, y, side, color):
    turtle.up()
    turtle.goto(x, y)
    if color != "none":
        turtle.color(color)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(side)
            turtle.right(90)
        turtle.end_fill()

def drawTurtle(x, y, side, color):
    turtle.up()
    turtle.goto(x, y)
    if color != "none":
        turtle.shape("turtle")
        turtle.color(color)
        turtle.stamp()

def drawMap():
    x = -screen_width / 2
    y = screen_height / 2
    originalX = x
    turtle.tracer(0, 0)
    for arr in myarr:
        for value in arr:
            if value == "0":
                drawSquare(x, y, side, "green")
            elif value == "1":
                drawTurtle(x, y, side, "yellow")
            elif value == "2":
                drawSquare(x, y, side, "red")
            elif value == "3":
                drawSquare(x, y, side, "blue")
            elif value == "4":
                drawSquare(x, y, side, "yellow")
            elif value == "5":
                drawSquare(x, y, side, "orange")
            elif value == "\n":
                drawSquare(x, y, side, "none")
            else:
                drawSquare(x, y, side, "black")
            x += side
        y -= side
        x = originalX
    turtle.update()

drawMap()

def up():
    global myarr, row, col
    if row > 0 and myarr[row-1][col] == "0":
        myarr[row][col] = "0"
        row -= 1
        myarr[row][col] = "1"
        drawMap()

def down():
    global myarr, row, col
    if row < num_rows - 1 and myarr[row+1][col] == "0":
        myarr[row][col] = "0"
        row += 1
        myarr[row][col] = "1"
        drawMap()

def left():
    global myarr, row, col
    if col > 0 and myarr[row][col-1] == "0":
        myarr[row][col] = "0"
        col -= 1
        myarr[row][col] = "1"
        drawMap()

def right():
    global myarr, row, col
    if col < num_cols - 1 and myarr[row][col+1] == "0":
        myarr[row][col] = "0"
        col += 1
        myarr[row][col] = "1"
        drawMap()

turtle.onkey(up, "w")
turtle.onkey(left, "a")
turtle.onkey(right, "d")
turtle.onkey(down, "s")

turtle.listen()
turtle.mainloop()
