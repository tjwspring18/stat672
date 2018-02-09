# Tom Wallace
# STAT 672
# Spring 2018
# HW #1 code submission

import numpy as np

# UnitBallRejectionSampling(d, n)
#
# Draw n random vectors from d-dimensional unit ball.
#
# Does so by generating a candidate vector, each coordinate of which is a random
# draw from a uniform (-1,1) distribution, and rejecting any candidate vector
# with a Euclidean norm >= 1
#
# Outputs observed probability of accepting a candidate vector
#
# Arguments:
#           d = dimensions (integer, 2 < d < \infty)
#           n = number of vectors to draw (integer, n > 0)
#
# Returns:
#           prints probability of acceptance
#
def UnitBallRejectionSampling(d, n):
	
	n_candidates = 0
	n_accepted = 0
	#vectorList = []
	
	while(n_accepted < n):

		#generate empty vector of length d
		vector = np.empty(d)

		#fill with (-1,1) random variables
		for i in range(0, d):
			vector[i] = np.random.uniform(-1,1)

		#update n_candidates
		n_candidates += 1

		#take Euclidean norm
		euclidean_norm = np.linalg.norm(vector, ord=2) 
		
		#accept only if Euclidean norm <= 1
		if(euclidean_norm <= 1):
			#print(vector)
			#vectorList.append(vector)
			n_accepted += 1
		else:
			pass

	#calculate and print observed probability of acceptance
	prob_accept = n_accepted / n_candidates
	print(prob_accept)


UnitBallRejectionSampling(10,100)
