import turtle
from random import *
import time

tser = turtle.Turtle()
tser.up()
tpom = turtle.Turtle()
tpom.up()
tpom.hideturtle()
tpom.pensize(3)
tpom.color("red")
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
points = 0

def pomme():
    tpom.speed(0)
    tpom.hideturtle()
    tpom.right(90)
    tpom.forward(10)
    tpom.left(90)
    tpom.down()
    tpom.forward(3)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(2)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(2)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(6)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(6)
    tpom.back(6)
    tpom.right(180)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(2)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(3)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(2)
    tpom.right(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(3)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(6)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(2)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(1)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(2)
    tpom.right(90)
    tpom.forward(1)
    tpom.left(90)
    tpom.forward(2)
    tpom.up()

tx = [0] * 34
x = -340
ty = [0] * 24
y = -240
for i in range(len(tx)):
    tx[i] = x
    x = x + 20
for i in range(len(ty)):
    ty[i] = y
    y = y + 20
pommes = [[choice(tx),choice(ty)] for _ in range(3)]
for i in range(len(pommes)):
    tpom.goto(pommes[i][0], pommes[i][1])
    pomme()

tser.shape("square")
tser.color("green")
serpent = [[0,0], [-20,0], [-40,0]]
jeu = True

sens = "droite"

def droite():
    global sens
    if sens != "gauche":
        sens = "droite"
def gauche():
    global sens
    if sens != "droite":
        sens = "gauche"
def haut():
    global sens
    if sens != "bas":
        sens = "haut"
def bas():
    global sens
    if sens != "haut":
        sens = "bas"
def deplacer():
    tser.clear()

    if sens == "droite":
        serpent.insert(0, (serpent[0][0] + 20, serpent[0][1]))
    if sens == "gauche":
        serpent.insert(0, (serpent[0][0] - 20, serpent[0][1]))
    if sens == "haut":
        serpent.insert(0, (serpent[0][0], serpent[0][1] + 20))
    if sens == "bas":
        serpent.insert(0, (serpent[0][0], serpent[0][1]  - 20))

    serpent.pop()

    for carre in serpent:
        tser.goto(carre[0],carre[1])
        tser.stamp()

screen.listen()
screen.onkey(droite, "Right")
screen.onkey(gauche, "Left")
screen.onkey(haut, "Up")
screen.onkey(bas, "Down")

while jeu:
    deplacer()
    for apple in pommes:
        if serpent[0][0] == apple[0] and serpent[0][1] == apple[1]:
            apple[0] = choice(tx)
            apple[1] = choice(ty)
            serpent.append(serpent[-1])
            points += 1
            tpom.clear()
            for i in range(len(pommes)):
                tpom.goto(pommes[i][0], pommes[i][1])
                pomme()
    for carre in serpent:
        x = carre[0]
        y = carre[1]
        if ((x == -380) or (x == 380) or (y == -280) or (y == 280)):
            print("Vous avez perdu car le serpent a touché le mur")
            jeu = False
    for i in range(1, len(serpent)):
        if serpent[0] == serpent[i]:
            print("Vous avez perdu car le serpent a touché son corps")
            jeu = False
    screen.update()
    if points <= 5:
        time.sleep(0.2)
    if points > 5 and points <= 10:
        time.sleep(0.15)
    if points > 10 and points <= 20:
        time.sleep(0.1)
    if points > 20:
        time.sleep(0.05)

screen.clear()
screen.bye()
print(f"Points = {points}")