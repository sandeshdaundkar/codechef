T = int(input())
for cas in range(1,T+1):
    X, Y, K, N = map(int, input().split())
    books = []
    for i in range(N):
        P, C = map(int, input().split())
        books.append((P, C))
    for P, C in books:
        if P >= X - Y and C <= K:
            print ("LuckyChef")
            break
    else:
        print ("UnluckyChef")
        