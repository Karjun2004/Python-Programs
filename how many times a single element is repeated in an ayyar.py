#Example 1:
#Input: array[] = {1,2,3,4,5} k=3
#Output: 2Explanation: The answer is 2 because 3 is present at 2nd index.
n=int(input())
a=list(n)
k=int(input())
for i in a:
    p=a.index(k)
print(p)
