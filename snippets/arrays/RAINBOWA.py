t = int(input())

res = []

if t in range(101):
	for i in range(t):
		l = int(input())
		if l in range(7, 101):
			d = list(map(int, input().split()))
			mid = l // 2

			if l%2 == 0:
				if d[:l//2] == d[l//2-1:][::-1] and 7 in d:
					res.append("yes")
				else:
					res.append("no")
			else:
				if d[:l//2] == d[l//2+1:][::-1] and 7 in d:
					res.append("yes")
				else:
					res.append("no")

for e in res:
	print(e)
