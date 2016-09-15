import math 

def quadratic(a,b,c):
    a = b**2-4*a*c #calculate the discriminant
    
    if a>=0: #equation has solutions
        x1 = ((-b + math.sqrt(a))/2*a)
        x2 = ((-b - math.sqrt(a))/2*a)
        return x1,x2
    else:
        print('No Real Number Solution')
        
    
    a = int(input('please enter a number:'))
    b = int(input('please enter a number:'))
    c = int(input('please enter a number:')) 
    print('results are:')
    print(quadratic(a,b,c))
    
