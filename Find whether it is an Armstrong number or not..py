n=input() # 153
b=len(n)
summ=0
for i in n:
    summ=summ+int(i)**b
    if summ==int(n):
        print("True")
