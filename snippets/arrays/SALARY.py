for i in range(int(input())):
	w = int(input())
	s = list(map(int, input().split()))
	m = min(s)
	print(sum(s)- m*w )
