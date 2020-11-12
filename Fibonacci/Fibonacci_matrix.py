# coding: utf-8
# @Time: 2020/10/28 $ {TIME}
# @File : Fibonacci_matrix.py

'''用矩阵方法实现斐波那契数列'''
import numpy as np


def fib_matrix(n):
    fibmat = np.mat([[1], [0]])
    A = np.mat([[1, 1], [1, 0]])
    res = pow(A, n) * fibmat
    return res[1][0]


n = int(input('请输入斐波那契数列的长度n：'))  # 输入斐波那契数列的长度
for i in range(n):
    print(int(fib_matrix(i)), end=' ')
    
