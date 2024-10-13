n=int(input())
count=0
for i in str(n):
    if n%int(i)==0:
        count=count+1
print(count)
