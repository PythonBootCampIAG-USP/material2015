import numpy as np
import multiprocessing as mp

def f(x):
   return x**2

p = mp.Pool(8)

print p.map(f,np.arange(5))


def f2(x,y):
   return x**2 + y**2

print p.map(f,(np.arange(5),np.arange(5)))
