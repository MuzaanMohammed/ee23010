import numpy as np
import matplotlib.pyplot as plt
import sympy

A = np.array([3.0, 4.0])  # Use floating-point numbers
B = np.array([-4.0, 6.0])  # Use floating-point numbers
C = np.array([-3.0, -5.0])  # Use floating-point numbers
#returning coefficients of the perpendicular bisector and constant 
def perpendicular_bisector(B, C):
    midpoint = (B + C) / 2
    direction = B - C
    
    
   
    constant = direction.T @ midpoint

    equation_coeffs = np.concatenate((direction, [-constant]))
    return equation_coeffs



equation_coeff1 = perpendicular_bisector(A, B)
equation_coeff2 = perpendicular_bisector(B, C)
equation_coeff3 = perpendicular_bisector(C, A)

print(f'Equation coefficients for AB: {equation_coeff1}')
print(f'Equation for AB: ({equation_coeff1[0]:.2f})x + ({equation_coeff1[1]:.2f})y + ({equation_coeff1[2]:.2f}) = 0')

print(f'Equation coefficients for BC: {equation_coeff2}')
print(f'Equation for BC: ({equation_coeff2[0]:.2f})x + ({equation_coeff2[1]:.2f})y + ({equation_coeff2[2]:.2f}) = 0')

print(f'Equation coefficients for CA: {equation_coeff3}')
print(f'Equation for CA: ({equation_coeff3[0]:.2f})x + ({equation_coeff3[1]:.2f})y + ({equation_coeff3[2]:.2f}) = 0')


#To find the intersection of the perpendicular bisectors
# Coefficient Matrix
M = np.array([equation_coeff1, equation_coeff2])

# Row reduced echelon form
res,pivots=sympy.Matrix(M).rref()
value1 = -res[0, 2]  # x value
value2 = -res[1, 2]  # y value

# Generate points along a line
def line_gen(A, B):
    len = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim, len))
    lam_1 = np.linspace(0, 1, len)
    for i in range(len):
        temp1 = A + lam_1[i] * (B - A)
        x_AB[:, i] = temp1.T
    return x_AB

# Generating all lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

# Plotting all lines
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
plt.plot(x_BC[0, :], x_BC[1, :], label='$BC$')
plt.plot(x_CA[0, :], x_CA[1, :], label='$CA$')

# Midpoint of each line
def midpoint(P, Q):
    return (P + Q) / 2

# Perpendicular bisector
def line_dir_pt(m, A, k1=0, k2=1):
    len = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim, len))
    lam_1 = np.linspace(k1, k2, len)
    for i in range(len):
        temp1 = A + lam_1[i] * m
        x_AB[:, i] = temp1.T
    return x_AB

# Calculate the perpendicular vector and plot arrows
def perpendicular(B, C, label):
    BC_direction = B - C
    perpendicular = np.array([-BC_direction[1], BC_direction[0]])
    mid = midpoint(B, C)
    x_D = line_dir_pt(perpendicular, mid, 0, 1)
    plt.arrow(mid[0], mid[1], perpendicular[0], perpendicular[1], color='blue', head_width=0.4, head_length=0.4, label=label)
    plt.arrow(mid[0], mid[1], -perpendicular[0], -perpendicular[1], color='blue', head_width=0.4, head_length=0.4)
    return x_D

x_D = perpendicular(A, B, 'OD')
x_E = perpendicular(B, C, 'OE')
x_F = perpendicular(C, A, 'OF')






# Label the triangle vertices and intersection point

mid12 = midpoint(A, B)
mid23 = midpoint(B, C)
mid31 = midpoint(C, A)
intersection = np.array([value1,value2])


points = {'A': A, 'B':B, 'C': C, 'D': mid12, 'E': mid23, 'F': mid31,'O':intersection }
for label, point in points.items():
  plt.annotate(label, point, textcoords="offset points", xytext=(0, 10), ha='center', fontsize=12)
  #labelling the 90 degree angle
  if label in ['D', 'E', 'F']:
    plt.text(point[0], point[1], ' L90°', fontsize=12, color='black', ha='center', va='center')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()



















    
