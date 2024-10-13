n=list(map(int, input().split()))#8 7 1 6 5 9
a=sorted(n)#[1,5,6,7,8,9]
b=len(n)#6
for i in range(b//2):
    print(n[i], end=" ")
for i in range(b - 1 , b // 2 -1 , -1):
    print(n[i], end=" ")
