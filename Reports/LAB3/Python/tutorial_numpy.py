import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a[0] # This gives us the first row of a
a[2] # This gives us the third row of a
a[:,1] # this gives us the second column of a
a[2][2] # this gives us the value of a(2,2), which is 9 here

print(a[:,1] )
a = np.array([1,2,3,4,5,6,7])
b = np.resize(a, (1,7)) # array([[1, 2, 3, 4]])
print(b)



# Question 1
array1 = np.array([0, 10, 4, 12])
result = array1 - 20
shape_of_array1 = array1.shape
print("Result after subtracting 20:", result)
print("Shape of array1:", shape_of_array1)

# Question 2
array2 = np.array([[0, 10, 4, 12], [1, 20, 3, 41]])
array2_new = np.array([array2[0, [2, 3]], array2[1, [0, 1]]])
print("array2_new:", array2_new)

# Question 3
horizontal_sequence = np.hstack((array1, array1))
array3 = np.vstack((horizontal_sequence, horizontal_sequence, horizontal_sequence, horizontal_sequence))
print(array3)

# Question 4 
array41 = np.arange(-3, 16, 6)
print("array41:", array41)
array42 = np.arange(-7, -20, -2)
print("array42:", array42)

# Question 5
array5 = np.linspace(0, 100, 49)
print(array5)

# Question 6
array6 = np.zeros((3, 4), dtype=int)

array6[0] = [12, 3, 1, 2]    
array6[:, 1] = [3, 0, 2]    
array6[2, :2] = [4, 2]       
array6[2, 2:] = [3, 1]       
array6[:, 2] = [1, 1, 3] 
array6[1, 3] = 2            
print(array6[0])     # [12 3 1 2]
print(array6[1,0])   # 0
print(array6[:,1])   # [3 0 2]
print(array6[2, :2]) # [4 2]
print(array6[2, 2:]) # [3 1] 
print(array6[:,2])   # [1 1 3]
print(array6[1,3])   # 2

# Question 7
string7 = "1,2,3,4"

row_values = np.array([int(num) for num in string7.split(',')])
array7 = row_values
for i in range(99):
    array7 = np.vstack((array7, row_values))

print("Shape of array7:", array7.shape)
print(array7)