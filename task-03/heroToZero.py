t = int(input())
while(t>0):
    n = int(input())
    heroes = [int(x) for x in input().split()]
    heroes.sort()
    count = 0
    flag = False
    if heroes[0] = 0:
        for i in heroes:
            if i is not 0:
                count += 1
    else:
        index = n - count
        health = heroes[index]
        for i in range(index+1,n):
            if heroes[i] == health:
                flag = True
                break
            else:
                health = heroes[i]
    if flag:
        print(count)
    else:
        print(count+1)             
    t -= 1