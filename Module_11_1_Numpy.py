import numpy as np

arr = np.array([[2,4,6], [3,7,11], [1,18,22]])
print(arr)

z_arr = np.zeros((3,3))
print(z_arr)

arr_1 = np.ones((3,3))
print(arr_1)

range_arr = np.arange(5,21,3)
print(range_arr)

lin_arr = np.linspace(1, 4, 6)
print(lin_arr)

summ_arr = range_arr + lin_arr
print(summ_arr)

mult_arr = range_arr * lin_arr
print(mult_arr)

print(arr[1,2])

print(arr[2])

resh_arr = range_arr.reshape(2,3)
print(resh_arr)



