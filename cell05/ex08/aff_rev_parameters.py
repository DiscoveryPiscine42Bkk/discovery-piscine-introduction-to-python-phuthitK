#!/usr/bin/env python3
import sys
user = len(sys.argv)
if user <= 3:
    print("none")
else:
    for i in range(len(sys.argv) - 1, 0 , -1):
        print(sys.argv[i])