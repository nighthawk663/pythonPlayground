#! /usr/bin/python
#

def print_spam(printIt):
  print('%s' % printIt)

def print_twice(printMe):
  print(printMe)
  print(printMe)


def do_twice(f, arg):
  f(arg)
  f(arg)

do_twice(print_spam, "Something")
