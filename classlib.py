class Person:
	def __init__(self, name, age, pay=0):
		self.name = name
		self.age = age
		self.pay = pay
	def getname(self):
		return self.name

	def sum(self):
		return self.age + self.pay

class Manager(Person):
	def __init__(self,name,age):
		Person.__init__(self,name,age,10000)
	def show_job_name(self):
		print "My name is %s and I'am a %s" % (self.name, "manager")
class Admin(Person):
	def show_job_name(self):
		print "My name is %s and I'am a %s" % (self.name, "admin")
	def new_show_job_name(self):
		return self.name
