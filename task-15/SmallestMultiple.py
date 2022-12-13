def lowest_factor (x) :
    i = 2
    while (i * i <= x) :
        if (x % i) == 0 :
            return i
        i += 1
    return x

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lcm = 1
    for i in range(2, n + 1) :
        if not lcm % i == 0 :
            lcm *= lowest_factor (i)
    print(int(lcm))
