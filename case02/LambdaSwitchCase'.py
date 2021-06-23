# Python 沒有switch case
#lambda + dict 合作

if __name__ == "__main__":
    id = "A123456789"
    sex = id[2]
    print(sex)

    sex_info = {
        1: lambda : print("男"),
        2:lambda : print("女")
    }
    sex_error = lambda : print("性別錯誤")
    sex_info.get(int(sex), sex_error)()

    score_weight = {
        1: lambda salary: print("男", salary),
        2: lambda salary: print("女", salary * 1.2),
    }
    sex_error = lambda: print("性別錯誤")
    score_weight.get(int(sex), sex_error)(30000)