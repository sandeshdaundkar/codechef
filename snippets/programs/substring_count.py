'''
Given a string find the number of time substring exists in the string.
'''
s = 'fbobbobooboobwboobpobobobobbbobbdbobbobtobobbobobl'

def substring_count(string, substring):
	count = 0
	ls = len(substring)
	for i in range(len(string) - (ls-1)):
		if string[i: i+ls] == substring:
			count += 1
	print(count)

substring_count(s, 'bwb')

