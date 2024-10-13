'''n=[10,5,10,15,10,5]
s={}#empty set
for i in n:
    if i in s: #means "i" value will be stored in s
        s[i]=s[i]+1
    else:
        s[i]=1
print(s)'''
a = [10,5,10,15,10,5]
s={}
for i in a:
    if i in s:
        s[i]=s[i]+1#using dictionary saving key value where(key as 10 and the value as 1)
    else:
        s[i]=1
print(s)
for key in s.keys():
    print(key,s[key])
