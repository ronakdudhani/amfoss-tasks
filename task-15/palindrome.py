
palindromelist = []
#appending every palindrome that is a multiple of two 3 digits number
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        if(a >100000):
            if str(a) == str(a)[::-1] and a not in palindromelist:
                palindromelist.append(a)
palindromelist.sort()
length = len(palindromelist)


t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())
    for i in range(length - 1, -1, -1):
        if palindromelist[i] < n:
            print(palindromelist[i])
            break
        
