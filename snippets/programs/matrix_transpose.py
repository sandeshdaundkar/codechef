# Write your code here
r, c = list(map(int,input().split()))
arr = []
for i in range(r):
    m = list(map(int, input().split(' ')))
    arr.append(m)

for i in range(c):
    for j in range(r):
        print(arr[j][i], end=' ')
    print('')
