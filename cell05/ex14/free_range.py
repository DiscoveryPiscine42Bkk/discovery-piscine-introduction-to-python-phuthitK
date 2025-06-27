#!/usr/bin/env python3
import sys
a = len(sys.argv)
if a != 3:
    print("none")
else:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = [j for j in range(x , y + 1)]
    print(z)