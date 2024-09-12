from stanfordkarel import *

"""
For this problem, the default
world contains a smily face.
However, the face has red eyes,
which makes it look demonic.
Your goal is to paint the face's
eye's blue and then move Karel
back to where it started.
You may use the following
functions:

turn_left()
move()
paint_corner(BLUE)
"""
def move_two_steps():
    move()
    move()
    
def move_three_steps():
    move()
    move()
    move()
    
def turn_left_three_times():
    turn_left()
    turn_left()
    turn_left()
    
def move_three_paint_corner_blue():
    move_three_steps()
    paint_corner(BLUE)
    
def main():
   move_two_steps()
   turn_left()
   move_two_steps()
   paint_corner(BLUE)
   move_two_steps()
   move()
   paint_corner(BLUE)
   turn_left_three_times()
   move_three_paint_corner_blue()
   turn_left_three_times()
   move_three_paint_corner_blue()
   move()
   turn_left_three_times()
   move()
   paint_corner(BLUE)
   move()
   paint_corner(BLUE)
   
   


if __name__ == "__main__":
    run_karel_program("third_world")