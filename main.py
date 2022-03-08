"""在实验一的基础上抽象出两个类对学生成绩进行管理"""
class Student():
    def __init__(self, name,chinese,english,math,PE,history,average = ''):
        self.name = name
        self.chinese = chinese
        self.english = english
        self.math = math
        self.PE = PE
        self.history = history
        self.average = average

    def printinfo(self):
        print("Name:", self.name, end=' ')
        print("chinese:", self.chinese, end=' ')
        print('english:', self.english,end = ' ')
        print("Math:", self.math,end = ' ')
        print('PE:',self.PE,end = ' ')
        print('history:',self.history,end = ' ')
        if self.average == '':
            return
        else:
            print('average:',self.average)
        return

class StudentSystem():
	studentinfo = []
	def __init__(self):#不需要其他参数，只有一个返归自身的self，调用时也不传递其它参数
		self.studentinfo.append(Student('Lucy', '94', '93','91','93','99'))
		self.studentinfo.append(Student('John', '98', '92','91','90','96'))
		self.studentinfo.append(Student('Flank', '95', '90','97','96','97 '))
		self.studentinfo.append(Student('Tony','95','93','92','90','98'))
		#类作为属性

	def printmenu(self):
		print('-'*20)
		print('学生信息管理系统v1.0')
		print('1.添加学生信息')
		print('2.删除学生信息')
		print('3.修改学生信息')
		print('4.显示所有学生信息')
		print('5.查找学生信息')
		print('6.按平均分排序显示所有学生信息')
		print('7.将文件中学生的数据资料写入系统')
		print('8.退出系统')
		print('-'*20)
		return

	def addinfo(self):
		# 检查学生是否已存在系统之中
		name = input('请输入需要添加学生的姓名： ')
		g = 0
		if name == '':
			while g <4:
				print('请输入需要添加信息的学生姓名！')
				name = input('请输入需要添加学生的姓名： ')
				if name == '':
					g += 1
					if g == 3:
						print('因为你不输入学生姓名，添加信息操作失败！')
						return
				else:
					for stu_1 in self.studentinfo:	#stu_1相当于Student这个类的一个实例
						if name.lower() == stu_1.name.lower():	#句点表示法stu_1为实例，没有用类调用句点表示的
							print("当前学生已存在于系统中，无需再次添加！")
							return
					break
		else:
			for stu_1 in self.studentinfo:	#stu_1相当于Student这个类的一个实例
				if name.lower() == stu_1.name.lower():	#句点表示法stu_1为实例，没有用类调用句点表示的
					print("当前学生已存在于系统中，无需再次添加！")
					return
		name = name.title()
		math = input("请输入学生数学成绩: ")
		e = 0
		while math == '':
			math = input("请输入学生数学成绩: ")
			e = e+1
			if e == 5:
				print('因为你不输入学生成绩，添加信息失败！')
				return
		chinese = input("请输入学生语文成绩: ")
		e = 0
		while chinese == '':
			chinese = input("请输入学生语文成绩: ")
			e = e + 1
			if e == 5:
				print('因为你不输入学生成绩，添加信息失败！')
				return
		english = input("请输入学生英语成绩: ")
		e = 0
		while english == '':
			english = input("请输入学生英语成绩: ")
			e = e + 1
			if e == 5:
				print('因为你不输入学生成绩，添加信息失败！')
				return
		PE = input("请输入学生体育成绩: ")
		e = 0
		while PE == '':
			PE = input("请输入学生体育成绩: ")
			e = e + 1
			if e == 5:
				print('因为你不输入学生成绩，添加信息失败！')
				return
		history = input("请输入学生历史成绩: ")
		e = 0
		while history == '':
			history = input("请输入学生历史成绩: ")
			e = e + 1
			if e == 5:
				print('因为你不输入学生成绩，添加信息失败！')
				return
		average = ''
		g = Student(name,chinese,english,math,PE,history,average)
		self.studentinfo.append(g)
		print("添加学生%s信息操作成功！" % name.title())
		return


	def delinfo(self):
		# 检查被删除学生不存在系统中
		name=input('请输入要删除信息的学生姓名： ')
		active = False
		for stu_2 in self.studentinfo:#加self表示属于当前类，不加self时是是句点表示法
			if name.lower() == stu_2.name.lower():#stu——2相当于对类Student的实例
				active=True
				del_stu = stu_2
		if active:
			self.studentinfo.remove(del_stu)	#remove删除特定值而不知道其位置
			print("删除学生%s信息操作成功!" % name.title())
		else:
			print("当前学生不存在于系统中，删除操作失败!")
		return

	def modifystuinfo(self):
		#检查被修改学生是否在系统中
		name=input('请输入要修改信息的学生姓名： ')
		length = len(self.studentinfo)
		for i in range(length):
			d = self.studentinfo[i]
			if name.lower() == d.name.lower():
				d.math = input("请输入学生%s修改后的数学成绩: " % name.title())
				d.chinese = input("请输入学生%s修改后的语文成绩: " % name.title())
				d.english = input("请输入学生%s修改后的英语成绩: " % name.title())
				d.PE = input("请输入学生%s修改后的体育成绩: "% name.title())
				d.history = input("请输入学生%s修改后的历史成绩: "% name.title())
				print('修改学生%s信息成功！'%name.title())
				return
		print("修改操作失败，学生不在系统中")

	def searchinfo(self):
		search=input('请输入需要查找信息的学生姓名： ')
		active = False
		for stu_4 in self.studentinfo:
			if search.lower() == stu_4.name.lower():
				active = True
				search_stu = stu_4
		if active:
			print("该学生信息如下：")
			search_stu.printinfo()
		else:
			print("当前学生不存在于系统中，查找操作失败~")
		return

	def showstuinfo(self):
		print('-'*20)
		print('所有学生信息如下： ')
		print('-'*20)
		for tempinfo in self.studentinfo:
			tempinfo.printinfo()
			print('\n')
		return

	def sort(self):
		print('学生信息按平均分从高到低排名如下： ')
		for stu in self.studentinfo:
			d = stu
			a=int(d.chinese)
			b=int(d.math)
			c=int(d.history)
			e=int(d.PE)
			d=int(d.english)
			average=(a + b + c + d + e) / 5
			stu.average = average
		for stu1 in self.studentinfo:
			sorted_studentinfo=sorted(self.studentinfo,key=lambda stu1:stu1.average,reverse=True)
		for stu1 in sorted_studentinfo:
			stu1.printinfo()
			print("\n")
		return

	def addstudent(self):
		with open('E:\编程文档\纯文本文件\实验二学生信息资料.txt') as add:
			d = add.readlines()
			f = d[1:]
			for i in f:
				name = i.split()[0]
				chinese = i.split()[1]
				english = i.split()[2]
				math = i.split()[3]
				PE = i.split()[4]
				history = i.split()[5]
				self.studentinfo.append(Student(name,chinese,english,math,PE,history))
			print('学生信息读入成功！')

	def saveinfo(self):
		a = 'E:\编程文档\纯文本文件\实验二学生信息资料.txt'
		with open('E:\编程文档\纯文本文件\实验二学生信息资料.txt','w') as f:
			f.write('Name Chinese English Math PE History'+'\n')
			for i in self.studentinfo:
				k = i.name+'   '+i.chinese+'    '+i.english+'    '+i.math+'    '+i.PE+'    '+i.history
				f.write(k+'\n')
			print('所有学生信息已保存到原文档！')#文件被更改，执行第一次以后源文件被更改

def main():
	stusystem = StudentSystem()		#创建了一个实例instance，不能直接用类名调用方法
	h = 0
	while h < 4:
		stusystem.printmenu()
		try:
			key = int(input('请输入功能对应的数字： '))
		except ValueError:
			if h < 3:
				print('请输入数字进行相应操作或输入7进行推出系统操作！')
			else:
				print('因为你不输入相应数字，系统自动关闭！')
			h = h+1
			continue
		else:
			if key == 1:
				stusystem.addinfo()
			elif key == 2:
				stusystem.delinfo()
			elif key == 3:
				stusystem.modifystuinfo()
			elif key == 4:
				stusystem.showstuinfo()
			elif key == 5:
				stusystem.searchinfo()
			elif key ==6:
				stusystem.sort()
			elif key == 7:
				print('如果你是第一次录入文件内学生信息，请输入enter进入'+
				'\n\n如果是第二次以上，对不起，学生信息不需要重复录入'+
				'\n任意键返回首页！\n')
				d = input('请确认你的命令： ')
				if d == 'enter':
					stusystem.addstudent()
				else:
					pass		#返回原函数执行
			elif key == 8:
				quitconfirm=input("Are you sure quiting?  （yes or no?）: ")
				if quitconfirm=='Yes'.lower():
					print('\n如果不想将所有学生信息存储到源文件，请输入nO\n'+
					'如果想要将学生信息保存到源文件，则以任意键结束并保存！')
					w = input('请输入你的命令（NO/任意键）： ')
					if w.lower() != 'no':
						stusystem.saveinfo()
					else:
						pass
					return
				else:
					print('please enter a true number. Try again!')
main()
