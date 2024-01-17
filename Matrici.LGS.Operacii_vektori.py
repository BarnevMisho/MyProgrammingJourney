import numpy as np ;
import matplotlib . pyplot as pl ;
import IPython . display as dp ;
import sympy as sp ;

'''
# Parameter :
G = sp . Matrix ([[2 ,3 ,1 ,8] ,[1 , -2 , -1 , -3] ,[4 ,1 , -3 ,6]]);
# Berechnungen :
H = G . rref ();
# Ausgabe :
dp . display (G);
print("\n")
dp.display(H[0])

'''
'''
a = np.array([3, 1.3, -2.4])
b = np.array([2.0, 1.0, 0.5])
c = np.linalg.solve(a, b)
print(c)
#c = np.dot(a,b)
x=np.array([1,2,3])
y=np.array([4,5,6])
print("\n" ,np.cross(x,y))
u = np.linalg.norm(x)
print("\n", u)

'''

np.eye(3) # einheitsmatrix
sp.eye(2,3)
np.diag((2,5)) #diagonalmatrix
np.ones((3,3)) 
sp.ones(2,3)
np.zeros((3,3))
sp.zeros(2,3)
A = np.array([
    [2 ,3 ,1],
    [1 , -2 , -1],
    [4 ,1 , -3]
            ])
b = np.array([[2,-4,2], [4,1,0], [5,-3,-3]])
M = A.T #Transponirane
P = A @ b #umnojenie pri numpy
R = A * b #umnojenie pri sympy
I = np.linalg.inv(A) 
O = A.inv() 
np.linalg.det(A)
np.trace(A)
np.poly(A)
np.linalg.eig(A)
A.charpoly() #pri sympy
x = sp.symbols("x")
A = sp.Matrix([
    [0.5-x, -np.sqrt(2)/2, 0.5],
    [np.sqrt(2)/2, -x,-np.sqrt(2)/2],
    [0.5, np.sqrt(2)/2, 0.5-x]
            ])
dp.display(A.det())
dp.display(A.charpoly())
dp.display(A.eigenvals(), A.eigenvects())

