number = int(input())
count = 0
while(number>9):
    total = 0
    count += 1
    while(number>0):
        total = total + number%10
        number = number//10
    number = total
print(count)
