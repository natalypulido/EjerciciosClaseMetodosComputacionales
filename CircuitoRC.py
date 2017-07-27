import numpy as np 
import matplotlib.pyplot as plt

#Me guie del notebook 

data = np.genfromtxt("CircuitoRC.txt")


t_obs = data[:,0]
obs = data[:,1]

def carga_model(t,Resistencia,Capacitancia):
	return 10.0*C*(1-np.exp(-t/R*C))  


def likelihood(obs,model):
	chi_squared = (1*10**-5)*(1.0/2.0)*np.sum((obs-model)**2)
	return np.exp(-chi_squared)




Resistencia_walk = np.empty((0))
Capacitancia_walk = np.empty((0))
l_walk = np.empty((0))

Resistencia_walk = np.append(Resistencia_walk,np.random.random())
Capacitancia_walk = np.append(Capacitancia_walk,np.random.random())


carga_init = carga_model(t_obs,Resistencia_walk[0],Capacitancia_walk[0])
l_walk = np.append(l_walk,likelihood(obs,q_init))

it= 2000

for i in range(it):
	Resistencia_p = np.random.normal(Resistencia_walk[i],0.1)
	Capacitancia_p = np.random.normal(Capacitancia _walk[i],0.1)
	

	

