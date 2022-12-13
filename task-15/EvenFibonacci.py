t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())
    a = b =1
    sum = 0
    while(b<n):
        temp = b
        b += a
        a = temp
        if a%2 == 0:
            sum += a
    print(sum)