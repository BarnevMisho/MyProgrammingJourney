'''
import numpy as np
a = np.array([[8,0,-10,0,-2],[6,1,-12,-1,0],[7,3,-14,-2,-1],\
              [0,1,-3,0,0]])
b = np.array([0,0,0,0])
A = np.linalg.lstsq(a,b)
print(A)

'''
import sympy as sp

A = sp.Matrix([[8,0,-10,0,-2],[6,1,-12,-1,0],[7,3,-14,-2,-1],\
              [0,1,-3,0,0]])
B = sp.Matrix([0,0,0,0])
H = (A,B)
print(sp.linsolve(H))
# s tozi mewtod se reshavat urawneniq, koito sa s parametur
# tova she reche che defekt e !=0
