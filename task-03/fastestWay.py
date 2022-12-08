N,M = list(map(int,input().split()))
Dict = {}
for i in range(0,M):
    a,b = input().split()
    if len(a) <= len(b):
        Dict[a] = a
    else:
        Dict[a] = b
s = input().split()
for i in range(0,N):
    print(Dict[s[i]],end=" ")
