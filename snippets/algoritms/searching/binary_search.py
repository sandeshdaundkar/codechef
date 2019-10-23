'''
Binary search works only on a sorted set of elements.
Time complexity of binary search is - O(logN)

'''

def binary_search(arr, element):
	low = 0
	high = len(arr)
	while low < high:
		mid = (low+high)//2
		if (arr[mid] < element):
			low = mid  + 1
		elif (arr[mid] > element):
			high = high - 1
		else:
			print(mid)
			return
	print(-1)


binary_search([4,5,6,7,8], 7)
