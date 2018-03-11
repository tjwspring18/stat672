import sklearn as skl
import scipy as sp
import numpy as np

# read data
X = np.genfromtxt('hw3_X.csv', delimiter = ',')
Y = np.genfromtxt('hw3_Y.csv', delimiter = ',')

# function to generate \Phi from X
def GeneratePhiMatrix(X):

	# get dimensions of X
	nrow = X.shape[0]
	ncol = X.shape[1]

	# preallocate final array
	mat = np.zeros((nrow, int(ncol*2 + sp.special.comb(ncol, 2))))

	# take quadratic form of X
	# assign to final array
	quad = pow(X, 2)
	mat[0:nrow, 0:ncol] = quad

	# create empty list
	lst = list()

	# generate all interaction terms
	# apppend to list
	for i in range(0, ncol):
		for j in range(i, ncol):
			col = quad[:,i] * quad[:,j]
			#col = np.reshape(quad[:,i] * quad[:,j], (-1, 1))
			lst.append(col)
	
	# append columns from list to preallocated array
	for i in range(0, len(lst)):
		col = lst[i]
		mat[0:nrow, ncol+i] = col

	return(mat)


print(GeneratePhiMatrix(X).shape)

'''
a = np.array([np.arange(1,3081), np.arange(1,3081)])
b = np.arange(1,3181)

# function to create test X
def GenerateTestX(X, i):

	# get number of columns in X
	ncol = X.shape[1]

	# select every i'th column as part of test
	train = X[:, range(i-1, ncol+1, i)]

	return(train)

# function to create test Y
def GenerateTestY(Y, i):

	# get number of rows in Y
	nrow = Y.shape[0]

	# select every i'th row as part of test
	train = Y[range(i-1, nrow+1, i)]

	return(train)

print(GenerateTestY(Y, 4).shape)

# function to create test matrix
#def GenerateTestMatrix(X):

# function to center matrix
#def CenterMatrix(X):

# function to scale matrix
#def ScaleMatrix(X):

# generate lambda

# compute SVD of X_train

# calculate \hat{w}_{ridge}

# function to compute test error
'''
