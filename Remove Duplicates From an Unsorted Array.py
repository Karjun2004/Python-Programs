n=list(map(int, input().split(",")))#2, 3, 1, 9, 3, 1, 3, 9
a=set()
b=[]
for i in n:
    if i not in a:
        a.add(i)
        b.append(i)
print(b)
