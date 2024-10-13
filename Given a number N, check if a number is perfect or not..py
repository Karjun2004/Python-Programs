'''Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number. Return 1 if the number is Perfect otherwise return 0.

Example 1:

Input:
N = 6
Output:
1 
Explanation:
Factors of 6 are 1, 2, 3 and 6.
Excluding 6 their sum is 6 which
is equal to N itself. So, it's a
Perfect Number'''
n=int(input())
a=[]
summ=0
for i in range(1,n):#1,2,3,4,5,6
    for j in range(1,n+1):
        if i*j==n:
            a.append(i)
            summ=summ+i
if summ==n:
    print("1")
else:
    print("0")
