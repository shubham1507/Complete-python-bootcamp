#numpy

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(np.__version__)

#NumPy Creating Arrays
create_arr = np.array([5,6,7,8,9])
print("Array created:", create_arr)

#NumPy Dimensions

arr_1d = np.array([1,2,3,4,5])
print("1D Array:", arr_1d)
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D Array:\n", arr_2d)
arr_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("3D Array:\n", arr_3d)

high_dim_arr = np.array([9,10,11,12], ndmin=5)
print("High Dimensional Array:\n", high_dim_arr)

#NumPy Array indexing

print("First element of 1D array:", arr_1d[0])
print("2nd element of 2D array:\n", arr_2d[0,1])
print("Element in 3D array:\n", arr_3d[0,1,1])
print('Last element from 2nd dim: ', arr_2d[1, -1])

#NumPy Array Slicing

print("Sliced 1D array:", arr_1d[1:4])
print("Sliced 2D array:\n", arr_2d[0:2, 1:3])
print("Sliced 3D array:\n", arr_3d[0:2, 0:2, 0:2])

#NumPy Array Data Types

print("Data type of 1D array:", arr_1d.dtype)
arr_float = np.array([1.0, 2.0, 3.0])
print("Data type of float array:", arr_float.dtype)
arr_int = np.array([1, 2, 3], dtype=np.int32)
print("Data type of int array:", arr_int.dtype)
arr_str = np.array(['a', 'b', 'c'], dtype=np.str_)
print("Data type of string array:", arr_str.dtype)
##Creating Arrays With a Defined Data Type

arr_defined = np.array([1, 2, 3], dtype=np.float64)
print("Array with defined data type:\n", arr_defined)
arr_defined_int = np.array([1.5, 2.5, 3.5], dtype=np.int32)
print("Array with defined integer data type:\n", arr_defined_int)   
arr_defined_str = np.array([1, 2, 3], dtype=np.str_)
print("Array with defined string data type:\n", arr_defined_str)

##Converting Data Type on Existing Arrays
arr_converted = arr_1d.astype(np.float64)
print("Converted array to float:\n", arr_converted)
arr_converted_int = arr_float.astype(np.int32)
print("Converted float array to int:\n", arr_converted_int)
arr_converted_str = arr_1d.astype(np.str_)
print("Converted array to string:\n", arr_converted_str)

#NumPy Array Views and Copies

arr_original = np.array([1, 2, 3, 4, 5])
x = arr_original.copy()
y = arr_original.view()
print("Original array:", arr_original)
print("Copy of original array:", x)
print("View of original array:", y)
x[0] = 10
print("Modified copy (x):", x)
arr_original[1] = 20
print("Original array after modifying copy:", arr_original)
print("View (y) after modifying original array:", y)

#NumPy Array Shape and Reshaping

arr_shape = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", arr_shape)
print("Shape of original array:", arr_shape.shape)
reshaped_arr = arr_shape.reshape(3, 2)
print("Reshaped array (3, 2):\n", reshaped_arr)
flattened_arr = arr_shape.flatten()
print("Flattened array:\n", flattened_arr)

#NumPy Array Iteration

arr_iter = np.array([[1, 2, 3], [4, 5, 6]])
print("Iterating over 2D array:")
for row in arr_iter:
    print("Row:", row)
    for element in row:
        print("Element:", element)

# NumPy Array joining 

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr3 = np.array([[7, 8], [9, 10]])
arr4 = np.array([[11, 12],[13,14]])
joined_arr = np.concatenate((arr1, arr2), axis=0)
joined_arr2 = np.concatenate((arr3, arr4), axis=1)
print("Joined array:", joined_arr)
print("Joined 2D array:\n", joined_arr2)

ex_hstacked_arr = np.hstack((arr3, arr4))
print("Horizontally stacked array:\n", ex_hstacked_arr) 
ex_vstacked_arr = np.vstack((arr3, arr4))
print("Vertically stacked array:\n", ex_vstacked_arr)
ex_dstacked_arr = np.dstack((arr3, arr4))
print("Depth stacked array:\n", ex_dstacked_arr)

#NumPy Array Splitting


arr_split_ex  = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.array_split(arr_split_ex, 3)
print("Split array into 3 parts:", split_arr)
access_split_part = split_arr[0][1]
print("Accessing first part of split array:", access_split_part)

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
split_2d_arr = np.array_split(arr, 3)
print("Split 2D array into 3 parts:", split_2d_arr)

#NumPy Array Searching

arr_search = np.array([1, 2, 3, 4, 5, 6])
index_of_4 = np.where(arr_search == 4)
print("Index of element 4:", index_of_4)
index_of_greater_than_3 = np.where(arr_search > 3)
print("Indices of elements greater than 3:", index_of_greater_than_3)
arr_2d_search = np.array([[1, 2], [3, 4], [5, 6]])
index_2d = np.where(arr_2d_search == 4)
print("Index of element 4 in 2D array:", index_2d)
index_search_sorted = np.searchsorted(arr_search, 4)
print("Index to insert 4 in sorted array:", index_search_sorted)

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)


#NumPy Array Sorting

arr_sort = np.array([5, 2, 9, 1, 5, 6])
sorted_arr = np.sort(arr_sort)
print("Sorted array:", sorted_arr)
arr_2d_sort = np.array([[3, 2], [1, 4]])
sorted_2d_arr = np.sort(arr_2d_sort, axis=0)
print("Sorted 2D array along columns:\n", sorted_2d_arr)
sorted_2d_arr_row = np.sort(arr_2d_sort, axis=1)
print("Sorted 2D array along rows:\n", sorted_2d_arr_row)


#NumPy Array Filtering

arr_filter = np.array([1, 2, 3, 4, 5, 6])
filtered_arr = arr_filter[arr_filter > 3]
print("Filtered array (elements > 3):", filtered_arr)
arr_2d_filter = np.array([[1, 2], [3, 4 ], [5, 6]])
filtered_2d_arr = arr_2d_filter[arr_2d_filter > 3]
print("Filtered 2D array (elements > 3):\n", filtered_2d_arr)

x =[True, False, True, False, True, False]
filtered_arr_bool = arr_filter[x]
print("Filtered array using boolean indexing:", filtered_arr_bool)