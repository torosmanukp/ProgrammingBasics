#tuple
a = (5, 8, 7, 6, 4)
b=([1, 2, 3], [4, 5, 6], [7, 8, 9])
b[0][1]=100
# print(b)

#set
am = {5, 6, 8, 7, 3, -1, 3, 6, 3, 8, 6, 7}
# print(am)
am.add(100)
# print(am)
am.pop()
# print(am)
am.remove(100)
# print(am)

# a = list(map(int, input().split()))
# un = set(a)
# # print(a)
# print(un)
# for i in a:
#     if i in un:
#         print(i, end=" ")
#         un.remove(i)

#string
text = "Hello, KSE!"
print(text+" Welcome!")
#text1= (text+"\n")*100
#print(text1)
print(text[1:8])

title="maryna petrenko"
title = title.title()
print(title)

text2="              Jello, Toros! "
print(text2)
text2=text2.strip()
text2=text2.replace("J", "H")
print(text2)

text3= "Hello Maryna  Petrenko"
name= text3.split("  ")
print(name)