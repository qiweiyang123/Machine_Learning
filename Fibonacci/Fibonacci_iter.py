# coding: utf-8
# @Time: 2020/10/28 $ {TIME}
# @File : Fibonacci_iter.py

'''用迭代器方法实现斐波那契数列'''


class Fib():
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.n = n
        self.current = 0  # current用来保存当前生成到数列中的第几个数了

    def __iter__(self):  # 迭代器的__iter__返回自身
        return self

    def __next__(self):  # 使用next()函数来获取下一个数
        if self.current < self.n:  # 设置循环次数
            num = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return num
        else:
            raise StopIteration


if __name__ == '__main__':
    n = int(input('请输入斐波那契数列的长度n：'))  # 输入斐波那契数列的长度
    fib = Fib(n)
    for num in fib:
        print(num, end=" ")
        

        
