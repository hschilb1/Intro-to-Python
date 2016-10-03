# Assignment 1, Question 1

import math

def prime_factors(n):
    '''
This code starts with a number, checks if it is divisible by 2 and works its way up until it finds something it is divisible by. If it is divisible by a number, it divides the number you are trying to factor by that number and keeps going. 
    '''
    i = 2
    factors = []
    while i*i <= n:
        if n%i!=0:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(150))


# Assignment 1, Question 2

def main():
      '''
This function takes a word as input and, utilizing the Palindrome function below, prints true or false. 
      '''
   inputStr = input("Enter a word: ")
   if Palindrome(inputStr):
      print("True.")
   else:
      print("False.")

def Palindrome(string) :
      '''
This function determines if a word is a Palindrome 
      '''
   if len(string) <= 1 :
      return True
   if string[0] == string[len(string) - 1] :
      return Palindrome(string[1:len(string) - 1])
   else :
      return False

main()


# Assignment 1, Question 3

import random
import math

def random_direction(n):
    '''
    This is a function that takes the number of random turns and outputs the total distance
    '''
    directions = [[0,1], [1,0], [-1,0], [0,-1]]
    # The coordinates above are equivalent to forward, right, backward and left 
    distance = [0,0]
    list_pick = []
    for i in range(n):
        list_pick = random.choice(directions)
        for i in range(len(distance)):
            distance[i] = distance[i] + list_pick[i]
    print(distance) 
    return (math.sqrt(distance[0]**2 + distance[1]**2))

    
print(random_direction(5))
#Input however many directions you want into the print statement above


# Assignment 1, Question 4

import math
import random

def game_of_nim():
    '''
This function plays the game of nim. There is a while loop that runs until the pile has 2 left. 
    '''
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
            # The zero above is an indicator that the computer will be taking its turn and its instructions are listed below
            print('Computer is taking its turn')
            if playing_intelligence == 0 or number_of_marbles_to_start in powers_of_two_minus_one:
                computer_will_take = random.randrange(1, number_of_marbles_to_start // 2+1)
            else:
                for p in powers_of_two_minus_one:
                    if(number_of_marbles_to_start // 2 >= number_of_marbles_to_start - p) and (number_of_marbles_to_start - p > 0):
                        computer_will_take = number_of_marbles_to_start - p
                        break
            number_of_marbles_to_start -= computer_will_take
            print('The computer decided to take %d from the pile. There are now %d left' %(computer_will_take, number_of_marbles_to_start))
            who_goes_first = 1
            # The person playing can now take their turn. Their instructions are described below. 
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
