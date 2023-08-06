from turtle import Screen,Turtle
import snake
import time
import food
import score

screen_object = Screen()
screen_object.setup(width = 600, height = 600)



screen_object.bgcolor("white")
c = snake.Snake()
c.snake_body()
f = food.Food()
game_on = True
T = score.Score_board()



while game_on:

	time.sleep(0.2)
	screen_object.onkey(c.up,"Up")
	screen_object.onkey(c.bottum,"Down")
	screen_object.onkey(c.left,"Left")
	screen_object.onkey(c.right,"Right")
	screen_object.listen()

	
	

	c.move()
	if c.empty[0].distance(f.tur.pos())<20:

		T.increase()
		
		f.tur.hideturtle()
		p = c.empty[len(c.empty)-1].xcor()
		new = Turtle("circle")
		new.penup()
		new.goto(p+20,0)
		c.empty.append(new)
		f = food.Food()
	
	if c.empty[0].xcor() >300 or c.empty[0].xcor()<-300 or c.empty[0].ycor()>300 or c.empty[0].ycor()<-300:
		Turtle().write("Game Over", move=False, align='center', font=('Arial', 50, 'normal'))


		break
		game_on = False
	else:
		for i in range(1,len(c.empty),1):
			if c.empty[0].distance(c.empty[i])<10:
				game_on = False
				Turtle().write("Game Over", move=False, align='center', font=('Arial', 50, 'normal'))

				break



	



screen_object.exitonclick()