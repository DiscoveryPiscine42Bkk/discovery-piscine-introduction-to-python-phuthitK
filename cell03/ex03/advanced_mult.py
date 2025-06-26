#!/usr/bin/env python3
i = 0
while i<11:
  j=0
  print(f"Table de {i}: ", end = " ")
  while j<11:
    print(f"{i*j}", end = " ")
    j+=1
  print("")
  i+=1