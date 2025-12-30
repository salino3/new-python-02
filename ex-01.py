from math import   pi, radians, degrees, sin, cos, tan, asin, e, exp, log, ceil, floor, trunc
import math
from random import random, seed, randrange, randint, uniform

# pi → a constant with a value that is an approximation of π;
# radians(x) → a function that converts x from degrees to radians;
# degrees(x) → acting in the other direction (from radians to degrees)


ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
    

#  sinh(x) → the hyperbolic sine;
#  cosh(x) → the hyperbolic cosine;
#  tanh(x) → the hyperbolic tangent;
#

print(math.pow(20 , 5), 20 ** 5) # it is the same, pow() return float number

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))


 # floor(x) → the floor of x (the largest integer less than or equal to x)
 # ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
 # trunc(x) → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor)
 # factorial(x) → returns x! (x has to be an integral and not a negative)
 # hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle
 # with the leg lengths equal to x and y (the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise)
print("----------------")

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y)) # tends to go opposite to zero
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y)) # tends to go towards zero
print(trunc(x), trunc(y)) # It does not round numbers, remove decimals
print(trunc(-x), trunc(-y)) # It does not round numbers, remove decimals

#

# seed(0) # always same result with method random()

for i in range(5):
    print(random())
    
print(randrange(5), end=' ')
print(randrange(0, 5), end=' ')
print(randrange(0, 6, 5), end=' ')
print(randrange(0, 5, 2), end=' ')
print(randint(0, 5)) # Return random integer in range [a, b], including both end points.

print(uniform(0, 5)) # decimals result, no controls 'step'