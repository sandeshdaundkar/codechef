'''
Count number of vowels in a string
'''

vowels = {'a', 'e', 'i', 'o', 'u'}

def vowels_count(word):
	word = word.lower()
	count = 0
	for e in word:
		if e in vowels:
			count += 1
	print(count)

vowels_count('sandeshdaundkar')
