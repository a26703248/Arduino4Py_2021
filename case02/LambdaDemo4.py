#Lambda 設計一個 bmi 函數式宣告
#並 "印出" 170, 60 的 "bmi 值"
#bmi <= 18 "過輕", bmi >= 23 "過重", 其他 "正常"



if __name__ == "__main__":
    h = 170
    w = 60
    bmi = lambda h,w: w / ((h/100)**2)
    result = lambda x:"過輕" if x <= 18 else "過重" if bmi > 23 else "正常"
    bmi = bmi(h,w)
    print("{:.2f}".format(bmi),result(bmi))
