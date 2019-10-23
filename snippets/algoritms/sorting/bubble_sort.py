'''
Bubble sort
===========
It is based on idea of repeatedly comparing pair of adjacent elements 
and then swapping their position if they exist in wrong order.

Time complexity is - O(n^2)
'''

def bubble_sort(arr):
	for i in range(len(arr)):	# iterating through the list
		for k in range(len(arr)-i-1):	
		# comparing between elements after swapping (n-i-1), to not include sorted elements.
			if arr[k] > arr[k+1]:
				arr[k], arr[k+1] = arr[k+1], arr[k]		# swapping elements
	print(arr)

bubble_sort([7,4,5,2, 1, 1, 3, 6])
