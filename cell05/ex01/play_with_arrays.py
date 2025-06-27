#!/usr/bin/env python3
array_1 = [2,8,9,48,8,22,-12,2]
array_2 = [array_1[i] + 2 for i in range(len(array_1))]
print(f"Original array: {array_1}")
print(f"New Array: {array_2}")