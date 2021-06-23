#嵌套函式 1

def message(text):
    text = text + " by 巨匠電腦"
    def print_message():
        print(text)

    return print_message

def message2(text):
    text = text + " by 巨匠電腦"
    def print_message():
        print(text)

    return print_message()

if __name__ == "__main__":
    m1 = message("Hello")
    m1()
    message2("Hello")