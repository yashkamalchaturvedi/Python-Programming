Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> t.pendown()
>>> t.penup()
>>> t.goto(-250,250)
>>> t.forward(100)
>>> t.pendown()
>>> t.forward(100)
>>> t.right(90)
>>> t.forward(100)
>>> t.right(90)
>>> t.forward(100)
>>> t.right(90)
>>> t.forward(100)
>>> for i in range(1, 5):
	t.forward(200)
	t.right(90)

	
>>> t.penup()
>>> t.goto(0,0)
>>> t.color('red')
>>> t.circle(20)
>>> t.circle(20)
>>> t.pendown()
>>> t.circle(20)
>>> t.circle(200)
>>> t.circle(100)
SyntaxError: multiple statements found while compiling a single statement
>>> t.circle(200)
>>> t.circle(100)
>>> t.goto(150,-250)
>>> for i in range(1, 10):
	t.forward(150)
	t.left(135)

	
>>> 
>>> 