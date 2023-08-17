#total number of students
T = 23
#number of students in each house
A, B, C, D = 4, 8, 5, 2
E = T - (A + B + C + D)
#no of students not in A,B and C
W = T - (A + B + C)
print("The probability that the selected student is not from A, B, and C is:")
print(W, '/', T, '=', W / T)
