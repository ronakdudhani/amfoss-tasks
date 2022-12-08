n,m = list(map(int,input().split()))
if m%n is not 0:
    print(-1)
else:
    count = 0
    m = m//n
    while(m is not 1):
        if m%3 is 0:
            m = m//3
            count += 1
        elif m%2 is 0:
            m = m//2
            count += 1
        else:
            print(-1)
            exit()
    print(count)
