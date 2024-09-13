from stanfordkarel import *

"""
For this problem, your goal is to
get karel to pick up all of the beepers
in the provided world. You may use any
of the following commands:

turn_left()
move()
pick_beeper()
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_two_steps():
    move()
    move()
    
def main():
    turn_left()
    move()
    pick_beeper()
    move()
    turn_right()
    move_two_steps()
    pick_beeper()
    turn_right()
    move_two_steps()
    pick_beeper()
    
    


if __name__ == "__main__":
    run_karel_program("first_world")
    
