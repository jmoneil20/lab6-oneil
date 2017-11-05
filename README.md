40 points
Due: Monday 10/23/17

##Problem: Roll a ball and make it bounce around the sides of a window 4 times

##Purpose: This lab gives you practice with:

Designing, programming, and calling functions
Designing and programming while loops
Designing loop conditions
Re-using many of the other aspects of Python we've learned so far
Testing code
##Details: You need to design, write, and test a program that rolls a ball as demonstrated at the beginning of the lab. The ball goes down and right, bounces against the right edge of the window, then goes down and left, bounces against the bottom edge, then goes up and left, bounces against the left edge, then goes up and right and stops when it hits the top edge.

##Program Requirements: When you plan your solution, you must take the following into account:

Your program should be designed using at least 1 function: it returns a value input by the user after checking that that value is between 2 values (a min and a max) it accepts 3 parameters representing the min, nmax, and a message to pass to the user when asking the user to input a value
Your program should use that function to get user input for the starting x and y coordinates of the ball. Important note: Point ( 0, 0 ) is at the top left of the window.
Your program should make sure that the x coordinate is bigger than the y coordinate; this will make sure that the ball hits the right edge first, then the bottom edge, then the left edge, and finally the top edge.
##Steps:

Understand the problem
Write an algorithm in algorithm.txt showing the steps the program will go through to solve this problem, and the function(s) that will be used. For each function you need to note the name, parameters, returned value, and algorithm. Professor Franceschi must approve your algorithm before you code
Test that your algorithm works by walking through it with example input
Rename Lab6Shell.py; name your file using your two last names. Place your code in that file. DO NOT modify graphics.py and graphicsCS151.py
Write your code following your algorithm and using good usability principles.
Properly comment your code with intro comments and line comments
We're going to take a break from flowcharts for this lab. Write a set of test cases to test that your program works correctly. Make sure you fully test the error checking aspects of your program, and that you have at least one test that goes into each if statement option. You are welcome to draw a flowchart to help you ensure you have tested all paths, but you don't need to turn it in. Save test cases into testcases.txt. Note: since you get visual feedback for this program, your test cases should be related to user input only.
##Extra Credit: If you have a fully working program, you may do the extra credit. Create a copy of your program in Lab6Name1Name2EC.py. EC 1: Modify the program so that it will make sure that the user enters integer coordinates; do not exit the program if the user does not enter integer coordinates; instead, keep asking the user for integer coordinates until the user does. EC 2: Delete the code checking that the x coordinate shopuld be greater than the y coordinate, and modify your loops so that the ball properly bounces around the window. Note: it is now possible that the ball hits the bottom edge of the window before the right edge.

##Submit:

To GitHub and Moodle: a. Your Python file (only 1 file, 2 files if you do the extra credit); be sure to include your two last names in the file name b. Your algorithm (algorithm.txt) c. Your test cases (testcases.txt)
In Hardcopy (print) in class: a. Your python file (1 per pair) b. Reflection (1 per partner): Discuss what you learned in lab, what it was like working with your partner, and what caused you the most trouble in lab. Also, what was different about using loops? What was different about using graphics?