import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# Tom Wallace
# STAT 672
# Spring 2018
# Homework 2

#####                     #####
#####     Problem 1 C     #####
#####                     #####

# we use np.random.uniform() to generate X ~ uniform(0,1)

# function to generate Y given X
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

# vectorized version of function
v_GenerateYGivenX = np.vectorize(GenerateYGivenX)

# run many iterations of the above functions
# plot results to verify correctness

# set random seed
np.random.seed(88)

# generate 10k x
X = np.random.rand(10000)

# generate 10k y | x
Y = v_GenerateYGivenX(X)

# round X to 2 digits
v_round = np.vectorize(np.round)
X = v_round(X, 2)

# count number of y=1 for every x
histX = np.arange(0, 1, 0.01)

histY = np.zeros(len(histX))

for i in range(0, len(histX)):
	for j in range(0, len(X)):
		if( histX[i] == X[j] and Y[j] == 1 ):
			histY[i] = histY[i]+1
# bin X's into 10 bins

histX2 = np.arange(0, 1, 0.1)
histY2 = np.zeros(10)

histY2[0] = sum(histY[0:9])
histY2[1] = sum(histY[10:19])
histY2[2] = sum(histY[20:29])
histY2[3] = sum(histY[30:39])
histY2[4] = sum(histY[40:49])
histY2[5] = sum(histY[50:59])
histY2[6] = sum(histY[60:69])
histY2[7] = sum(histY[70:79])
histY2[8] = sum(histY[80:89])
histY2[9] = sum(histY[90:99])

plt.bar(x=histX2, height=histY2, width=0.155555)
plt.title("10,000 Simulations of Y|X")
plt.xlabel("X")
plt.ylabel("N(Y=1|X=x)")
plt.savefig("hist.png")

# code to generate feature matrix for arbitrary dimensions d and number of
# observations n
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

# 

X1 = GenerateFeatureMatrix(100, 1)
y1 = v_GenerateYGivenX(X1[:,1])
lr1 = linear_model.LogisticRegression(C=1e5)
lr1.fit(X1, y1)
print(lr1.predict_proba(X1))


X2 = GenerateFeatureMatrix(100, 2)
y2 = v_GenerateYGivenX(X2[:,1])
lr2 = linear_model.LogisticRegression(C=1e5)
lr2.fit(X2, y2)
print(lr2.predict_proba(X2))

X2 = GenerateFeatureMatrix(100, 2)
y2 = v_GenerateYGivenX(X2[:,1])
lr2 = linear_model.LogisticRegression(C=1e5)
lr2.fit(X2, y2)
print(lr2.predict_proba(X2))
	

