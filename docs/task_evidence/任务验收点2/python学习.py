import math
print("hello world")
print("I'm eng")
print("I say \" It's a good day\"")
print("How are you?\nI'm fine,thank you,and you?")
print("""12345
67890
12345
67890""")
greet_chinese="你好"
greet_english="Hello"
print(greet_chinese+" 张三")
print(greet_english+" Mike")
print("""python变量命名规则
一 下划线命名法
1 字母全部小写
2 不同单词用“_”隔开
二 驼峰命名法
单词用首字母大写分割

""")
print("整数为数字，如6，加上引号的是字符串，如\"6\",形如6.0为浮点数，加减乘除与cpp一样")
print("乘方写法为n**m,为n的m次方")
print("""引入math库后，可进行更复杂运算
下写一元二次函数求根公式
以-x*x-2*x+3=0为例
""")
a=-1
b=-2
c=3
x1=(-b+(b**2-4*a*c)**0.5)/2*a
x2=(-b-(b**2-4*a*c)**0.5)/2*a
print("x1=",x1)
print("x2=",x2)
"""注释的写法：
1 三引号
2 #开头，但是只能适用于单行"""
"""数据类型：
1 字符串str：用""包裹，可用"abcd"[0]提取a，用len("1234")获取字符串长度
2 整形 int
3 浮点型 float
4 布尔类型 bool True False
5 空值类型 NoneType 只有None一个值，用法为在创建变量而不知道变量的值的时候，可以用None赋值
当不清楚变量类型，可用type()返回变量类型
"""
# 1 str
a="abcdefg "
b=len(a)
print(b)
print(a[2])
print(a[(len(a)-6)])
# 2整形
zx=1
#3 浮点型
fdx=1.0
# 4 布尔类型
a1=True
a2=False
#5 空值类型
a3=None
# 6 type函数
print(type(a1),type(a2),type(a3),type(zx),type(fdx),
      type(a))
""" input 的运用
例：计算BMI
"""
weight=input("请输入您的体重（单位：kg）：")
height=input("请输入您的身高（单位：m）：")
height=float(height)
weight=int(weight)
BMI=weight/(height*height)
print("您的BMI为"+str(BMI))
# if语句
temperature=int(input("请输入今天的温度："))
sun=bool(input("今天是否有太阳（有为True，无为False）："))
if temperature>=10:
    print("天气不错，可以出门")
else:
    if sun==True:
        print("勉强可以出门吧")
    else:
        print("今日不宜出门")
#条件判断中 and和&&一个意思，or和||一个意思，not和！一个意思
#优先级 not>and>or 闹太套
"""列表 ："""
shopping_list=["apple","watch"]
"""再加入东西"""
shopping_list.append("cat")
print(shopping_list)
shopping_list.remove("cat")
print(shopping_list)
#用len可以获得列表的元素个数，列表[n]可获得第n个元素
print(len(shopping_list))
print(shopping_list[0])
#一些简单的函数
price=[113,13243,3543,23,1]
max=max(price)
print(max)
min=min(price)
print(min)
sorted_price=sorted(price)
print(sorted_price)
#字典的应用
#形式上是字典名={"键名1":"值1","键名2":"值2"}
#获取值：字典名[”键名“],即可获取对应的值
#键的类型必须不可变，即不能用列表
#此山是需要用元组tuple来代替列表的作用，元组名=("1","2"),对于元组，remove和append都不能用（不可改变）
#字典是可变的，字典名["键名"]=“值”即可加入键值对或者修改键值对
#del 字典名[]即可删除某个键值对
# print("键名" in 字典名 )会返回相应的布尔值，判断字典中是否存在相应的键值对
#下面是一个练手
Alice_dict={("爱丽丝","蔚蓝档案"):"千年科学学园游戏开发部的吉祥物，真实身份是不可名状的古代兵器“光之剑”的载体（Key）。她是一个被桃伊和绿从废墟里捡回来的机器人少女，把现实世界当成RPG游戏来理解，口头禅是“邦邦咔邦！”。性格纯真无邪，拥有极高的物理破坏力（拿着巨大的电磁炮），但在朋友们的呵护下，她战胜了作为兵器的宿命，立志成为一名守护他人的“勇者”。",
            ("爱丽丝","Nikke"):"隶属无限部队的狙击型妮姬，常年穿着粉色紧身衣。由于体温过高，必须依靠这套带有冷却功能的战斗服维持机能。她的心智停留在童话世界中，患有严重的妄想症，坚信自己是在寻找“红桃皇后”的旅途中，并将指挥官视为引导她的“兔子先生”。虽然言行像个孩子，但她拥有极强的战斗力和穿透能力，是许多玩家推图的主力。",
            ("爱丽丝","东方Project"):"居住在魔法森林的“七色的人偶使”，一位由人类修行而成的魔法使。她性格冷淡、孤僻但有些傲娇（尤其是对魔理沙），擅长同时操控多个人偶（如上海人形、蓬莱人形）进行战斗和日常生活。她不仅仅是操纵人偶，更是致力于创造出拥有自主意识的“自律人偶”，在弹幕游戏中以华丽而复杂的“人偶海”战术著称。",
            ("爱丽丝","刀剑神域"):"原本是卢利特村村长的女儿，因触犯禁忌被带走并改造成“整合骑士 Alice Synthesis Thirty”。她身披金甲，手持神器“金木樨之剑”，是公理教会的最强战力之一。她突破了人工智能（Bottom-up AI）的限制，拥有了真正超越系统的自我意志（右眼的封印），性格高洁、刚毅，是为了守护人类界而战的女武神。",
            ("爱丽丝","爱丽丝梦游仙境"):"维多利亚时代的英国小女孩。她是一切“爱丽丝”概念的起点：金发、蓝裙、白色围裙。她拥有强烈的好奇心和一种近乎冷酷的逻辑感——即使在完全荒诞的仙境中，她也在试图用礼仪和常识去理解世界。她既不是战士也不是法师，她只是一个在逻辑崩坏的世界里保持清醒的“观察者”。",


          }
char=input("请输入您想查询的角色名：")
work=input("请输入该角色所在的作品：")
if (char,work) in Alice_dict:
    print("您查询的爱丽丝设定如下："+Alice_dict[(char,work)])
#for循环：for 变量 in 可迭代对象
#           对变量的操作
for (char,work),intro in Alice_dict.items():
    if char=="爱丽丝" :
        print(char+","+work+":"+Alice_dict[(char,work)])
#for与range结合
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)
#while循环主要用在不知道循环次数但是知道循环条件的时候用
total_sum = 0.0
count = 0
print("请输入数字(输入 q 结束)：")
while True:
    user_input = input()

    if user_input == 'q':
        break


    total_sum = total_sum + float(user_input)
    count = count + 1

# 循环结束后计算平均值
if count > 0:
    ave = total_sum / count
    print(f"您输入了 {count} 个数字，平均值为：{ave:.2f}")
else:
    print("您没有输入任何数字。")
#.format的运用：可用于替换关键词，在字符串“dwqdqwdwqdqwdqwfcqw{0}uhihiuuiuui{11}”.format(变量1，变量2)，此时0就会变成变量1，1会变成变量2
#f字符串：f“sadasdas{变量名}sad”此时打印会直接带入该变量的值
#对浮点数，浮点数1:.2f就是保留两位小数
#函数：def 函数名(变量1，变量2)：
#        具体内容
def calculate_circle(r):
    S=math.pi*r**2
    C=2*math.pi*r
    print("半径为"+str(r)+"的圆的面积为"+f"{S:.2f}")
    print("半径为"+str(r)+"的圆的周长为"+f"{C:.2f}")
calculate_circle(10)
#此时默认return None，用a=calculate_circle(10),只能得到a=None
def calculate_circles(r):
    S=math.pi*r**2
    C=2*math.pi*r
    return S
a=calculate_circles(10)
print(a)
#类与对象  给类命名的时候一般用帕斯卡命名法 class Abc
##构造函数的名字必须为__innt__(self,参数1,参数2，参数3)
#然后构造函数内部：self.参数一=参数1......
#使用时，abc=Abc(参数，参数)即可
#print(字符串*数字)，打印数字遍字符串
class Student():
    def __init__(self,name,number):
        self.name=name
        self.number=number
        self.grades={"线性代数":0,"微积分":0,"cpp":0}

    def SetGrade(self,course,grades):
        if course in self.grades:
            self.grades[course]=grades
    def ShowGrade(self):
        print(str(self.name)+"  "+str(self.number)+"  "+str(self.grades))
ming=Student("小明" ,"U202513133")
ming.SetGrade("线性代数",95)
ming.ShowGrade()
#子类与父类
#class 父类  class 子类(父类)此时子类会继承父类的成员以及成员函数，在调用函数时，
# 如果子类有自己的优先调用自己的，没有的话就会使用父类的
#如果想在子类中调用父类函数，用super().父类函数即可
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"大家好，我是 {self.name}，今年 {self.age} 岁。")

    def eat(self):
        print(f"{self.name} 正在吃饭。")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"大家好，我是学生 {self.name}，学号 {self.student_id}。")
    def study(self):
        print(f"{self.name} 正在努力修学分！")
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"大家好，我是 {self.name} 老师，教 {self.subject}。")

    def teach(self):
        print(f"{self.name} 正在讲台上讲课。")

ming = Student("小明", 20, "U202513133")
ming.introduce()
ming.eat()
ming.study()
lao_wang = Teacher("老王", 45, "线性代数")
lao_wang.introduce()
lao_wang.eat()
lao_wang.teach()
#对文件进行操作
#f=open("文件地址"，“r（只读）”或“w（只写）”，encording=“utf-8”（编码方式）)
#print(f.read(字节数))即可，并且会记忆阅读的位置，下次再print会接着从上次结束的地方开始
#print(f.readline)则会读取一行，同样会记忆阅读的位置，可用while循环逐行打印
#f.readlines会将每一行内容存在字符串中，可用for循环逐行打印
#关闭文件用f.close
#或用 with open("地址") as f：
#下面接对文件的操作
#即可实现自动关闭文件
with open(r"C:\Users\eng\Desktop\短歌行.txt","r", encoding="utf-8") as f:
    lines=f.readlines()
    for line in lines:
        print(line)
#对于写内容，可以用w或者a，a为附加，w为只写，w会清空之前的内容，a不会，a+可同时追加与阅读，r+可同时覆写与阅读

file_path = "静夜思.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("床前明月光，\n")
    f.write("疑是地上霜。\n")

with open(file_path, "a", encoding="utf-8") as f:
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")
with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())
#错误捕捉
"""可以用try：
           要执行的代码
        except 错误类型  ：
        else ：
              没错误的时候执行的语句
        finally：
                无论有没有错都执行的
"""