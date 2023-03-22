
Oop: Object Oriented Programming -solving a problem by creating an object is one of the most approch in programming. this is called Object Oriented Programming.this concept is focus on reuse the code.

class : a class is a blueprint for creating object, class not store memory it is just a instance.
camel case : rajendraKumarRanda
pascal case : RajendraKumarRanda
syntax:
class class_name:   # it is written in pascal case
  # variable and mathod

object : it is an instantiation of a class,when class is defined,memory is allocated only after object instantiation. object of a class can be invoke the method available to it without revealing the implementation details to the user.---abstraction & encapsulation
syntax:
object_name = class_name()
object_name.properties = value

example:
class RailwayForm:
  formType = "RailwayForm"
  def printData(self):
    print(f"name: {self.name}")
    print(f"train: {self.train}")

rajForm = RailwayForm()
rajForm.name = 'raj kumar'
rajForm.train = 'xyz express'
rajForm.printData()

example:
class EmployeeData:
  company = "VS CODE"
  def employee(self):
    print(f"{self.name} Details:")
    print(f"name:{self.name}")
    print(f"salary:{self.salary}")
    print(f"city:{self.city}")
    print(f"*********************")
# object 1
emp1 = EmployeeData()
emp1.name = 'rajendra'
emp1.salary = 20000
emp1.city = 'INDORE'
print(EmployeeData.company)
emp1.employee()
# object 2
emp2 = EmployeeData()
emp2.name = 'mohan'
emp2.salary = 15000
emp2.city = 'BHOPAL'
# EmployeeData.company = "YAHOO!"    #change the value of company for all object
emp2.company = "XYZ"   #change the value of company for this object
print(emp2.company)
emp2.employee()

example change value using class_name
class Employee:
  company = 'Google'
  salary = 100
raj = Employee()
ram = Employee()
raj.salary = 500
print(raj.company)
print(ram.company)
print(raj.salary)
print(ram.salary)

raj.salary = 500   #creating instance attribute for 'raj' object
Employee.company = 'Yahoo!'
print(raj.company)
print(ram.company)
print(raj.salary)
print(ram.salary)
ram.company = 'youtube'
print(raj.company)
print(ram.company)

print(ram.address)  #attributeError: 'Employee' object has no attribute 'address' ,attribute not exist in class or instance
ram.address = 'dhar'
print(ram.address)

class attribute: attribute defined inside the class
instance attribute: an attribute that belongs to instance(object) assuming the class from previous example.
syntax: raj.salary = 500 #adding instance attribute
instance attribute take preference over class attribute during assignment & retrival


SELF: it refers instance of class it is automatically passed with function call from an object
after remove 'self ' you'll get error like that ".getSalary()" takes 0 positional arguments but 1 was given.
# example:
class Employee:
  company = "Google"
  def getSalary(self):
    print("sal is 100K")
harry = Employee()
harry.getSalary() #it means 'employee.getSalary(harry)' <--just for understanding

example:
class Employee:
  company = "Google"
  def getSalary(self):
    print(f"company: {self.company} \nsalary is {self.salary}")
harry = Employee()
harry.salary = 100000
harry.getSalary()

staticmethod: sometimes, we need to define a function who don't use/need self parameter so for that we can define them as static method.
exapmle:
class Employee:
  company = "Google"
  def getData(self,sign):
    print(f"company: {self.company} and salary will be {self.salary} \n{sign}")
  @staticmethod   #it's a decorator to mark greet as a static method
  def greet():
    print("have a good day...")
  @staticmethod   #it's a decorator to mark greet as a static method
  def greet():
    print("now, it's 9am")

harry = Employee()
harry.salary = 1000
harry.getData("thanks!")
harry.greet()  #employee.greet()
harry.time()


constructor: '_ _ init _ _' it is a special method which is first run as soon as the object created, it is known as constructor, it takes self args and also take further args.
example
class Employee:
  company = "Google"
  def __init__(self):
    print("employee is created!")
harry = Employee()  # employee is created!

example
class Employee:
  company = 'facebook'
  def __init__(self,name, salary, subunit):
    self.name = name
    self.salary = salary
    self.subunit = subunit
    print("employee created!")

  def getDetails(self):
    print(f"name :{self.name}")
    print(f"salary :{self.salary}")
    print(f"subunit :{self.subunit}")

  def getData(self,signature):
    print(f"company is {self.company} and salary will be {self.salary} \n(signature)")

  @staticmethod
  def greet():
    print("have a good day !!!")

  @staticmethod
  def time():
    print("time : 9am")

raj = Employee("raj",1000, "Youtube")
# raj = Employee()   #error:missing 3 args
raj.getDetails()
you dont need to write manually like raj,name = 'raj'

prectice set
ques 1 : create a class  programmer for storing data of few programmer working on ms.
class Programmer:
  def __init__(self, name, product):
    self.name = name
    self.product = product
  def getInfo(self):
    print(f"programmer's details:\n name : {self.name} , product : {self.product}")

ram = Programmer("ram", "skype")
sita = Programmer("sita","git")
ram.getInfo()
sita.getInfo()

ques 2: write a class calculator capable of finding square, cube and squareroot of a number.
class Calculator:
  def __init__(self,num):
    self.number = num
  def square(self):
    print(f"the square of {self.number} is :{self.number **2} ")
  def cube(self):
    print(f"the cube of {self.number} is :{self.number**3} ")
  def squareRoot(self):
    print(f"the square-root of {self.number} is :{self.number**.5} ")

a = Calculator(9)
a.square()
a.cube()
a.squareRoot()

ques 3: create a class with aclass attribute a ,create an object from it and set directly using object a = 0, does this change class attribute?
class Sample:
  a = 10

ob = Sample()
ob.a = 20
print(Sample.a)
print(ob.a)   # ans: no it'll not change, coz object create instance of class attribute for self.

ques 4: add a static method in ques 2 to greet the user with hello [ques 2: write a class calculator capable of finding square, cube and squareroot of a number.]
class Cal:
  def __init__(self,num):
    self.number = num
  def square(self):
    print(f"square of {self.number} is {self.number**2}")
  @staticmethod
  def greet():
    print("thanks for using it.....")
ob = Cal(3)
ob.square()
ob.greet()

ques 5: wriet a class train which has method to book a ticket and eget status(nu of seat) and get fare information of train running under indian railways.
class Train:
  def __init__(self, name, fare, seats):
    self.name = name
    self.seats = seats
    self.fare = fare
  def info(self):
    print(f"train name:{self.name}\n ticket fare: {self.fare} \n total seat:{self.seats}")

enterCity = Train("XYZ-express", 90, 300)
enterCity.info()

just for fun
class Train:
  def __init__(self, name, fare, seats):
    self.name = name
    self.seats = seats
    self.fare = fare
  def status(self):
    print(f"train name:{self.name}\n ticket fare: {self.fare} \n total seat:{self.seats}")
  def bookTicket(self):
    if(self.seats>0):
      print(f"ticket booked!! your sit no. is {self.seats}")
      self.seats = self.seats-1
    else:
      print("sorry all ticket are already booked!!!")

enterCity = Train("XYZ-express", 10, 3)
enterCity.status()
enterCity.bookTicket()
enterCity.bookTicket()
enterCity.bookTicket()
enterCity.bookTicket()
enterCity.status()

ques 6 : can you change self parameter inside a class to something else (say 'sir'),try changing self to "slf","harry" and see the efect

class Sample:
  def __init__(slf,name):   #you can use any key in the place of self
    slf.name = name
ob = Sample("harry")
print(ob.name)

INHERITANCE: creating a new class to use old class with adding new features

example
class Employee:
  company = "Google"
  def showDetails(self):
    print(f"this is an employee..")

class Programmer(Employee):
  language = 'python'
  def getlanguage(self):
    print(f"language is {self.language}")
e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
print(e.company)
print(p.company)
# e.getlanguage() #AttributeError: 'Employee' object has no attribute 'getlanguage'
p.getlanguage()

example
class Employee:
  company = "Google"
  def showDetails(self):
    print(f"this is an employee..")

class Programmer(Employee):
  language = 'python'
  company = 'Yahoo!'          #overriding
  def getlanguage(self):
    print(f"language is {self.language}")
  def showDetails(self):
    print("i am programmer...")   #overriding
e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
print(e.company)
print(p.company)
# e.getlanguage() #AttributeError: 'Employee' object has no attribute 'getlanguage'
p.getlanguage()

type: 1.single 2.multiple 3. multilevel
1. single inheritance
class Employee:
  company = 'google'
  def showDetails(self):
    print("i am an employee..")
class Programmer(Employee):
  company = 'google'
  def showDetails(self):
    print("i am an programmer..")
e = Employee()
p = Programmer()
print(e.company)
print(p.company)
e.showDetails()
p.showDetails()

2. mutiple inheritance : multiple parent class with single child class
class Employee:
  company = 'visa'
  ecode = 120
class FreeLancer:
  company = 'fiver'
  level = 0
  def upgradeLevel(self):
    self.level = self.level+1

class Programmer(Employee,FreeLancer):
  name = "rohit"
p = Programmer()
print(p.level)
print(p.ecode)
print(p.company)      # output: visa (coz of args)
p.upgradeLevel()
print(p.level)

2. mutilevel inheritance :when child become parent for another class {class1-->class2-->class3-->class4}
class Person:
  country = 'india'
  def takeBreath(self):
    print("i am breathing")

class Employee(Person):
  company = 'google'
  def getSalary(self):
    print(f"salary is {self.salary}")
  def takeBreath(self):
    print("i am luckily beathing...")

class Programmer(Employee):
  company = 'fiverr'
  def getSalary(self):
    print("no salary for programmer")
  def takeBreath(self):
      print("i am programmer so i am luckily beathing ++++++")
p = Person()
e = Employee()
pr = Programmer()

# p.takeBreath()   #i am breathing
# e.takeBreath()   #i am luckily beathing...
# pr.takeBreath()  #i am luckily beathing...

# #print(p.company)  #throw error
# print(e.company)  #google
# print(pr.company) #fiverr

print(p.country)  # output: india
print(p.country)  # output: india
print(p.country)  # output: india

SUPER(): it is a method to access the method of super class to derived class

super() with constructor
class Person:
  country = 'india'
  def takeBreath(self):
    print("i am breathing")

class Employee(Person):
  company = 'google'
  def getSalary(self):
    print(f"salary is {self.salary}")
  def takeBreath(self):
    super().takeBreath()
    print("i am luckily beathing...")

class Programmer(Employee):
  company = 'fiverr'
  def getSalary(self):
    print("no salary for programmer")
  def takeBreath(self):
    super().takeBreath()
    print("i am programmer so i am luckily beathing ++++++")
p = Person()
e = Employee()
pr = Programmer()

p.takeBreath()   #i am breathing
e.takeBreath()   #i am breathing i am luckily beathing...
pr.takeBreath()  #i am breathing i am luckily beathing... i am luckily beathing...

super() with constructor

class Person:
  def __init__(self):
    print("initializing person")
  country = 'india'
  def takeBreath(self):
    print("i am breathing")

class Employee(Person):
  def __init__(self):
    super().__init__()
    print("initializing employee")
  company = 'google'
  def getSalary(self):
    print(f"salary is {self.salary}")
  def takeBreath(self):
    super().takeBreath()
    print("i am luckily beathing...")

class Programmer(Employee):
  def __init__(self):
    super().__init__()
    print("initializing programmer")
  company = 'fiverr'
  def getSalary(self):
    print("no salary for programmer")
  def takeBreath(self):
    super().takeBreath()
    print("i am programmer so i am luckily beathing ++++++")

pr = Programmer()
output: initializing person initializing employee initializing programmer

class (): it is a method which is bound to the class and not the object of class
'@classmethod' --> decorator used to create class method

class Employee:
  company = 'camel'
  salary = 100
  location = 'delhi'
  # # way 1
  # def changeSalary(self,sal):
  #   self.__class__.salary = sal
  # # way 2
  @classmethod
  def changeSalary(cls,sal):     #alternative
    cls.salary = sal

e = Employee()
print(e.salary)   #100
print(Employee.salary)    #100
e.changeSalary(150)
print(e.salary)     #150
print(Employee.salary)     #150


decorator: getter & setter method

getter and setter: getter is also called property decorator and in setter method getter method name with setter property. when we want to set any property and change auto like function so we use getter mthod/decorator, it is a function but work like a class property and get value as property, and we use setter method to set value of property related to getter method
getter syntax:
@property
def name(self):
  ......pass

setter syntax:
@name.setter
def name(self,value):
  self.... pass

example:
class Employee:
  company = 'Indian Way'
  salary = 5000
  salarybonus = 500
  # totalSalary = 5500
  # @property     #getter or property decorator: to get value as property
  def totalSalary(self):
    return self.salary + self.salarybonus

  @totalSalary.setter    #setter method: to set value of getter method
  def totalSalary(self,value):
    self.salarybonus = value - self.salary

e = Employee()

print(e.salary)
print(e.salarybonus)
print(e.totalSalary)

e.totalSalary = 5800

print(e.salary)
print(e.salarybonus)
print(e.totalSalary)

perator overloading: operator in python can be overloaded usinf dunder method,these method are called when a given operator is on used on the object
syntax: 
def __methodName__(...):
    ....pass

example:
class Number:
  def __init__(self,num):
    self.num = num

  def __add__(self,num2):
    print("let's add")
    return self.num + num2.num

n1 = Number(3)
n2 = Number(5)
sum = n1 + n2
print(sum)

prectice with all dunder method under operator  overloading:
class Number:
  def __init__(self,num):
    self.num = num
  def __add__(self,num2):
    print("let's get add. : ")
    return self.num + num2.num
  def __sub__(self,num2):
    print("let's get sub. : ")
    return self.num - num2.num
  def __mul__(self,num2):
    print("let's get mul. : ")
    return self.num * num2.num
  def __truediv__(self,num2):
    print("let's get div : ")
    return self.num / num2.num
  def __floordiv__(self,num2):
    print("let's get floor : ")
    return self.num // num2.num

n1 = Number(13)  # it'll be args in dundle/constructor method
n2 = Number(5)   #it'll be args in dundle method
sum = n1 + n2
print("sum: ",sum)
sub = n1 - n2
print("sub: ",sub)
mul = n1 * n2
print("mul: ",mul)
div = n1 / n2
print("div: ",div)
floor = n1 // n2
print("floor:",floor)

prectice other important duddle method or you can go for python documentation for operator overloading
class Number:
  def __init__(self,num):
    self.num = num

  def __str__(self):
    return f"decimal number {self.num}"
  def __len__(self):
    return 1

n = Number(9)
print(n)
print(len(n))

prectice set
ques 1: create a class c-2dvector and use it to create another class representing a 3-d vector
class C2dvec:
  def __init__(self,i,j):
    self.icap = i
    self.jcap = j
  def __str__(self):
    return f"{self.icap}i + {self.jcap}j"
class C3dvec(C2dvec):
  def __init__(self, i, j, k):
    super().__init__(i, j)
    self.kcap = k
  def __str__(self):
    return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
v2d = C2dvec(1,3)
v3d = C3dvec(1,3,5)
print(v2d)
print(v3d)

ques 2: create a class pets from a class animals and further create class dog from pet, add a method bark to class dog
class Animals:
  animalType = "memmal"
class Pets(Animals):
  color = 'white'
class Dog(Pets):
  @staticmethod
  def bark():
    print("dog barks...")
d = Dog()
d.bark()

ques 3: create a class employee and add salary increment properties of it: write a method salary after increment method with a '@property' decorator with a setter method which changes the the value of increament based on salary.
class Employee:
  salary = 1000
  increment = 1.5
  @property
  def salaryAfterIncrement(self):
    return self.salary * self.increment
  @salaryAfterIncrement.setter
  def salaryAfterIncrement(self, salAfterInc):
    self.increment = salAfterInc/self.salary
e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 2000
print(e.salary)
print(e.increment)
print(e.salaryAfterIncrement)

ques 4: write a class comples to represent complex number along with overloaded operator + and * operators which calculates the sum and dot product of them.
formula: (a+bi)(c+di)=(ac-bd)+(ad+bc)i
class Complex:
  def __init__(self,r,i):
    self.real = r
    self.imaginary = i
  def __add__(self,c):
    return Complex(self.real + c.real , self.imaginary + c.imaginary)
  def __mul__(self,c):
    finalReal = (self.real*c.real - self.imaginary*c.imaginary)
    finalImag = (self.real*c.imaginary + self.imaginary*c.real)
    return f"{finalReal} + {finalImag}i"
  def __str__(self):
    return f"{self.real} + {self.imaginary}i"
c1 = Complex(3,2)
c2 = Complex(1,7)
print(c1 + c2)
print(c1 * c2)

ques 5: write a class vector to represent vector of  n diamention overload operator + and * operators which calculates the sum and dot product of them.
class Vector:
  def __init__(self,vec):
    self.vec = vec
  def __str__(self):
    str1 = ""
    index = 0
    for i in self.vec:
      str1 += f" {i}a{index} +"
      index += 1
    return str1[:-1]
  def __add__(self,vec2):
    newList = []
    for i in range(len(self.vec)):
      newList.append(self.vec[i]+vec2.vec[i])
    return Vector(newList)
  def __mul__(self,vec2):
    sum = 0
    for i in range(len(self.vec)):
      sum += self.vec[i] * vec2.vec[i]
    return sum

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print("vector of [1, 3, 5] is",v1)
print("vector of [2, 4, 6] is",v2)
print(v1+v2)
print(v1*v2)

ques 6: write __str__()method to print the vector as following 7i +8j+10k
class Vector:
  def __init__(self,vec):
    self.vec = vec
  def __str__(self):
    return f" {self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
v = Vector([7,2,3])
print(v)

ques 7: over ride the __len__() method on vector of problem no.5 [ques 5: write a class vector to represent vector of  n diamention overload operator + and * operators which calculates the sum and dot product of them.]
class Vector:
  def __init__(self,vec):
    self.vec = vec
  def __len__(self):
    return len(self.vec)
v1 = Vector([2,3,4])
v2 = Vector([2,3,4,5])
print(len(v1))
print(len(v2))

OOP end in python




























oop completed