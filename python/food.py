from turtle import Turtle,Screen
import random

class Food():
	def __init__(self):
		
		self.x = random.randint(-280,280)
		self.y = random.randint(-280,280)
		

		self.tur = Turtle("circle")
		
		self.tur.penup()
		
		self.tur.goto(self.x,self.y)
		
		
		


		# self.tur.showturtle()

