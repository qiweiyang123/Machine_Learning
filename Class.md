# 面向对象中类的三大特性

### 面向对象技术简介
### 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
### 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
### 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
### 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
### 实例变量：定义在方法中的变量，只作用于当前实例的类。
### 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，素以Dog也是一个Animal。
### 实例化：创建一个类的实例，类的具体对象。
### 方法：类中定义的函数。
### 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

## 1. 继承

#### 父类的属性、方法会被继承给子类，举例：如果子类没有__init__方法，父类有，那么在子类继承父类的时候这个方法就会被继承，如果只是创建对象，就默认执行了那个继承过来的__init__方法。

#### 重写父类的方法：就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖父类的同名方法。
#### 调用父类的方法：1.父类名.父类的方法名（）2.super()


```python
class Car():
    '''一次模拟汽车的简单尝试'''
    
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

class ElectricCar(Car):
    def __init__(self, make, model, year):   
        super().__init__(make, model, year)   # self(). 可以让父类和子类关联起来，父类成为super class


car = ElectricCar('audi', 'a4', 2016)
print(car.get_descriptive_name())

```

    2016 Audi A4
    

## 2. 多态

#### 以封装和继承为前提，不同的子类对象调用相同的方法，产生不同的执行结果


```python
class Man:
    def eat(self):
        print("饿了，吃饭了!")
class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")

class English(Man):
    def eat(self):
        print("英国人用刀叉吃饭")

class Indian(Man):
    def eat(self):
        print("印度人用右手吃饭")

def manEat(m):
    if isinstance(m,Man):
        m.eat()
    else:
        print("不能吃饭")


#子类Chinese实例化的
manEat(Chinese())
#子类English实例化的
manEat(English())

```

    中国人用筷子吃饭
    英国人用刀叉吃饭
    

## 3. 封装（私有化）

#### 封装，顾名思义就是将内容封装到某个地方，以后再去调用被封装在某处的内容。所以，在使用面向对象的封装特性时，需要：1. 将内容封装到某处 2.从某处调用被封装的内容
#### 调用被封装的内容时，有两种情况：1. 通过对象直接调用 2.通过self间接调用

### 3.1 通过对象直接调用被封装的内容


```python
# 创建一个表示小狗的类 Dog

# 包含名字和年龄 +  蹲下和打滚

# 使用类去创建表示特定小狗的实例

# 创建 Dog实例时，通过实参向 Dog()传递名字和年龄，self会自动传递

class Dog:
    
    def __init__(self, name, age):     # 以self为前缀的变量可供类中所有方法使用
        '''注意__init__是两个英文状态下的下划线'''
        
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is now setting.")
        
    def roll_over(self):
        print(self.name.title() + " rolled over!")
        
dog = Dog('willie', 6)
print("My dog's name is " + dog.name.title() + '.')     # 直接调用dog对象的name属性
print("My dog is " + str(dog.age) + ' years old.')      # 直接调用dog对象的age属性

```

    My dog's name is Willie.
    My dog is 6 years old.
    

### 3.2 通过self间接调用被封装的内容


```python
class Dog:
    
    def __init__(self, name, age):     # 以self为前缀的变量可供类中所有方法使用
        '''注意__init__是两个英文状态下的下划线'''
        
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is now setting.")
        
    def roll_over(self):
        print(self.name.title() + " rolled over!")
        
dog = Dog('willie', 6)
dog.roll_over()

```

    Willie rolled over!
    


```python

```


```python

```


```python

```


```python

```


```python

```
