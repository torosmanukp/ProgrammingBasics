# n = int(input())
# text=input()
# i=1
# for i in range(n+1):
#     print(f"- {text}")

# a, b, n = map(int, input().split())
#
# print(a*n+(b*n)//100)
# print((b*n)%100)

# n,m,k = map(int, input().split())
# i=1
# j=1
# while True:
#     if n%i*k==0:
#         break
#     else:
#         i+=1
# while True:
#     if m%j*k==0:
#         break
#     else:
#         j+=1
# print(i+j)


# a1, a2, b1, b2, c1, c2 = map(int, input().split())
#
# dis1=((a1-c1)**2+(a2-c2)**2)**0.5
# dis2=((b1-a1)**2+(b2-a2)**2)**0.5
# dis=((b1-c1)**2+(b2-c2)**2)**0.5
#
# print(dis1, dis2, dis)
# if dis1+dis2==dis:
#     print(1)
# else:
#     print(0)

n,m,k = map(int, input().split())
i=0
j=0

if n%k==0:
    i=n/k
elif n%k:
    i=n//k+1

if m%k==0:
    j=m/k
elif m%k:
    j=m//k+1
print(int(i+j))
