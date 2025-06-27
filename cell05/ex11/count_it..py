#!/usr/bin/env python3
import sys
user = len(sys.argv)
if user == 1:
    print("none")
else:
    print("Parameters: " + str(len(sys.argv) - 1))
for a in range(1, len(sys.argv)):
   print(f"{sys.argv[a]}: {len(sys.argv[a])}")