# task1
#
# s=5490
#
# hours= s // 3600
# minutes= (s % 3600) //60
# seconds= s%60
#
# print(f"Hours: {hours}, minutes: {minutes}, seconds: {seconds}")
#
# task2
#
# h=int(input("enter hours"))
# m=int(input("enter minutes"))
# s=int(input("enter seconds"))
#
# final=h*3600+m*60+s
#
# print(final)
#
# task3
#
# v=10
# a=20
# t=10
#
# s= v*t + (a*t)**2/2
# print(f"The movement is: {s} meters")
#
# task4
#
# x1=10
# x2=4
# y1=20
# y2=12
#
# d=((x2-x1)**2+(y2-y1)**2)**(1/2)
#
# print(f"Distance is: {round(d , 2)} meters")
#
# task5 - apple
#
# N=int(input("enter quantity of students: "))
# K=int(input("enter quantity of apples: "))
#
# apple= K // N
# left= K%N
#
# print(f"each student received {apple} apples and {left} apples left in box")
#
# task 6 - triangle
#
# a=float(input("enter the 1st side: "))
# b=float(input("enter the 2nd side: "))
#
# c=(a**2 + b**2)**0.5
#
# print(f"the 3rd side is {round(c,2)}")
#
# task7 - number

a=int(input("enter your number: "))

a_1=a//100
a_2=(a//10)%10
a_3=a%10
sum=a_1+a_2+a_3

print(f"sum is {sum}")