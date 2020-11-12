# coding: utf-8
# @Time: 2020/10/28 $ {TIME}
# @File : Fibonacci_loop_while.py

'''用生成器方法实现斐波那契数列'''


def fib_loop_while(n):
    a, b = 0, 1
    for i in range(0, n):
        yield a
        a, b = b, a + b


n = int(input('请输入斐波那契数列的长度n：'))  # 输入斐波那契数列的长度
fib = fib_loop_while(n)
for num in fib:
    print(num, end=" ")

    
