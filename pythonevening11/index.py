# s = "bootcamp"
# print (s[1:2])


# hello = 'Salam World'
# print(hello)

# hello =  "Salam World"
# print (hello)

# lorem_ipsum = """Lorem gh hg hh hdhbf hfbhf hfbh knfeofoewb
#              eoinewionewoicnew
#              kcnewoicnewoicew
#          kenceoiwcnwoeic
#           keccnhoeiwheio"""
# print (lorem_ipsum)          

# error_string = """Don't repeat yourself"""
# print (error_string)

# number = 95
# message = "Your points: "+" "  + str(number )
# print (message)

# formatirovanie
# student_points = 100
# message = "Student1: %s ponts"
# print (message % student_points)


# name = "john"
# print (name [0])
# print (name[1])
# print (name[2])
# print (name[3])
# print (len(name))


# var = 'birthday'
# b == 0
# i == 1
# r == 2
# t == 3
# h == 4
# d == 5
# a == 6
# y == 7

# b == 0
# i == -7
# r == -6
# t == -5
# h == -4
# d == -3
# a == -2
# y == -1

# print (var [-8])

# flavor = "birthdaycake"
# print ( flavor [0:3])
# print (flavor[0:5])
# print (flavor [1:5])

# start:end:Step

# print (flavor[0:12:2])

# var = 'John Snow'
# print (var[0:10:3])
# print (var[0:len(var):3])

# cjjjj
# laptop = 'Acer, Asus, HP'
# print (laptop [:])
# print (laptop [-5:-1])

# focus = 'John'
# print (focus[::-1])

# word = input("Enter your word:") 
# if word [::-1] == word:
#     print('word +  " " + is palindrom')
# else:
#     # print( word + " " + "is't palindrom")

# hello =  " %s hello" 
# print (hello % "John")

# # method format
# name = input ( 'Enter your name')
# full_name = "{} Connor ".format(name)
# # print(full_name)

# result = 'I am programmer. I know {} , learning for the moment {}'
# message = result.format ( 'Python', 'Golang')
# print (message)

# name = input ( " Fill your name: ")
# last_name = input ( 'Fill your surname: ')
# message = "my name is {} and my surname is {}". format (last_name, name)
# print (message)
#  lang_1 = 'Python'
#  lang_2 = 'JS'
#  result = 'languages {python}, {js}'.format(python=lang_1, JS=lang_2)
#  print (result)




# s0 = 'abrac'
# s1 = 'a'
# s2 = 'dabra'
# print (s0 + s1.replace ('a' , 'k')+ s2)

# age = input ( "How old are you?: ")
# country = input ( " where are you from?: ")
# message = "I am {} years old and I am from {}". format (age, country)
# print (message)

# s = 'countryside'
# print = (s[4:9])

# name = 'John'
# print (dir(name))





# first_name = input ( "fiil your name: ")
# last_name = input ("fill your surname: ")
# print ("before: ", first_name)
# print ("after: ", first_name.lower())   .upper()
# print ("before: ", last_name)
# print ("after :", last_name.lower())   .upper()

# laptop = input ('Name of the company: ')
# print ( laptop.swapcase())

# car = "Don't repeat yourself or principle solid"
# print (car.find('solid'))


# car = 'BMW, Audi, Honda accord,  Honda Fit. Toyota camry'
# print (car.find ('Honda', 12))



# method rfind

# car = 'BMW, Audi, Honda accord,  Honda Fit. Toyota camry'
# print (car.rfind ('Honda'))

# string = 'soccer so'
# print (string.index("hello"))

# method rindex

# string = 'soccer so'
# print (string.index("o"))

# method replace

# title = "Makers Bootcamp hello"
# print (title[0:7] + title[7:].replace (" ", "/" , ))

# replace (old_str, new, count)
 
#  method split

# names = "John, Peter, Raychel, Vanya"
# generate_names = names.split(",")
# print (generate_names)


# isdigit ()
# isalpha ()
# islower ()
# isupper ()
# istitle()
# isalnum ()

# string = input ("Fill numbers: ")
# print (string.isdigit())

# string = input ("Fill string: ")
# print (string.isalpha())

# string = input ("Fill string: ")
# print (string.isalnum())

# string = input ("Fill string: ")
# print (string.isalpha())


# word = input ("Fill word: ")
# if not word.isupper()
# print (" Fill with lockom")
# else :
#     print ("Good, I have saved word")

# spaces = '/n/t/b'
# print (spaces.isspace())

# title()
# capitalize()

# language = input ('Your best programming language: ')
# print ( language.title())

# print (language.capitalize())


# startswith()
# endswith()

# result = 'My name is John'
# if result.stratwith("My"):
#     print ("Okey")
# else:
#     print ("Not okay")

# phone_numbers = input ('Fill your number:')  
# if phone_number.startwith("+996"):  
# print ("Your country KG")
# else:
# print ("Web working only in kg")


# ls = ['al@gmail.com',
#       "john@gmail.com"
#       "raychel@gmail.com"]



# string = "Perfection"
# print = (string.title())


# name = input('Enter your name: ')
# surname = input ('Enter your surname: ')
# age = ('Enter your age: ')
# town = ('where are you from ?')
# print (f "Your name is {name} {surname}."
# f " You are {age} years old."
# f "You live in {town})


s = "john snow"
print (s.title())