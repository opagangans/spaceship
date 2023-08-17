import turtle
import time
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

player_speed = 15

# Set up the player's bullets
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 20
bullet_state = "ready"

# Set up the sound effect
bullet_sound = "bullet.wav"

# Set up the alien ships
aliens = []
alien_speed = 2
alien_dx = 10
alien_dy = 40
num_aliens = 5

for i in range(num_aliens):
    alien = turtle.Turtle()
    alien.color("red")
    alien.shape("circle")
    alien.penup()
    alien.speed(0)
    alien.setposition(-200 + i * 100, 250)
    aliens.append(alien)

# Set up the barriers
barriers = []
num_barriers = 3

for i in range(num_barriers):
    barrier = turtle.Turtle()
    barrier.color("green")
    barrier.shape("square")
    barrier.penup()
    barrier.speed(0)
    barrier.setposition(-200 + i * 200, -200)
    barriers.append(barrier)

# Set up the alien bullets
alien_bullets = []

# Move the alien bullets
def move_alien_bullets():
    for bullet in alien_bullets:
        y = bullet.ycor()
        y -= bullet_speed
        bullet.sety(y)

        # Check for collisions between the alien bullets and the barriers
        for barrier in barriers:
            if bullet.distance(barrier) < 20:
                bullet.hideturtle()
                alien_bullets.remove(bullet)
                barrier.hideturtle()
                barriers.remove(barrier)

        # Check for collisions between the alien bullets and the player's spaceship
        if bullet.distance(player) < 20:
            bullet.hideturtle()
            bullet_state = "ready"
            player.hideturtle()
            message = turtle.Turtle()
            message.color("white")

# Create a list to keep track of all the bullets
bullets = []

# Modify the fire_bullet function to create a new bullet object and add it to the list
def fire_bullet():
    global bullet_state
    bullet_state = "fire"
    x = player.xcor()
    y = player.ycor() + 10
    bullet = turtle.Turtle()
    bullet.speed(0)
    bullet.shape("triangle")
    bullet.color("white")
    bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
    bullet.penup()
    bullet.setposition(x, y)
    bullet.showturtle()
    bullets.append(bullet)
    winsound.PlaySound(bullet_sound, winsound.SND_ASYNC)
    screen.update()

class Bullet:
    def __init__(self, x, y):
        self.state = "ready"
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("triangle")
        self.turtle.color("white")
        self.turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.turtle.penup()
        self.turtle.setposition(x, y)
        self.turtle.hideturtle()
        print("Created new bullet turtle")

# Define the player bullet state
player_bullet_state = "ready"

def fire_player_bullet():
    global player_bullet_state
    if player_bullet_state == "ready":
        player_bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet = Bullet(x, y)
        player_bullets.append(bullet)
        print("Added new player bullet")
        winsound.PlaySound(bullet_sound, winsound.SND_ASYNC)

# Move all the bullets in the list
for bullet in bullets:
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)
        print("Bullet y-coordinate:", y)

        # Check if the bullet has gone off the top of the screen
        if y > 300:
            bullet.hideturtle()
            bullets.remove(bullet)
            bullet_state = "ready"

        # Check for collisions between the player's bullets and the alien ships
        for alien in aliens:
            if bullet.distance(alien) < 20:
                bullet.hideturtle()
                bullets.remove(bullet)
                bullet_state = "ready"
                alien.hideturtle()
                aliens.remove(alien)

player_bullets = []

# Move the player's bullets
def move_player_bullets():
    for bullet in player_bullets:
        if bullet.state == "fire":
            y = bullet.ycor()
            y += bullet_speed
            bullet.sety(y)

            # Check if the bullet has gone off the top of the screen
            if y > 300:
                bullet.hideturtle()
                player_bullets.remove(bullet)
                bullet.state = "ready"

            # Check for collisions between the player's bullets and the alien ships
            for alien in aliens:
                if bullet.distance(alien) < 20:
                    bullet.hideturtle()
                    player_bullets.remove(bullet)
                    bullet.state = "ready"
                    alien.hideturtle()
                    aliens.remove(alien)

# Set up the game loop
while True:
    # Move the player's spaceship
    def move_left():
        x = player.xcor()
        x -= player_speed
        if x < -280:
            x = -280
        player.setx(x)

    def move_right():
        x = player.xcor()
        x += player_speed
        if x > 280:
            x = 280
        player.setx(x)

    screen.listen()
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")
    screen.onkeypress(fire_bullet, "space")

    # Move the player's bullets
    move_player_bullets()
    screen.onkeypress(fire_player_bullet, "space")
    # Move the alien bullets
    move_alien_bullets()

    # Move the alien ships
    for alien in aliens:
        x = alien.xcor()
        x += alien_dx
        alien.setx(x)

        # Reverse the direction and move down when hitting the edge
        if x > 280 or x < -280:
            alien_dx *= -1
            y = alien.ycor()
            y -= alien_dy
            alien.sety(y)

            # End the game if the alien ships touch the player's spaceship
            if alien.ycor() < -250:
                player.hideturtle()
                bullet.hideturtle()
                for alien in aliens:
                    alien.hideturtle()
                for barrier in barriers:
                    barrier.hideturtle()
                message = turtle.Turtle()
                message.color("white")
                message.penup()

    # Check for collisions between the alien bullets and the player's spaceship
    for bullet in alien_bullets:
        if bullet.distance(player) < 20:
            bullet.hideturtle()
            player.hideturtle()
            game_over = True

    # End the game if all the alien ships are destroyed
    if not aliens:
        player.hideturtle()
        bullet.hideturtle()
        for barrier in barriers:
            barrier.hideturtle()
        message = turtle.Turtle()
        message.color("white")
        message.penup()
        message.goto(0, 0)
        message.write("You Win!", align="center", font=("Arial", 24, "bold"))
        time.sleep(3)
        screen.bye()

    # Move the alien bullets
    for bullet in alien_bullets:
        y = bullet.ycor()
        y -= bullet_speed
        bullet.sety(y)

        # Check for collisions between the alien bullets and the barriers
        for barrier in barriers:
            if bullet.distance(barrier) < 20:
                bullet.hideturtle()
                alien_bullets.remove(bullet)
                barrier.hideturtle()
                barriers.remove(barrier)

    # Fire the alien bullets
    for alien in aliens:
        if random.randint(1, 100) == 1:
            alien_bullet = turtle.Turtle()
            alien_bullet.color("white")
            alien_bullet.shape("triangle")
            alien_bullet.penup()
            alien_bullet.speed(0)
            alien_bullet.setheading(270)
            alien_bullet.shapesize(0.5, 0.5)
            alien_bullet.setposition(alien.xcor(), alien.ycor())
            alien_bullets.append(alien_bullet)

    # Update the screen
    screen.update()