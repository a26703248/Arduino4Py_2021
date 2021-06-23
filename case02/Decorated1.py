#裝飾器

def make_dress(func):
    def dress():
        print("穿衣服")
        func()
    return dress

def out():
    print("出門了")

if __name__ == "__main__":
    john = make_dress(out)
    john()
