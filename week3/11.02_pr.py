import math
eolymp 8878

n=int(input())
lg=math.log10(n)
if int(lg) == lg:
    print(int(lg))
else:
    print('No')

eolymp 8872

a, b, c = map(int, input().split())

if a<b<c:
    print(a,b,c)
elif a<c<b:
    print(a,c,b)
elif b<a<c:
    print(b,a,c)
elif b<c<a:
    print(b,c,a)
elif c<a<b:
    print(c,a,b)
else:
    print(c,b,a)

eolymp 8891

n = int(input())

cond1= (n%2==0)
cond2= (n<0) and (n%3==0)

rule1= cond1 and (not cond2)
rule2= (not cond1) and cond2

if rule1 or rule2:
    print('YES')
else:
    print('NO')

while loop

a=2
b=20
while a<=b:
    if a%2 and a%3 and a%5 and a%7:
        print(a, end=' ')
        break
    a += 1
else:
    print('number is not found')

for loop

for i in range(10):
    print(i)

for _ in range(0, 1000, 67): #start stop step
    print(_, end=' ')

eolymp 8927

n=int(input())
div=2
sqrt_n=int(n**0.5)+1

while div < sqrt_n:
    if(n%div==0):
        print(div)
        break
    div+=1
else:
    print(n)

eolymp 8946

n=int(input())

for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print("*", end='')
        else:
            print(" ", end='')
    print()