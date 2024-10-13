n=list(map(int, input().split()))
k=int(input())
a=len(n)
for i in range(k,a):
    print(n[i], end=" ")
for i in range(0,k):
    print(n[i], end=" ")
