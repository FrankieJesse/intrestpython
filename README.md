# intrestpython
## 参考文献：https://www.runoob.com/python/python-func-enumerate.html
## 第一章：python基础
### 1.1 python数据类型
  python基础数据类型有六种：数值，字符串，列表（数组），元组，集合，字典。
  #### 1.1.1 整型
      （1）O开头为8进制；0x开头为16进制
      （2）浮点型：2.5E+03 = 2.5 * 10 ^ 3
      （3）复数：a + bi 或者complex(a, b)
      **类型转换：int(x), float(x), complex(x)：将x转为复数，实数部分为x，虚数部分为0；complex(x, y)：将x和y转换为复数，实数部分为x，虚数部分为y。str(x)将x专为string类型 **
  #### 1.1.2 字符串
      python中没有字符类型，只有字符串类型，单字符也需要使用字符串表示，可以使用单引号，双引号。
      转义，使用\，转义字符（\）的用法：
      \(在行尾时)：表示续行符
      \\ 反斜杠符号
      \' 单引号
      \" 双引号
      ![image](https://user-images.githubusercontent.com/98450396/151285440-3dc0099e-a7b5-4599-b06c-a0598e0d9eb6.png)
      
      字符串格式化，使用%。例如：print("My Name = %d, Birthday = %d" %('lifei', '2012-05-04'))
### 1.2 变量赋值
#### 1.2.1 变量命名规则
    以字母或下划线开头，数字、字母、下划线的组合。大小写敏感，不能与关键字相同。
#### 1.2.2 变量赋值
    赋值使用 = ， 该符号本质上是方法，有做操作数和右操作数，做操作数的数量必须与右操作数的数量一致。
    例如：a, b, c = 'lifei', 'Jesse', 3
    变量的类型，在赋值时确认。
    type(para)，该函数，可以确认para的数据类型。
### 1.3 运算符
#### 1.3.1 算数运算符
    +，-，*，/，
    % ： 取模，相除取余数
    // ：取商，相除，取商的整数部分
    ** ：幂，x的y次方，x ** y
#### 1.3.2 赋值运算符
    =
    +=
    -=
    *=
    /=
    %=
    //=
    **=   x **= y   等价于 x = x ** y
#### 1.3.3 位运算符
    & 按位与
    | 按位或
    ^ 按位异或
    ~ 按位非
    << 左移
    >> 右移
### 1.4 python的代码格式
#### 1.4.1 代码缩进
    使用代码缩进来表示{}，表示代码块。
#### 1.4.2 代码注释
    # 单行注释
    ''' 多行注释 
        多行注释
    '''
#### 1.4.3 空行
    在不同的定义之间，一般用空行隔开，非python语法。
#### 1.4.4 同一行显示多条语句
    不建议。语句之间使用;分隔即可。
## 第三章 Python选择结构
### 3.1 if语句
#### 3.1.1 if语句的一般格式
    if expression1 :
        statement1
    elif expression2 :
        statement2
    else :
        statement3
### 3.2 关系运算符
  ==
  !=
  />
  /<
  />=
  /<=
  例子：打印一个数字从个位开始的各个数位上的数值。
## 3.3 逻辑运算符
  and
  or
  not
  优先级顺序：not > and > or
  例子：判断一个年份是否是闰年
## 3.4 if嵌套
  if  ：
  elif ：
  else ：
# 第四章 循环结构
## 4.1 while 循环
    一般格式：
    while condition :
        statement
## 4.2 while中的else
    whle condition ：
        statement
    else 
## 4.3 while 无限循环
    while i == 1 :
        statement
## 4.4 for 循环的一般格式
    for variable in sequence :
        statement
## 4.5 for 中的range函数
    rang() 函数含义如下：
    range(start, stop, step)  其中，
    step可选，如果没有待step参数，默认step = 1， range函数反馈的是一个列表，即为左闭右开区间。range(2, 5)为2,3,4
    start可选，如果没有start，则start为1
## 4.6 其他语句
### break语句
    break语句会终止本层循环，且对于while else语句，会把else语句一并跳过
### continue语句
    强制回到循环最开始的部分，注意，循环变量会自动处理。
### pass语句
    空语句，无实际意义。

# 第五章 Turtle 画图
## 5.2 画笔运动命令
    描绘海龟的命令有很多，可以分为三类：画笔运动命令；画笔控制命令；全局控制命令
    turtle.forward()   想当前画笔方向移动多少像素
    turtle.backward()  向当前画笔相反方向移动多少像素
    turtle.right()  顺时针旋转多少度
    turtle.left() 逆时针旋转多少度
    turtle.pendown() 画笔移动时，不提笔（如果画笔从（1,1）移动到(10,10)， 不提笔的话，在两个点之间会有线）
    turtle.goto(x, y)  将画笔移动到新坐标
    turtle.penup()  移动时，不会只图形
    turtle.speed(speed)  画笔绘制的速度，0到10，包含0和10
    turtle.circle() 画圆，半径为正，表示圆心在画笔左边，否则在右边
## 5.3 画笔控制命令
    画笔控制命令，即为设置画笔的颜色、宽度的命令。
    turtle.pencolor 设置画笔颜色
    turtle.pensize() 设置画笔宽度
    turtle.color(color1, color2) 设置画笔的pencolor和fillcolor
    turtle.filling() 设置画笔是否在填充状态
    turtle.begin_fill() 画笔准备开始填充图形---所谓填充，是指在turtle画的封闭的图形中，填上颜色。
    turtle.end_fill() 画笔填充完成
    turtle.hideturtle() 隐藏画笔的turtle形状
    turtle.showturtle() 显示画笔的turtle形状
## 5.4 全局控制命令
    turtle.screensize() 设置画布的宽（单位像素）、高、背景颜色
    turtle.setup() 设置画布的大小，还可以设置窗口左上角顶点的位置
    turtle.clear() 清空turtle窗口，但是turtle的位置和状态不会改变
    turtle.reset() 清空窗口，充值turtle状态为起始状态
    turtle.undo() 撤销上一个turtle动作
    turtle.isvisible() 返回当前turtle是否可见
    turtle.stamp() 复制当前图形
    turtle.write() 写文本
    turtle.shape() 设置乌龟的图形形状，取值："arrow" "turtle" "circle" "square" "triangle" "classic"
# 第六章 Python特征数据类型
    enumerate函数：
    enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    Python 2.3. 以上版本可用，2.6 添加 start 参数。
## 6.1 列表
    列表跟数组一个性质，列表中的元素可以是异构的。列表中的元素时可以被更改和删除的。列表也可以做合并操作，要通过函数来操作。
    列表的访问有三种形式：list[1:3]即返回list[1],list[2]两个元素；list[3]直接访问第四个元素；for listItem in list。
### 6.1.1 列表的函数
    len(list)
    max(list)
    min(list)
    list(seq)---将元组转换为列表
    id(list) 获取列表对象的内存地址
### 6.1.2 列表的方法
    list.copy() 返回一个新的列表
    list.clear() 将list中元素清空，长度为0
    list.sort() 列表元素按升序排序
    list.sort(reverse = True) 列表元素按照降序排序
    list.reverse() 反向列表中的元素
    list.remove(obj) 删除某个元素，输入为list的某一个元素
    list.pop(index) 移除列表中的一个元素（默认最后一个元素）， 并且返回该元素的值
    list.insert(index, obj) 对obj插入到index的位置，原index后边的值向后移动
    list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值，扩展为新的列表
    list.count(obj) 统计obj出现的次数
    list.index(obj) obj第一次出现的index的值
## 6.2 元组
    元组与列表相比，元组是不可更改的列表。即他是常量的元组。元组可以扩展，即不同的元组可以相加。
    元组的访问与列表的访问是一致的。
### 6.2.1 元组连接与删除
    连接使用+，删除使用del，元组不存在删除单个元素的操作，因为元组是不可更改的。
### 6.2.2 元组的函数
    len(tuple)   元组元素的个数
    max(tuple)   元组元素最大值
    min(tuple)   元组元素最小值
    tuple(seq)   将其他序列转换为元组
### 6.2.3 元组的方法--待定，验证未通过。
    tuple.count()   同len方法
    tuple.index(tupleValue) 获取tupleValue在tuple中的位置。   
## 6.3 字典
    字典与列表比较相似，只不过把每个元素编程了健值对，即，健与值，其中，主键必须唯一。
    字典的访问：
    值的访问，可以通过下标来访问，也可以通过values()来访问。
    健的访问，可以通过keys()来访问。
    健值同时访问，可以通过items()来访问。
### 6.3.1 字典元素的增删改查
    增加：
    dictionary['newKeys'] = 'newValues'
    删除：
    del dictionary['keys1']
    修改：
    dictionary['oldKeys'] = 'newValues'
### 6.3.2 字典元素函数
    1	cmp(dict1, dict2)
    比较两个字典元素。
    2	len(dict)
    计算字典元素个数，即键的总数。
    3	str(dict)
    输出字典可打印的字符串表示。
    4	type(variable)
    返回输入的变量类型，如果变量是字典就返回字典类型。
### 6.3.3 字典元素的方法
    1	dict.clear()
    删除字典内所有元素
    2	dict.copy()
    返回一个字典的浅复制
    3	dict.fromkeys(seq[, val])
    创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
    4	dict.get(key, default=None)
    返回指定键的值，如果值不在字典中返回default值
    5	dict.has_key(key)
    如果键在字典dict里返回true，否则返回false
    6	dict.items()
    以列表返回可遍历的(键, 值) 元组数组
    7	dict.keys()
    以列表返回一个字典所有的键
    8	dict.setdefault(key, default=None)
    和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
    9	dict.update(dict2)
    把字典dict2的键/值对更新到dict里
    10	dict.values()
    以列表返回字典中的所有值
    11	pop(key[,default])
    删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
    12	popitem()
    返回并删除字典中的最后一对键和值。
