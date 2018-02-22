import numpy as np
import sklearn as skl

def GenerateX():
	x = np.random.uniform()
	return(x)

def GenerateYGivenX(x):

	r = np.random.uniform()
	
	if(x < 0.2 or x > 0.8):
	
		if(r <= 0.9):
			y = 1
		else:
			y = 0
	else:
		if(r <= 0.2):
			y = 1
		else:
			y = 0
	
	return(y)

def GenerateFeatureMatrix(n, d):

	#fill vector of ones
	ones = np.ones(n)

	#create vector of uniform(0,1) random variables
	X = np.random.rand(n)

	#column bind these two vectors
	mat = np.column_stack((ones, X))

	#create vectorized version of pow function
	vexp = np.vectorize(pow)

	print(X)
	for i in range(2, d):
		print(vexp(X,d))

GenerateFeatureMatrix(4,4)
