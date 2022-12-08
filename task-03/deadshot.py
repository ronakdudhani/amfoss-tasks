t = int(input())
X=[]
Y=[]
count=0
for i in range(0,t):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
for i in range(0,t):
    count1=count2=count3=count4=0
    for j in range(0,t):
        if((X[i]==X[j] and Y[i]>Y[j])):
            count1=1
        elif((X[i]==X[j] and Y[i]<Y[j])):
            count2=1
        elif((Y[i]==Y[j] and X[j]>X[i]) ):
            count3=1
        elif((Y[i]==Y[j] and X[j]<X[i])):
            count4=1
    if((count1+count2+count3+count4)==4):
        count+=1
print(count)