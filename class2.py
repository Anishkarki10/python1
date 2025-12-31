# while True:
#     a=input("Enter your age : ")
#     if a=='stop':
#         break
#     a=int(a)
#     if a<18:
#         print("You are minor")
#     elif a>18 and a<60:
#         print("You are an adult")
#     elif a>60:
#         print("You are a senior citizen")
#     else: 
#         print("please enter a correct value")


# # while (userinput:=intinput(('Enter a number')))>1

# while True:
#     a=input("Enter the vehicle name : ").title()
#     if a == "Bus":
#         print("finally the wait is over")
#         break
#     else:
#         print("waiting")

# while True:
#     a=input("Enter a fruit name: ").lower()
#     if a == 'apple':
#         print("You got it")
#         break
#     else:
#         print("Try again!")

# while True:
#     a=input("Enter your password")
#     if a == "open sesame":
#         print("Acess granted!")
#         break
#     else:
#         print("Try again !")

# ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
# a={}
# i=0
# while i<len(ratings):
#     if ratings[i] in a:
#         a[ratings[i]]+=1
#     else:
#         a[ratings[i]]=1
#     i=i+1
# print(a)

# ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
# a={}
# i=0
# while i<len(ratings):
#     a[ratings[i]]=a.get(ratings[i],0)+1
#     i=i+1
# print(a)

# ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
# a={}

# while ratings:
#     rating=ratings.pop()
#     a[rating]=a.get(rating,0)+1
# print(a)
# import random
# number=random.randint(1,10)
# i=0
# while True:
#     a=int(input("Enter a number : "))
#     if a >number:
#         print("Too High")
#         i+=1
#     elif a<number:
#         print("Too low")
#         i+=1
#     elif a == number:
#         print(f"you have tried for {i}")
# i=0
# while True:
#     if i <= 3:
#         a=input("Enter your username: ")
#         b=input("Enter your password: ")
#         if a == "admin" and b=="1234":
#             print("login sucessful")
#             break
#         else:
#             print("try again!")
#             i+=1
#     else: 
#         print("To many attempts")
#         break
# import random
# a=random.randint(1,30)
# b=random.randint(1,30)
# mul = a*b
# print(mul)
# while True:
#     c=input("Guess the number: ")
#     if c == "stop":
#         break
#     c=int(c)
#     if c == mul:
#         print("Good Guess")
#         a=random.randint(1,30)
#         b=random.randint(1,30)
#         mul=a*b
#         print(mul)
#         c=input("second question :")
#         if c == 'stop':
#             break
#         c=int(c)
#         if mul == c:
#             print("Good guess")
#             break
#     else:
#         print("Incorrect")
# b=['python','jython','c']
# while True:
#     a=input("Enter a secreat code : ")
#     if a in b:
#         print("Congratulations")
#     elif a== "exit":
#         print("you have exit the game")
#         break
#     else:
#         print("incorrect")

# while True:
#     currentfloor=1
#     floor=int(input("Where you want to go"))
#     if floor>currentfloor:
#         print(f"going up {floor}")
#         currentfloor=floor
#     elif floor>currentfloor:
#         print(f"going down {floor}")
#         currentfloor=floor
#     elif floor == 0:
#         print("good bye")
#         break
#     elif floor == currentfloor:
#         print(f"You are currently at same floor {floor}")
#     else:
#         print(f"dosen't exist{floor}")

# gl=0
# while True:
#     if gl<3:
#         a=input("Enter good luck to track").lower()
#         if a == "goodluck":
#             gl+=1
#         else:
#             print("Try again")
#     else:
#         print(f"you have entered {a} for {gl} times")
#         break
