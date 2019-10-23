'''
Given an array and an element, find the last occurrence index of the element.
'''

def last_occurrence(arr, e):
	idx = -1

	for i in range(len(arr)):
	    if arr[i] == e:
	        idx = i
	    
	print(idx)

last_occurrence([2,3,4,1,2,7], 2)
