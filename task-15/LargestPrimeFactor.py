import math
t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())
    while(n%2==0):
        factor = 2
        n = n//2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i == 0):
            n //= i
    if n>2:
        factor = n
    print(n)
        
        
