import turtle
import winsound


win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(800, 600)
win.tracer(0)


# Score
score_a = 0
score_b = 0


# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(5, 1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(5, 1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25


# Pen
pen = turtle.Turtle()
pen.color("White")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0  Player B : 0",
          align="center",
          font=("courier", 24, "normal"))


# functions

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

    if paddle_a.ycor() < -250:
        paddle_a.goto(-350,-250)


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
    if paddle_a.ycor() > 250:
        paddle_a.goto(-350,250)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

    if paddle_b.ycor() < -250:
        paddle_b.goto(350,-250)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

    if paddle_b.ycor() > 250:
        paddle_b.goto(350,250)


# keyboard binding

win.listen()

win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_a_up, "w")

win.onkeypress(paddle_b_down, "Down")
win.onkeypress(paddle_b_up, "Up")


# game loop

while True:

    win.update()

    # movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('pong/wallhit.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('pong/wallhit.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()

        pen.write(f"Player A : {score_a}  Player B : {score_b}",
                  align="center",
                  font=("courier", 24, "normal"))

        winsound.PlaySound('pong/out.wav', winsound.SND_ASYNC)


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()

        pen.write(f"Player A : {score_a}  Player B : {score_b}",
                  align="center",
                  font=("courier", 24, "normal"))

        winsound.PlaySound('pong/out.wav', winsound.SND_ASYNC)


    # paddle ball collision

    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor(
    ) > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('pong/hit.wav', winsound.SND_ASYNC)


    if ball.xcor() < -340 and ball.ycor() > paddle_a.ycor() - 50 and ball.ycor(
    ) < paddle_a.ycor() + 50:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('pong/hit.wav', winsound.SND_ASYNC)
