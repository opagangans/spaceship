import time
import turtle
import random
import winsound

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

# Set up the borders
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set up the player's spaceship
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Set up the player's bullets
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# Set up the alien ships
aliens = []
for i in range(5):
    alien = turtle.Turtle()
    alien.color("red")
    alien.shape("circle")
    alien.penup()
    alien.speed(0)
    alien.setposition(random.randint(-200, 200), random.randint(100, 250))
    aliens.append(alien)

# Set up the barriers
barriers = []
for i in range(3):
    barrier = turtle.Turtle()
    barrier.color("green")
    barrier.shape("square")
    barrier.penup()
    barrier.speed(0)
    barrier.setposition(random.randint(-200, 200), -200)
    barriers.append(barrier)

# Game loop
while True:
    for alien in aliens:
        # Move the alien
        x = alien.xcor()
        x += random.randint(-2, 2)
        alien.setx(x)

        # Check for collision with the border
        if alien.xcor() > 290 or alien.xcor() < -290:
            for a in aliens:
                y = a.ycor()
                y -= 40
                a.sety(y)
            break

        # Check for collision with the bullet
        if alien.distance(bullet) < 20:
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            # Reset the bullet
            bullet.hideturtle()
            bullet.setposition(0, -400)
            # Reset the alien
            alien.setposition(random.randint(-200, 200), random.randint(100, 250))

        # Check for collision with the player
        if alien.distance(player) < 20:
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            alien.hideturtle()
            print("Game Over")
         

