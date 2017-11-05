#Programmer: Josh O'Neil
#Class: CS151, Franceschi
#Date: 19 October 2017
#Lab 6
#purpose: to bounce a ball off four walls
#Inputs: x and y
#Output: bouncing ball

print("This program will bounce a ball.")
print("Your x coordinate must be larger than the y coordinate.")

# import the graphicsCS151 file so we have access to its functions
from Graphics151 import *

# Height and width of window, radius of the ball
# THIS IS ALREADY CODED FOR YOU
HEIGHT = 500
WIDTH = HEIGHT # keep it simple
radius = 20

# 1 - code a function that returns an int between a min value and a max value,
# two parameters of the function; that int is input by the user
# Assume that the user will enter an int (extra credit # 1 for checking if the user does)
# Add a third parameter so that the input question to the user can be
# customized when you call the function


min_value = radius
max_value = HEIGHT - radius

def return_int(min_value, max_value,message):
    value = input(message)
    while not value.isdigit():
        print("Not an integer")
        value = input(message)
    value = int(value)
    while value < min_value or value > max_value:
        print("Not a valid input")
        value = int(input(message))
    return value



# 2 - Use the function in 1 above to get the starting x and y coordinates
# from the user; make sure that the x coordinate is strictly greater than the y coordinate
x = return_int(min_value, max_value, "Enter an x coordinate: ")
y = return_int(min_value, max_value, "Enter a y coordinate: ")
while x < y:
    print("Your x coordinate must be larger than the y coordinate.")
    x =return_int(min_value, max_value, "Enter an x coordinate: ")
    y = return_int(min_value, max_value, "Enter a y coordinate: ")


# 3 - Create the window; use the make_window function
# Look at its function header in the graphicsCS151 file
# THIS IS ALREADY CODED FOR YOU
win = make_window( "Play Ball!", WIDTH, HEIGHT )

# 4 - Create the ball; use the make_circle function
# Look at its function header in the graphicsCS151 file
circle = make_circle(x,y,radius)



# 5 - Color the ball and draw it in the window; use the draw_and_color_circle function
# Look at its function header in the graphicsCS151 file
design = draw_and_color_circle(win,circle,"chartreuse")


# 6 - Decide how fast your ball will be moving
# horizontal speed and vertical speed
# speed is essentially a number of pixels that the the ball will move
# at every iteration of the various loops
moveX = 4
moveY = 3



# 7 - 1st loop: move down and right
while x <= max_value:
    sleep(50)
    x += moveX
    y += moveY
    speed_dr = move(circle, moveX, moveY)


# To move the ball, use the move function
# Look at its function header in the graphicsCS151 file
# Do not move the ball too fast; use the sleep function to slow it down
# Look at its function header in the graphicsCS151 file
# At this stage, before actually coding this loop, you can test the move and sleep function


# 8 - move down and left
while y <= max_value:
    sleep(50)
    x -= moveX
    y += moveY
    speed_dl = move(circle, -moveX, moveY)


# 9 - move left and up
while x >= min_value:
    sleep(50)
    x -= moveX
    y -= moveY
    speed_ul = move(circle, -moveX, -moveY)


# 10 - move right and up
while y >= min_value:
    sleep(50)
    x += moveX
    y -= moveY
    speed_ur = move(circle, moveX, -moveY)

# During the testing stage, if you want to keep the window open at the end,
# write this code:
point = win.getMouse( )