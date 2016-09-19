import turtle
import math
trianglecircle = turtle.Turtle()
trianglecircle.pensize(4)


print(trianglecircle)

def twotris(t):
    t.lt(30)
    t.fd(200)
    t.rt(120)
    t.fd(200)
    t.rt(120)
    t.fd(400)
    t.lt(120)
    t.fd(200)
    t.lt(120)
    t.fd(200)

twotris(trianglecircle)

trianglecircle.lt(60)
twotris(trianglecircle)

trianglecircle.fd(200)
trianglecircle.lt(91)
trianglecircle.circle(200)
trianglecircle.lt(90)
trianglecircle.fd(100)
trianglecircle.circle(55)
trianglecircle.rt(.5)
trianglecircle.fd(100)
trianglecircle.lt(28)
trianglecircle.fd(100)
trianglecircle.circle(57)
trianglecircle.rt(178)
trianglecircle.fd(200)
trianglecircle.circle(55)
trianglecircle.lt(180)
trianglecircle.fd(100)
trianglecircle.rt(90)
trianglecircle.fd(100)
trianglecircle.circle(55)





turtle.mainloop()


