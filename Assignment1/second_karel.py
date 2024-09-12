from stanfordkarel import *

"""
For this problem, your goal is to
move the beeper to the designated
red square. You may use the following
commands:

turn_left()
move()
pick_beeper()
put_beeper()
"""
def turn_left_three_times():
    turn_left()
    turn_left()
    turn_left()
    
def move_two_steps():
    move()
    move()

def turn_left_three_move_once():
    turn_left_three_times()
    move()
    
def turn_left_move_once():
    turn_left()
    move()
    
def main():
    turn_left_move_once()
    turn_left_three_move_once()
    turn_left_move_once()
    turn_left_three_move_once()
    pick_beeper()
    turn_left_move_once()
    turn_left_three_move_once()
    move()
    turn_left_three_move_once()
    move()
    put_beeper()


if __name__ == "__main__":
    run_karel_program("second_world")
    
