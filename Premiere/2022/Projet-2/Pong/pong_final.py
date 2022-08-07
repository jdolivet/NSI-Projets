import turtle

sc = turtle.Screen()
sc.setup(width = 1000 , height = 800)
sc.bgcolor("black")
sc.title("Pong")

#MENU :

menu = turtle.Turtle()
menu.speed(0)
menu.penup()
menu.ht()
menu.setx(-95)
menu.sety(250)
menu.pendown()
menu.color("green")
menu.write("Pong NSI", move=False, align='left', font=('Spectral', 50, 'normal'))

menu.penup()
menu.setx(-205)
menu.sety(0)
menu.pendown()
menu.color("green")
menu.write("Presser SPACE pour commencer", move=False, align='left', font=('Spectral', 30, 'normal'))
menu.penup()
menu.setx(-300)
menu.sety(- 40)
menu.pendown()
menu.color("green")
menu.write("Presser SPACE de nouveau pour recommencer", move=False, align='left', font=('Arial', 30, 'normal'))

#SCORE :

s1 = turtle.Turtle()
s1.speed(0)
s1.penup()
s1.ht()
s1.setx(-250)
s1.sety(200)
s1.pendown()
s1.color("green")

s2 = turtle.Turtle()
s2.speed(0)
s2.penup()
s2.ht()
s2.setx(250)
s2.sety(200)
s2.pendown()
s2.color("green")

#GAME OVER:

over = turtle.Turtle()
over.speed(0)
over.penup()
over.ht()
over.setx(-100)
over.sety(0)
over.pendown()
over.setx(-180)
over.sety(0)
over.pendown()
over.color("red")

#COMMENCER JEU :

def gamestart():
    menu.clear()
    main()
        
#RESTART :
    
def restart():
    sc.clear()
    sc.setup(width = 1000 , height = 800)
    sc.bgcolor("black")
    sc.title("Pong")
    main()
    
    
#GAME :

def main():
    global over
    global s1
    global s2
        
    #LIMITE :
    limite = turtle.Turtle()
    limite.penup()
    limite.color("green")
    limite.width(5)
    limite.speed(0)
    limite.ht()
    limite.goto(-470, -370)
    limite.pd()
    limite.goto(470, -370)
    limite.goto(470, 370)
    limite.goto(-470, 370)
    limite.goto(-470, -370)
    limite.speed(0)
    
    #BALLE:
    
    balle = turtle.Turtle()
    balle.shape("circle")
    balle.color("green")
    balle.penup()
    balle.goto(0,0)
    balle.speed()
    
    #MOUVEMENT :
    
    move_x = 1
    move_y = 1    
    
    #RAQUETTE 1 :
    
    r1 = turtle.Turtle()
    r1.speed(0)
    r1.shape("square")
    r1.speed(0)
    r1.setheading(90)
    r1.shapesize(1,5)
    r1.penup()
    r1.goto(-450, 0)
    r1.color("green")

    #RAQUETTE 2 :
    
    r2 = turtle.Turtle()
    r2.shape("square")
    r2.speed(0)
    r2.setheading(90)
    r2.shapesize(1,5)
    r2.penup()
    r2.goto(450, 0)
    r2.color("green")


    #SCORE :

    score_r1 = 0    
    score_r2 = 0  
        
    s1.write(score_r1, move=False, align='left', font=('Spectral', 50, 'normal'))
    s2.write(score_r2, move=False, align='left', font=('Spectral', 50, 'normal'))

    #MOUVEMENT BALLE:
    def r1_up():
        r1.penup()
        r1.fd(25)
        
    def r2_up():
        r2.penup()
        r2.fd(25)

    def r1_down():
        r1.penup()
        r1.bk(25)
        
    def r2_down():
        r2.penup()
        r2.bk(25)    
    
    sc.listen()
    sc.onkeypress(r1_up, "w")
    sc.onkeypress(r2_up, "Up")
    sc.onkeypress(r1_down, "s")
    sc.onkeypress(r2_down, "Down")
            
    #UPDATE :

    while True:
        sc.update()
        sc.tracer(0)
        
        x = balle.xcor() + move_x
        y = balle.ycor() + move_y
        balle.setx(x)
        balle.sety(y)

        
        #COLLISION:
        
        #DROITE ET GAUCHE :
        if balle.xcor() > 450:
            balle.goto(0,0)  #restart
            balle.speed(0)
            score_r1 += 1
            s1.clear()
            s1.write(score_r1, move=False, align='left', font=('Arial', 50, 'normal'))
        
        if balle.xcor() < -450:
            balle.goto(0,0)  #restart
            balle.speed(0)
            score_r2 += 1
            s2.clear()
            s2.write(score_r2, move=False, align='left', font=('Arial', 50, 'normal'))
            
        # TOP :
        if balle.ycor() > 360 :
            balle.sety(360)
            move_y = move_y * -1
        
        #BOTTOM :
        if balle.ycor() < -360 :
            balle.sety(-360)
            move_y = move_y * -1
        
        #RAQUETTES : 
        
        if r1.ycor() + 50 > 360:
            r1.sety(330)
            r1_down()
            
        if r2.ycor() + 50 > 360:
            r2.sety(330)
            r2_down()
            
        if r1.ycor() - 50 < -360:
            r1.sety(-330)
            r1_up()
        
        if r2.ycor() - 50 < -360:
            r2.sety(-330)
            r2_up()
        
        if balle.ycor() < r2.ycor() + 60 and balle.ycor() > r2.ycor() - 60 and balle.xcor() > 440 and balle.xcor() < 450:
            balle.setx(440)
            move_x = move_x * -1
        
        if balle.ycor() < r1.ycor() + 60 and balle.ycor() > r1.ycor() - 60 and balle.xcor() <- 440 and balle.xcor() > -450:
            balle.setx(-440)
            move_x = move_x * -1    
            
        #RESULTAT : 
            
        if score_r1 == 10 :
            over.write("Player 1 Won !!!", move=False, align='left', font=('Spectral', 50, 'normal'))
            break
        
        if score_r2 == 10 :
            over.write("Player 2 Won !!!", move=False, align='left', font=('Spectral', 50, 'normal'))
            break
        
        sc.listen()
        sc.onkeypress(restart, "space")
        

sc.listen()
sc.onkeypress(gamestart, "space")