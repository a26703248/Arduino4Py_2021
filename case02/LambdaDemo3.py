#Lambda lab:
#請利用Lambda 做出判斷 odd 奇數, even 偶數的函式

if __name__ == "__main__":
    while True:
        odd = lambda x: "even" if (x%2) == 0 else "odd"
        user = int(input("輸入數值: "))
        result = lambda:print(odd(user))
        result()




