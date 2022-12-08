t = int(input())
while(t>0):
    n = int(input())
    tank = [int(i) for i in input().split()]
    count = 0
    for i in range(0,n-1,-1):
        if(tank[i]==0 and tank[i-1] != 0):
            count+=1
            tank[i]+=1
            tank[i-1]-=1
    tank[n-1] = 0
    print(count+sum(tank))
    t = t-1