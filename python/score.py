from turtle import Turtle

class Score_board(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.penup()
		self.goto(0,260)

		self.hideturtle()
		self.display()
	def display(self):
		self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))
	def increase(self):
		self.score +=1
		self.clear()

		self.display()

