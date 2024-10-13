n=[1,1,2,2,2,3,3]
n.sort()#1 1 2 2 2 3 3
a=len(n)
count=1
for i in range(1,a):
    if n[i]!=n[i-1]:
        n[count]=n[i]#in count we have 1 that's y we used n[1]=n[i] which is 2
        count=count+1#then it becomes 2 at 2nd iteration
while count < a:#2<7
    n[count]= "_"
    count=count+1
print(n)


