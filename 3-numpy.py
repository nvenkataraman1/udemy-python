## Lecture 7: Creating arrays

import numpy as np

my_list1 = [1,2,3,4]

my_array1 = np.array(my_list1)
my_array1

my_list2 = [11,22,33,44]

my_lists = [my_list1, my_list2]

my_array2 = np.array(my_lists)
my_array2

my_array2.shape ## dimensions

my_array2.dtype ## datatype

np.zeros(5) ## special form: initialize array with zeroes

my_zero_array = np.zeros(5)

my_zero_array.dtype

np.ones(5) ## special form: initialize array with ones

np.ones([5,5]) ## special form: multi-dimensional array

np.empty(4) ## same as np.zeroes

np.eye(5) ## identity matrix

np.arange(5) ## sequence

np.arange(10,100,2) ## start, stop, step size

## Lecture 8: Using arrays and scalars

