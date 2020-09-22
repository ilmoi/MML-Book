import numpy as np

x = np.array([1,2,3])


#=========== CASE1: A = square, full rank
I = np.array([[1,0,0],[0,1,0],[0,0,1]])
A = np.array([[1,3,3],[4,5,6],[7,8,9]])
A_det = np.linalg.det(A)

#y
y = A@x
x_rec = np.linalg.inv(A)@y

#covariance
C = A@I@A.T
C_det = np.linalg.det(C)
C_vals,C_vecs = np.linalg.eig(C)
I_rec = np.linalg.inv(A)@C@np.linalg.inv(A.T)




#=========== CASE2: A = non-square, full rank
I = np.array([[1,0,0],[0,1,0],[0,0,1]])
A = np.array([[1,3,3],[4,5,6],[7,8,9],[7,8,10]])
#there is no A det, since A is not square

#y
y = A@x
x_rec = np.linalg.inv(A.T@A)@A.T@y #pseudo-inverse because otherwise no inverse for non-square matrix

#covariance
C = A@I@A.T
C_det = np.linalg.det(C)
C_vals,C_vecs = np.linalg.eig(C)
I_rec = np.linalg.inv(A.T@A)@A.T@C@A@np.linalg.inv(A.T@A) #pseudo-inverse because otherwise no inverse for non-square matrix



#=========== CASE3: A = square, but not full rank
I = np.array([[1,0,0],[0,1,0],[0,0,1]])
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
noise = np.array([[0,0,0.00001],[0,0,0],[0,0,0]]) #interesting. so i tried adding values from 0 to 1 to various ones - they all pretty much give the same C, so adding noise must work!!
A = A+noise
A_det = np.linalg.det(A)

#y
y = A@x
x_rec = np.linalg.inv(A)@y

#covariance
C = A@I@A.T
C_det = np.linalg.det(C)
C_vals,C_vecs = np.linalg.eig(C)
I_rec = np.linalg.inv(A)@C@np.linalg.inv(A.T)