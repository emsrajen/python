# ''' source : CWH youtube
# written: rajendra'''

# # import os #this is buiid in module                 #use pip install module name in cmd prompt

# print("welcome to python world.....")

# # this is problem 1
#  print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.''')

# # this is problem 2 use xternal module
# from playsound import playsound
# playsound('E:\\PROJECT_MEDIA\\Aathma Rama Ananda Ramana - Brodha V - No English Only Hindi Version - Spirituality - ॐ_2.mp3')

# use os module
# import os
# print(os.listdir())

# variable
# a = 10
# b = 10.5
# c = 'anc'
# d = "anc"
# e = False
# f = None
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))
# print(d)
# print(type(d))
# print(e)
# print(type(e))
# print(f)
# print(type(f))

# arithmatic operator
# a = 10
# b = 5
# c = a + b
# print("sum :",1+5)
# print("sum :",c)
# print("sum :",a+b)
# print("sub :",a-b)
# print("mul :",a*b)
# print("div :",a/b)

# assignment operator
# a = 12
# a += 2
# print(a)

# comparision operator
# b = (14<3)
# print(b)
# a = (3==3)
# print(a)
# c = (1<3)
# print(c)

# logical operator
# bool1 = True
# bool2 = False
# print("value of bool1 and bool2 is",bool1 and bool2)
# print("value of bool1 or bool2 is",bool1 or bool2)
# print("value of not bool2 is",not bool2)

# type casting
# a = '333'
# print(type(a))
# a = int(a)
# print(type(a))
# print(a + 10)

# input function

# a = input("enter your name: ")
# b = input("enter your address: ")
# print("my name is",a," ","i live in",b)

# c = float(input("enter any Number:"))
# print(c)
# print(type(c))

# add 2 no
# a = float(input("enter 1st number : "))
# b = float(input("enter 2nd number : "))
# sum = a + b
# print("sum:",sum)

# #  just for fum
# a = float(input("enter 1st number : "))
# b = float(input("enter 2nd number : "))
# c = a + b
# sum ="sum of %f and %f is"%(a,b)
# print(sum,c)

# find reminder div by 2
# a = 45
# b = 7
# print("reminder of a/b :",a%b)

# a = 45
# b = 25
# print(a>b)
# print(a<b)

# a = float(input("enter 1st number : "))
# b = float(input("enter 2nd number : "))
# avg = (a+b)/2
# print("average is : ",avg)

# a = input("enter 1st number : ")
# a =  int(a)
# sqr =a*a
# print("square is : ",sqr)

# a = 12
# b = "harry"
# print(a, b)
# print(type(a))
# print(type(b))

# a = "rajendra's learning"
# b = 'raj is a "good" person'
# c = '''"rajendra's" learning'''
# print(a)
# print(b)
# print(c)
# print(len(a))

# greet = "good morning....!!! "
# name = "raj"
# print(greet+name)

# name = input("enter your name:")
# greet = "good morning....!!! "
# massage = greet + name
# print(massage)

# name = "Rajendra Kumar Randa"
# print(name)
# print(type(name))

# print(name[0])
# print(name[3])
# print(name[4]) #not work for out of index
# print(name[:5])
# print(name[:4])
# print(name[0:])
# # print(name[1:3])    #[1:2]
# c = name[-4:-2]         #nagative index
# print(c)
# print(name[-4:-2])

# d = name[1::5]      #ski p indexing value
# d = name[0:6:1]      #string[start_index:end_index:skip_index]
# print(d)


# story = '''In “The Necklace” by Guy de Maupassant, the main character, Mathilde, has always dreamed of being an aristocrat but lives in poverty. Embarrassed about her lack of fine possessions, she borrows a necklace from a wealthy friend but loses it. The story is known for its subversive and influential twist ending.'''  #"A quick brown fox jumps over the lazy dog ."
# print(len(story))
# print(story.endswith("dog"))
# print(story.endswith("."))
# print(story.count("v"))
# print(story.count(" "))
# print(story.count("brown"))
# print(story.find("fox"))
# print(story.find("fox"))
# print(story.count(" "))
# print(story.count("a"))
# print(story.count("aw"))
# print(story.count("f"))
# print(story.capitalize())  #syntax error:print(story.capitalize("find"))
# print(story.find("de"))
# print(story.replace("main", "lead")) #replace all accurances

# escape sequence character \n: new line \t: tab \':'
# story = "this is a ball. \nthis color is blue.\tif we divide 2 in to 2 (2/2) is 1\n and this is harry\'s\tball,\\"
# print(story)

# name = input("enter your name:\n")
# greet = "good afternoon!!! "
# print("good morning!!! ",name)
# print(greet+name)

# letter = '''Dear <|NAME|> ,
#   greeting from company 'ABC'. I'm happy to tell about your selection. you're selected.
#           have a great day!
#             date: <|DATE|>'''
# name=input("enter your name : \n")
# date=input("enter date : \n")
# letter = letter.replace("<|NAME|>",name)
# letter = letter.replace("<|DATE|>",date)
# print("*********gretting**********")
# print(letter)

# str1 = "this is my  ball."
# str2 = "this is my pen."
# str3 = "this  is my  book."
# doubleSpace1 = str1.find("  ")
# doubleSpace2 = str2.find("  ")
# print(doubleSpace1)
# print(doubleSpace2)
# str3 = str3.replace("  "," ")
# print(str3)

# ltr = "dear harry, this python course is nice! thanks!"
# formatted_ltr = "dear harry,\n\t this python course is nice!\n\t\t thanks!"
# print(ltr)
# print(formatted_ltr)

# list tuple
# a = [1,23, 45,56 ,67, 44, 0]
# print("list: ",a)
# print(type(a))

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])  #  out of endex : print(a[7])

# a[6] = 100
# print(a[6])
# print("updated list:",a)

# a1 = [ 101, "python", 10.5 , False]
# print("list: ",a1)
# print(type(a1))
# print(type(a1[0]))
# print(type(a1[1]))
# print(type(a1[2]))
# print(type(a1[3]))

# friends = ["ram","syam","mohan","sohan","meena","sita", 4, 500]
# print(friends)
# print(friends[:4])  #slice with index
# print(friends[-4:])  #slice with index
# friends[-1] = "kajal"
# print(friends)

# num = [1 ,16, 56, 10, 14]
# print(num)
# num.sort()
# print(num)
# num.reverse()
# print(num)
# num.append(12)
# num.append(82)
# print(num)

# num.insert(0, 4.5)      #add 4.5 on index 0
# print(num)

# num.pop(4)      #pop on index 4
# print(num)

# num.remove(1)      #remove 1
# print(num)

# empty_list = []
# print(empty_list)
# print(type(empty_list))

# tuple

# empty_tuple = ()
# print(empty_tuple)
# print(type(empty_tuple))

# tuple_with_single_element = (1)           #wrong way
# print(tuple_with_single_element)
# print(type(tuple_with_single_element))    # this is 'int' type

# tuple_with_single_element = (1,)           #right way
# print(tuple_with_single_element)
# print(type(tuple_with_single_element))    # this is 'tuple' type

# t = (0, 12, 2, 24, 50, 2, 2)    #unable to changable
# print(t)
# print(t[0])
# print(t[4])

# print(t.count(2))
# print(t.index(50))    #return index number ,index() takes value as args

# revision for list and tuple
# ques 1

# f1 = input("enter fruit no 1: ")
# f2 = input("enter fruit no 2: ")
# f3 = input("enter fruit no 3: ")
# f4 = input("enter fruit no 4: ")
# f5 = input("enter fruit no 5: ")
# f6 = input("enter fruit no 6: ")

# myFruitList = [f1, f2, f3, f4, f5, f6]

# print(myFruitList)
# print(type(myFruitList))

# ques 2
# m1 = int(input("enter mark of student no. 1: "))
# m2 = int(input("enter mark of student no. 2: "))
# m3 = int(input("enter mark of student no. 3: "))
# m4 = int(input("enter mark of student no. 4: "))
# m5 = int(input("enter mark of student no. 5: "))
# m6 = int(input("enter mark of student no. 6: "))

# myMarks = [m1, m2, m3, m4, m5, m6]
# print(myMarks)
# myMarks.sort()
# print(myMarks)

# proved that tuple can't change
# t = ( 10, 20 ,30 ,30)
# t[0] = 12
# print(t)

# sum of element
# a = [2,4, 12, 2]
# print("sum via mannual:",a[0]+a[1]+a[2]+a[3])
# print("sum via mathod:",sum(a))

# count 0
# t = (7, 0, 8, 0, 0, 9)
# print(t)
# print(t.count(0))

#  dictionary: or sets time - 03:20:20
#  dictionary: collection of key-value pair

# myDict = {
#   "Red" : "one type of color",
#   "Fast" : "In a Quick Manner",
#   "Harry" : "A Programmer",
#   "Marks" :[1, 2, 5],
#   "anotherDict" : {'harry' : 'player' },
#   "anotherList" : [10.20, 30, 10],
#   "anotherTuple" : (10, 0 ,20 ,30 ,0 ,45),
#   'dictionaryDef' : "Dictionary is mutable, indexed, unordered & hold non-duplicate-key",
# }
# print(myDict)
# print(type(myDict))

# print(myDict['Red'])
# print(myDict['Fast'])
# print(myDict['Harry'])
# print(myDict['Marks'])
# print(myDict['anotherDict'])
# print(myDict['anotherDict']['harry'])
# print(myDict['anotherList'])
# print(myDict['anotherList'][0])
# print(myDict['anotherTuple'])
# print(myDict['anotherTuple'][0])
# print(myDict['dictionaryDef'])

# myDict['Marks'] = [10, 20, 50]
# print(myDict['Marks'])

# newDict = {
#   "Fast" : "In a Quick Manner",
#   "Harry" : "A Programmer",
#   "Marks" :[1, 2, 5],
#   "anotherDict" : {'harry' : 'player' },
#   1 : 2,
# }

# print(newDict)
# print(type(newDict))

# print(newDict.keys())
# print(type(newDict.keys() ))

# print(newDict.values())
# print(type(newDict.values() ))

# print(list(newDict.keys()))       #type casting dict to list
# print(type(list(newDict.keys())))

# # dictionary mathod
# print(newDict)
# print(newDict.keys())
# print(newDict.values())
# print(newDict.items())  #print all key-value pair
# print(newDict)
# updateDict = {
#   "raj" : "a friend",
#   "sword" : "a weapan",
#   "harry" : "a coder",    #update value if you want to update
# }
# newDict.update(updateDict) #add new key-value pair from updateDict into newDict
# print(newDict.items())

# print(newDict.get("harry"))     #print value of key
# print(newDict["harry"])     #print value of key

#  # difference: we use get mathod in the place of using [] mathod b'coz if that pair would not exist in our dictionary than get() will return 'none' but [] will throw error
# print(newDict.get("harry2"))    #output : None
# print(newDict["harry2"])        #output : error(keyError)

# emptyDict = {}
# print(emptyDict)
# print(type(emptyDict))

# sets : collection of non-repeatative items, non-changable, unordered,unindexed

# mySet = {1, 3, 5, 8, 9, 1}
# print(mySet)
# print(type(mySet))

# emptyDict = {}          # it'll create empty dictionary not empty set
# print(type(emptyDict))

# b = set()                    # syntax to create empty sets
# print(b)
# print(type(b))

# b.add(10)
# b.add(30)         # .add mathod take only one values as args
# print(b)

#   # mathod of sets

# b = set()   #it is non changable data type but you can add or re,ove items in it.

# b.add(3)
# b.add(4)
# b.add(3)
# b.add(7)
# b.add(9)
# b.add([1,3,5])      #TypeError: unhashable type: 'list' ,we can't add list in it coz its changable,

# b.add((7,8,9))      # add a tuple coz it is also immutable/non-changable
# b.add({1:2, 2:4})           ##TypeError: unhashable type: 'dict' coz its mutable

# print(b)
# b.remove(9)
# b.remove(100)     #throw error if you try to remove the element what doesn't exist in set

# print(b)

# s = {1, 8, 2, 3}
# print(len(s))
# print(s)

# print(s.pop())    # its pop/ remove a item randomly
# print(s)

# print(s.clear())  # it makes your set empty

# s1 = {2,4,6,8,10,11}
# s2 = {1,3,5,7,9,10,11}

# print("intersection in s1 and s2",s1.intersection(s2))
# print("union in s1 and s2",s1.union(s2))

# ques: make dict with eng word as key with their hin value pair and add some pair after it

# myDict = {
#   "fan" :"पंखा",
#   "box" : "डिब्बा",
#   "item":"वस्तु",
# }

# print(myDict.keys())
# a = input("enter word to see hindi meaning:\n")
# print("hindi meaning of your word is:",myDict.get(a))
# #  we use .get mathod coz if user will enter non-define key than user will get none inn the place of any kind of error

#  create a program who take 8 num from user that'll be unique

# num1 = int(input("enter number 1:\n"))
# num2 = int(input("enter number 2:\n"))
# num3 = int(input("enter number 3:\n"))
# num4 = int(input("enter number 4:\n"))
# num5 = int(input("enter number 5:\n"))
# num6 = int(input("enter number 6:\n"))
# num7 = int(input("enter number 7:\n"))
# num8 = int(input("enter number 8:\n"))

# mySet = {num1 ,num2, num3, num4, num5, num6, num7, num8}
# print("set of numbers entered by you is : ",mySet)

# ques: can we have a set with 18 int and 18 str as a values in it

# mixValueSet = {18,'18'}
# mixValueSet = {18,'18',18.0}
# print(mixValueSet)

# ques: check len of set

# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s))

# ques:findout type of s={}
# s = {}
# print(type(s))

# create empty dict and allow your 4 friend to enter their fav_lang and use keys as their names, assume name will be unique

# myNewDict = {}

# a = input("enter your favourite language ram:\n")
# b = input("enter your favourite language sita:\n")
# c = input("enter your favourite language geeta:\n")
# d = input("enter your favourite language meena:\n")
# e = input("enter your favourite language sohan:\n")

# myNewDict['ram'] = a
# myNewDict['sita'] = b
# myNewDict['geeta'] = c
# myNewDict['meena'] = d
# myNewDict['sohan'] = e

# print("so here is a new dictionary as their fav languages: ",myNewDict)
# print("so here is a new dictionary as their fav languages: ",myNewDict.items()) #to show it better

# if two keys wpuld be same than key will hold new updated value and if values are same it doesn't matter

# ques: can you change the value inside a list which is contained in sets like that s = {8, 7, 12, [1, 2]}
# ans: no, coz set is immutable so list can never containned in set and another thing if it'll be tuple than you can't change coz it's non-changable means hashable
# Indentation: the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.
# conditional expression
# it's work ladder if 1st will true than it'll never go for next
# if, elif and else also optional and work anywhere
# if-elif-else ladder
# a = 10
# if(a<3):
#   print("value of a is greater than 3")
# elif(a>13):
#   print("value of a is greater than 13")
# elif(a>7):
#   print("value of a is greater than 7")
# elif(a>17):
#   print("value of a is greater than 17")
# elif(a>7):
#   print("value of a is greater than 7")
# else:
#   print("value of a is not greater than 3 or 7")
# print("DONE...!!!")
# output: value of a is greater than 7   DONE...!!!

# example

# a = 18
# if(a<3):
#   print("value of a is greater than 3")

# if(a>13):
#   print("value of a is greater than 13")

# if(a>17):
#   print("value of a is greater than 17")

# if(a>7):
#   print("value of a is greater than 7")
# else:
#   print("value of a is not greater than 3 or 7")
# print("DONE...!!!")
# value of a is greater than 13 value of a is greater than 17 value of a is greater than 7 DONE...!!!

# example
# a = 22
# if(a>9):
#   print("greater")
# else:
#   print("lesser")
# # output:greater

# example
# age = int(input("enter age:\n"))
# if age>18:
#     print("yes")
# else:
#   print("no")


# example
# age = int(input("enter your age:"))

# if(age>34 and age<55):
#   print("you're ",age,",you can work....")
# else:
#   print("you're ",age,",you can't work...")

# 'in' and 'is'
# a = None

# if(a is None):
#   print("yes....")
# else:
#   print("no.....")


# a = [ 3, 4, 65, 7, 8 ]
# if(45 in a):
#   print("yes....")
# else:
#   print("no.....")

# a = 12
# if(a==7):
#   print("yes")
# elif(a>56):
#   print("yes or no")   //no output


# a = 12
# if(a==7):
#   print("yes")
# elif(a>56):
#   print("yes or no")
# else:
#   print("I'm optional")

# find grester no in user define 4 no
# num1 = int(input("enter no 1 :\n "))
# num2 = int(input("enter no 2 :\n "))
# num3 = int(input("enter no 3 :\n "))
# num4 = int(input("enter no 4 :\n "))

# if(num1>num2 and num1>num3 and num1>num4):
#   print("num 1 is greater")
# elif(num2>num1 and num2>num3 and num2>num4):
#   print("num 2 is greater")
# elif(num3>num2 and num3>num2 and num3>num4):
#   print("num 3 is greater")
# else:
#   print("num 4 is greater")

# enter 3 sub and find pass or fail
# sub1 = int(input("enter marks of sub 1 :\n "))
# sub2 = int(input("enter marks of sub 2 :\n "))
# sub3 = int(input("enter marks of sub 3 :\n "))

# total = (sub1+sub2+sub3)
# grand_total = (total*100)/3
# per = float(grand_total)

# print("percentage:",per)

# if(per>85):
#   print("grade 'A' ")
# elif(per>65):
#   print("grade 'B' ")
# elif(per>45):
#   print("grade 'C' ")
# elif(per>33):
#   print("grade 'D' ")
# else:
#   print("failed")


# quiz: a spam comment is defined as a text containing keywords[make a lot of money,buy now,suscribe this,click this,]WAP to detect it.

# way 1
# text = input("enter your text:\n")
# spam = False

# if("make a lot of money"):
#   spam = True
# elif("buy now"):
#   spam = True
# elif("suscribe this"):
#   spam = True
# elif("click this"):
#   spam = True
# else:
#   spam = False

# if(spam):
#   print("your comment is spam..")
# else:
#   print("your comment is not spam..")

# way 2
# print("make a lot of money,buy now,suscribe this,click this")
# comment = input("to check your comment spam or not\nenter your comment :\n")

# if("make a lot of money" in comment or "buy now" in comment or "suscribe this" in comment or "click this" in comment):
#   print("your comment is spam..")
# else:
#   print("your comment is not spam..")


# WAP given username hold 10char or not
# username = input("enter username: ")
# char = len(username)
# if(char<10):
#   print("valid")
# else:
#   print("invalid")

# WAP to check ,whether name in list or not
# collection = ["raj","mohan","sohan","sita","gita"]
# name = input("enter name to check whether name in list or not:\n")
# if name in collection:
#   print("name found.....!!!")
# else:
#   print("name not found.....!!!")

# wap to findout any string/name is exixt in post or not

# loop in python : for , while
# loop: repeatation of block of statement
# i=0
# while i<10:
#   print("yes")
# infinite loop

# i = 0
# while i<10:
#   print("yes"+str(i))
#   i = i + 1
# print("Done....!!!")

# print 1 tp 50
# i = 1
# print("print-> 1-50:")
# while i<=50:
#   print(i)
#   i = i + 1

# example
# i = 0
# while i<5:
#   print("harry")
#   i = i + 1   # print harry -5 times

# containt using while loop
# fruits = ['banana', 'watermalon','grapes','mango']
# i = 0
# while i<len(fruits):
#   print(fruits[i])
#   i = i + 1


# for loop: used to iterate through a sequesnce like list, tuple,string[iterables] (is,in,range)
# example:
# l = [1, 7, 8]
# for item in l:
#   print(item)

# example:
# fruits = ['banana', 'watermalon','grapes','mango']
# for item in fruits:
#   print(item)

# example: range in for
# range: used to generate sequence of number and it's print until 'range'
# ex.
# print("range(8)")
# for i in range(8):         #range(8) = 0-7
#   print(i)    #output:0 1 2 3 4 5 6 7

# print("range(1, 8)")
# for i in range(1, 8):     #range(1,8) = 1-7
#   print(i)    #output:1 2 3 4 5 6 7

# print("range(2, 8)")
# for i in range(2,8):    #range(2,8) = 2-7
#   print(i)      #output:2 3 4 5 6 7

# print("range(1, 10 with space 2)")
# for i in range(1,10,2):    #range(1,10,2) = 1-10 with spacing 2
#   print(i)    #output: 1 3 5 7 9

# for loop with else
# for i in range(10):
#   print(i)
# else:   #when condition will be false
#   print("this is inside of 'for'")
# 0 1 2 3 4 5 6 7 8 9 this is inside of 'for'
# you also can use else with while also

# break statement
# for i in range(10):
#   print(i)
#   if(i==5):
#     break
# else:
#   print("this is inside of 'for'") #0 1 2 3 4 5
#   else will execute when for loop will exit with condition not exit with break, else will run with suceess termination of for

# for i in range(8):
#   print(i)
#   if(i==5):
#     break
# else:
#   print("this is inside of 'for'")  #0 1 2 3 this is inside of 'for'

# continue statement
# for i in range(10):
#   if i == 5:
#     continue
#   print(i)    #it'll skip 5 b'coz of 5
# when i start to print to print their value than if check their condition all time and condition will be true in 'if' that'll be skip and continue for next values

# pass statement: null statement(stands for do nothing with previous statement)
# i = 4
# if i>3:
#   pass
# while i>6:
#   pass
# def run(player):
#   pass
# print("that's it...")

# pass to use empty function and we can implement it later
# def  dummy(args):
#     pass
# print("usefull to create empty function using 'pass' statement ")

# print multiplication table using loop
# num = int(input("enter number to print table:"))
# i = 1
# # way 1
# for i in range(1,11):
#   print("1. ",i*num)    # 20
# # way 2
# for i in range(1,11):
#   print("2. ", str(num) + " X "+ str(i)+ " = "+ str(i*num)) #2 X 10 = 20
# # way 3
# for i in range(1,11):
#   print("3. ", f"{num}X{i}={num*i}")  #i.e. 2X1=2

# try to study str() deeply later and fstrings too  f"string_char {values,express,calculation}string_char {values,express,calculation}string_char {values,express,calculation}"

# ques: greet everyone whose name start with 's'
# l1 = ["Harry", "Sohan","Sachin","Rahul"]

# for name in l1:
#   if name.startswith("S"):
#     print("hello " + name)

# check no is prime or not
# num = int(input("enter number: "))

# prime = True
# for i in range(2,num):
#   if(num%i == 0 and num!=2):
#     prime = False
#     break

# if prime:
#   print("this number is prime....")
# else:
#   print("this number is not prime....")

# ques: sum of first 5 number using while:
# i = 1
# sum = 0
# print("natural no are:")
# while i<=5:
#   sum = sum + i
#   n = i
#   print(n)
#   i = i+1
# print("sum : ",sum)

# factorial of given number
# num = int(input("enter number: \n"))
# factorial = 1
# for i in range(1, num+1):
#   factorial = factorial * i
# print(f"factorial of {num} is :{factorial}") #enter number:  5 factorial of 5 is :120

# print * pattern triangle
# n = 3
# for i in range(3):
#   print(" " * (n-i-1),end="")
#   print("*" * (2*i+1),end="")
#   print(" " * (n-i-1))

# n = int(input("enter range to print pattern:"))
# for i in range(n):
#   print(" " * (n-i-1),end="")
#   print("*" * (2*i+1),end="")
#   print(" " * (n-i-1))

# print * pattern Right triangle
# i = 4
# for i in range(4):
#   print("*"*(i+1))

# n = int(input("enter range to print pattern:"))
# for i in range(n):
#   print("*"*(i+1))

# to print oposite tringle
# n = int(input("enter range to create pattern:"))
# for i in range(n+1):
#   print(" "*(n-i),"*"*i)



# do prectice set -- square pattern



# ques Reverse Multiplication Table using
# num = int(input("enter number to print table:\n"))
# limit = num*5
# print("table of ",num,":\n")
# for i in range(limit,0,-1):
#   print(f"{num} X {i} = {num*i}")


# function and recursion

# function: group of statement or specific task you can use it and we can stop repeatation to write code and use it many times

# def Percentage(marks):
#   m = ((marks[0]+marks[1]+marks[2]+marks[3]))
#   per = (m/400)*100
#   print(per)

# # mark = [45,89,56,89]
# # Percentage(mark)
# Percentage([90,78,89,85])  #coz we have single args
# mark1 = [65,89,56,89]
# percent = Percentage(mark1)
# print(percent)


# def Percentage(marks):    #function sign
#   m = ((marks[0]+marks[1]+marks[2]+marks[3]))
#   per = (m/400)*100           #function defination/body
#   return per

# mark = [45,89,56,89]
# percent = Percentage(mark)     #function calling
# print(percent)


# def fun1():
#   print("hello...")
# fun1()
# fun1()

# def greet(name):
#   print("good day,"+name)
# greet("raj")    #good day,raj

# TYPE OF FUNCTION: 1.BUILD-IN[i.e. range()]  2.USER DEFINE[greet()]

# def addition(a,b):
#   sum = a + b
#   print("sum:"+sum)

# def subtraction(a,b):
#   sub = a - b
#   return sub
# sum(12,13)
# a = subtraction(18,13)
# print(a)

# DEFAULT PERAMETER: default value as args if you don't put valid args or not pass args than default keyword give their own default as args
# def Greetings(name='username'):
#   print("hello !!!,"+name+" have a good day....")

# Greetings() #hello !!!,username have a good day....
# Greetings("raj") #hello !!!,raj have a good day....

# RECURSION:who call itself, use it carefully with end call of function at recursive calling
# i.e. factorial()

# def Factorial(n):
#   if(n==1 or n==0):
#     return 1
#   else:
#     return (n*Factorial(n-1))   #calling itself

# a = Factorial(5)
# print(a)    #120

# find greater in 3 number
# def Maximum(a,b,c):
#   if(a>b):
#     if (a>c):
#       return a
#     else:
#       return c
#   else:
#     if (b>c):
#       return b
#     else:
#       return c
# a = int(input("enter number 1:\n"))
# b = int(input("enter number 2:\n"))
# c = int(input("enter number 3:\n"))
# m = Maximum(a,b,c)
# print(m," is max")

# celsius to fahrenheit (0°C × 9/5) + 32 = 32°F

# def fer_temp(cel):
#   fer = (cel * (9/5)) + 32
#   return fer

# def cel_temp(fer):
#   cel = (fer-32)*(5/9)
#   return cel

# celsious = float(input("enter celsious :\n"))
# fehrenhite = fer_temp(celsious)
# print(celsious," equal to ",fehrenhite)

# a = cel_temp(14)
# print(a)


# how do you prevent/stop a print() to print a new line at the end
# print("hello",end=" ")
# print("!!!",end=" ")
# print("how",end=" ")
# print("are",end=" ")
# print("you?",end=" ")

# sum of natural nnumber using recursion
# def rec_sum(n):
#   if(n<=1):  #b'coz natural no start with 1 so can never be less than or equal to 1
#     return n
#   else:
#     return (n + rec_sum(n-1))
# num = int(input("enter no.:"))
# a = rec_sum(num)
# print("sum of ",num," natural no is :",a)

# write a function to print following funtion
# *****
# ****
# ***
# **
# *

# def pattern(n):
#   for i in range(n):
#     print("*"*(n-i))

# num = int(input("enter range to create pattern:"))
# pattern(num)

# cm into inches inch = cm/2.54
# def conv(cm):
#   inch = cm/2.54
#   return inch
# num = float(input("enter no :\n"))
# inc = conv(num)
# print(num,"cm equal to",inc,"inch")

# WAP to create function to remove a given word from string and strip it at the same time
# strip():used to remove unneccessary

# def rmv_n_strip(string,word):
#   newstr = string.replace(word,"")
#   return newstr.strip()

# str = input("enter a string:\n")
# n = input("enter a word to strip from string:\n")
# a = rmv_n_strip(str,n)
# print(a)

# project let's play snake gun and water, file name: "./CHW_project1_SWG_game.py"

# files I/O : YOU CAN INTERACT WITH FILES(read,write) VIA PY-CODE
# theory:
# FILE: collection of data to store data in computer in ram, HDD
# VOLATILE-> file storaged in ram like if you are playong games, NON-VOLATIL E: data stored in HDD or pendrive
# TYPES OF FILE:1.TEXT FILE(.txt, .c) 2.BINARY FILE(.jpg, .dot)
# open(): it is build-in func., used to opening a file,it takes 2 parameter (file name, mode) i.e.open("sample.txt","r")
# USED FILE: "./CHW_sample.txt"


# use open function to read the content of a file!
# open(),read(),close()

# f = open("CHW_sample.txt","r")
# f = open("CHW_sample.txt")   #by default open() choose "r" mode
# # data = f.read()   #it shows all char of file i.e. harry is a good boy. he is the best....
# data = f.read(5)   #it read only 5 char of file i.e. harry
# print(data)
# f.close()

# readline():read one by one line from .txt file
# f = open("CHW_sample.txt")  #open file

# data = f.readline() #read 1st line i.e. harry is a good boy.
# print(data)
# data = f.readline() #read 2nd line i.e. he is the best....
# print(data)
# data = f.readline() #read 3rd line i.e. new line
# print(data)
# data = f.readline() #read 4th line i.e. please
# print(data)
# data = f.readline() #read 5th line i.e. more... lines
# print(data)

# f.close()


# MODE:
# r: open for read
# w: open for write
# a: open for append
# +: open for update
# 'rb': open for read in binary mode(binary files)
# 'rt': open for read in text mode(binary files)


# write a file write()

# f = open("CHW_another.txt","w")
# data = f.write("NO-please")
# data = f.write("please write this to the file")  #it'll write 'msg' to the text file who exist with that name,if not exist than it'll create auto new file than write on it and if you write new 'msg' than it'll replace it to old data in .txt file, replacing is upto mode(w)
# f.close()

# append data in txt file
# f = open("CHW_another.txt","a")
# data = f.write("I am appending new line...")
# data = f.write("I am appending new line...")
# f.close()
# if you'll run this code more than a time it'll add each time append data in txt file

# f= open("this.txt","w")
# data = f.write("this is nice.")
# f.close()

# WITH statement:
# with open("CHW_another.txt","r") as f:
#   data = f.read()  #to read file
# with open("CHW_another.txt","a") as f:
#   data = f.write("hello....") #to append 'msg'
#   print(data)  # these's no need to exexute close()

# ques 1: find word in txt file
# f = open("poem.txt",)
# data = f.read()
# if 'twinkle' in data:
#   print("word present...")
# else:
#   print("word not present...")
# f.close()


# ques2:the game() in a program lets a user play a game and return the score as in integer, you need to read previous value and you break the score than update it from higher.txt file
# def game():
#   return 1
# score = game()
# with open("higher.txt") as f:
#   hiscoreStr = f.read()

# if hiscoreStr=='':
#   with open("higher.txt",'w') as f:
#     f.write(str(score))
# elif int(hiscoreStr)<score:
#   with open("higher.txt",'w') as f:
#     f.write(str(score))
# else:
#   print("high score is higher....")

# ques 3. generate table 2-20 and write it in diff diff text files

# for i in range(2,21):
#   with open(f"table/table_of_{i}","w") as f:
#     for j in range(1,11):
#       # f.write(f"{i}X{j}={i*j}\n")  #way 1 but it'll add new line in line no.11
#       f.write(f"{i}X{j}={i*j}")
#       if j!=10:
#         f.write('\n')


# a file contain word "donkey" multiple time,WAP toreplace it with ###### by updating some files

# with open("CHW_sample.txt") as f:
#   content = f.read()
# content = content.replace("donkey","$^$$$%%^#")
# with open("CHW_sample.txt","w") as f:
#   content = f.write(content)

# list of such bad words to consered
# words=["donkey","mote","kaddu"]

# with open("sample.txt") as f:
#   content = f.read()

# for word in words:
#   content = content.replace(word,"@#####")
#   with open("sample.txt","w") as f:
#     f.write(content)

# WAP to mine a log file and findout whether it contains 'python'
# and make new code to find out line number

# with open("log.txt") as f:
#   data = f.read().lower()

# if 'python' in data:
#   print("string present...")
# else:
#   print("string not present...")


# find out which line "python" present in log file
# content = True
# i = 1
# with open("log.txt") as f:
#   while content:
#     content = f.readline()
#     if 'python' in content.lower():
#       print(content)
#       print(f"string present in line number {i}")
#       i += 1

# write a copy of txt file

# with open("this.txt") as f:
#   content = f.read()
# with open("copy.txt","w") as f:
#   f.write(content)

# WAP to check 2files are identical or not and match content or not

# file1 = "copy.txt"
# file2 = "this.txt"
# with open("copy.txt") as f:
#   f1 = f.read()
# with open("this.txt") as f:
#   f2 = f.read()
# if f1==f2:
#   print("files are identical...")
# else:
#   print("files are identical...")

# wap to wipe out content of txt file

# filename = "copy.txt"
# with open(filename,'w') as f:
#   f.write("")

# rename txt file

# import os
# oldname = "sample2.txt"
# newname = "renemed_by_python"
# with open(oldname) as f:
#   content = f.read()
# with open(newname,'w') as f:
#   content = f.write(content)
# os.remove(oldname)     # it'll create new same txt file and we can delete old one & 'os' is build-in module
















