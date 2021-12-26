import turtle as t
t.speed(0)
t.tracer(10)
t.bgcolor('black')
color=('steelblue','coral','magenta','palegreen')
for i in range(800):
    t.pencolor(color[i%4])
    t.pensize(2)
    t.backward(i)
    t.rt(120)
    t.circle(40,60)
    t.fd(i)
    t.right(121)
t.exitonclick()    
