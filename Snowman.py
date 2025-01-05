import turtle as t
t.bgcolor ("#06E3FC")

t.width (6)
t.color ("black","white")
t.begin_fill ()
for x in range (36):
    t.forward (20)
    t.right (10)
t.end_fill()

t.color ("black","white")
t.begin_fill ()
for x in range (36):
    t.forward (15)
    t.left (10)
t.end_fill()

t.mainloop ()