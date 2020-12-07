import random


def guess_number():
    # 随机生成100以内的整数
    a = random.randint(0, 100)
    count = 0
    while True:
        num = input("输入一个整数：")
        if int(num) > 100:
            print("请输入100以内的整数！")
        else:
            count += 1
            # 若猜对，结束循环，输出循环次数
            if int(num) == a:
                print(f"您猜对了！共猜测了{count}次")
                break
            elif int(num) > a:
                print("The number is bigger!")
            else:
                print("The number is smaller!")
            # 超过循环次数，选择是否结束循环
            if count == 10:
                if input("您已输入十次，是否继续输入？（yes/no）：") == "no":
                    print(f"该整数是：{num}")
                    break

guess_number()


