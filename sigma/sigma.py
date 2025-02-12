import math

# input the a b c value
a = float(input('enter value of a : '))
b = float(input('enter value of b : '))
c = float(input('enter value of c : '))

# formula of quadractic formula(the + version)
x = (((-b) + math.sqrt(((b**2) - (4*a*c)))) / (2*a))

# formula of quadractic formula (the - version)
x2 = (((-b) - math.sqrt(((b**2) - (4*a*c)))) / (2*a))

# printing the answer of quadractic formula
print(f'the x is {x} and {x2}')
