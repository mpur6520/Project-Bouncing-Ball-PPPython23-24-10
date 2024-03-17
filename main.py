import play #loads the play module library
import random #loads the random library
import pygame

w = 500 #defines global variable for the horizontal size of court
h = 400 #defines global variable for the vertical size of court

halfW = w/2 #defines global variable for the middle half of horizontal court
halfH = h/2 #defines global variable for the middle have of vertical court

score = 0 #global variable for points earned
speed = 3 #global variable for the speed of ball

@play.when_program_starts #this creates a keyframe to start the game function as soon as you press run
def doBackGround():
  play.set_backdrop((255, 209, 220)) #defines color of backdrop

court = play.new_box( #open for parameters
  color = (255, 179, 201), #set the court color; darker shade of background
  x = 0, #x coordinate of the court
  y = 0, #y coordinate of the court
  width = w, #use global variable to populate local variable
  height = h, #use global variable to populate local variable
) #close the parameters

paddle = play.new_box( #open for parameters
  color = (255,0,127), #set the color of paddle
  width = 50, #set the width of paddle
  height = 5, #set the height of paddle
  x = 0, #x value, changes with mouse location
  y = -halfH + 15, #sets y value for the paddle
) #close parameters

ball = play.new_circle( #open for parameters
  color = (255,0,127), #sets color of ball
  radius = 10, #sets the ball's radius
  x = 0, #sets x value for the ball, changes
  y = halfH - 30, #sets y value for the ball, changes
  angle = random.randint(210,330) #set random angle to begin with
) #close parameters


#### FACE 1, right
face1 = play.new_circle(
  color = (255, 236, 128),
  radius = 40,
  x = halfW - 30,
  y = halfH + 50
)

face1_eye1 = play.new_circle(
  color = (0,0,0),
  radius = 7,
  x = halfW - 45,
  y = halfH + 55
)

face1_eye2 = play.new_circle(
  color = (0,0,0),
  radius = 7,
  x = halfW - 15,
  y = halfH + 55,
)

face_1_mouth_1 = play.new_circle(
  color = (0,0,0),
  radius = 15,
  x = halfW - 30,
  y = halfH + 37,
)

face_1_mouth_cover = play.new_circle(
  color = (255, 236, 128),
  radius = 15,
  x = halfW - 30,
  y = halfH + 40,
)

#### FACE 2, left
face2 = play.new_circle(
  color = (255, 236, 128),
  radius = 40,
  x = halfW - 470,
  y = halfH + 50
)

face2_eye1 = play.new_circle(
  color = (0,0,0),
  radius = 7,
  x = halfW - 485,
  y = halfH + 55
)

face2_eye2 = play.new_circle(
  color = (0,0,0),
  radius = 7,
  x = halfW - 455,
  y = halfH + 55
)

face_2_mouth_1 = play.new_circle(
  color = (0,0,0),
  radius = 15,
  x = halfW - 470,
  y = halfH + 37,
)

face_2_mouth_cover = play.new_circle(
  color = (255, 236, 128),
  radius = 15,
  x = halfW - 470,
  y = halfH + 40,
)

###

name_text = play.new_text( #open parameters 
  words = "Python Pong Game",
  x = 0,
  y = halfH + 50,
  font = None,
  color = (224, 0, 102)
)

score_text = play.new_text( #open for parameters
  words = "SCORE" + str(score), #makes text display the score
  x = 0, #sets x value of the text
  y = halfH + 15, #sets y value location of the text
  font = None, #indicates font of text
  color = (224, 0, 102) #sets color for text indicating score
) #close parameters

@play.repeat_forever #makes sure game plays when run
def do(): #create a definition for the game function
  global score #calls the global variable, score
  paddle.x = play.mouse.x #sets the paddle to the same x coordinate as the mouse
  if (play.mouse.x < -halfW + paddle.width/2):
    paddle.x = -halfW + paddle.width/2
  if (play.mouse.x > halfW - paddle.width/2):
    paddle.x = halfW - paddle.width/2
  ball.move(speed) #makes the ball move
  #bounce the ball off the walls, top and bottom 360 and right and left 180
  #top:
  if(ball.y + ball.radius > halfH):
    ball.angle = 360 - ball.angle
  #bottom:
  if(ball.y - ball.radius < -halfH):
    ball.angle = 360 - ball.angle
    score -= 1
  #right:
  if (ball.x + ball.radius > halfW):
    ball.angle = 180 - ball.angle
  #left:
  if (ball.x - ball.radius < -halfW):
    ball.angle = 180 - ball.angle
  #when the ball hits the paddle make sure its trajectory changes
  if (ball.is_touching(paddle)):
    ball.angle = 360 - ball.angle + random.randint(-30,30)
    ball.angle %= 360
    score += 1
  #make sure ball bounces up after hitting paddle
    if(ball.angle < 20):
      ball.angle = 20
    elif(ball.angle > 160):
      ball.angle = 160



  
  if (score >= 5 and paddle.width != 30): #decreases paddle size when score is 5 or higher
    paddle.width -=5
  if (score >= 10): #increases ball speed when score is 10 or higher
    ball.move(speed + 1)
  elif (score <5): #increases paddle size when score is less than 5
    paddle.width = 50
  ball.angle %= 360 #ensure the angle is valid
  score_text.words = "SCORE: " + str(score) #update the score text
  
play.start_program() #plays the program when it starts