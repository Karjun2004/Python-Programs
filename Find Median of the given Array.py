n=list(map(int, input().split(',')))
b=sorted(n)#[2,5,1,7]
c=len(b)
d=c//2
e=[d]
if(c%2==0):#if the length by 2 gives even number then
    element1=d - 1 #element1=(4//2=2-1==1)
    element2=d
    median=(b[element1]+b[element2]) / 2.0
else:
    median=b[d]
print(median)

'''for i in range(b[1],b/2):
    print(i)'''

    
