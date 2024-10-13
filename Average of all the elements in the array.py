n=list(map(int, input().split()))
a=len(n)
count=0
for i in n:
    count=count+i
print(float(count/a))
