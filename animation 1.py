import turtle
t=turtle.Turtle()
list=["green",
      "red",
      "purple",
      "blue",
      "cyan"]
for i in range(200):
    t.color(list[i%5])
    t.pensize(i/10+i)
    t.forward(i)
    t.left(59)
turtle.mainloop()    
    
