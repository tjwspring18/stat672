import numpy as np

def GenerateXPlusVector(d):

	vector = np.empty(d)

	for i in range(0, d):

		vector[i] = np.random.normal(5/np.sqrt(d), 4)
	
	return(vector)

def GenerateXMinusVector(d):

	vector = np.empty(d)

	for i in range(0, d):

		vector[i] = np.random.normal(-5/np.sqrt(d), 1)

	return(vector)

def ComputeError(x_plus, x_minus, z):

	norm1 = np.linalg.norm((x_plus - z))
	norm2 = np.linalg.norm((x_minus - z)) 

	if(norm1 > norm2):
		return(1)
	else:
		return(0)

def RunSimulation(n, d):

	frequency = 0

	for i in range(0, n):
		
		x_plus = GenerateXPlusVector(d)
		z = GenerateXPlusVector(d)
		x_minus = GenerateXMinusVector(d)

		frequency += ComputeError(x_plus, x_minus, z)

	print(d, frequency)


for d in [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]:

	RunSimulation(1000, d)

		
		

