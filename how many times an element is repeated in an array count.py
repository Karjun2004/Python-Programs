'''n=map(int, input().split())
b=len(n)
count=0
arr_1=[]
for i in n:
    for j in range(n[1],b):
        if(i==j):
            count=count+i
            count=arr_1
print(arr_1)'''
a=list(map(int,input().split()))
li={}
for i in a:
    if i in li:
        li[i]+=1
    else:
        li[i]=1
for key in li:
    print(key,li[key])