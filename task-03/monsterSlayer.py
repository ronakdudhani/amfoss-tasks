t = int(input())
while(t>0):
    n = int(input())
    groups = [int(i) for i in input().split()]
    if groups[0] is 1:
        print("YES")
    else:
        for i in range(0,n):
            if(groups[i]%groups[0] is not 0):
                print("NO")
                break
            elif(i is n-1):
                print("YES")
    t -= 1
    