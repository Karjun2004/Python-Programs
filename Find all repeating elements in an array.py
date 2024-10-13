n = list(map(int, input().split(",")))  # Example input: 1,1,2,3,4,4,5,2
s = set()
a = set()
for i in n:
    if i in s:
        a.add(i)
    else:
        s.add(i)
print(list(a))

            
