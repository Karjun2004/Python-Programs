n=list(map(int, input().split(",")))#1,2,-1,1,3,1
s=set()#1,2,-1,3
c=set()#1,1 bt set will not take the repeateed values so the set contains 1 
for i in a:
    if i in s:
        c.add(i)
    else:
        s.add(i)
d=s-c # from 1 2 -1 3 (- minus) 1  
print(list(d)) # the the remaining will be 2 -1 3 
