import math 
from math import pi 

print(math.sin(math.pi/2))

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

# for name in dir(math):
#   print(name, end=" " ) 

print(dir(math))
  
#  radian = 57.3 degrees. 6 radians are 1 circle or 360 degrees
#  Tangent = sine / cosine #> proportion using math.atan(X) finding 'radiants'
#  sine = proportion high scale compare with hipotenuse
#  cosine = proportion length scale compare with hipotenuse

 
# SIN()

wall_height = 3
angle = math.radians(30)
print("angles (radians):", angle)
# Since Sine = Opposite (Height) / Hypotenuse
# Therefore Hypotenuse = Height / Sine
required_scale_length = wall_height / math.sin(angle)
print("SIN", math.sin(angle)), 
print("Scale length", required_scale_length) # Result: 6.000000000000001 Hypotenuse

# COS()

scale_length = 6.0  # Hypotenuse
angle = math.radians(30)

# Since Cosine = Adjacent (Base) / Hypotenuse
# Therefore Adjacent = Hypotenuse * Cosine
distance_from_wall = scale_length * math.cos(angle)
print("COS", math.cos(angle)), 
print("Distance from the wall (Base):", distance_from_wall) # Result: 5.196152422706632 meters

# TAN()

base_distance = 5.196
angle = math.radians(30)

# Since Tangent = Opposite (Height) / Adjacent (Base)
# Therefore Opposite = Base * Tangent
calculated_wall_height = base_distance * math.tan(angle)
print("TAN", math.tan(angle)), 
print("Calculated wall height:", calculated_wall_height) # Result: 2.9999119987092953 meters

# ATAN()

opposite = 15  # Height of the building
adjacent = 40  # Distance on the ground

# 1. Calculate the proportion (Tangent)
# This represents the ratio of Height to Distance
tangent_value = opposite / adjacent 
print(f"Tangent Ratio: {tangent_value}") # 0.375

# 2. Use atan() to find the angle in RADIANS
# This is the "Inverse Tangent"
angle_radians = math.atan(tangent_value)
print(f"Angle in radians: {angle_radians:.4f}")

# 3. Convert to DEGREES for human readability
angle_degrees = math.degrees(angle_radians)
print(f"Aiming angle: {angle_degrees:.2f}°")