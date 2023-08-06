from turtle import Turtle,Screen

s = Screen()

s.title("snake game")

position = [(0,0),(-20,0),(-40,0)]

class Snake():
	def __init__(self):
		self.empty = []

	def snake_body(self):
		s.tracer(0)
		for i in position:

			body = Turtle("circle")

			body.penup()
			body.goto(i)


			self.empty.append(body)
	def move(self):
		s.update()


		for _ in range(len(self.empty)-1,0,-1):

			x=self.empty[_-1].xcor()
			y = self.empty[_-1].ycor()
			self.empty[_].goto(x,y)
		self.empty[0].fd(20)
	def up (self):
		if self.empty[0].heading() == 0 or self.empty[0].heading()== 180:


			self.empty[0].setheading(90)
	def bottum(self):
		if self.empty[0].heading() == 0 or self.empty[0].heading() == 180:
			self.empty[0].setheading(270)
	def right(self):
		if self.empty[0].heading() == 90 or self.empty[0].heading() == 270:
			self.empty[0].setheading(0)
	def left(self):
		if self.empty[0].heading() == 90 or self.empty[0].heading() == 270:
			self.empty[0].setheading(180)
	




