from ctypes import *

cfat = CDLL("./fatC.so")
cfat.fatC.restype = c_double

print cfat.fatC(5)
