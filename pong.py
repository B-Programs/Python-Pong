import turtle

win = turtle.Screen()
win.title("Pong by B-Programs")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=1, stretch_len=1) 
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)

# Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")

win.onkeypress(paddle_b_up, "p")
win.onkeypress(paddle_b_down, "l")

#Main Game Loop
while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
   
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
   
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        score_a += 1
        print('>>> Player A has scored', '\n')
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        score_b += 1
        print('>>> Player B has Scored', '\n')
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    newscorea = str(score_a)
    newscoreb = str(score_b)

    with open('recent-scores.txt', 'w') as f:
        f.write('Score A = ')
        f.write(newscorea)
        f.write('\n')
        f.write('Score B = ')
        f.write(newscoreb)
        f.write('\n')
