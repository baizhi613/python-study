# import this
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name.title())

string = 'python '
print(string.rstrip())

print(3 ** 3)

age = 18
message = "Happy " + str(age) + "rd Birthday!"
print(message)

list0 = [1, 2, 3, 4, 5]
print(list0)
print(list0[-1])
list0[0] = 0
print(list0)
list0.append(6)
print(list0)
list0.insert(0, -1)
print(list0)
del list0[0]
print(list0)
list0.pop()
print(list0)
list0.remove(3)
print(list0)

# 定义一个汽车列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)
print(len(cars))

magicians = ['alice', 'david', 'carlina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!,")

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))
print(min(digits))
print(sum(digits))

squares = [value ** 2 for value in range(1, 11)]
print(squares)

# for v in range(1,1000000):
#     print(v)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')

friend_foods = my_foods
print(my_foods)
print(friend_foods)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)
dimensions = (400, 40)
print(dimensions)

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 定义了一个名为 alien_0 的字典，表示一个外星人的属性，包括颜色和点数
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
del alien_0['points']
print(alien_0)

for k, v in alien_0.items():
    print("\nKey:" + k)
    print("value:" + str(v))

for name in alien_0.keys():
    print(name.title())

for name in alien_0.values():
    print(name)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')

print(str(len(aliens)))

# message=input("hello：")
print(message)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying users:" + current_user.title())
    confirmed_users.append(current_user)

for confirmed_user in confirmed_users:
    print(confirmed_user.title())


def greet_user(username, userage=18):
    print("Hello," + username.title() + "!" + str(userage))


greet_user(username='jesse', userage=19)


def greet_user(names):
    for name in names:
        msg = "Hello," + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_user(usernames)


def make_pizza(*topping):
    print(topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', filed='physics')
print(user_profile)

import pizza
from pizza import make_pizza as mp

pizza.make_pizza(16, 'pepperoni')


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("tank")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def fill_gas_tank(self):
        print("no gas tank")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

with open('test.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('test.txt') as file_object:
    for line in file_object:
        print(line)

filename = 'test.txt'
with open(filename, 'w') as file_object:
    file_object.write("66666666\n")

with open(filename, 'a') as file_object:
    file_object.write("66666666")

try:
    print(5 / 1)
except ZeroDivisionError:
    print("NO")
else:
    print('Yes')

import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

name = "Alice"
age = 30
message = "My name is {}, and I am {} years old.".format(name, age)
print(message)

name = "Alice"
age = 30
message = "My name is %s, and I am %d years old." % (name, age)
print(message)

name = "Alice"
age = 30
message = f"My name is {name}, and I am {age} years old."
print(message)

# 基本用法：使用空格分隔字符串
sentence = "Hello world"
words = sentence.split()
print(words)  # 输出: ['Hello', 'world']

# 使用其他分隔符分隔字符串
csv_data = "apple,orange,banana,grape"
fruits = csv_data.split(',')
print(fruits)  # 输出: ['apple', 'orange', 'banana', 'grape']

# 指定分割次数
sentence = "Python is a powerful programming language"
words = sentence.split(maxsplit=2)
print(words)  # 输出: ['Python', 'is', 'a powerful programming language']


def outer_function(x):
    # 外部函数的局部变量
    y = 10

    # 内部函数定义在外部函数内部
    def inner_function(z):
        # 内部函数可以访问外部函数的局部变量
        return x + y + z

    # 外部函数返回内部函数
    return inner_function


# 创建闭包函数
closure = outer_function(5)
# 调用闭包函数
result = closure(15)
print(result)  # 输出: 30


# 定义装饰器函数
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # 调用原始函数
        print("Something is happening after the function is called.")

    return wrapper


# 使用装饰器语法装饰函数
@my_decorator
def say_hello():
    print("Hello!")


# 调用被装饰的函数
say_hello()

# 创建一个列表
my_list = [1, 2, 3, 4, 5]
# 使用iter()函数将列表转换为迭代器
my_iterator = iter(my_list)
# 使用next()函数遍历迭代器中的元素
print(next(my_iterator))  # 输出: 1
print(next(my_iterator))  # 输出: 2
print(next(my_iterator))  # 输出: 3
print(next(my_iterator))  # 输出: 4
print(next(my_iterator))  # 输出: 5


# 迭代器耗尽，抛出StopIteration异常
# print(next(my_iterator))  # 抛出 StopIteration 异常

def my_generator():
    yield 1
    yield 2
    yield 3


# 调用生成器函数创建生成器对象
gen = my_generator()
# 使用for循环迭代生成器中的值
for value in gen:
    print(value)
