'''Given n, a and r as the number of terms, first term and common ratio respectively of an Geometric Progression Series. Find the sum of the series upto nth term.
 

Example 1:

Input: 3 3 2
Output: 21
Explanation: Series upto 3td term is
3 6 12, so sum will be 21.'''
n=int(input())
a=int(input())
b=int(input())
summ=0
series=[]
first=n
series.append(first)
second=n*b
series.append(second)
third=n*(b**b)
series.append(third)
for i in (series):
    summ=summ+i
print(summ)
