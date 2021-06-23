#嵌套函式 3
#多重相乘

def multi(n):
    if n == 0:
        return None

    #def multi(x):
    #    return n * x

    multi = lambda x: n * x

    return multi #得到第 8 行的方法參考

if __name__ == "__main__":
    n3 = multi(3)
    n5 = multi(5)
    print(n3(6)) # x = 6
    print(n5(n3(6)))  # n5(n3(6)) -> n3(18) -> 90