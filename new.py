import turtle
bob = turtle.Turtle()
'''
def square(nam):
    forward = 100
    leftTurn = 90
    smaller = 0
    while smaller < 100:
        for i in range(4):
            nam.fd(100 - smaller)
            nam.lt(90)
        smaller += 6
'''
def panda(nam):
    for i in range(4):
        nam.fd(100)
        nam.lt(90)
    nam.penup()
    nam.lt(225)
    nam.fd(100)
    nam.pendown()
    for i in range(4):
        nam.fd(100)
        nam.lt(90)
print(panda(bob))
turtle.mainloop()  
