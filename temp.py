import numpy as np

#to check with tom 2.20
#A = np.array([[1,1],[-1,3],[1,-5]])
#b = np.array([[2,-1],[1,-1]])
#c = np.array([[1,0,1],[2,-1,0],[-1,2,-1]])
#
#Cb = np.linalg.inv(b)
#Cc = c
#Af = Cc@A@Cb

a = np.array([[1,0],[0,6]])
b = a.T@a