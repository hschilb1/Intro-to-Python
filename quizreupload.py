# Question 1

def crazy_about_9(a, b):
    if a == 9 or b == 9:
        return True 
    elif a + b == 9: 
        return True 
    elif a - b == 9: 
        return True 

#print(crazy_about_9(2, 9))
#print(crazy_about_9(4, 5))
#print(crazy_about_9(3, 8))



# Question 2

def leap_year(n):
    if n % 400==0:
        return True
    elif n % 100 == 0: 
        return False
    elif n % 4 == 0:
        return True 
    else:
        return False  

#print(leap_year(1900))
#print(leap_year(2016))
#print(leap_year(2017))
#print(leap_year(2000))



#Question 3:

def sum_squares(n):
    answer = 0
    for i in range(1, n+1):
        answer = answer + i**2
    return answer

#print(sum_squares(1))
#print(sum_squares(100))
