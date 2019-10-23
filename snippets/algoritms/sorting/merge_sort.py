'''
Merge sort
==========
'''

def merge_sort(arr):
	count = 0
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]

		merge_sort(L)
		merge_sort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if i < j and arr[i] > arr[j]:
				count+=1

			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
	print(count)
	
a = merge_sort([2,3,1,4,5,0,8])
print(a)