n=int(input())
if(n%4==0 and n%100==0 or n%400==0):
    print(n, "is a leap year")
else:
    print(n, "Not a leap year")
