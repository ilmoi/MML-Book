import numpy as np

Xa = np.array([[1,0],[0,1]])
Xb = np.array([[1,1],[0,2]])
C_inv = Xb
C = np.linalg.inv(C_inv)
A = np.array([[2,1],[0,2]])
D = C_inv@A@C
TXa = A@Xa
TXb = D@Xb
E = np.linalg.solve(np.linalg.inv(TXa),np.linalg.inv(TXb))

#E2 = np.linalg.inv(A)@C@D
E2 = A@C@np.linalg.inv(D)
TXa2 = E@TXb
Xa2 = np.linalg.inv(A)@TXa
A2 = C@D@np.linalg.inv(C)
#
#
#Xa = np.array([[1,0],[0,1]])
#Xb = np.array([[1,1],[0,2]])
#C = Xb
#A = np.array([[2,1],[0,2],[1,2]])
#
#TXa = A@Xa
#Xb2 = C@Xa
#Xa2 = np.linalg.inv(C)@Xb
#
