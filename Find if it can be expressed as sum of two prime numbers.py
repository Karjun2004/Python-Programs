n=int(input())
c=[]
if n>1:
    for i in range(2,n):
        flag=True
        for j in range(2,i):
            if i%j==0:
                flag=False
                break
        if flag==True:
            c.append(i)
flag2=False
for k in range(len(c)):
    for l in range(len(c)):
        if c[k]+c[l]==n:
            flag2=True
            print("Yes")
            break
        if flag2:       #imp line to break flag2 to not to repeat the numbers of iteraation after finding the yes or no
            break
if flag2==False:
    print("No")
        
