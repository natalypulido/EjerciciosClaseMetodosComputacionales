import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

  
h=0.001
g = 9.8
l=1
mi=-5
ma=5
##Cantidad de puntos
n=int((ma-mi)/h)
#print n
##x
t=np.zeros(n)
##teta
y_1= np.zeros(n)
y_2= np.zeros(n) 

##Teniendo en cuenta Second Order ODEs 
def funcion_y1prime (t, y_1, y_2):
	return y_2
def funcion_y2prime (t, y_1, y_2):
	return (-g/l)*np.sin(y_1)

##Condiciones iniciales
t[0]=mi
y_1[0]=1
y_2[0]=0
#print y_1[0]
#print y_2[0]

##ME GUIE DEL NOTE BOOK - METODO EULER 
##Calculamos primeras derivadas 
for i in range (1, n):
	y1prime = funcion_y1prime(t[i-1], y_1[i-1], y_2[i-1])
	#print y1prime
	y2prime = funcion_y2prime(t[i-1], y_1[i-1], y_2[i-1])
	#print y2prime 
	t[i] = t[i-1] + h
        y_1[i] = y_1[i-1] + h * funcion_y1prime(t[i-1], y_1[i-1], y_2[i-1])
        y_2[i] = y_2[i-1] + h * funcion_y2prime(t[i-1], y_1[i-1], y_2[i-1])

#plt.plot(t,y_1)
plt.plot(t,y_2)
plt.xlabel('x')
plt.ylabel('y(x)')
#plt.show()

##Cambio de coordenadas 
x=np.sin(y_1)*l
y=np.cos(y_1)*l
#print x 
#print y

plt.plot(t,x)
#plt.show()

##Animation 
fig = plt.figure()
ax = plt.axes(xlim=(-5,5), ylim(-2,2))
line, = ax.plt([], [], lw=2)

def init():
	line.set_data([],[])
	return line,

##Se me dificulto la parte de la animacion 


