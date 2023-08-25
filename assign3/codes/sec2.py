
import sys                                          #for path to external scripts
#sys.path.insert(0, '/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/CoordGeo')        #path to my scripts
sys.path.insert(0,'solutions/codes/CoordGeo')        #path to my scripts
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
#sys.path.insert(0, '/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/CoordGeo')        #path to my scripts

#if using termux
import subprocess
import shlex
#end if

#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 

np.set_printoptions(precision=2)

def midpoint(x,y):
	return (x+y)/2

def norm_vec(A,B):
	return np.matmul(omat, dir_vec(A,B))

#direction
def dir_vec(A,B):
	return B-A

#given coordinates A,B,C
A=np.array([1,-1])
B=np.array([-2,2])
C=np.array([-5,-3])

#Given D,E,F are midpoints of BC,CA,AB
D=midpoint(B,C)
E=midpoint(C,A)
F=midpoint(A,B)

#intersection of lines
def line_intersect(n1,A1,n2,A2):
	N=np.block([[n1],[n2]])
	p = np.zeros(2)
	p[0] = n1@A1
	p[1] = n2@A2
	#Intersection
	P=np.linalg.inv(N)@p
	return P
G=line_intersect(norm_vec(F,C),C,norm_vec(E,B),B)
print("("+str(G[0])+","+str(G[1])+")")

#Hence verified that A - F = E - D and AFDE is a parallelogram
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_BE = line_gen(B,E)
x_CF = line_gen(C,F)
x_AD = line_gen(A,D)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')
plt.plot(x_CF[0,:],x_CF[1,:],label='$CF$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
#Labeling the coordinates
A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)
D = D.reshape(-1,1)
E = E.reshape(-1,1)
F = F.reshape(-1,1)
G = G.reshape(-1,1)
tri_coords = np.block([[A, B, C, D, E, F, G]])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for i, txt in enumerate(vert_labels):
    offset = 10 if txt == 'G' else -10
    plt.annotate(txt,
                 (tri_coords[0, i], tri_coords[1, i]),
                 textcoords="offset points",
                 xytext=(0, offset),
                 ha='center')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig("Triangle2.png",bbox_inches='tight')