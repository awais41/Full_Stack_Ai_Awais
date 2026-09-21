# # 1
# # 1D

# import numpy as np


# a = np.array([10, 20, 30, 40])

# print(a.shape)
# print(a.ndim)

# # 2

# # 2D array

# import numpy as np
# b = np.array([[1,2,3],
#               [4,5,6]])

# print(b.shape)
# print(b.ndim)

# # 3

# # 2D array

# import numpy as np
# c = np.array([[10,20,30],
#               [40,50,60],
#               [70,80,90]])

# print(c.shape)
# print(c.ndim)


#  # 4

# import numpy as np
# c = np.array([[10, 20, 30],
#               [40, 50, 60],
#               [70, 80, 90]])

# print(c[1])       # second row
# print(c[2, 1])    # row 2, column 1
# print(c[:, 2])    # entire third column


# # 5
# # Concept 4: Element-wise Math
# a = np.array([1, 2, 3])
# b = np.array([10, 20, 30])

# print(a + b)  
# print(a - b)   
# print(a * b)   
# print(a / b)   
# print(a ** 2)  

# # 6
# # Concept 5: Broadcasting (thoda magic wala part )
# a = np.array([1, 2, 3])
# print(a + 5)     # [6, 7, 8]   <- 5 har element mein add ho gaya
# print(a * 2)     # [2, 4, 6]

# # 7
# # 2D array + 1D array

# matrix = np.array([[1, 2, 3],
#                     [4, 5, 6]])
# row = np.array([10, 20, 30])

# print(matrix + row)

# # 8
#Exercise 3
# import numpy as np 
# prices = np.array([100,200,300])
# discount = np.array([10,20,30])
# print(prices - discount)
# print(prices * 1.1)  

# grid = np.array([[1, 2], [3, 4]])
# print(grid + 10)       

# # Concept 6: Aggregation Functions

# data = np.array([10, 20, 30, 40, 50])

# print(data.sum())      # 150  -> sab elements ka total
# print(data.mean())     # 30.0 -> average
# print(data.max())      # 50   -> sabse bada
# print(data.min())      # 10   -> sabse chota
# print(data.std())      # standard deviation (spread kitna hai)
# print(data.argmax())   # 4    -> index jahan max value hai
# print(data.argmin())   # 0    -> index jahan min value hai

# # Concept 7: Aggregation with axis (2D arrays mein important)

# grid = np.array([[1, 2, 3],
#                   [4, 5, 6]])

# print(grid.sum())          # 21   -> sab elements ka total
# print(grid.sum(axis=0))    # [5, 7, 9]   -> column-wise sum (upar se neeche)
# print(grid.sum(axis=1))    # [6, 15]     -> row-wise sum (left se right)


# Exercise 4
# import numpy as np 
# marks = np.array([[85, 90, 78],
#                    [60, 95, 88],
#                    [70, 65, 92]])

# print(marks.sum(axis = 1))
# print(marks.mean(axis = 0))
# print(marks.max())

# Concept 8: Reshaping
# import numpy as np 

# a = np.arange(12)     # [0, 1, 2, ..., 11]  -> shape (12,)
# print(a)

# b = a.reshape(3, 4)    # same 12 numbers, ab 3 rows x 4 columns mein
# print(b)

# Exercise 5
# import numpy as np 

# nums = np.arange(1, 13)   # 1 se 12 tak
# print(nums)
# a = nums.reshape(3,4)

# # print(a)

# # b = nums.reshape(2, 6)
# # print(b)

# # c = nums.reshape(6, -1)   # -1 trick
# print(c)

# concept 9  
# import numpy as np 
# original = np.array([10, 20, 30, 40, 50])
# view_arr = original[1:4]
# view_arr[0] = 999 
# print(view_arr)
# print(original)



# # 9.2
# import numpy as np 
# original = np.array([0,1,2,3,4,5,6])
# copy_arr = original[1:5].copy()
# copy_arr[0]  = 999
# print(copy_arr)
# print(original)  

# 12
# Condition lagao array pe
# Concept 12: Boolean Indexing (Simple Explanation)

# import numpy as np

# a = np.array([10, 25, 3, 47, 8, 62])

# print(a[a > 20])



# 12-B
# Condition lagao array pe
# import numpy as np 
# temps = np.array([15, 22, 8, 30, 18, 25, 5, 33])
# print(temps[temps>20])

# 12-B 
# Condition lagao array pe
import numpy as np 
temps = np.array([15,22,8,30,18,25,5,33])
print(temps[(temps > 10) & (temps < 30)])
print(temps[(temps < 10) |  (temps > 30)])



# 12-C 

# Modifying values with a condition

import numpy as np 
temps = np.array([15, 22, 8, 30, 18, 25, 5, 33])
temps[temps > 20] = 0
print(temps)


# 12-D 
import numpy as np 
awa = np.array([12,34,56,78,5,45])
awa[awa > 50] = 0 
print(awa)


# Stacking & Combining Arrays
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

print(np.vstack([x,y]))
print(np.hstack([x,y]))

# Do 1D arrays banao

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.concatenate([a,b]))
 