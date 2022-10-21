import math

"""Practice different math expressions and calculations."""



#declare num_a and num_b
num_a = 4
num_b = 2
radius = 6
side_lenght = 5

#num_a and num_b sum and difference
sum = num_a + num_b
difference = num_a - num_b

#num_a and num_b float division
division_float = num_a / num_b

#num_a and num_b int division
division_int = num_a // num_b

#num_a times num_b
multiply_numbers = num_a * num_b

#num_a to the power of num_b
power = num_a ** num_b

#remainder of num_a divided by num_b
remainder = num_a % num_b

#average of num_a and num_b
average = (num_a + num_b) / 2

#area of circle
circle_area = round(math.pi * (radius ** 2), 2)

#Defining side_lenght
side_lenght = 5

#Calculating height
height = math.sqrt(side_lenght ** 2 - (side_lenght / 2) ** 2)

#Calculating triangle area
triangle_area = round(height * side_lenght / 2)

#Defining a, b, and c
a = 3
b = 4
c = 5

#Calculating discriminant
discriminant = b ** 2 - 4 * (a * c)

#Calculating hypothenus from a and b using pythagorean theorem
hüpotenuus = math.sqrt(a ** 2 + b ** 2)

#Calculating cathetus from c and a using the pythagorean theorem
kaatet = math.sqrt(c ** 2 - a ** 2)

#Define seconds
seconds = 69420

#Converting seconds to minutes and then minutes to hours
minutes = seconds // 60
hours = minutes // 60

#Define angle
angle = 96

#Angle to sin/cos
sine = round(math.sin(angle), 1)
cosine = round(math.cos(angle), 1)

#Define n
n = 27

#Writing as many Heys n amount of times
lots_of_heys = n * "Hey"

#Making numbers into strings and adding them together
string_numbers = str(num_a) + str(num_b)

