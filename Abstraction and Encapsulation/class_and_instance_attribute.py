Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Employee:
	numberOfWorkingHours = 40

	
>>> employeeOne = Employee()
>>> employeeTwo = Employee()
>>> employeeOne.numberOfWorkingHours
40
>>> employeeTwo.numberOfWorkingHours
40
>>> Employee.numberOfWorkingHours
40
>>> Employee.numberOfWorkingHours = 45
>>> employeeOne.numberOfWorkingHours
45
>>> employeeTwo.numberOfWorkingHours
45
>>> 
>>> # Create Instance Attribute
>>> employeeOne.name = "John"
>>> employeeOne.name
'John'
>>> employeeTwo.name
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    employeeTwo.name
AttributeError: 'Employee' object has no attribute 'name'
>>> employeeTwo.name = "Mary"
>>> employeeOne.numberOfWorkingHours = 40
>>> employeeOne.numberOfWorkingHours
40
>>> employeeTwo.numberOfWorkingHours
45
>>> employeeOne.age
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    employeeOne.age
AttributeError: 'Employee' object has no attribute 'age'
>>> 
