import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def y(x):
    return np.cos(x)

def funcionderivada(x):
    return -np.sin(x)

npuntos = 100
x = 0.1
h = np.logspace(0, -14, npuntos)


#FD
FD=(y(x+h)-y(x))/h
error1 = abs((FD-funcionderivada(x)))
print error1

#CD
CD=(y(x+h/2)-y(x-h/2))/h
error2 = abs((CD - funcionderivada(x)))
print error2

#ED
ED=(4*(y(x+h/4)-y(x-h/4)/(h/2))-(y(x+h/2)-y(x-h/2)/h))/3
error3 = abs((ED-funcionderivada(x)))

plt.loglog(h, error1, label="FD")
plt.loglog(h, error2, label="CD")
plt.loglog(h, error3, label="ED")
plt.legend()
plt.show()
