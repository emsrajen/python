# exception handling:

# try: there are many build-in exception which are reised in python when something goes wrong exception in python can be handled using a 'try' statement.the code that handled exception is written in except clause.
# syntax
# try:
#   pass
# except Exception as e:
#   print(e)

# example
# while(True):
#   print("press 'q' to exit:")
#   a = input("enter any number:")
#   if a == 'q':
#     break
#   try:
#     print("trying...")
#     a = int(a)
#     if a>6:
#       print("entered number is greater than six")
#   except Exception as e:
#     print(f" your input throwing an error that is : {e}")
# print("thank you...!!")

# when exception is handled,the code flow contain without python interruption. handling code write in try() and showing error in except()

# let's see errors:
# print(1/0)    #xerodivision error
# a = int(str); print(a) #type error
# b = int('23av45'); print(a) #type error

# # syntax:
# try:
#   pass # code
# except SyntaxError:
#   pass # code
# except ZeroDivisionError:
#   pass # code
# except TypeError:
#   pass # code
# except:
#   pass # code if any else error detect


# # example:
# try:
#   a = int(input("enter a number : "))
#   c = 1/a
#   print(f"1/{a} is : ",c)
# except Exception as e:
#   print("Exception occured..")
#   print("ERROR :"+e)

# print("thanks for using this code...")

# example: whith different exception
# try:
#   a = int(input("enter a number : "))
#   c = 1/a
#   print(f"1/{a} is : ",c)
# except SyntaxError as e:
#   print("Exception 1 occured..")
#   print("ERROR :",e)
# except ZeroDivisionError as e:
#   print("Exception 2 occured.. dont divide by zero")
#   print("ERROR :",e)
# except ValueError as e:
#   print("Exception 3 occured... enter excepted value")
#   print("ERROR :",e)

# print("thanks for using this code...")


# raised exception: own exception msg using 'raise' keyword and except only use once.
# def increment(num):
#   try:
#     return int(num) + 1
#   except:
#     raise ValueError("enter valid value or this is not good...")
# a = increment(12)
# a = increment("x")
# print(a)


# try with else claus: else will run when code execute successfully bur error occired than else will not execute.

# # syntax:
# try:
#   pass # code
# except:
#   pass # code
# else:
#   pass # code

# example:
# try:  #if code exe normal
#   i = int(input("enter number :"))
#   c = 1/i
#   print(c)
# except Exception as e:  # error occured
#   print(e)
# else:
#   print("we are successful")  #run with try but with except, else not run

# try with finally: try will work same but finally always run in the end as welcome massage if error occure or not.
# example:
# try:  #if code execute without error
#   i = int(input("enter number :"))
#   c = 1/i
#   print(c)
# except Exception as e:  # error occured
#   print("exception occure: ",e)
# finally:
#   print("we are done")  # always execute in the end and also execute if you use exit() in try or except block

# example:
# try:  #if code execute without error
#   i = int(input("enter number :"))
#   c = 1/i
#   print(c)
# except Exception as e:  # error occured
#   print("exception occure: ",e)
#   exit()   // finally block execute after exit the code
# finally:
#   print("we are done")  # always execute in the end and also execute if you use exit() in try or except block

# if __name__=='__main__' (u can write it with type main keyword in vs code) it eveluate to the name of the module
# __name__ evaluates to the name of the module in python from where code is run,if the module is being run directly from cmd-line,the __name__ is to set to string "__main__",thus this beheviour is used to check whether the module is run directly or import to another file

# create file file_1.py  #python dont allow to import to file as module if its not start with charactor
# def greet(name)
#  #print(__nmae__) it print file name,if you print via curent file or use it as module
# if __name__ == '__main__':
#   n = input("enter name : \n")
#   greet(n)
# #create another file as file2 and use file1 as module
# import flie_1
# flie_1.greet("raj") #good morning !!! raj
# using file1 as module


# global: this keyword is use to modify the variable outside of current scope
# example:
# a = 54  #global variable
# def fun1():
#     global a
#     print(f"statement 1: {a}")
#     a = 7 #local variable if global keyword is not used
#     print(f"statement 2: {a}")
# fun1()
# print(a)
# print(f"statement 3: {a}")
# global keyword change the scope of local to globle of any variable

# enumerate: this function add counter to an iterable and return it,
# l1 = [23, 34, 32.2, 'raj', False,22]
# for index, item in enumerate(l1): # always write indext them item/element
#   print(index,item)

# without it
# l1 = [23, 34, 32.2, 'raj', False,22]
# index = 0
# for index, item in l1:
#   print(index,item)
#   index += 1

# list_comprehension: it is an elegent way to create a list based on existing list
# example:
# a = [3,5,7,8,10,5,9,2,4,23,75,23,67]
# b = [i for i in a if i%2==0] #shortcut to write the same
# print(b)

# in simple way: without list_comprehension
# a = [3,5,7,8,5,9,2,4,23,75,23,67]
# b = []
# for item in a:
#   if item%2==0:
#     b.append(item)
# print(b)

# example 2:
# list1 =[1, 7, 12, 11, 22]
# list2 =[item for item in list1 if item>8]
# print(list2) #12,11,22

# for set/dictionary
# t = [1, 4, 2, 4, 1, 2, 3]
# s = {i for i in t}
# print(s)  #{1, 2, 3, 4}


# prectice set
# ques 1: write a program to open 3 files file1.txt, file2.txt,file3.txt if any of these files are not present, a msg without exiting the program must be printed promopting the same?

# first create files with following text, file1.txt: this is file1.txt, file2.txt: this is file2.txt, file3.txt: this is file3.txt

# def readFile(filename):
#   try:
#     with open(filename,'r')as f:
#       data = f.read()
#       print(data)
#   except FileNotFoundError:
#     print(f"file '{filename}' is not found")

# readFile('file1.txt')
# readFile('file2.txt')
# readFile('file4.txt')
# readFile('file3.txt')
# output: this is file1.txt this is file2.txt file 'file4.txt' is not found  this is file3.txt

# ques 2: wap to print 3rd, 5th, 7th element from a list using enumerate function

# l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# for index, item in enumerate(l):
#   if index==2 or index==4 or index==6:
#     print(index,item)


# ques 3: write a list comprehension to print which contain the multiplication table of user enter number.
# num = int(input("enter a number: "))
# table = [ num*i for i in range(1,11)]
# print(table)

# ques 4: write a program to display a/b, where and a,b both are integer if b = 0 than display infinite by handline ZeroDivisionError
# a = int(input("enter a:"))
# b = int(input("enter b:"))
# print("answer:")
# try:
#   print(a/b)
# except ZeroDivisionError:
#   print("Infinite")

# ques 5: store the multiplication table generated in ques.3 in a file names table.txt[ques 3: write a list comprehension to print which contain the multiplication table of user enter number]

# num = int(input("enter number"))
# table = [num*i for i in range(1,11)]
# print(table)
# with open("table.txt",'a') as f:
#   f.write(str(table))
#     f.write("\n")

# virtual environment: environment which is same as the system interpretor butis isolated from the other pythonenvironment on system
# cmd: pip install virtualenv [to create virtual environment]
# virtualenv project_name [virtualenv myproject] it'll create a new project in your folder
# for guidance you can visit 'digitalocean' after searching 'digitalocean django' just for learning [ https://docs.digitalocean.com/tutorials/app-deploy-django-app/ ]
# to activate in terminal [linux/mac -- source myproject/bin/activate][windows-- myproject/script/activate..ps1] if u type click 'tab' after type 1st char than click tab so it'll auto-complete
# after run if you'll get virtualenv wont activate on windows tham you can visit[ https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows ]
# now if you'll install flask or pandas than it'll installed in your specific project
# to deactivate or come back to system environment then type 'deactivate' in terminal

# demo code
# import flask   #flask 0.5.2
# import pandas as pd
# import pygame  #pip install pygame

# after creating it is to activate it, we can now use this v.e. as a separate python installation, to delete it, just delete your project..that's it
# **************************************************************
# pip freeze cmd : this cmd return list of all installed modules insystem or created virtual environmant [>>>pip freeze]
# copy from terminal and paste it in your file(mannually)
# (by cmd): pip freeze > file_name.txt [i.e. >>>> pip freeze > module.txt] it'll create your file 'module.txt' with all list
#  to distribute the file to the to create the same environment using [>>>pip install -r file_name.txt i.e.: >>>pip install -r module.txt ] just like '>>>npm install' and import all modules and virtual environment,filename should be same as the filename you create to store module than it'll install all package and models

# ************************************************
# lambda function: this function create using 'lanbda' keyword
# A lambda function is a small anonymous function. it takes any number of arguments, but can only have one expression, syntax => lambda args : expression
# why we use: if you wwant to create any function with one expression or need to return function as so you can use it that time and also can use it anywhere
# example
# a = lambda num : num +1; print(a(5))
# square = lambda x : x*x
# sum = lambda x, y, z : x+y+z
# x = 3
# y = 2
# print(square(x))        #9
# print(sum(x,y,1))       #6


# join method:[ var name = "separator".join(list name or iterable object)]
# to create a sting with any separator from iterable object(i.e. list, dictionary,tuple,etc.)

# list = ['camera', 'laptop', 'phone', 'ipad', 'hard disk', 'nivida graphics card']
# sentence = " and ".join(list)
# print(sentence)     #camera and laptop and phone and ipad and hard disk and nivida graphics card
# sentence1 = " -- ".join(list)
# print(sentence1)     #camera -- laptop -- phone -- ipad -- hard disk -- nivida graphics card
# sentence2 = " \n ".join(list)
# print(sentence2)     #camera laptop phone ipad hard disk nivida graphics card (each element in new line)


# format method:formats the values inside the string into a desire output [ tamplate.format(args1,args2,...args)]
# in old ver of python there is no option for f{string} so that time we use formate method, it's old method so some feature not available in f{string} but exist in format method
# example:
# name = "python"
# #with f-string
# a = f"{name} is simple pro. lang." using f-string
# print(a)    #python is simple pro. lang.
# #with format method
# b = "{} is a simple pro. lang.".format(name)
# print(b)  #python is simple pro. lang.

# name1 = "ram"
# name2 = "syam"
# rel = "friends"
# a = "{} and {} are friends".format(name1,name2); print(a)    #ram and syam are friends
# a = "{1} and {0} are {2}".format(name1,name2,rel); print(a)    #syam and ram are friends [with using index]   ....see output carefully,you can exchange value by index


# map(), filter(), reduce():you also can use annonyoums function in the place of simple function

# 1. map() : map(function,input iteraable object)
# it applies a function to all items in an input list
# "map(square,L1)" return a object so you can also store it after convert in list or iterable object like this:"list(map(square,L1))"
# def square(num):
#     return num*num

# L1 = [1, 2, 4]
# way 1
# L2 = []
# for item in L1:
#     L2.append(square(item))
# print(L2)       #[1, 4, 16]
# way2
# print(list(map(square,L1)))       #[1, 4, 16]


# 2. filter(): list(filter(function,input iteraable object))
# filter create a list of items for which the function return true
# def g_fiv(num):
#     if num>5:
#         return True
#     else:
#         return False

# L = [2, 4, 7, 8 ,10, 0]
# print(list(filter(g_fiv,L)))        #[7, 8, 10]

# just for fun using annonyoums function
# m = list(filter(lambda num:(num>5),L)) ;print(m)  #[7,8,10]
# print(list(filter(lambda num:(num>5),[1,2,3,4,5,6,7,8,9])))  #[6,7,8,9]

# 3. reduce(): reduce(function,input iteraable object))
# you have to import 'reduce()' from functools using "from functools import reduce" statement
# reduce applies a rolling computation to sequential pair of elemets

# example:
# from functools import reduce
# L = [ 1, 2, 3, 4 ]
# sum = lambda a,b: a+b      # return 1+2+3+4
# val = reduce(sum,L)
# print(val)    #output: 10

# prectice set:
# ques 1: create 2 virtual environments install some pkg in 1st and using it create same environment in 2nd
# in terminal to  create : virtualenv project_name, to activate it: go to the path until activate.ps1, deactivate: type deactivate (it'll close current env)
# install using pip:pip install pandas flask numpy matplotlib,,,than wait
#  to store file : pip freeze > env1module.txt
# open another env:  .\myenv2\Scripts\activate.ps1
# to import all module as env1: pip install -r env1module.txt
# now you can deactivate it

# ques 2: WAP to input name, marks, phone number of student and formate it using format(), like this -> the name of student is 'abc' and marks is 72 and his contact number is 9100000012
# name = input("enter name : ")
# marks = int(input("enter marks : "))
# phone_number = input("enter contact number : ")
# template = 'the name of student is {} and marks is {} and his contact number is {}'
# result = template.format(name,marks,phone_number)
# print(result)

# ques 3: a list contains multiplication table of 7. WAP to convert it to a vertical string of same number.
# l = [i*7 for i in range(1,11)]     # TypeError: sequence item 0: expected str instance, int found
# l = [str(i*7) for i in range(1,11)]
# print(l)
# vertical_name = "\n".join(l) #join work with string
# print(vertical_name)


# ques 4: WAP to filter a list of number which are divisible by 5.
# l = [1, 4, 5, 2, 5, 7, 9, 0, 12, 15, 10, 60, 20, 25, 4, 61, 56, 78, 23, 22,20]
# result = filter(lambda item: item%5==0,l)
# print(list(result))

# ques 5: WAP to find the max num in list using reduce()
# from functools import reduce
# l = [3, 5, 7, 12, 11]
# a = reduce(max,l)       #max() is build-in function
# print(a)

# ques 6: run pip freeze for the system interpretor,take the contents and create a similar virtualenv.

# steps: 1. >>pip install freeze module.txt
# steps: 2. >>pip install virtualenv myprojectenv
# steps: 3. >>.\myprojectenv\scripts\activate.ps1
# steps: 4. >>pip install -r module.txt
# steps: 5. >>pip install freeze module.txt

# ques 7: explore the flask module and create a web server using flask and python
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello_world():
#     return ' Hello, World !'
# if __name__ == "__main__":
#     app.run(debug=True)
# output: show msg ' Hello, World !' on web browser after starting server by flask, you can use html bootstrap to in the place of msg . for more.. visit flask playlist in codewithharry
