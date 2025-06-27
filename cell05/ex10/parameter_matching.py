#!/usr/bin/env python3
import sys
user = len(sys.argv)
if user != 2:
  print("none")

else:
    something = input("What was the parameter? ")
    if  something == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")