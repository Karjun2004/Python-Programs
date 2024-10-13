n=int(input())
arr=list(map(int, input().split()))
b=len(arr)
sum=0
if(n==b):
    for i in arr:
        sum=sum+int(i)
    print(sum)
else:
    print("enter ab appropriate value in an array")
