#!/usr/bin/env python3
import sys
user = len(sys.argv)
if user != 2:
    print("none")
else:
    print(sys.argv[1].upper())