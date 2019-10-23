'''
Given a string s = 'azcbobobeeghakl', find the longest substring with characters in alphabetical sequence
'''

def sequential_substring(word):
	start = 0
	end = 1
	result = word[0]
	while end < len(word):
		if word[end-1] <= word[end]:
			if len(result) <= len(word[start: end+1]):
				result = word[start: end+1]
			end += 1
		else:
			start = end
			end += 1
	print(result)

sequential_substring('azcbobobeeghakl')
