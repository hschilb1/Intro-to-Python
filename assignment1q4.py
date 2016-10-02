# Assignment 1, Question 4

import math
import random

def game_of_nim():
    powers_of_two_minus_one = [3, 7, 15, 31, 63]
    number_of_marbles_to_start = random.randrange(10, 101)
    who_goes_first = random.randrange(0,2)
    playing_intelligence = random.randrange(0,2)
    print('The pile size has %s marbles to start' %(number_of_marbles_to_start))
    if playing_intelligence == 0:
        print('Computer is stupid')
    else:
        print('Computer is smart')
    while number_of_marbles_to_start > 2:
        if who_goes_first == 0:
            print('Computer is taking its turn')
            if playing_intelligence == 0 or number_of_marbles_to_start in powers_of_two_minus_one:
                computer_will_take = random.randrange(1, number_of_marbles_to_start // 2+1)
            else:
                for p in powers_of_two_minus_one:
                    if(number_of_marbles_to_start // 2 >= number_of_marbles_to_start - p) and (number_of_marbles_to_start - p > 0):
                        computer_will_take = number_of_marbles_to_start - p
                        break
            number_of_marbles_to_start -= computer_will_take
            print('The computer decided to take %2 from the pile. There are now %d left' %(computer_will_take, number_of_marbles_to_start))
            who_goes_first = 1
    else: 
        if number_of_marbles_to_start == 2:
            break
        print('You may now take your turn')
        your_take = 0
        while your_take < 1 or your_take > number_of_marbles_to_start // 2:
            your_take = int(input('Please enter a number between 1 and %d: ' %(number_of_marbles_to_start // 2)))
        number_of_marbles_to_start -= your_take
        print('There are now %d marbles left' %(number_of_marbles_to_start))
        who_goes_first = 0
if who_goes_first ==0:
    print('You lose')
    return False
else:
    print('You Win')

            
game_of_nim()
