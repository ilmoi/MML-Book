import numpy as np
import scipy.linalg as la
from sympy import * 

##exercise 2.5
#a = np.array([1,-1,0,0,1,3])
#b = np.array([1,1,0,-3,0,6])
#c = np.array([2,-1,0,1,-1,5])
#d = np.array([-1,2,0,-2,-1,-1])
#
#b = b-a
#c = c-2*a
#d = d+a
#b = b-c
#c = c-b
#d = d-b
#c = c-d*2
#d = d-c*2
#a +=b
#a+=4*c
#b+=4*c

#exercise 2.7
#a = np.array([-6,4,3,0])
#b = np.array([2,-4,3,0])
#c = np.array([0,2,-3,0])
#
#b*=3
#b+=a
#c*=4
#c+=b
#a= a/(-6)
#b= b/(-8)
#a+=b*2/3

#exercise 2.13
#HOW TO DO RREF
#from sympy import * 
#a2 = Matrix([[1,2,3,9],[2,-1,1,8],[3,0,-1,3]])
#a_rref = a2.rref()
#print(a_rref)
#PROOF: https://i.stack.imgur.com/ST1qx.png

a = Matrix([[1,2,-1,-1,2,-3],[1,-1,1,-2,-2,6],[-3,0,-1,2,0,-2],[1,-1,1,1,0,-1]])
#a = Matrix([[1,0,2,0,0],[0,1,4,0,0],[-1,1,0,np.sqrt(3),0]])
a_rref = a.rref()
print(a_rref)

#a = np.array([[1,0,1],[2,-1,0],[-1,2,-1]])
#b = np.linalg.det(a)