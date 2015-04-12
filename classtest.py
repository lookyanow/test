#!/usr/bin/env python

#class Person:
#	def __init__(self, name, age, pay=0):
#		self.name = name
#		self.age = age
#		self.pay = pay
#	def getname(self):
#		return self.name
#	
#	def sum(self):
#		return self.age + self.pay
#
#class Manager(Person):
#	def show_job_name(self):
#		print "My name is %s and I'am a %s" % (self.name, "manager")
#class Admin(Person):
#	def show_job_name(self):
#		print "My name is %s and I'am a %s" % (self.name, "admin")		
#

from classlib import Admin
from classlib import Manager

ivan = Admin('Ivan Lookyanow', 12, 5000)
vasya = Manager('Vasya Pupkin', 20)

ivan.show_job_name()
vasya.show_job_name()

name = ivan.new_show_job_name()
print name 
print vasya.pay  
print ivan.pay  
