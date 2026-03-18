def sign(x : float) -> int :
    """
    Пояснення
    :param x:
    :return:
    """
    if x>0:
        y=1
    elif x==0:
        y=0
    else:
        y=-1
    return y

print(sign(17.98))

def average(*array, pres=3) -> float:
    return round(sum(array)/len(array), pres)

print(average(1,2,3,4, pres=4))

for i in range(10):
    print(i)