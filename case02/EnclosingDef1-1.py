#嵌套函式 1-1

def message(text):
    text = text + " by 巨匠電腦"
    def print_message():
        print("print_message 方法執行")
        print(text)

    return print_message#有加 () 回傳結果, 沒有加回傳方法

if __name__ == "__main__":
    m1 = message("Hello")
