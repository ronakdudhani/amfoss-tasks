N,M = list(map(int,input().split()))
x=1
y = (N-x)//2
i = 1
if N<M:
    print(-1)
    exit()
while(x+y)%M is not 0:
    x += 1
    if(N-x)%2 is not 0:
        y = (N-x)//2
print(x+y)