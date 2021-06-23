'''
作業 (利用 lambda)
id = 'A123456789'
第二碼 sex  = id[1] -> 1 (1: 男生, 2: 女生)
第三碼 area = id[2] -> 2 (0~5: 台灣, 6: 外國, 7: 無戶籍, 8: 港澳, 9: 大陸)
印出: 台灣男
'''
def Belonging(x):
    sex = ""
    if x == 1:
        sex = "男"
    else:
        sex = "女"
    def nation(y):
        country = " "
        if y <= 5 and y > 0:
            country = "台灣"
            country = country + sex
        else:
            dcl ={
                6: "外國",
                7: "無戶籍",
                8: "港澳",
                9: "大陸"
            }
            country = dcl.get(y) + sex
        return country
    return nation

if __name__ == "__main__":
    id = "A123456789"

    # Lambda語法
    sex = int(id[1])
    country = int(id[2])
    sex_func = lambda x: "男" if sex == 1 else "女"
    country_func = lambda x: "台灣" if country <= 5 else "外國" if country == 6 else "無戶籍" if country == 7 else "港澳" if country == 8 else "大陸"
    print("{0}{1}".format(country_func(country), sex_func(sex)))

    #嵌套函式
    b = Belonging(sex)
    print(b(country))