import turtle
from turtle import Turtle, Screen
from map import dotted_lines
screen = Screen()
screen.setup(width=700, height=500)
screen.bgcolor('black')
screen.tracer(0)

border_top = 215
border_bottom = -215

ball = Turtle()
ball.shape('circle')
ball.color('blue')
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = -2

t = Turtle()
score_turtle = turtle.Turtle()
t.penup()
t.shape('square')
t.color('white')
t.shapesize(stretch_wid=4, stretch_len=0.5)
t.goto(x=-300, y=0)

t_2 = Turtle()
t_2.penup()
t_2.shape('square')
t_2.color('white')
t_2.shapesize(stretch_wid=5, stretch_len=0.5)
t_2.goto(x=300, y=0)
direction = 5

left_score_turtle = turtle.Turtle()
left_score_turtle.color("white")
left_score_turtle.penup()
left_score_turtle.hideturtle()
left_score_turtle.goto(-100, 210)

right_score_turtle = turtle.Turtle()
right_score_turtle.color("white")
right_score_turtle.penup()
right_score_turtle.hideturtle()
right_score_turtle.goto(100, 210)



game_over = turtle.Turtle()
game_over.color('white')
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)



def move_up():
    t.sety(min(t.ycor() + 10, border_top))

def move_down():
    t.sety(max(t.ycor() - 10, border_bottom))

screen.listen()
screen.onkeypress(move_up, 'w')
screen.onkeypress(move_down, 's')

t_score = 0
t_2_score = 0
def update_score():
    score_turtle.clear()
    left_score_turtle.write(f"{t_score}", align='center', font=("Courier", 24, "normal"))
    right_score_turtle.write(f"{t_2_score}", align='center', font=("Courier", 24, "normal"))
def update():
    global direction, t_score, t_2_score

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() >= 330:
        left_score_turtle.clear()
        t_score += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() <= -330:
        right_score_turtle.clear()
        t_2_score += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.ycor() >= border_top or ball.ycor() <= border_bottom:
        ball.dy *= -1

    new_y = t_2.ycor() + direction
    t_2.sety(new_y)
    if new_y > border_top or new_y < border_bottom:
        direction *= -1

    if ball.xcor() < -290 and t.ycor() - 30 < ball.ycor() < t.ycor() + 30:
        ball.dx *= -1

    if ball.xcor() > 290 and t_2.ycor() - 30 < ball.ycor() < t_2.ycor() + 30:
        ball.dx *= -1


    if t_score == 11:
        game_over.write(f"Game Over: Player 1 wins {t_score} : {t_2_score}",align='center', font=("Courier", 24, "normal"))
        return
    elif t_2_score == 11:
        game_over.write(f"Game Over: Player 2 wins {t_2_score} : {t_score}", align='center', font=("Courier", 24, "normal"))
        return
    screen.update()
    screen.ontimer(update, 10)



dotted_lines()
update_score()
update()
screen.exitonclick()