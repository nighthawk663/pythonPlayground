#! /usr/bin/python3
#

def drawLine(w):
  print('+','-'*w,'+','-'*w,'+')

def drawCellSpace(w):
  print('|',' ' *w, '|', ' ' * w, '|')


def do_twice(f, arg):
  f(arg)
  f(arg)

def do_4x(f, arg):
  do_twice(f, arg)
  do_twice(f, arg)

# Draw it.
drawLine(4)
do_4x(drawCellSpace, 4)
drawLine(4)
do_4x(drawCellSpace, 4)
drawLine(4)
