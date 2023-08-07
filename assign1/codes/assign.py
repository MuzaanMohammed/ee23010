import numpy as np

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





















    
