# Q1: Câu nào sau đây là đúng để
# tạo mảng 1 chiều từ 0 đến 9

import numpy as np
arr = np.arange(0, 10, 1)
print(arr)

# Q2: Cách tạo một mảng boolean 3x3
# với tất cả giá trị là True

print(np.ones((3, 3)) > 0)
print(np.ones((3, 3), dtype=bool))
print(np.full((3, 3), fill_value=True, dtype=bool))

# Q3

arr = np.arange(0, 10)
print(arr[arr % 2 == 1])

# Q4

arr = np.arange(0, 10)
arr[arr % 2 == 1] = -1
print(arr)

# Q5

arr = np.arange(10)
arr_2d = arr.reshape(2, -1)
print(arr_2d)

# Q6

arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=0)
print("Result: \n", c)

# Q7

arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=1)
print("C = ", c)

# Q8

arr = np.array([1, 2, 3])
print(np.repeat(arr, 3))
print(np.tile(arr, 3))

# Q9

a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((a >= 5) & (a <= 10))
print("result", a[index])

# Q10


def maxx(x, y):
    if x >= y:
        return x
    else:
        return y


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a, b))

# Q11
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print("Result", np.where(a < b, b, a))
