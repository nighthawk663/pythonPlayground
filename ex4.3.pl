#! /usr/bin/python3

import turtle
import time

bob = turtle.Turtle()

# exercise 2
def square(t,l):
	for i in range(4):
		t.fd(l)
		t.lt(90)

#square(bob,50)


# excercise 3
def polygon(t,l,n):
	angle = 360 / n

	for i in range(n):
		t.fd(l)
		t.lt(angle)

#polygon(bob,50,10)

#maxLength=90
#for i in range(21):
#	polygon(bob,maxLength,5)
#	maxLength += -10


# Exercise 4
def circle(t,r):
	import math
	circumference = 2 * r * math.pi

	polygon(t,(circumference/360),360)

def circleBook(t,r):
	import math
	circumference = 2 * math.pi * r
	n = int(circumference / 2 ) + 3
	length = circumference / n

	polygon(t,length,n)

circle(bob,r=-50)
circleBook(bob,r=50)
bob.lt(90)
bob.fd(2*50)

# Excercise 5
def arc(t,r,a):
	"""Draws an arc of radius r over an angle of a using turtle t"""
	import math
	circumference = 2 * r * math.pi
	stepLength = circumference / 360

	for i in range(a):
		t.fd(stepLength)
		t.lt(1)

#arc(bob,r=50,a=270)

# The first two are a radius check and the last two are for a little fun.
#bob.lt(90)
#bob.fd(50)
#bob.rt(90)
#bob.fd(50)

time.sleep(10)
