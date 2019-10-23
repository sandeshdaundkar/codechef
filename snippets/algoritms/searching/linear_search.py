'''
Linear search:

'''

def linear_search(arr, element):
	if element in arr:
		print(arr.index(element))

linear_search([3,4,5,1], 1)
