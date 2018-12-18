'''
	On this assignment, you should work with a partner. You must submit what you have completed at the end of the class period, but you do not need to complete any leftover problems for homework. 

	For some of these problems you will need to create a class; for others, you will need to use a library. 
	You do NOT need to put all your solutions in this file, however you should keep all your solutions together, clearly labeled with descriptive file names, in one folder. 
'''





''' 1.
	Create a class, Point, that keeps track of two properties: x and y
	When a point is created, values for x and y should be provided.

	The methods for this class are as follows:
	rotate90: rotate the point 90° about the origin
	rotate180: rotate the point 180° about the origin
	rotaten90: rotate -90° about the origin
	translate: given 2 values, translate the point by the given amount.
	flip_horizontally: flip the point on the x-axis
	flip_vertically: flip the point on the y-axis
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def rotate90(self):
        tempx = self.x
        tempy = self.y
        self.x = tempy * -1
        self.y = tempx
    def rotaten90(self):
        tempx = self.x
        tempy = self.y
        self.x = tempy
        self.y = self.x * -1
    def rotate180(self):
        self.x = self.x * -1
        self.y = self.y * -1
    def translate(self, h, k):
        self.x = self.x + h
        self.y = self.y + k
    def flip_horizontally(self):
        self.x = self.x * -1
    def flip_vertically(self):
        self.y = self.y * -1

''' 2.
	Create a class, Bicycle, that keeps track of three properties: cadence, gear, speed. 
	When a Bicycle is created, cadence, gear, and speed are accepted as arguments.

	The methods for this class are as follows:
	set_gear: given a value, set the gear to that value
	set_cadence: given a value, set the cadence to that value
	apply_brake: given a value, decrease the speed of the bike by that value
	speed_up: given a value, increase the speed of the bike by that value
'''

class Bicycle:
	def __init__(self, cadence, gear, speed):
		self.cadence = cadence
		self.gear = gear
		self.speed = speed
	def set_gear(self, a):
		self.gear = a
	def set_cadence(self, b):
		self.cadence = b
	def apply_brake(self, c):
		self.speed -= c
	def speed_up(self, d):
		self.speed += d


''' 3.
	Create a class, student, that keeps track of four properties: energy, hunger, stress, and hours.
	These properties have a range from 0-100, except hours, which has a range from 0-24. 100 energy means they are energetic; 100 hunger means they are very hungry; 100 stress means they are extremely stressed. When you create a new student, assume they have moderate hunger, low stress, a lot of energy, and 24 hours.

	The methods for the student class are as follows:
	study: Given a value (to adjust hours), study for that given length of time. Studying decreases energy and increases hunger based on the length of the study.
	sports: Given a value (to adjust hours), play sports for that given length of time. This decreases energy, increases hunger, and decreases stress based on the length of the sports.
	class: Given a value (to adjust hours), attend classes for a given length of time. This decreases energy, increases hunger, and increases stress based on the length of the class.
	take_test: Given a value (to adjust hours), this increases stress. 
	submit_paper: this decreases stress.
	eat_meal: Given a value (to adjust hours), this decreases stress, decreases hunger, and increases energy.
	sleep: Given a time (to adjust hours), this decreases stress, increases energy, and increases hunger.
	new_day: resets the hours in a day.

	You may not let a student do more than 24 hours worth of activities in a given day. 
'''

class Student:
    def __init__(self):
        self.energy = 90
        self.hunger = 75
        self.stress = 10
        self.time = 24
    def time_check(self, test):
        if self.time - test < 0:
            assert ValueError
    def study(self, time):
        self.time_check(time)
        self.energy -= time*5
        self.hunger += time*5
        self.time -= time
    def sports(self, time):
        self.time_check(time)
        self.energy -= time*8
        self.hunger += time*8
        self.stress -= time*5
        self.time -= time
    def school(self, time):
        self.time_check(time)
        self.energy -= time*6
        self.hunger += time*5
        self.stress += time*6
        self.time -= time
    def take_test(self, time):
        self.time_check(time)
        self.energy -= time*7
        self.hunger += time*5
        self.stress += time*7
        self.time -= time
    def submit_paper(self):
        self.stress -= 10
    def eat_meal(self, time):
        self.time_check(time)
        self.energy += time*7
        self.hunger += time*7
        self.stress -= time*5
        self.time -= time
    def sleep(self, time):
        self.time_check(time)
        self.energy += time*10
        self.hunger += time*4
        self.stress -= time*6
        self.time -= time

''' 4. 
	Use numpy to create an array of numbers going from 20 to 100 by increments of .25
	Then, multiply all the values in the array by 4. 
	Then. find the sum of all the values.
'''
import numpy as np
a = np.array([0.]*321)
for i in range(0, 321):
	a[i] = 20+i/4

print(a)

for j in range(0,321):
	a[j] = 4*a[j]
print(a)

print(sum(a))



''' 5.
	Use turtle to draw a star.
'''

from turtle import *
color('blue', 'yellow')
begin_fill()
while abs(pos)) >= 1:
    forward(200)
    left(170)
end_fill()
done()



''' 6.
	Use SymPy to determine the area of a triangle given points a, b and c.
'''


from sympy import *
from sympy.geometry import *
x, y, z, t = symbols('x y z t')
x = Point(0,0)
y = Point(0,1)
z = Point(1,0)
t = Triangle(x,y,z)
print(t.area)


''' 7. 
	Use VPython to build a 3D snowman.
'''

from vpython import *
sphere()


''' Sources:
	https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html
n'''
