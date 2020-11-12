# coding: utf-8
# @Time: 2020/10/28 $ {TIME}
# @File : Fibonacci_recur.py

'''用递归方法实现斐波那契数列'''


def fib_recur(n):
    if n <= 1:
        return n
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)


n = int(input('请输入斐波那契数列的长度n：'))  # 输入斐波那契数列的长度
for i in range(n):
    print(fib_recur(i), end=' ')
    
