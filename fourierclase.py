import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import fftpack

fas=[]
mag=[]
#Descargo fase y magnitud 
fase = np.genfromtxt ('phase.dat', delimiter = " ")
fas.append(fase)
magnitud = np.genfromtxt ('magnitude.dat', delimiter = " ")
mag.append(magnitud)
#print fase
#print magnitud
#print fas
#print mag

#Tengo mi parte real en x y y 
realx=[]
realy=[]
x = magnitud*(np.cos(fase))
realx.append(x)
#print x
y = magnitud*(np.sin(fase))
realy.append(y)
#print y 
#print real

inver = ((x)+(y)*(1j))
#print inver 

#inversa = scipy.fftpack.ifft2(inver)
inversa = np.fft.ifft2(inver)
inversa_1= abs(inversa)
#print inversa_1

#plt.imshow(inversa_1)
#plt.show()
plt.savefig('secret.jpg')



#ifft inversa 2D
