'''
Selection sort
==============
It is based on the idea of idea of finding the minimum or maximum element in 
unsorted array and then putting it in correct position  in sorted array.

Time complexity is - O(n^2)
'''

def selection_sort(arr):
	for i in range(len(arr)):	# iterating through the list
		minimum = i 	# setting minimum at i
		for j in range(i+1, len(arr)):	# In this loop, we find minimum element in the array
			if arr[j] < arr[minimum]:	# if j-th element less than minimum
				minimum = j 	# just set minimum to j-th index 
		arr[minimum], arr[i] = arr[i], arr[minimum]	# once minimum is found, swap them and iterate over.			
	print(arr)

selection_sort([2,6,3,4,1,5])
