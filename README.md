# intrestpython
## 第一章：python基础
### 1.1 python数据类型
  python基础数据类型有六种：数值，字符串，列表（数组），元组，集合，字典。
  #### 1.1.1 整型
      （1）O开头为8进制；0x开头为16进制
      （2）浮点型：2.5E+03 = 2.5 * 10 ^ 3
      （3）复数：a + bi 或者complex(a, b)
      类型转换：int(x), float(x), complex(x)：将x转为复数，实数部分为x，虚数部分为0；complex(x, y)：将x和y转换为复数，实数部分为x，虚数部分为y。 
  #### 1.1.2 字符串
      python中没有字符类型，只有字符串类型，单字符也需要使用字符串表示，可以使用单引号，双引号。
      转义，使用\，转义字符（\）的用法：
      \(在行尾时)：表示续行符
      \\ 反斜杠符号
      \' 单引号
      \" 双引号
      ![image](https://user-images.githubusercontent.com/98450396/151285440-3dc0099e-a7b5-4599-b06c-a0598e0d9eb6.png)
      
      字符串格式化，使用%。例如：print("My Name = %d, Birthday = %d" %('lifei', '2012-05-04'))
