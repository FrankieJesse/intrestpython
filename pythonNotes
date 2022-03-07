Python编程从入门到实践201907
关键字：
+—————————————————————–+
False | class | finally | is | return | None | continue
for | lambda | try | True | def | nonlocal | while
and | del | global | not | with | as | elif | if | or | yield
assert | else | import | pass | break | except | in | raise
+—————————————————————–+
内置函数：
+—————————————————————–+
abs() | divmod() | input() | open() | staticmethod()
all() | enumerate() | int() | ord() | str()
any() | eval() | isinstance() | pow() | sum()
basestring() | execfile() | issubclass() | print() | super()
bin() | file() | iter() | property() | tuple()
bool() | filter() | len() | range() | type()
bytearray() | float() | list() | raw_input() | unichr()
callable() | format() | locals() | reduce() | unicode()
chr() | frozenset() | long() | reload() | vars()
classmethod() | getattr() | map() | repr() | xrange()
cmp() | globals() | max() | reversed() | Zip()
compile() | hasattr() | memoryview() | round() | _ import_()
complex() | hash() | min() | set() | apply()
delattr() | help() | next() | setattr() | buffer()
dict() | hex() | object() | slice() | coerce()
dir() | id() | oct() | sorted() | intern()
+—————————————————————–+
变量
每个变量都存储了一个值，在程序中可随时修改变量的值，而Python将始终记录变量的
最新值
变量命名
只能包含字母（最好用小写字母）、数字（不能以数字开头）、下划线，不能包含
空格
简短且具有描述性
不能用Python关键字和函数名
注意变量名在代码中的一致性
慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0
字符串
一系列字符。在Python中，用引号括起的都是字符串，单引号和双引号都可以
修改字符串大小写的方法
方法 是Python可对数据执行的操作。
str.title('name') == 'Name'
str.upper('name') == 'NAME'
str.lower('NAME') == 'name'
str = 'a' + 'b'
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
print(prompt)
\(在行尾时)：续行符
\\：反斜杠符号
\'：单引号
\"：双引号
\a：响铃
\b：退格(Backspace)
\e：转义
\000：空字符(NULL)
\n：换行
\v：纵向制表符
\t：横向制表符
\r：回车
\f：换页
\oyy：八进制数，yy代表的字符，例如：\o12代表换行
\xyy：十六进制数，yy代表的字符，例如：\x0a代表换行
\other：其它的字符以普通格式输出
.title() 每个单词首字母大写
.upper() 所有字母大写
.lower() 所有字母小写
拼接字符串：+
创建多行字符串可以用+=
转义字符（只能用在""内）
制表符：\t
换行符：\n
删除空白
.rstrip() 删除末尾空白
.lstrip() 删除开头空白
.strip() 删除两端空白
str(num)：将非字符串值表示为字符串
数字
整数
浮点数：带小数点的数字
Python2中整数除法的结果只包含整数部分，小数部分被删除，而不是四舍五入，要避免这种情况，
需确保至少有一个操作数为浮点数
常用于文件开头备注说明
运算符号
+ - * / 加减乘除
% 求模返回除法的余数。除2取余可以用来判断奇偶数
** 表示乘方运算，x**y返回x的y次幂
//取整除，返回商的整数部分
注释
单行注释 #：注释#号后面的当前行的代码
多行注释 """ """ 或者 ''' '''：注释两个'''或两个"""之间的代码（多行保留换行格式）
列表
列表是什么
一系列按特定顺序排列的元素
给列表指定一个复数的名称：bicycles
用方括号[]表示列表，并用逗号来分隔其中元素
访问列表元素
访问正数元素 ， [ ]索引从0而不是1开始：bicycles[0]
访问倒数元素，访问列表最后一个元素，将索引指定为-1：bicycles[-1]，以此类推
可像使用其他变量一样使用列表中的各个值
修改列表元素
指定列表名和要修改的元素索引，再指定该元素的新值：bicycles[0] = 'new'
在列表中添加元素
.append() 在末尾添加元素：bicycles.append('new')
.insert( , ) 在列表中插入元素，需指定新元素的索引和值：bicycles.insert(0, 'new')；这
种操作将插入位置及其后面的每个元素都右移一个位置
在列表中删除元素
del 删除已知位置的元素，且不再使用该元素：del bicycles[0]
.pop() （弹出）
删除列表末尾的元素并且获取该元素：bicycles.pop()
删除列表中已知位置的元素，且获取该元素：bicycles.pop(0)
.remove() 删除已知元素值，无需知道该元素的位置（只删除列表中第一个指定的值
的元素）：bicycles.remove('new')
列表排序
.sort() 永久性按字母顺序/倒序排序：cars.sort()、cars.sort(reverse=True)
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".n")
print("Thank you everyone, that was a great magic show!")
"方法1"
squares = []
for value in range(1, 11):
square = value**2
squares.append(square)
print(squares)
"方法2与方法1等价"
squares = [value**2 for value in range(1, 11)]
print(squares)
.sorted(列表名) 临时性按字母顺序/倒序显示，保留列表元素原来的排列顺序：
cars.sorted()、casrs.sorted(reverse=True)
.reverse() 永久性地反转列表元素的排列顺序：cars.reverse()
获取列表的长度：len(cars)
操作列表
for循环遍历整个列表：for 变量 in 列表:
使用单数和复数式名称：for cat in cats:
for语句末尾紧跟冒号:
属于for循环组成部分的代码行，一定要缩进
数值列表
使用range()生成数字序列，从你指定的第一个值开始数，并在到达你指定的第二
个值后停止，不包含第二个值，还可以指定步长；再使用list()生成列表：
messages = list(range(2, 11, 2))
将for循环和创建新元素的代码合并，并自动添加附加新元素：squares =
[value**2 for value in range(1, 11)]。注意这里的for 语句末尾没有冒号。
处理数字列表的函数
min(digits)，最大值
max(digits)，最小值
sum(digits)，求和
切片（处理列表的部分元素）
创建切片，指定要使用的第一个元素和最后一个元素的索引，不包含最后一个元
素的值：players[0:3]
没有指定第一个索引，将自动从列表开头开始：players[:3]
my_foods = ['pizza', 'falafel', 'carrot cake']
#会有两个不同的列表存在
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
my_foods = ['tomato', 'patato', 'fish', 'pork', 'banana']
friend_foods = my_foods
del(my_foods[0])
print(my_foods)
print(friend_foods)
print("\n")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
print(player.title())
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
print(dimension)
从指定元素到列表末尾，可省略终止索引，负数表示返回列表的倒数几位：
players[1:]、players[-3:]
复制整个列表（会有两个列表）：friend_foods = my_foods[:]
如果只是简单的把一个列表赋给一个变量，这两个变量都指向同一个列表，
而不是得到两个列表friend_foods = my_foods
使用for循环遍历切片：for player in players[-3:]:
元组
不可变的列表，使用圆括号标识：dimensions = (200, 50)
不能修改元组的元素，但可以给存储元组的变量赋值
if条件语句
条件测试
= 赋值
== 检查字符是否相等时，会区分大小写，若要不区分的话，可使用.lower()
!=，>，<，>=，<=
and，or
in包含在列表中，not in未包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
print(user.title() + ", you can post a response if you wish.")
requested_toppings = []
if requested_toppings:
for requested_topping in requested_toppings:
print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
else:
print("Are you sure you want a plain pizza?")
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
if requested_topping in available_toppings:
print("Adding " + requested_topping + ".")
else:
print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
布尔表达式：True，False；
if语句格式
if
if 列表名： 如果列表不为空，则会返回True;如果列表为空，返回值为False
使用多个列表
if-else
if-elif-else可多个elif，可省略else
注意：
（1）冒号：不能丢
（2）if、else后面的语句换行时要缩进
（3）elif可以有多句，else可以没有
（4）当需要检测多个条件满足的情况应该用多个if语句
字典
字典用放在{键:值}中的一系列键值对表示，键是字符串，需要加''，而值不一定：alien_0
= {'color': 'green', 'point': 5}
访问：指定字典名[键]，得到值：alien_0['color']
修改：alien_0['color'] = 'green'
添加：字典名[键]=值 alien_0['x_position'] = 0，Python不关心键-值对的添加顺序，而只关
心键和值的关联关系
alien_0={
'color':'gerrn',
'points':5,
'head':'big',
'phil':'python',
}
"还可以用于判断某值是否在字典的键里"
if 'erin' not in alien_0.keys(): print()
"以下两者等价"
for name in favorite_languages.keys():
for name in favorite_languages:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
print(name.title() + ", thank you for taking the poll.")
favorite_languages = {
'jen': 'python',
删除：del 字典名[键]——永远消失：del alien_0['point']
字典名={}：很多时候是先建立一个空字典，再分别添加键值对
较长的列表和字典，可以将键值对放在不同的行里，注意行前缩进。建议在最后一个键值对后面也加上逗号，为以后在下一行添加键-值对做好准备
遍历字典
遍历键值对：for key, value in user_0.items()
遍历字典中键值对 for 变量名1,变量名2 in 字典名.items()： for循环将每个键值对
存储到指定的变量中,变量1为键，变量2为值；
for 语句的第二部分包含字典名和方法items() ，它返回一个键—值对列表
即便遍历字典时，键-值对 的返回顺序也与存储顺序不同。Python不关心键—值
对的存储顺序，而只跟踪键和值之间的关联关系。
遍历键：for key in uers_0.keys()
.keys()方法实质上是返回一个列表，包含字典的所有键
遍历字典时，会默认遍历所有的键
按顺序遍历字典中的所有键，可使用函数sorted() 来获得按特定顺序排列的键列
表的副本
遍历值：for value in user_0.vlaues()
方法values() ，它返回一个值列表，而不包含任何键
为剔除重复项，可使用集合（set）；集合类似于列表，但每个元素都必须是独
一无二的
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
print(language.title())
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
print(alien)
aliens = [] # 创建一个用于存储外星人的空列表
# 生成30个字典，创建30个绿色的外星人
for alien_number in range(30):
new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
aliens.append(new_alien) # 在列表中存储字典
# 显示前五个外星人
for alien in aliens[:5]:
print(alien)
print("...")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
'''下面例子是有多个网站用户，每个都有独特的用户名，可在字典中将用户名作为键，然后将每
位用户的信息存储在
键从逻辑上讲是不能重复的，但重复了不会报错，只会认为是对键重新赋值，值
可以重复
嵌套
在列表中存储字典：[{}, {}, ..., {}]，aliens=[alien_0,alien_1,alien_2]
在字典中存储列表，即 键 对应的 值 可以为列表：{key: [value1, value2, ...]}
字典中存储字典，即键对应的值可以为字典：{key: {key1: value1, key2: vlaue2}}
一个字典中，并将该字典作为与用户名相关联的值。在下面的程序中，对于每位用户，我们都存
储了其三项信息：名、姓和居住地；为访问这些信息，我们遍历所有的用户名，并访问与每个用
户名相关联的信息字典'''
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():
print("\nUsername: " + username)
full_name = user_info['first'] + " " + user_info['last']
location = user_info['location']
print("\tFull name: " + full_name.title())
print("\tLocation: " + location.title())
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
print("\nYou're tall enough to ride!")
else:
print("\nYou'll be able to ride when you're a little older.")
current_number = 1
while current_number <= 5:
print(current_number)
current_number += 1
while unconfirmed_users:
current_user = unconfirmed_users.pop()
用户输入
input()函数用来等待用户输入，括号里可以为字符串变量也可以为字符串，其返回的值
是用户输入的字符串
int()函数可以将input的字符串转为数值，以供运算使用
while循环
while循环会不断运行，直到指定的条件不满足为止
while 'cat' in pets:
pets.remove('cat')
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
city = input(prompt)
if city == 'quit':
break
else:
print("I'd love to go to " + city.title() + "!")
current_number = 0
while current_number < 10:
current_number += 1
if current_number % 2 == 0:
continue
print(current_number)
# 首先，创建一个待验证用户列表，和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
current_user = unconfirmed_users.pop()
print("Verifying user: " + current_user.title())
confirmed_users.append(current_user)
# 显示所有已验证的用户
终止循环
用好标志（True,False）可以简化判断、循环语句
使用break终止整个循环
使用continue返回循环开头，忽略循环中余下的代码
注意避免无限循环，使用Ctrl+C关闭程序输出终端
使用while循环处理列表和字典
for 循环是一种遍历列表的有效方式，但在for 循环中不应修改列表，否则将导致
Python难以跟踪其中的元素
要在遍历列表的同时对其进行修改，可使用while 循环。通过将while 循环同列表和字
典结合起来使用，可收集、存储并组织大量输入，供以后查看和使用。
假设有一个列表，其中包含新注册但还未验证的网站用户；验证这些用户后，如
何将他们移到另一个已验证用户列表中呢？
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
print(confirmed_user.title())
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
# 提示输入被调查者的名字和回答
name = input("\nWhat is your name? ")
response = input("Which mountain would you like to climb someday? ")
# 将答卷存储在字典中
responses[name] = response
# 看看是否还有人要参与调查
repeat = input("Would you like to let another person respond? (yes/ no) ")
if repeat == 'no':
polling_active = False
# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
print(name + " would like to climb " + response + ".")
def greet_user(username):
"""显示简单的问候语"""
print("Hello, " + username.title() + "!")
greet_user('jesse')
def describe_pet(animal_type, pet_name):
"""显示宠物的信息"""
print("\nI have a " + animal_type + ".")
print("My " + animal_type + "'s name is " + pet_name.title() + ".")
可使用while循环提示用户输入任意数量的信息。下面来创建一个调查程序，其
中的循环每次执行时都提示输入被调查者的名字和回答。我们将收集的数据存储
在一个字典中，以便将回答同被调查者关联起来：
函数
def 函数名(参数): 定义以冒号结尾，函数的语句要缩进
将实参传递给函数，并将其值存储到形参username中
def greet_user(username)， username为形参
greet_user('Harry')，'Harry'为实参。
三引号文本是被称为文档字符串（docstring）的注释，描述了函数是做什么的。文档
字符串用三引号括起，Python使用它们来生成有关程序中函数的文档。
传递实参
位置实参，要求实参的顺序与形参顺序相同
关键字实参，其中每个实参都由变量名和值组成，所以就无需区分位置
describe_pet(animal_type='hamster', pet_name='harry')
'''在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认
值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调
用，还可清楚地指出函数的典型用法。'''
def describe_pet(pet_name, animal_type='dog'):
print("\nI have a " + animal_type + ".")
print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie') # 使用默认值
describe_pet('willie') # 使用默认值
describe_pet('harry', 'hamster') # 不使用默认值，传递位置实参
describe_pet(animal_type='hamster', pet_name='harry') # 不使用默认值，传递关键字实参
def get_formatted_name(first_name, last_name, middle_name=''):
if middle_name:
print(first_name + ' ' + middle_name + ' ' + last_name)
else:
print(first_name + ' ' + last_name)
get_formatted_name('Quincy', 'Zou')
get_formatted_name('Quincy', 'Zou', 'Middle')
def fuction_name(
a,b,c,
d,e.f):
fuction body...
在函数中，可使用return 语句将值返回到调用函数的代码行。返回值让你能够将程序的大部分繁重工
作移到函数中去完成，从而简化主程序。
编写函数时，还可以给某一形参给定默认值
可给每个形参指定默认值，在调用函数时，就无需再指定此形参的实参，函数会
使用默认值；
但在编写函数时要注意：形参列表中必须先列出没有默认值的形参，再列出有默
认值的形参
在指定默认值时，等号两边不要有空格，调用时也是如此，当然如果不适用默认
值，那么就可以重新传递新的实参
有时候需要将函数的实参变成可选的，这样使用函数的人就只需在必要时才提供
额外的信息。这时可以将那个不一定需要的形参默认值设为空，即''，并将其移
到形参列表末尾，再来个判断语句
函数形参过多时，导致代码长度超出80，不符合PEP8，可将 形参都放到下一行，甚
至下几行，要注意缩进(2个tab)
返回值
返回简单值 return full_name.title()
def get_formatted_name(first_name, last_name):
"""返回整洁的姓名"""
full_name = first_name + ' ' + last_name
return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
def build_person(first_name, last_name):
"""返回一个字典，其中包含有关一个人的信息"""
person = {'first': first_name, 'last': last_name}
return person
musician = build_person('jimi', 'hendrix')
print(musician)
你经常会发现，向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（如字
典）。将列表传递给函数后，函数就能直接访问其内容，提高处理列表的效率。
def print_models(unprinted_designs, completed_models):
"""
模拟打印每个设计，直到没有未打印的设计为止
打印每个设计后，都将其移到列表completed_models中
"""
while unprinted_designs:
current_design = unprinted_designs.pop()
# 模拟根据设计制作3D打印模型的过程
print("Printing model: " + current_design)
completed_models.append(current_design)
def show_completed_models(completed_models):
"""显示打印好的所有模型"""
print("\nThe following models have been printed:")
for completed_model in completed_models:
print(completed_model)
#函数调用
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
除非有充分理由使用副本，否则少使用，提高效率。函数使用现成列表可以避免浪费时间和内存
创建副本，尤其处理大型列表时
返回字典
传递列表
在函数中永久性修改列表
有时候需要禁止函数修改列表，则可以利用切片传递列表的副本，即
function_name(list_name[:])
def make_pizza(size, *toppings):
"""概述要制作的比萨"""
print("\nMaking a " + str(size) +
"-inch pizza with the following toppings:")
for topping in toppings:
print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
def build_profile(first, last, **user_info):
"""创建一个字典，其中包含我们知道的有关用户的一切"""
profile = {}
profile['first_name'] = first
profile['last_name'] = last
for key, value in user_info.items():
profile[key] = value
return profile
user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)
传递任意数量的实参
结合使用位置实参和任意数量实参，必须在函数定义中将接纳任意数量实参的形参
放在最后：def make_pizza(size, *toppings)
形参名*toppings 中的星号让Python创建一个名为toppings 的空元组，并将收到
的所有值都封装到这个元组中。注意，Python将实参封装到一个元组中，即便函
数只收到一个值也如此
Python将先匹配位置实参和关键字实参，余下的实参将收集到最后一个形参中去
使用任意数量的关键字实参：传递键值对，def build_profile(first, last, **user_info)
有时候需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信
息。在这种情况下，可将函数编写成能够接受任意数量的 键-值对 ——调用语句
提供了多少就接受多少。
形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收
到的所有键值对封装到这个字典中
将函数存储在被称为模块的独立.py文件中，再将模块导入主程序
import语句放在文件开头，import pizza 导入模块，然后就可以通过
pizza.funname()，使用pizza.py中的函数了
导入指定模块的指定函数：from module_name import function_0, function_1, ...；这
种情况下，不用再用module_name.function_name()调用，直接function_name()调用
就好
class Dog():
"""一次模拟小狗的简单尝试"""
def __init__(self, name, age):
"""初始化属性name和age"""
self.name = name
self.age = age
def sit(self):
"""模拟小狗被命令时蹲下"""
print(self.name.title() + " is now sitting.")
def roll_over(self):
"""模拟小狗被命令时打滚"""
print(self.name.title() + " rolled over!")
在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与
普通方法发生名称冲突。
def __init__(self, name, age):
self.name = name
self.age = age
使用*可以导入模块中的所有函数 from module_name import *，但不建议这么用，因
为可能会有很多函数重名
如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可
使用as给模块或函数指定别名，就可以用别名来调用函数和模块
from module_name import function_name as fn
import module_name as mn
函数编写指南
给形参指定默认值和函数调用关键字实参时，等号两边不要有空格：def
function_name(parameter_0, parameter_1='default_value')
函数定义超过了79字符，可在函数定义中输入左括号后按回车键，并在下一行按两
次Tab键，将形参列表和只缩进一层的函数体区分开
用两个空行将相邻的函数区分开
所有import语句都应放在文件开头
类
创建和使用类
创建类：class Dog(): 注意类名的首字母要大写
类中定义的函数称为方法：def 方法名称():
第一个定义的方法一般是__init__() ，这是一个特殊的方法，每当你根据Dog 类创建
新实例时，Python都会自动运行它
def __init__(self,形参): 其中形参self必不可少，且必须位于其他形参的前面
每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引
用，让实例能够访问类中的属性和方法
def sit(self):
print(self.name.title() + " is now sitting.")
def roll_over(self):
print(self.name.title() + " rolled over!")
class Car():
def __init__(self, make, model, year):
"""初始化描述汽车的属性"""
self.make = make
self.model = model
self.year = year
self.odometer_reading = 0 # 此值设为默认值，所以在设置形参时没有设置这个量
def get_descriptive_name(self):
"""返回整洁的描述性信息"""
long_name = str(self.year) + ' ' + self.make + ' ' + self.model
return long_name.title()
def read_odometer(self):
"""打印一条指出汽车里程的消息"""
print("This car has " + str(self.odometer_reading) + " miles on it.")
#使用类
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car=Car('audi','24',2016)
my_new_car.odometer_reading=23 # 这样就直接修改了默认值0
之后可以定义其他的方法，如果不需要其他的信息，方法的形参只有一个self
根据类创建实例：实例名=类() 可传入参数，my_dog = Dog('willie', 6)
根据类创建实例,Python将使用实参调用类中的方法_init_()创建表示特定的实
例，并自动返回给一个变量，这个变量可以自己设置
我们创建Dog 实例时，Python将调用Dog 类的方法__init__() 。我们将通过实参向
Dog() 传递名字和年龄；self 会自动传递，因此我们不需要传递它。每当我们根
据Dog 类创建实例时，都只需给最后两个形参（name 和age ）提供值。
访问实例属性：实例名.属性，
my_dog.name
调用方法：实例名.方法()，my_dog.sit()
使用类和实例
类中的每个属性都必须有初始值，哪怕这个值是0或空字符串
如果已在__init__()方法中设置属性默认值，则无需包含为它提供初始值的形参
修改属性值的三种方法
直接修改属性的值，通过实例直接访问
通过方法修改属性的值，无需直接访问属性，而是将值传递给一个方法，由它在
内部进行更新
def update_odometer(self,mileage):
self.odometer_reading = mileage
my_new_car.update_odometer(23) # 修改了默认值0
def increment_odometer(self,miles)
self.odometer_reading += miles
my_new_car.increment_odometer(100) # 通过+=改变了属性值
编写一个类的时候可以继承另一个类，原先的类称为父类，新的类称为子类。子类可以自动获得父类
的全部属性和方法，同时还可以定义自己的属性和方法
class Car(): #省略了父类的内容
class ElectricCar(Car)：
class Car(): #省略了父类的内容
class ElectricCar(Car)：
def __init__(self, manufacturer, model, year):
super().__init__(manufacturer, model, year) # 调用父类的方法_init_()，初始化父类的属性
class Car(): #省略了父类的内容
class ElectricCar(Car)：
def __init__(self, manufacturer, model, year):
super().__init__(manufacturer, model, year) # 调用父类的方法_init_()，初始化父类的属性
self.battery_size = 70 # 添加子类的新属性
def describe_battery(self): # 添加新方法
print()
class ElectricCar(Car)：
def fill_gas_tank(): #重新定义父类的方法
print()
class Battery():
def __init__(self, battery_size=60):
self.battery_size = battery_size
def describe_battery(self):
print("This car has a " + str(self.battery_size) + "-kWh battery.")
class ElectricCar(Car):
def __init__(self, manufacturer, model, year):
super().__init__(manufacturer, model, year)
self.battery = Battery() # battery属性是类Battery的一个实例
通过方法对属性的值进行递增/递减
继承
创建子类时，父类必须包含在当前文件中，且位于子类的前面，格式为 class 子类名
(父类名):
子类需要写继承父类属性的语句，super()函数将父类与子类关联，即调用
super().__init__()
super()函数调用之后，可添加子类新属性和新方法
重新定义父类方法，Python会忽略同名父类方法，只关注子类中定义的新方法
可以定义一个新的类，作为另一个类的一个属性
my_tesla = ElectricCar('tesla','model s',2016)
my_tesla.battery.describe_battery() #调用实例的battery属性里的方法
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
print(name.title() + "'s favorite language is " +
language.title() + ".")
要以任何方式使用文件——哪怕仅仅是打印其内容，都得先打开 文件，这样才能访问它
with open('pi_digits.txt') as file_object: #关键字with在不再需要访问文件后将文件关闭
contents = file_object.read() #方法.read()读取文件的全部内容
print(contents)
你也可以调用open() 和close() 来打开和关闭文件，但这样做时，如果程序存在bug，导致
close() 语句未执行，文件将不会关闭。
导入类：将一个类写在一个.py文件里，在另一个.py文件里导入这个类
from module import Class_1, Class_2, ...在调用类时，直接建立实例就可以，不需要其
他格式
也可以导入整个模块，格式为 import 模块名，但是在建立实例时，就需要用点号表
达式指定具体的类 my_beetle = car.Car()
Python标准库：
Python标准库 是一组模块，安装的Python都包含它
from collections import OrderdDict，OrderdDict实例行为几乎与字典相同，区别只在
于记录了键-值对的添加顺序
注意事项
类名应采用驼峰命名法 ，即将类名中的每个单词的首字母都大写，而不使用下划
线。实例名和模块名都采用小写格式，并在单词之间加上下划线
编写类时，都应紧跟在类定义后面包含一个文档字符串；每个模块也都应包含一个
文档字符串，对其中的类可用于做什么进行描述
类中可用一个空行分隔方法；模块中可用两个空行分隔类
导入模块时，应先写导入标准库的语句，再写导入自己编写的模块的语句
文件和异常
从文件中读取数据
读取整个文件：with open('路径') as 变量:
关键字with 在不再需要访问文件后自动将其关闭（隐式地调用close()函数）。使
用关键字with 时，open() 返回的文件对象只在with 代码块内可用
with open('text_files/filename.txt') as file_object:
file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
with open(file_path) as file_object:
'''使用关键字with时，open()返回的文件对象只能在with代码块中使用，要想在代码块外访问文
件内容，可将文件的各行存储在一个列表里，并在代码块外使用该列表'''
filename = 'pi_digits.txt'
with open(filename) as file_object:
lines = file_object.readlines() # 用方法readlines()将每一行的内容放到了lines列表中
for line in lines:
print(line.rstrip())
open()接受一个要打开的文件文件名称为参数，Python在当前执行的文件所在的
目录中查找读取文件，函数open() 返回一个表示文件的对象
方法read()读取文件的全部内容，在到达文件末尾时返回一个空字符串，而这个
空字符串显示出来就是一个空行，要删除多出来的空行，可在print 语句中使用
rstrip()
文件路径
相对路径
绝对路径
绝对路径在windows系统里是用\隔开，例如
D:\code_work\Pythonpi_digits.txt
过长的路径影响美观，可以将其放在一个变量里
逐行读取文件只需使用for循环将每一行的内容放到变量中即可：for line in
file_object: # 每一行的内容就放到了line中
方法readlines() 从文件中读取每一行，并将其存储在一个列表中
读取文本文件时，Python 将其中所有内容都解读为字符串，如果要作为数值使用，
就必须用int()或者float()转换
写入文件
调用open()时提供两个实参，第一个是要打开的文件名称，第二个实参告诉Python以
什么模式打开这个文件，如果省略了模式实参，默认为只读模式
'r'，读取模式
'w'， 写入模式
'a'，附加模式
'r+'，读取和写入模式
如果要写入的文件不存在，函数open()会自动创建它；
以('w')模式打开文件时，如果指定的文件已存在，Python会在返回文件对象前清空该
文件；
如果不想清空原文件，则可以使用'a'附加模式，写入的内容将会被添加到文件末尾
with open('programming.txt', 'a') as file_object:
file_object.write("I also love finding meaning in large datasets.n")
file_path = 'D:\code_work\Python\pi_digits.txt'
with open(file_path,'w') as file_object:
file_object.write('I lOVE YOU') #如果要写入多行语句，则需要添加换行符号
Python使用被称为异常 的特殊对象来管理程序执行期间发生的错误。
当发生错误时，如果编写了处理问题的代码，程序将继续运行，如果没有，程序将会停止，且会返回
一个traceback。
try-except——如果try代码块中的代码运行无误，将跳过except代码块；否则查找except代码块并运
行。
try:
print(5/0)
except ZeroDivisionError:
print("you can't divide by zero !")
filename = 'alice.txt'
try:
with open(filename) as f_obj:
contents = f_obj.read()
except FileNotFoundError as e:
msg = "Sorry, the file " + filename + " does not exist."
print(msg)
while True:
first_number = input("nFirst number: ")
if first_number == 'q':
break
second_number = input("Second number: ")
try:
answer = int(first_number) / int(second_number)
except ZeroDivisionError:
pass
else:
print(answer)
写入的语句用方法.write()函数write()不会在你写入的文本末尾添加换行符
Python只能将字符串写入文本文件，要存储数值数据时，必须先使用函数str()将其转
换为字符串格式
异常：处理问题的代码块为 try-except
try：可能引发错误的代码
except：如何处理错误
ZeroDivisionError除以0的异常
FileNotFoundError找不到文件的异常
pass：失败时一声不吭
else：仅在try代码块成功执行的正常情况下才运行的代码
while True:
first_number = input("nFirst number: ")
if first_number == 'q':
break
second_number = input("Second number: ")
try:
answer = int(first_number) / int(second_number)
except ZeroDivisionError:
print("You can't divide by 0!")
else:
print(answer)
你还可以使用json 在Python程序之间分享数据。更重要的是，JSON数据格式并非Python专用
的，这让你能够将以JSON格式存储的数据与使用其他编程语言的人分享。这是一种轻便格式，
很有用，也易于学习。
JSON（JavaScript Object Notation）格式最初是为JavaScript开发的，但随后成了一种常见格式，
被包括Python在内的众多语言采用。
import json #导入json模块
numbers = [2, 3, 5, 7, 11, 13] #创建一个数字列表
filename = 'numbers.json' #指定所存储的文件名称
with open(filename, 'w') as file_object: #以写入模式打开文件，让json能够将数据写入其中
json.dump(numbers, file_object) #使用json.dump()函数将数字列表存储到文件中
import json #导入模块
filename = 'numbers.json' #之前写入的文件
with open(filename) as file_object: #读取模式打开文件
numbers = json.load(file_object) #使用ison.load()加载存储在文件里的信息，并将其存
储到变量numbers中
print(numbers)
'''下面是一个只包含一个方法的测试用例，它检查函数get_formatted_name() 在给定名和姓时能否正
确地工作。（通常测试文件和函数文件最好是两个文件，这里为了方便看放一起了）'''
import unittest # 导入模块unittest
分析文本， 方法split()：以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储
到一个列表中
存储数据
模块json（JavaScriptObjectNotation）能将简单的Python数据结构转储到文件中，并
在程序再次运行时加载文件中的数据
json.dump()：接受两个实参，要存储的数据、可用于存储数据的文件对象
json.load()，加载文件中的数据
测试代码
测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求
导入Python中专门用于测试的模块unittest，创建一个包含Test字样的类继承
unittest.TestCase类，类中创建test_打头的方法，所有以test_打头的方法都将自动运行
# 以下是待测试的函数
def get_formatted_name(first, last):
"""Generate a neatly formatted full name."""
full_name = first + ' ' + last
return full_name.title()
class NamesTestCase(unittest.TestCase): # 定义测试用例NamesTestCase，它继承了unittest.TestCase类
def test_first_last_name(self): # 定义测试方法，命名以test打头
"""能够正确地处理像Janis Joplin这样的姓名吗？"""
formatted_name = get_formatted_name('janis', 'joplin')
self.assertEqual(formatted_name, 'Janis Joplin') # 比较测试值与预期值
unittest.main()
import unittest
from survey import AnonymousSurvey # 导入要测试的类AnonymousSurvey
class TestAnonmyousSurvey(unittest.TestCase): # 定义测试用例类TestAnonymousSurvey ，它继承了
unittest.TestCase类
def test_store_single_response(self): # 定义测试方法，命名以test打头
"""测试单个答案会被妥善地存储"""
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
my_survey.store_response('English')
self.assertIn('English', my_survey.responses)
unittest.main()
unittest.TestCase 类中提供的断言方法：核实结果与期望是否一致
assertEqual(a,b)——核实a==b
assertNotEqual(a,b)——核实a!=b
assertTrue(x)——核实x为True
assertFalse(x)——核实x为False
assertIn(item,list)——核实item在list中
assertNotIn(item,list)——核实item不在list中
测试类
使用unittest.TestCase.setUp()创建实例对象，并在每个测试方法中使用它们。如果在
TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以test_打头的方法
代码格式规范PEP8
https://www.python.org/dev/peps/pep-0008/
缩进每次用4个空格，在程序中混合使用制表符和空格可能导致极难解决的问题
==、>=、<= 两边各添加一个空格
行长：建议每行不超过80个字符
空行：将程序的不同部分分开，让代码看上去更整洁
包含多个函数时，建议每个函数之间空2行
