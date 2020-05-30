import turtle
import time
import random
wn = turtle.Screen()
wn.title("flappy bird")
wn.bgcolor("blue")
wn.setup(width=300, height=500)
wn.tracer(0)


player = turtle.Turtle()
player.speed(0)
player.penup()
player.color("yellow")
player.shape("turtle")
player.shapesize(stretch_wid=1, stretch_len=1, outline=2)
player.goto(-75, 0)
player.dx = 0
player.dy = 1
gravity = -0.04


pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("green")
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid=18, stretch_len=3, outline=2)
pipe1_top.goto(100, 280)
pipe1_top.dx = -0.5
pipe1_top.dy = 0


pipe1_bottom = turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("green")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=2)
pipe1_bottom.goto(100, -280)
pipe1_bottom.dx = -0.5
pipe1_bottom.dy = 0


pipe2_top = turtle.Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color("green")
pipe2_top.shape("square")
pipe2_top.shapesize(stretch_wid=18, stretch_len=3, outline=2)
pipe2_top.goto(300, 280)
pipe2_top.dx = -0.5
pipe2_top.dy = 0


pipe2_bottom = turtle.Turtle()
pipe2_bottom.speed(0)
pipe2_bottom.penup()
pipe2_bottom.color("green")
pipe2_bottom.shape("square")
pipe2_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=2)
pipe2_bottom.goto(300, -280)
pipe2_bottom.dx = -0.5
pipe2_bottom.dy = 0

def restart():
    pipe1_top.goto(100, 280)
    pipe1_bottom.goto(100, -280)
    pipe2_top.goto(300, 280)
    pipe2_bottom.goto(300, -280)
    player.dy = 1
    pipe1_top.dx = -0.5
    pipe1_bottom.dx = -0.5
    pipe2_top.dx = -0.5
    pipe2_bottom.dx = -0.5
    
def stopgame():

    player.dy = -gravity
    pipe1_top.dx = 0
    pipe1_bottom.dx = 0
    pipe2_top.dx = 0
    pipe2_bottom.dx = 0


def go_up():
    player.dy = 2.5

turtle.onkey(restart, "Down")
turtle.onkey(go_up, "Up")
turtle.listen()
#main game loop

while True:
    time.sleep(0.003)
    # for wn.tracer 
    wn.update()

    player.dy += gravity
    y = player.ycor()
    y += player.dy
    player.sety(y)
    

    x = pipe1_top.xcor()
    x += pipe1_top.dx
    pipe1_top.setx(x)
    
    a = pipe1_bottom.xcor()
    a += pipe1_bottom.dx
    pipe1_bottom.setx(a)
  
    h = pipe2_top.xcor()
    h += pipe2_top.dx
    pipe2_top.setx(h)
    
    y = pipe2_bottom.xcor()
    y += pipe2_bottom.dx
    pipe2_bottom.setx(y)
    # RETURN PİPES
    if pipe1_top.xcor() < -300:
        pipe1_top.setx(100)
        pipe1_bottom.setx(100)
        g = random.randint(0,500)
        h = g - 560
        pipe1_top.sety(g)
        pipe1_bottom.sety(h)


        

    if pipe2_top.xcor() < -300:
        pipe2_top.setx(100)
        pipe2_bottom.setx(100)
        w = random.randint(0,500)
        q = w - 560
        pipe2_top.sety(w)
        pipe2_bottom.sety(q)

        

    if (player.xcor()  < pipe1_top.xcor() + 48) and (player.xcor() > pipe1_top.xcor() -48):
        if (player.ycor() + 10 > pipe1_top.ycor() - 180) or (player.ycor() - 10  < pipe1_bottom.ycor() + 180):
            stopgame()
            
  

    if (player.xcor() < pipe2_top.xcor() + 48) and (player.xcor() > pipe2_top.xcor() -48):
        if (player.ycor() + 10  > pipe2_top.ycor() - 180) or (player.ycor() - 10  < pipe2_bottom.ycor() + 180):
            stopgame()
            

            
wn.mainloop()