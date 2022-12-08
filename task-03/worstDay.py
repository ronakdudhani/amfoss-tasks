n = int(input())
groups = [int(i) for i in input().split()]
count1 = count2 = count3 = count4 = 0
for i in groups:
    if i is 1:
        count1 += 1
    elif i is 2:
        count2 += 1
    elif i is 3:
        count3 += 1
    else:
        count4 += 1
if count3>count1:
    count1 = 0
else:
    count1 -= count3
print(count4 + count3 + count2 // 2 + (count2 % 2 + count1 + 3) // 4)

