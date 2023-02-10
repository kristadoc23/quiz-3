#Katherine O'Roark Krista Dockery
#Problem 5
import math
def net_value(salary):
    value = 0.14 *(salary - 100) + 0.24 *(salary+1000)
    print("The value is", value)

net_value(6000)

#problem 6
def next_stop(location):
    print("next stop is:" , location)
    print("next stop is:" , location)

next_stop("South Bend")

#problem 7

def diff(radius):
    area = math.pi * radius**2
    circum = 2 * math.pi  * radius
    print("The difference between the area and the circumference is:", area-circum)

diff(4)

#problem 8
def new_name(x):
    print("Hello", x, "!")

new_name("Sally")

#problem 9
def equation(x):
    value = math.sin(x)**3 + math.cos(x) - 3*(math.tan(x)/(math.tan(x)+1)**2)
    print("the value is:", value)

equation(4)
