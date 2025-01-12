import turtle as t
t.bgcolor ("#06E3FC")
t.speed(0)

t.width (6)
t.color ("black","white")
t.begin_fill ()
for x in range (36):
    t.forward (20)
    t.right (10)
t.end_fill() #circle 1

t.color ("black","white")
t.begin_fill ()
for x in range (36):
    t.forward (15)
    t.left (10)
t.end_fill() #circle 2


t.penup()
t.goto(0,174)
t.pendown()
t.color ("black","white")
t.begin_fill ()
for x in range (36):
    t.forward (10)
    t.left (10)
t.end_fill() #circle 3

t.penup()
t.goto(-20,214)
t.pendown()
t.setheading(270)
t.circle(26,180) #smile


t.penup()
t.goto(-15,250)
t.pendown()
t.circle(2) #lefteye

t.penup()
t.goto(25,250)
t.pendown()
t.circle(2) #righteye

t.penup()
t.goto(-75,90)
t.pendown()
t.setheading(230)
t.goto(-75,90)

t.mainloop ()
