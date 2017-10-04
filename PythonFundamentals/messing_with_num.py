import numpy as np


print np.arange(5,105,10)

x = np.zeros((5, 10))

print x

y = np.ones((5,5))

print y

a = np.arange(10)

print a

b = np.arange(25).reshape(5,5)

print b


big_arr = np.hstack((b,x,y))

print big_arr

print np.hsplit(big_arr, 2)

