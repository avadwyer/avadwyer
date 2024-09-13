from stanfordkarel import *

"""
For this problem, there
are 8 colored squares
and 8 beepers on the map.
Your job is to move the
beepers so that there is one
beeper on each colored square.
Try to do this with as few
lines of code as possible.
You may use any of the following
functions:

turn_left()
move()
pick_beeper()
put_beeper()
"""
def move_two_steps():
    move()
    move()
    
def move_four_steps():
    move()
    move()
    move()
    move()
    
def pick_two_beepers():
    pick_beeper()
    pick_beeper()
    
def turn_left_three_times():
    turn_left()
    turn_left()
    turn_left()
    
def turn_left_move_two_steps():
    turn_left()
    move_two_steps()
    
def main():
    move_four_steps()
    turn_left_move_two_steps()
    pick_two_beepers()
    pick_beeper()
    move_four_steps()
    move()
    pick_two_beepers()
    move()
    turn_left_move_two_steps()
    pick_two_beepers()
    turn_left()
    turn_left()
    move_four_steps()
    put_beeper()
    move()
    put_beeper()
    turn_left_three_times()
    move()
    put_beeper()
    turn_left_three_times()
    move()
    put_beeper()
    turn_left_move_two_steps()
    turn_left_move_two_steps()
    pick_beeper()
    turn_left_three_times()
    move_two_steps()
    put_beeper()
    move()
    put_beeper()
    turn_left_three_times()
    move()
    put_beeper()
    turn_left_three_times()
    move()
    put_beeper()
   
   

if __name__ == "__main__":
    run_karel_program("fourth_world")
