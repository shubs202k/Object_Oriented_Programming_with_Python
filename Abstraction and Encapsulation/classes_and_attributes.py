Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Employee:
	name = 'Ben'
	designation = 'Sales Executive'
	salesMadeThisWeek = 6
	def hasAchievedTarget(self):
		if self.salesMadeThisWeek >= 5:
			print("Target has been achieved")
		else:
			print("Target has not been achieved")

			
>>> employeeOne = Employee()
>>> employeeOne.name
'Ben'
>>> employeeOne.hasAchievedTarget()
Target has been achieved
>>> employeeTwo = Employee()
>>> employeeTwo.name
'Ben'
>>> 
>>> # Everything in Python is an Object
>>> numbers = [1,2,3]
>>> type(numbers)
<class 'list'>
>>> numbers.append(4)
>>> numbers
[1, 2, 3, 4]
>>> 
