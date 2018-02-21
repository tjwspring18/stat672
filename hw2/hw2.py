import numpy as np

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

x = GenerateX()
y = GenerateYGivenX(0.2)

print(x)

print(y)
