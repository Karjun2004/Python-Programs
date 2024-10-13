n=list(map(int, input().split(",")))#1,2,3,4,5
a=len(n)
b=[6] + n
c=b+[7]
c.insert(3,8)
print(c)

