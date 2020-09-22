import numpy as np

a = np.array([[1,1],[-1,3],[1,-5]])
aTa = a.T@a
vals,V = np.linalg.eig(aTa)

#resorting by biggest value
idx = vals.argsort()[::-1]
vals = vals[idx]
V = V[:,idx]

V = V/np.linalg.norm(V,axis=0)
sigma = np.array([[np.sqrt(vals[0]),0],[0,np.sqrt(vals[1])],[0,0]])
aaT = a@a.T
vals2, U = np.linalg.eig(aaT)

#resorting by biggest value
idx2 = vals2.argsort()[::-1]
vals2 = vals2[idx2]
U = U[:,idx2]

U = U/np.linalg.norm(U,axis=0)

#must be equal to a
test = U@sigma@V.T

#!!!!! If it's giving me a matrix that's with the wrong signs, that's ok. Rem we can multiply each row by -1. Otherwise multiply one of the eigenvector sets (U or V) by -1
#The code works equally well for 2x3 and 3x2

#breaking down by rank
rank1 = (U[:,0]*np.sqrt(vals[0])).reshape(3,1) @ V[:,0].reshape(2,1).T
rank2 = (U[:,1]*np.sqrt(vals[1])).reshape(3,1) @ V[:,1].reshape(2,1).T
test2 = rank1+rank2