'''
Insertion sort
==============

'''

def insertion_sort(arr):
	for i in range(len(arr)):
		temp = arr[i]
		j = i
		while j > 0 and temp < arr[j-1]:
			arr[j] = arr[j-1]
			j -= 1
		arr[j] = temp
	print(arr)

insertion_sort([7,4,5,2,6,1,8])
