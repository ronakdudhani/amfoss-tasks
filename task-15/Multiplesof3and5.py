t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
    n -= 1
    count3 = n//3
    # using AP to calculate sum of all factors
    sum3 = (3*count3*(count3+1))//2
    count5 = n//5
    sum5 = (5*count5*(count5+1))//2
    count15 = n//15
    sum15 = (15*count15*(count15+1))//2
    total_sum = sum3+sum5-sum15
    print(total_sum)