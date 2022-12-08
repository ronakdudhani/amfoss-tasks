t = int(input())
while(t>0):
    key = int(input())
    realms = [int(i) for i in input().split()]
    count = 0
    while(key!=0):
        count += 1
        key = realms[key-1]
    if count is 3:
        print("YES")
    else:
        print("NO")
    t -= 1