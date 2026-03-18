import sys
# task 1


def calculator_battery_usage(x_start, y_start, x_target, y_target, drop = 1.5):
    if x_start==x_target and y_start==y_target:
        return 0.0
    distance_x= abs(x_start-x_target)
    distance_y= abs(y_start-y_target)
    total= distance_x+distance_y
    battery_used=total * drop
    return battery_used

print(calculator_battery_usage(*map(int, input().split())))
print(calculator_battery_usage(1, 2, 3, 4, 5))

# task 2
def can_go(x_target, y_target, current_battery, current_x=0, current_y=0):
    battery_used=2*calculator_battery_usage(current_x, current_y, x_target, y_target)
    if battery_used>current_battery:
        return False
    return True
print(can_go(current_x=2, current_y=2, x_target=5, y_target=6, current_battery=50))

# task 3

def factorial_iterative(n):
    result=1
    for i in range(1, n+1):
        result*=i
    return result
print(factorial_iterative(5))

def factorial_recursive(n):
    if n<0:
        return None
    if n==0:
        return 1
    return n*factorial_recursive(n-1)
print(factorial_recursive(100))

# extra 67 task
sys.set_int_max_str_digits(100000)
n=1
result=1
ss="67"

while True:
    result*=n
    result_string=str(result)
    if ss in result_string:
        print(n)
        print(result)
        break
    else:
        n+=1

# task 4
def degree(x, n):
    if n==0 and x!=0:
        return 1
    if n==0 and x==0 or x<0:
        return None
    if n==1:
        return x
    return x*degree(x, n-1)
print(degree(2, 6))
print(degree(0, 2))
print(degree(0, 0))

# task 5
def convert(C):
    return C*1.8+32


celsius = [0, 20, 30, 100]

temps_faren_1= list(map(convert, celsius))
print(temps_faren_1)
temp_faren_2=list(map(lambda x: x*1.8+32, celsius))
print(f"Lambda - {temp_faren_2}")