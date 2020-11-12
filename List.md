# Python内置对象类型“列表”

## 1. 列表的基本知识和应用特点

列表是由一系列按特定顺序排列的元素组合，用[ ]表示，并用逗号隔开其中的元素。

列表中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。


列表可以进行的操作包括索引，切片，加，乘，检查成员。

列表的数据项不需要具有相同的类型。

如下所示：


```python
list1 = [1,3,4,5,6]
list2 = ['a','b','c','c']
list3 = [1,4,'a','c']
```


```python
list1
```




    [1, 3, 4, 5, 6]




```python
list2
```




    ['a', 'b', 'c', 'c']




```python
list3
```




    [1, 4, 'a', 'c']



### 1.1 访问列表元素

可直接通过元素的索引访问列表元素


```python
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
```


```python
list[0]      # 索引从零开始
```




    'red'




```python
list[-1]      # 访问列表最后一个元素
```




    'black'



使用切片访问列表前三个元素


```python
list[0:3]
```




    ['red', 'green', 'blue']



### 1.2 修改、添加和删除元素

#### 1.2.1 修改列表
改列表元素，可指定列表名称和要修改的元素的索引，再指定该元素的新值


```python
list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
list[2] = 'Baidu'     # 将第三个元素改为'Baidu'
list
```




    ['Google', 'Runoob', 'Baidu', 'Taobao', 'Wiki']



#### 1.2.2 在列表中添加元素

使用append()方法在列表最后添加元素


```python
list.append('Souhu')     # # 在最后一个位置添加'Souhu'
list
```




    ['Google', 'Runoob', 'Baidu', 'Taobao', 'Wiki', 'Souhu']



使用insert()方法在列表任意位置添加元素


```python
list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
list.insert(1, 'Baidu')     # 在第二个位置添加'Baidu'
list
```




    ['Google', 'Baidu', 'Runoob', 'Zhihu', 'Taobao', 'Wiki']



#### 1.2.3 从列表中删除元素

使用del语句删除元素


```python
list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
del list[0]
list
```




    ['Runoob', 'Zhihu', 'Taobao', 'Wiki']



使用pop()方法删除指定位置元素，并继续使用它


```python
list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
poped_list = list.pop(1)     # 删除索引为1的元素，pop()默认删除末尾元素
poped_list
```




    'Runoob'




```python
list
```




    ['Google', 'Zhihu', 'Taobao', 'Wiki']




```python
list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
poped_list = list.pop()     # 默认删除末尾元素
list
```




    ['Google', 'Runoob', 'Zhihu', 'Taobao']



使用remove()方法根据值删除元素

只删除第一个指定的值，如果要删除的值在列表中出现多次，需要使用循环进一步判断


```python
list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki",'Taobao']
list.remove('Taobao')      
list
```




    ['Google', 'Runoob', 'Zhihu', 'Wiki', 'Taobao']



### 1.3 组织列表

#### 1.3.1 使用方法sort()对列表进行永久性排序


```python
cars = ['bmw','audi','toyota','subaru']     # 按字母顺序排列
cars.sort()
cars
```




    ['audi', 'bmw', 'subaru', 'toyota']




```python
cars = ['bmw','audi','toyota','subaru']     # 按字母顺序相反的顺序排列
cars.sort(reverse = True)
cars
```




    ['toyota', 'subaru', 'bmw', 'audi']



#### 1.3.2 使用方法sorted()对列表进行临时排序


```python
cars = ['bmw','audi','toyota','subaru'] 
sorted(cars)
```




    ['audi', 'bmw', 'subaru', 'toyota']




```python
cars      # 列表的排列顺序没有变
```




    ['bmw', 'audi', 'toyota', 'subaru']



#### 1.3.3 倒着打印列表


```python
cars = ['bmw','audi','toyota','subaru']
cars.reverse()     # 方法reverse()永久地修改列表排列顺序
cars
```




    ['subaru', 'toyota', 'audi', 'bmw']




```python
cars.reverse()     # 再次调用reverse()可恢复到列表原来的顺序
cars
```




    ['subaru', 'toyota', 'audi', 'bmw']




```python
cars[::-1]      # 此处也可使用切片的方法进行倒序打印
```




    ['bmw', 'audi', 'toyota', 'subaru']



#### 1.3.4 确定列表长度


```python
cars = ['bmw','audi','toyota','subaru']     
len(cars)      # 使用len()方法获得列表长度
```




    4



### 1.4 使用列表的一部分

#### 1.4.1 切片（处理列表的部分元素称为切片）


```python
players = ['charles','martina','michael','florence','eli']
players[0:3]      # 提取前三个元素
```




    ['charles', 'martina', 'michael']




```python
players = ['charles','martina','michael','florence','eli']
players[1:4]       # 提取2～4个元素，将起始索引指定为1，终止索引指定为4
```




    ['martina', 'michael', 'florence']



如果没有指定索引，列表自动从头开始


```python
players = ['charles','martina','michael','florence','eli']
players[:4]        # 提取列表前四个元素
```




    ['charles', 'martina', 'michael', 'florence']



让切片终止于列表末尾，可省略终止索引


```python
players = ['charles','martina','michael','florence','eli']
players[2:]        # 提取列表3～5个元素
```




    ['michael', 'florence', 'eli']



提取列表最后几个元素


```python
players = ['charles','martina','michael','florence','eli']
players[-3:]        # 提取列表最后三个元素
```




    ['michael', 'florence', 'eli']



#### 1.4.2 使用循环遍历列表


```python
magicians = ['alice','david','carolina']
for magician in magicians:       # 遍历列表所有元素
    print(magician)
```

    alice
    david
    carolina
    


```python
magicians = ['alice','david','carolina','eli','michael']
for magician in magicians[:4]:       # 遍历列表前四个元素
    print(magician)
```

    alice
    david
    carolina
    eli
    

#### 1.4.3 复制列表

使用切片复制列表


```python
my_food = ['pizza','falafel','carrot take']
friend_food = my_food[:]
friend_food
```




    ['pizza', 'falafel', 'carrot take']



使用copy()方法复制列表


```python
my_food = ['ice cream','pizza','falafel','carrot take']
friend_food = my_food.copy()
friend_food
```




    ['ice cream', 'pizza', 'falafel', 'carrot take']



### 1.5 Python列表函数&方法

#### 1.5.1 Python包含以下函数:

1. cmp(list1, list2)：比较两个列表的元素
2. len(list)：列表元素个数
3. max(list)：返回列表元素最大值
4. min(list)：返回列表元素最小值
5. list(seq)：将元组转换为列表

#### 1.5.2 Python包含以下方法:

1. list.append(obj)：在列表末尾添加新的对象
2. list.count(obj)：统计某个元素在列表中出现的次数
3. list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4. list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
5. list.insert(index, obj)：将对象插入列表
6. list.pop([index=-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7. list.remove(obj)：移除列表中某个值的第一个匹配项
8. list.reverse()：反向列表中元素
9. list.sort(cmp=None, key=None, reverse=False)：对原列表进行排序

## 2. 列表与数组之间的异同

### 2.1 相同点

#### 2.1.1 二者都可以用于处理多维数组
Numpy使用ndarray对象来处理多维数组，Python列表可以通过列表的嵌套实现多维数组。


```python
import numpy as np


arr = np.array([[2,4,3],[1,4,7],[8,2,4]])      # 使用ndarray对象生成二维数组
list = [[2,4,3],[1,4,7],[8,2,4]]        # 使用列表的嵌套生成二维数组
print(arr)
print(list)
```

    [[2 4 3]
     [1 4 7]
     [8 2 4]]
    [[2, 4, 3], [1, 4, 7], [8, 2, 4]]
    

#### 2.1.2 访问方式相同
列表和数组都可以通过索引访问元素，并且索引都是从零开始


```python
'''访问前两个元素'''
arr = np.array([2,4,8,3,5])
list = [2,4,8,3,5]
```


```python
list[:2]
```




    [2, 4]




```python
arr[:2]
```




    array([2, 4])




```python
arr1 = np.array([[3,2,5],[1,2,3]])
list1 = [[3,2,5],[1,2,3]]  
'''访问第一行第三个元素'''
print(arr1[0][2])    
print(list1[0][2])
```

    5
    5
    

#### 2.1.3 列表和数组之间可以相互转换

将列表转换成数组


```python
list2 = [2,4,3,7,8]
list2
```




    [2, 4, 3, 7, 8]




```python
np.array(list2)
```




    array([2, 4, 3, 7, 8])



使用tolist()方法将数组转换成列表


```python
arr2 = np.array([2,4,3,7,8])
arr2
```




    array([2, 4, 3, 7, 8])




```python
arr2.tolist()
```




    [2, 4, 3, 7, 8]



#### 2.1.4 数组和列表都可以进行修改、添加和删除

通过索引直接修改


```python
list3 = ['red', 'green',  'yellow', 'white', 'black']
arr3 = np.array(['red', 'green',  'yellow', 'white', 'black'])
arr3[0] = 'blue'
list3[0] = 'blue'
```


```python
arr3
```




    array(['blue', 'green', 'yellow', 'white', 'black'], dtype='<U6')




```python
list3
```




    ['blue', 'green', 'yellow', 'white', 'black']



列表可通过灵活删除和添加元素，但是数组只能按轴删除和添加行或列


```python
list3 = ['red', 'green',  'yellow', 'white', 'black']
arr3 = np.arange(12).reshape(2,2,3)
print(arr3)
```

    [[[ 0  1  2]
      [ 3  4  5]]
    
     [[ 6  7  8]
      [ 9 10 11]]]
    


```python
arr = np.delete(arr3,1,axis=0)
arr
```




    array([[[0, 1, 2],
            [3, 4, 5]]])




```python
del list3[0]
list3
```




    ['yellow', 'white', 'black']



### 2.2 不同点

#### 2.2.1 元素数据类型
数组中的所有元素的类型都是相同的，而Python列表中的元素类型不必相同


```python
list = [1,2,3,'alice','cake','peter']       # 列表中既包含字符串也包含数字
arr = np.array([[1,4],['alice','cake']])       # 数组会把所有元素类型都转换成同一种类型
print(list)
print(arr)
```

    [1, 2, 3, 'alice', 'cake', 'peter']
    [['1' '4']
     ['alice' 'cake']]
    

#### 2.2.2 使用布尔数组
nparray对象可以使用布尔数组，但是列表不可以


```python
a=np.array([0,1,2,3,4,5,6])
b=a>3       # 判断a中元素是否大于3，返回布尔型
b
```




    array([False, False, False, False,  True,  True,  True])




```python
a[b]       # 返回Ture的数组元素
```




    array([4, 5, 6])



#### 2.2.3 科学计算
Numpy是一个专门用于数据处理的库，能很好的支持一些数学运算，而列表进行数学运算则比较麻烦


```python
a = [1, 2, 3, 4]
b = np.array([1, 2, 3, 4])
c = a * 2
d = b * 2
```


```python
c
```




    [1, 2, 3, 4, 1, 2, 3, 4]




```python
d
```




    array([2, 4, 6, 8])




```python
np.mean(b)     # 使用mean()方法直接求数组均值
```




    2.5




```python
np.sum(b)        # 使用sum()进行求和运算
```




    10



#### 2.2.4 长度
list数据结构内容可以被程序修改，可动态增减，长度不固定；数组一般是固定长度 


```python
list = ['alice','peter','michael','david']
list.append('viki')
list
```




    ['alice', 'peter', 'michael', 'david', 'viki']




```python
list.pop()
list
```




    ['alice', 'peter', 'michael', 'david']



#### 2.2.5 两个list可“链接”（通过+加法）构成一个更大的list ，而数组则不可以


```python
list1 = ['alice','peter','michael','david']
list2 = [1,2,3,4]
list1 + list2
```




    ['alice', 'peter', 'michael', 'david', 1, 2, 3, 4]



#### 2.2.6 存储效率和输入输出性能不同。

Numpy专门针对数组的操作和运算进行了设计，存储效率和输入输出性能远优于Python中的嵌套列表，数组越大，Numpy的优势就越明显。
