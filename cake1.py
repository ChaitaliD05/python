import turtle as t

def happy_bday(x=0,y=0):
    t.penup()
    t.color('orange')
    t.goto(x,y)
    t.pendown()
    #s_fill
    t.begin_fill()
    t.goto(x+50,y)
    t.goto(x+50,y+50)
    t.goto(x-50,y+50)
    t.goto(x-50,y)
    t.goto(x,y)
    t.end_fill()
    #e_fill
    t.goto(x,y+70)
    #flame
    t.color('yellow')
    t.goto(x,y+75)
    t.goto(x,y+70)
    #candle
    t.color('Black')
    t.goto(x,y+50)
    t.penup()
    t.goto(x,y+40)
    #greet
    t.color('green')
    t.goto(x,y)
    t.goto(x-100,y)
    t.goto(x-100,y+100)
    t.write("WISHING YOU HAPPY BIRTHDAY DUGIE")

happy_bday(0,0)
        
