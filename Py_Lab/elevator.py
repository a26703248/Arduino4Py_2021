import time

if __name__ == "__main__":
    l = 1
    while True:
        g = '您現在在{}樓。請問要去哪一樓(輸入 0 可離開電梯)？'.format(str(l))
        print('幸福大廈共有1~7層樓')
        k = int(input(g))
        if (k > 0) and (k <= 7):
            if l < k:
                print('電梯上樓')
                for i in range(l, k+1):
                    print(i)
                    time.sleep(1)
                l = k
            elif l > k:
                print('電梯下樓')
                for i in range(l, k-1, -1):
                    print(i)
                    time.sleep(1)
                l = k
        elif k == 0:
            print('exit')
            break
        elif k == 1:
            print('本樓層就是%d' % k)
            continue
        else:
            print('無此樓層')



