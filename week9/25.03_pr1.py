a = [6, 8, -5, 8, 3, -2, 6, 8, 9, 18, -23, 0]
b=[]
for i in a:
    if i>0:
        b.append(i)
print(b)

b = [el for el in a if el>0]

c = [[i, j] for i in range(1, 4) for j in range(1, 4)]
print(c)

USD_UAH= 43.83
price = [10, 14, 98, 123, 67, 3, 9.5]
new_price = [p*USD_UAH*1.1 if p*USD_UAH>3000 else p*USD_UAH for p in price]
print(new_price)


# f(x)=6x+7
f = {x:6*x+7 for x in range(10-20, 10)}
print(f)

a = [[i*j for j in range(1,6)] for i in range(1,6)]
print(a)