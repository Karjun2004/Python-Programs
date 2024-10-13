'''A series with same common difference is known as arithmetic series. The first term of series is 'a' and common difference is d. The series looks like a, a + d, a + 2d, a + 3d, . . . Find the sum of series upto nth term.

 

Example 1:

Input: n = 5, a = 1, d = 3
Output: 35
Explanation: Series upto 5th term is
1 4 7 10 13, so sum will be 35.'''
n=int(input())
a=int(input())
d=int(input())
summ=0
for i in range(n):
    j=a+i*d
    summ=summ+j
print(summ)
