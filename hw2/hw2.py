import numpy as np
from sklearn import linear_model

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

v_GenerateYGivenX = np.vectorize(GenerateYGivenX)

def GenerateFeatureMatrix(n, d):

	#fill vector of ones
	ones = np.ones(n)

	#create vector of uniform(0,1) random variables
	X = np.random.rand(n)

	#column bind these two vectors into a matrix
	mat = np.column_stack((ones, X))

	#create vectorized version of pow function
	vexp = np.vectorize(pow)

	#raise vector X to the 2, 3...d power
	#column bind this new vector with our matrix
	for i in range(2, d+1):
		vec = vexp(X,i)
		mat = np.column_stack((mat, vec))
	
	#return the matrix
	return(mat)

fm = GenerateFeatureMatrix(5, 3)
y = v_GenerateYGivenX(fm[:,1])

lr = linear_model.LogisticRegression(C=1e5)

lr.fit(X=fm, y=y)

print(lr.predict_proba(fm))


	

