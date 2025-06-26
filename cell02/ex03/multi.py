#!/usr/bin/env python3
first_num = int(input("Enter the first number"))
second_num = int(input("Enter the second number"))
multiply = first_num * second_num
if multiply > 0: 
   print(first_num , " * " ,second_num , " = " , multiply , "\nThe result is positive.")
elif multiply < 0: 
   print( first_num , " * " , second_num , " = " , multiply , "\nThe result is negative.")
else: 
  print( first_num , " * " , second_num , " = " , multiply ,"\nThe result is both positive nad negative.")