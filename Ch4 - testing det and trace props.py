import numpy as np

# to test during lesson
#A = np.array([[1,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
#C_inv = np.array([[1,1,1,1],[0,-1,-1,-1],[0,0,1,0],[0,0,0,1]])
#C = np.linalg.inv(C_inv)
#D = C_inv@A@C

a = np.array([[3,0,2],[2,1,-2],[1,2,1]])
#a = a.T@a
b = np.array([[9,2,3],[2,0,2],[-1,2,1]])
#b = b.T@b
c = np.array([[3,0,2],[1,-3,2],[2,2,1]])
#c = c.T@c
det_a = np.linalg.det(a)
det_b = np.linalg.det(b)
det_c = np.linalg.det(c)

trace_a = np.trace(a)
trace_b = np.trace(b)
trace_c = np.trace(c)

#1 testing MULTIPLICATION
#testing det total
t11 = det_a*det_b*det_c - np.linalg.det(a@b@c) 
#testing det cyclicity
t12 = np.linalg.det(a@b@c) - np.linalg.det(c@a@b) 
#testing det random permutations
t13 = np.linalg.det(a@b@c) - np.linalg.det(a@c@b) 

#testing trace total
t14 = trace_a*trace_b*trace_c - np.trace(a@b@c) 
#testing trace cyclicity
t15 = np.trace(a@b@c) - np.trace(c@a@b) 
#testing trace random permutations
t16 = np.trace(a@b@c) - np.trace(a@c@b) 

#2 testing CHANGE OF BASIS
vals_a, vecs_a = np.linalg.eig(a)
#NO YOU DONT NEED TO ORDER AND NORMALIZE, YOU COULD IF YOU WANTED TO THOUGH
#idx = vals_a.argsort()[::-1]
#vals_a = vals_a[idx]
#vecs_a = vecs_a[:,idx]
#vecs_a = vecs_a/np.linalg.norm(vecs_a, axis=0)
vecs_a_inv = np.linalg.inv(vecs_a)
#sigma = np.array([[vals_a[0],0,0],[0,vals_a[1],0],[0,0,vals_a[2]]])
#test_sigma = vecs_a@sigma@vecs_a_inv

sigma = vecs_a_inv@a@vecs_a
t21 = np.linalg.det(a) - np.linalg.det(sigma) 
t22 = np.trace(a) - np.trace(sigma) 

#3 testing sum
t31 = det_a + det_b + det_c - np.linalg.det(a+b+c)
t32 = trace_a + trace_b + trace_c - np.trace(a+b+c)

#4 testing alpha
t41 = 5*det_a - np.linalg.det(a*5)
t42 = 2.4*det_b - np.linalg.det(b*2.4)
t43 = -5*det_c - np.linalg.det(-5*c)
#we know trace works so cba

#5 testing transpose
#we know det works so cba
t51 = np.trace(a) - np.trace(a.T)
t52 = np.trace(b) - np.trace(b.T)
t53 = np.trace(c) - np.trace(c.T)

#6 testing inverse
#det
t60 = np.linalg.det(a) - 1/np.linalg.det(np.linalg.inv(a))

t61 = np.trace(a) - 1/np.trace(np.linalg.inv(a))
t62 = np.trace(b) - 1/np.trace(np.linalg.inv(b))
t63 = np.trace(c) - 1/np.trace(np.linalg.inv(c))

#7 testing 


""" summary of properties for f = det / tr
signe volume / derivative of the determinant (near the identity matrix)
f(ABC) = f(A) * f(B) * f(C) : yes / no
f(ABC) = f(CAB) : yes / yes => both are cyclically permutable
f(ABC) = f(ACB) : yes / no => only det commutative
f(A) = f(sigma) : yes / yes => both indifferent to change of basis
f(A+B) = f(A) + f(B) = no / yes
f(aA) = af(A) : no / yes
f(A) = f(A.T) : yes / yes
f(A-1) = 1/f(A) : yes / no
I = 1 / n

"""