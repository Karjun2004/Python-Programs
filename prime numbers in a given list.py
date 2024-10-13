n=list(map(int, input().split()))
sum=0
for i in n:
    flag=True
    for j in range(2,i):
        if(i%j==0):
            flag=False
            break
    if(flag==True):
        sum=sum+i
        print(sum, end=" ")
