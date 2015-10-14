import numpy as np

N = int(raw_input("Type a number to calculate the fatorial\n"))

fat = 1
for i in range(1,N+1):
   fat = fat * i
print fat
