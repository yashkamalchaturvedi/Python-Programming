Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> t.goto(-100,-100)
>>> t.goto(100,-10)
>>> t.goto(200,10)
>>> t.penup()
>>> t.goto(50,-50)
>>> t.pendown()
>>> t.goto(150,-50)
>>> t.color('blue')
>>> t.goto(250,80)
>>> t.pensize(20)
>>> t.goto(50,80)
>>> t.pensize(2)
>>> t.goto(50,30)
>>> t.goto(350,30)
>>> t.speed(50)
>>> t.goto(-350,40)
>>> t.goto(-350,140)
>>> t.getscreen.bgcolor('blue')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t.getscreen.bgcolor('blue')
AttributeError: 'function' object has no attribute 'bgcolor'
\
>>> t.getscreen.bgcolor('blue')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    t.getscreen.bgcolor('blue')
AttributeError: 'function' object has no attribute 'bgcolor'
>>> t.getscreen().bgcolor('blue')
>>> t.getscreen().bgcolor('white')
>>> t.forward(300)
>>> t.speed(1)
>>> t.forward(300)
>>> t.left(90)
>>> t.forward(30)
>>> t.right(180)
>>> t.forward(130)
>>> t.forward(130)
>>> 