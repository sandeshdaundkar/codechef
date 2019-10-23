n = int(input())
res = []

for i in range(n):
	e, c = map(int, input().split())
	ak = list(map(int, input().split()))
	if sum(ak) <= c:
		res.append("Yes")
	else:
		res.append("No")

for e in res:
	print(e)