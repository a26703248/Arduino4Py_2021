def add(x):
    return x + 1

def sub(x):
    return x - 1

def oprator(func, x):#高階函式:再函式裡面再帶入函式
    if(x > 0):
        return func(x)
    else:
        return x

def multi(func1, func2, x):
    if(x > 0):
        return func1(x) * func2(x) * oprator(add, x)
    else:
        return x

if __name__=='__main__':
    x = 1
    x = add(x)
    print(x)
    x = sub(x)
    print(x)
    #--------------------------------
    y = 3
    y = oprator(sub, y)
    print(y)
    #--------------------------------
    z = 5
    z = multi(add, sub, z)
    print(z)