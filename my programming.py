#from math import hypot
#import random

alphabets=["a","b","c","d","e","f","g","h","i"]

#i=5
#while i<40:
    #print(i)
    #i += 5
    #if i==30:
      # break
#find area of square
#l=float(input("Enter the l:"))
#w=float(input("Enter the w:"))
#area=l*w
#print(f"the area of square is{area}")


#find the number of even odd
#pop=1,2,3,4,5,6,7,8,9
#count_even=0
#count_odd=0
#for x in pop:
    #if x % 2==0:
        #count_even+=1
    #else:
     #   count_odd+=1
#print(f"the number of even digits are {count_even}")
#print(f"the number of odd digits are {count_odd}")

# the price of cherry is twice of banana
#apples=int (input('the price of one apple is:'))
#bananas=int(input("the price of one banana is :"))
#cherry=2*bananas
#print(f"the price of cherry is {cherry}")

#madlibs game is word where we create a story by filling blacks with random words
#adjective=input('enter an adjective :')
#verb=input("enter verb(show action):")
#noun=input("enter noun: ")
#print(f"today {noun} saw a {adjective} lady on his way to home")
#print(f"then he became very {verb} ")

#important reserved words
#x=12.4
#y=-4
#result=int(x)
#print(result)
#result=abs(y)
#print(result)
#result=pow(8,3)
#print(result)
#result=int (max(x,y))
#print(result)

#import math
#NUMBER=int(input("Enter a number :"))
#result=math.pow(NUMBER,3)
#print(result)

#import math
#num=int(input("Enter the number :"))
#result=math.sqrt(num)
#print(result)

#import math is use to find the mathematical values

#import math
#number=int(input("Enter a number :"))
#result=math.sqrt(number)
#print(result)

#x=49
#import math
#result=math.sqrt(x)
#print(result)

#import math
#radius=int(input("Enter the radius of circle :"))
#pi=math.pi
#result=2*pi*radius*radius
#print(result)

#calculate the area of circle
#import math
#r=float(input("enter the radius of circle ="))
#area=math.pi*r*r
#print(f'the area of circle is equal to {round(area)}')

#calculate the hp  right angle triangle
#import math
#b=float(input("enter the base of right angle triangle ="))
#p=float(input('enter the perpendicular of RAT ='))
#p=pow(b,2)+pow(p,2)
#print(int(math.sqrt(p)))


#import math
#base=int(input("Enter the base of triangle :"))
#perpen=int(input("Enter the perpendicular of triangle :"))
#hyport=int(input("Enter the hypo of trianlgle :"))
#p=math.pow(base,2)+math.pow(perpen,2)
#print(math.sqrt(p))


#import math
#a=int (input("enter the base value ="))
#b= int (input("enter the perpendicular = "))
#c=pow(a,2)+pow(b,2)
#print(math.sqrt(c))

#name=input("ENTER YOUR NAME :")
#if name=="":
 #   print('you did not enter your name')
#else:
 #   print(f"hello {name}")

#for_sale=False
#for_sale=True
#if for_sale:
    #print("THIS ITEM IS FOR SALE")
#else:
   # print("this item is not for sale")

#food=True
#if food:
 #   print("yes food is available")
#else :
    #print("out of main you")

#calculator
#num1=int(input("ENTER THE FIRST NUMBER ="))
#operator=input("ENTER THE OPERATOR (+,-,%,/) =")
#num2=int(input("ENTER THE SECOND NUMBER ="))
#if operator=="+":
    #result=(num1+num2)
    #print(result)
#elif operator=="-":
    #result=(num1-num2)
    #print(result)
#elif operator=="%":
    #result=num1%num2
    #print(result)
#elif operator=="/":
   # result=num1+num2
    #print(result)
#else:
 #   print("you put wrong operator")


#convert unit weight
#weight=float(input("ENTeR TOUR WEIGHT :"))
#unit=input("ENTER THE UNIT (kilo or pounds :)")
#if unit=="kilo":
   # weight=weight *2.20
  #  unit=kg
#elif unit=="pound":
  #  weight=weight/2.20
 #   unit=pounds
#else:
 #   print("you have enter a wrong unit")
#print(f"your weight is {weight}{unit} ")


#value=int(input("Enter the value :"))
#unit=input("Enter the unit (kilo or gram) :")
#if unit=="kilo":
 #   result=value/1000
  #  print(result)
#elif unit=="pound":
 #   result=value*4
  #  print(result)
#else:
    #print(f"your values in {unit} become {result}")

#temperature=float(input("ENTER THE TEMPERATURE "))
#unit=input("unit is kelvin or far(k or f) : ")
#if unit=="k":
#    temperature=temperature-273
 #   print(temperature)
#elif unit=="f":
 #   temperature=temperature+313
  #  print(f"{temperature}{unit}")
#else:
 #   print("u enter wrong unit")

#tem=50
#is_raining=False
#if tem>36 or tem<0 or is_raining:
 #   print("the weather is hot")
#else :  
    #print("u can go outside")

#number=50
#print("yes"if number>40 else "false")

#print odd numbers of multiple of 3
#a=3
#while a<=30:
#   if a%2==1:
   #    print(a)
   # a+=3


#name=input("ENTER YOUR FULL NAME :")
#result=len(name)
#result=name.find("")
#result=name.isdigit()
#result=phone_number.isdigit()
##print(result)
#result=phone_number.count("3")
#result=phone_number.replace("k","90")
#print(result)



#username=input("ENTER YOUR FULL NAME =")
#if len(username)>12:
 #   print("Your name must not be greater then 12 characters")
#elif username.find(" ")==-1:
 #   print("your name doesnt contain any spaces")
#elif not username.isalpha():
 #   print("USER NAME CANNOT CONTAIN DIGITS")
#else:
  #  print(f"welcome {username}")


#products=input("ENTER THE PRODUCT YOU WANT TO BUT =")
#if products=="vegetables":
 #   vegetables=input("Enter the vegetable name u want to buy =")
  #  print(f"you order {vegetables}")
#elif products=="fruits":
 #   print("price is 400")
#else:
 #   print("you have buy nothing")


#index
#name="pakistan is my beautiful country"
#result=name[0:15]
#print(result)
#result=name[:8]
#print(result)
#print((name[4:]))

#number="324-6567-86--4"
#result=number[::2]
#print(result)

#number="16101-7098856-7"
#result=number[-4::]
#print(result)

#make a program to print last 4 digits of CNIC
#number="16101-7098856-7"
#result=number[-5:]
#result=number[::]
#result=number[::-1]
#print(result)

#NAME=input("enter your name :")
#if NAME=="":
 #   print("you have not enter your name")
#else:
 #   print(f"hello {NAME}")

#while loop
#food=input("Enter the food u want to order :")
#while not food=="k":
 #   print("yes its available")
  #  food=input("enter another food u want to order :")
#print("bye")


#foods=[]
#food = input("Enter the food u want to order :")
#while food:
 #   if food=="k":
  #      print(f"your order food is {food}")
   #     break
    #else:
     #   food=input("Enter another food u want to order :")
      #  foods.append(food)
#print(f"you order food is {food}")

#foods=[]
#prices=[]
#total=0
#while True:
  #  food= input("ENter the food u want to order :")
 #   if food=="k":
   #     break
    #else:
    #price=int(onput("ENter the price"))
     #  foods.append(food)
     #   prices.append(price)
#print(f"your ordered food are {foods}")
#print(f"prices {prices}")



#age=int(input("Enter your age :"))
#while age<=0:
  #  print("you r under age")
 #   age=int(input("Enter your name :"))
#print(f"{age} age is eligible to apply for the post")

#age=int(input("Enter your age :"))
#while age<18:
  #  print("You r under age ")
 #   age=int(input("Enter your age :"))
#print(f"yes u r eligible {age}")

#age=18
#if age>=15:
  #  print("you r eligible")
#else:
  #  print("u r under age ")


#number=int(input("Enter the number(from 20 to 30) :"))
#while number<20 or number>30:
  #  print("you have wrong number")
 #   number = int(input("Enter the number(from 20 to 30) :"))
#print(f"your enter number is {number}")

#number=int(input("Enter a number between 20 and 30 : "))
#while number<20 or number>30:
 #   print("YOu have enter a wronge number ")
  #  number=int(input("Enter a number between 20 and 30 :"))
#print(f"your enter is {number}")

#number=int(input("Enter a number"))
#if number % 2==1:
 #   print("Its an odd number ")
#else:
 #   print("its even")





#program to print odd number
#number=int(input("Enter an odd number :"))
#while number%2==0:
 #   print("you have enter an even number so its wrong")
  #  number=int(input("Enter an odd number "))
#print(f"you enter odd number is {number}")

#i=1
#while i<=30:
   #print(i)
   # i+=2

#principal=0
#rate=0
#time=0
#while principal<=0:
 #   principal=float(input("enter the principal amount :"))
  #  if principal<=0:
   #     print("principal amount must not be less then or equal to xero")
#while rate<=0:
 #   rate=float(input("Enter rate if interest :"))
  #  if rate<=0:
   #     print("interest must not be less or equal to zero")
#while time<=0:
  #  time=int(input("enter time :"))
 #   if time<=0:
   #     print("time must not be less then or equal to zero")
#total_amount=principal*(pow(1+rate/100,time))
#print(f"the total amount of compound interest is {total_amount} rupees for {time} year")

#principal=0
#rate=0
#time=0
#while principal<=0:
 #   principal=float(input("enter the principal amount :"))
  #  if principal<=0:
   #     break
#while rate<=0:
 #   rate=float(input("Enter rate if interest :"))
  #  if rate<=0:
   #     break
#while time<=0:
 #       print(int(input("ENTer the time")))
  #      if time<=0:
   #         break
#total_amount=principal*(pow(1+rate/100,time))
#print(f"the total amount of compound interest is {total_amount} rupees for {time} year")


#for x in range(1,21):
   # print(x)


#for x in range(1,11):
 #   if x==5:
  #      continue
   # else:
    #    print(x)





#import time
#my_time=int(input("Enter the time :"))
#for x in range(0,my_time):
 #   print(x)
  #  time.sleep(2)

#import time
#for x in range(0,5):
 #   print(x)
  #  time.sleep(1)
#print("times up")


#for x in range(3):
 #   for y in range(0,3):
  #      print("*",end=" ")
   # print()







#rows=int(input("Enter the number of rows :"))
#column=int(input("Enter the number of colums :"))
#string=input("Enter the string :")
#for x in range(rows):
 #   for y in range(column):
  #      print(string,end=" ")
   # print()




#fruits=["apple","banana","orange"]
#print(fruits)
#print(fruits.index("apple"))
#print(fruits.index("orange"))
#print(help(fruits))
#print("pineapple"in fruits)
#print("banana" in fruits)
#print(list)
#for x in list:
 #   print(x,end=" ")()
#for x in list:
 #   for y in list:
  #      print(y,end=" ")
   # print()
#print(fruits.append("pine"))
#print(fruits[::-1])
#print(fruits.insert(0,"pine"))
#print(fruits.reverse())

#for x in range(3):
 #   for y in range(0,5):
  #      print("*",end="")
   # print()






#CART CARD
#foods=[]
#prices=[]
#total=0
#while True:
 #   food = input("Enter the food u want to order :")
  #  if food=="q":
   #     break
   # else:
    #    price=int(input("Enter the price of food :"))
     #   foods.append(food)
      #  prices.append(price)
#for food in foods:
 #   print(food)
#for price in prices:
 #   print( price)
#for price in prices:
 #   total+=price
#print(f"the total of your odered meal is {total}")


#question_num=0
#questions=("what is your name :",
 #          "What is your father name:")
#choices=(("a:ehtisham","b:mushtaq","c:kamran","d:pizza"),
 #        ("a:sardar","b:kamran"))
#for x in questions:
 #   print("-------------")
  #  print(x)
   # for y in choices[question_num]:
    #    print(y)

    #question_num+=1

#dic={
   # "name":"ehtisham",
    #"class":"2nd semester",
    #"roll number":29,
#}
#result=dic.values()
#print(result)
#print(dic.get("roll number"))


#dic={
   # "USA":"washington DC",
  #  "PAKISTAN":"ISLAMABAD",
 #   "U.K":"NONE"
#}

#print(dic.get("PAKISTAN"))
#if "USA" in dic:
 #   print("YEs its present in dic")
#else:
 #   print("No it doesnt exist")


#for x in range(0,20):
 #   if x==15:
  #      break
   # print(x)

#find the amount of balance after 2 years
#amount=int(input("Enter the amount :"))
#rate=int(input("Enter the rate :"))
#time=int(input("Enter the time :"))
#result=amount*pow(1+rate/100,time)
#print(result)
#print(f"balance after {time}year is {result}$")

#food=[]
#price=[]
#total=0
#while True:
    #foods=input("Enter the food u want to order :")
   # if foods=="q" or foods=="Q":
    #    break
   # else:
  #      prices=int(input(f"Enter the price of food :"))
 #       food.append(foods)
#        price.append(prices)

#print("..........Your cart............")
#for foods in food:
 #   print(foods)
#for prices in price:
 #   total=total+prices
#print(f"total price become {total} rupees")


#total=[["apple","banana","pineapple"],["cucumber","spanich","pizza"],["cowmeat","bearmeat","sheepmeat"]]
#for x in total:
 #   for y in x:
  #      print(y.end=" ")
    #print()

#dic={
 #   "USA": "washington DC",
  #  "PAKISTAN": "islamabad",
   # "GERMANY": "moscow"
#}
#print(dic)
#print(dic.values())
#print(dic.keys())
#print(dic.popitem())

#num1=int(input("Enter the first number :"))
#num2=int(input('Enter the second number :'))
#sum=num1+num2
#average=num1+num2/2
#print(sum)
#print(average)

#num=8
#for x in range(num):
 #   for y in range(x):
  #      print("*",end="")
   # print()
#for j in range(num,0,-1):
 #   for k in range(j):
  #      print("*",end="")
   # print()

#n=5
#for x in range(n):
 #   for j in range(x):
  #      print('*',end='')
   # print('')
#for x in range(n,0,-1):
 #   for j in range(x):
  #      print('*',end='')
   # print('')


#class candidates:
    #def __init__(self, age, city):
      #  self.age = age
     #   self.city = city
    #def __str__(self):
   #     return f"{self.age}({self.city})"
  #  def myfuc(self):
 #      print("he lives in" + " " + self.city)
#obj1 = candidates(21, "hakeemanbad")
#obj1.myfuc()


#menu={
    #"lemon": 50,
   # "chips": 300,
  #  "pizza": 350,
 #   "burger": 250
#}
#print(".............MENU.................")

#for key,x in menu.items():
 #   print(f"{key}  :  {x} Rupees")
#print(".................................")


#def add(val1,val2):
 #   print("This is an add function ",val2+val1)
#add(2,4)





#options=("rock",'paper',"scissor")
#choices=random.choice(options)
#print(choices)



#cards=["2","4","6","10","J","k","Q"]
#choice=random.shuffle(cards)
#print(cards)


#lowest_num=1
#highest_num=100
#answer=random.randrange(lowest_num,highest_num)
#print("python Guessing game ")
#print(f"Guess the number from 1 to 100 ")
#while True:
 #   guess=input("Enter the number of guess :")
  #  if guess.isdigit():
   #      guess=int(guess)

    #     if guess<lowest_num or guess>highest_num:
     #        print("The number is out of range")
      #   elif guess<answer:
       #      print("to low try again")
        # elif guess>answer:
         #    print("To high try again")
         #else:
          #   print(f"correct {answer}")
           #  break
    #else:
     #   print("invalid number")
      #  int(input("Enter the number of guess :"))

#list=["rock","paper","scissor"]
#answer=random.choice(list)
#print(answer)
#while True:
 #   num=input("ENter your guess")
  #  if not num.isdigit():
   #     pass
    #    if guess==answer:
     #       print("your answer is correct")
      #  else:
       #     print("you r wronge")
    #else:
       # print("you must not enter digits")


#list=["rock","paper","scissor"]
#answer=random.choice(list)
#while True:
 #   guess=input("Enter the guess :")
  #  if not guess.isdigit():
   #     pass
    #    if guess==answer:
     #       print("you pass ")
      #      break
       # else:
        #    print("you fail")
    #else:
     #   print("invalid string")
      #  input("Enter the guess :")
#print(f"your guess {guess}")
#print(f"computer guess {answer}")

#def myfuc():
 #   print("hey buddy")
#myfuc()

#def add(a,b):
 #   print(a+b)
#add(3,5)

#def myfuc(fname,age):
 #   print(f"hey {fname} r u {age} year old ? ")
#myfuc("ehtihsam",21)

#def myfuc(fname,lname):
   # fname=fname.capitalize()
  #  lname=lname.capitalize()
 #   return fname +" "+lname
#fullname=myfuc("ehtihsam","hussain")
#print(fullname)

#import time
#def myfuc(start,end):
 #   for x in range(start,end+1):
  #      print(x)
   #     time.sleep(1)
    #print("over")
#myfuc(0,10)


#import time
#def myfuc(start,end):
    #for x in range(start,end):
   #     print(x)
  #      time.sleep(1)
 #   print("times up")
#myfuc(1,10)

#import time
#def myfuc(start,end):
 #   for x in range(start,end+1):
  #      print(x)
   #     time.sleep(1)
    #print("times up")
#myfuc(1,10)


#argument types _positional-default-keywords-arbitrary
#def myfuc(company,title,name,fname):
 #   print(f"{company} {title} {name} {fname}")
#positional argument
#myfuc("pop","Kp","eht","sar")
#keywords
#myfuc(title="pak",company="pop",name="ehti",fname="sar")
#print("1","2","3","4","5",sep="-")


#def myfuc(country,area,fnum,lnum):
 #   print(f"{country}-{area}-{fnum}-{lnum}")
#myfuc(country="PAK",area=16101,fnum=70988,lnum=567)

#arbitrary___*args(tuple)___**kwargs(dic)
#def add(a,b,c):
 #   print(a+b)
#add(1,2,3)


#def add(*args):
 #   total=0
  #  for x in args:
   #     total+=x
    #print(total)
#add(1,2,3)

#def happy_birthday(name,wish):
 #   print(f"hello {name}")
  #  print(f"{wish} birthday")
   # print()
#happy_birthday("ehtisham","birthday")


#def myfuc(price,discount,tax):
 #   return price*(1-discount)*(1+tax)
#print(myfuc(3000,0,0.05))




#def myfuc(price,saleprice=0,tax=0.05):
 #   return price+saleprice-tax
#print(myfuc(1000))

#def myfuc(*args):
 #   for x in args:
  #      print(x,end=" ")
#myfuc("Ehtisham","hussain")

#def myfuc(*args):
 #   for x in args:
  #      print(x,end=" ")
#myfuc("pakistan","zindabad")

#def myfuc(**kwargs):
 #   for x,values in kwargs.items():
  #      print(f"{x}:{values}")
#myfuc(name="ehtihsam",
 #     place="nowshera",
  #    age=21)

#def myfuc(*args,**kwargs):
 #   for x in args:
  #      print(x,end=" ")
   # print()
    #for y,values in kwargs.items():
     #   print(f"{y}:{values}",end=" ")
    #print()
    #for z in kwargs:
     #   print(f"{kwargs.get("street")}")
      #  print(f"{kwargs.get("city")}")
    #if "ehtisham" in args:
     #   print(f"{kwargs.get("street")}")
    #else:
     #   print(f"{kwargs.get("city")}")

#myfuc("ehtisham","hussain",
 #     street="MOQ",
  #    city="Nowshera")


#dic={
 #  "subhan":"B",
  #  "afaq":"c",
   # "hasnain":"D"
#}
#name=input("Enter the name of student :")
#if name in dic:
 #   print(f"{name} grade is {dic[name]}")
#else:
 #   print(f"{name} is not found")

#dic={
 #   "ehtisham":"1st position",
  #  "subhan":"2nd position",
   # "Ali":"3rd position"
#}
#name=input("ENter the name of a student :")
#if name in dic:
 #   print(f"{name} got {dic[name]}")
#else:
 #   print(f"{name} not in dic")

#email="ehtishamhussain4444@gmail.com"
#if "@" and ".com" in email:
 #   print("your email is valid")
#else:
 #   print("your email is not valid")


#list=[x*2 for x in range(1,11)]
#print(list)
#list=[z*z for z in range(1,11)]
#print(list)

#fruits=[x.upper() for x in ["apple","mangoes","banana"]]
#print(fruits)

#fruits=["apple","banana","orange"]
#result=[x[1] for x in fruits]
#print(result)

#fruits=["ehtihsam","husain","khan"]
#result=[x[0] for x in fruits]
#print(result)

#num=[-1,-2,-3,-4]
#result=[-1*x for x in list]
#positve=[x for x in num if x>=0]
#negative=[x for x in num if x<0]
#print(positve)

#def my_cnic(country,area,first,last):
 #    print(f"{country}-{area}-{first}-{last}")
#my_cnic(country=92,area=16101,first=70988,last=567)

#def myfuc(**kwargs):
 #   for key,x in kwargs.items():
  #      print(f"{key}:{x}")
#myfuc(name="Ehtihsam",
 #     father="sardaaar",
  #    DOB=2003)


#MEMBERSHIP OPERATOR (IN and NOT IN)
#name="Ehtisham"
#user=input("Enter your name :")
#if user in name:
 #   print(f"yes {user} in present")
#else:
 #   print("not found")

#Grades={
 #   "Ehtisham":"A+",
  #  "Subhan":"A",
   # "kamran":"B"
#}
#student=input("ENter the name of student :")
#if student in Grades:
 #   print(f"{student} grade is {Grades[student]}")
#else:
 #   print("not found")


#email="ehtishamhussain4444@gmail.com"
#if "@" and "." in email:
 #   print("its valid")
#else:
 #   print("invalid")

#triple=[]
#for x in range(1,11):
 #   triple.append(x*3)
#print(triple)


#list comprehention
#double=[x*2 for x in range(1,11)]
#triple=[x*3 for x in range(1,11)]
#square=[x*x for x in range(1,11)]
#print(square)

#vegetables=["potatoes","Tomatoes","Bringle"]
#vegetables=[x.upper() for x in vegetables]
#print(vegetables)


#fruits=["apple","banana","mangoes"]
#fruits=[fruits[2] for x in fruits]
#print(fruits)

#numbers=[1,-2,3,-4,5,-6]
#positive=[x for x in numbers if x>=0]
#print(positive)

#number=[1,-2,3,-4,5]
#negative=[x for x in number if x<0]
#even=[x for x in number if x%2==0]
#odd=[x for x in number if x%2==1]
#print(even)
#print(negative)
#print(odd)

#number=int(input("Enter a number :"))
#if number==1:
 #   print("its monday")
#elif number==2:
 #   print("its tuesday")
#elif number==3:
 #   print("its wednesday")
#else:
 #   print("its over")


#def myfuc(x):
 #   if x==1:
  #      print("its monday")
   # elif x==2:
    #    print("its tuesday")
    #elif x==3:
     #   print("its wed")
    #else:
     #   print("fucked up")
#myfuc(4)

#MATCH CASE(switch)

#def myfuc(day):
 #   match day:
  #      case 1:
   #         return "its sunday"
    #    case 2:
     #       return "its monday"
      #  case 3:
       #     return "its wed"
        #case _:
         #   return "invalid"
#print(myfuc(5))

#numbers=[1,-2,3,-4,5,-6]
#negatives=[x for x in numbers if x<=0]
#print(negatives)

#import math
#print(math.sqrt(25))

#import math
#print(math.e)

#import  math as m
#print(m.pi)

#from math import sqrt
#print(sqrt(25))

#from math import e
 #a,b,c,d=1,2,3,4
#print(e**a)
#print(e**b)
#print(e**c)

#import example
#print(example.pi)
#result=example.square(2)
#print(result)
#result=example.circumference(4)
#print(result)

#x=3
#def fuc():
 #   global x
  #  print(x)
#def myfuc():
 #   x=2
  #  print(x)
#fuc()
#myfuc()

#LEGB

#from math import e
#def fuc():
 #   print(e)
#e=2.34
#fuc()

#from example import *
#print(__name__)

#def myfav(food):
 #   print(f"my fav food is {food}")
#def main():
 #   print("hi")
  #  myfav("sushi")
   # print("good bye!")
#if __name__=='__main__' :
 #   main()

#subject=[]
#numbers=[]
#totalmarks=300
#total=0
#while True:
#    subjects=(input("Enter your subjects :"))
 #   if subjects=="q":
  #      break
   # else:
    #    number=int(input("ENter your numbers :"))
     #   numbers.append(number)
      #  subject.append(subjects)
#print("_______________DETAILS MARKSHEET______________")
#print(f"{subject} with its {numbers}")
#for number in numbers:
 #   total+=number
#print(total)
#percentage=(total/totalmarks)*100
#print(percentage)

#balance program

#def show_balance():
 #   print(f"your current balance is {balance}Rs")
  #  print("_____________________")
#def deposit():
 #   deposited=int(input("ENter the amount u want to deposit "))
  #  if deposited <0:
   #     print("AMOUNT MUST NOT BE LESS THEN ZERO")
    #    return 0
    #else:
     #   return deposited
#def withdrawal():
 #   withdraw=int(input("Enter the amount you want to withdraw"))
  #  if withdraw >balance:
   #     print("your amount is not that much")
    #    return 0
    #elif withdraw <0:
     #  print("amount must not be less then zero")
      #  return 0
    #else:
     #    return withdraw
#balance=0
#is_running=True

#while is_running:
 #   print("Bank balance")
  #  print("1.SHOW BALANCE ")
   # print("2.DEPOSIT")
    #print("3.WITHDRAWAL")
    #print("4.EXIT")

    #choice=(input("Enter a choice :"))
    #if choice=="1" :
     #   show_balance()
    #elif choice=="2":
     #   balance+=deposit()
    #elif choice=="3":
    #    balance-=withdrawal()
   # elif choice=="4":
  #      is_running=False
 #   else:
#        print("Invalid choice")




























































