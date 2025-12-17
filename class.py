# for i in range(1,6):
#     if i%2==0:
#         print(f"Number {i} is even")
#     else:
#         print(f"Number {i} is odd")

# sum=0
# list = [10,20,30,40]
# for i in list:
#     sum=sum+i
#     print(f"Added {i}. Running total is {sum}")
    
# print(f"total{sum}")
# print(" ' --- Email Greetings Generated ---'")
# student_names = ["Ram", "Hari", "Sita"]
# for i in student_names:
#     print(f"Hi {i}, Your course has been approval is ready!")
# count=0
# a=[45, 30, 50, 40]
# for i in a:
#     count=count+1
#     print(f"Chapter {count} has {i} Pages ")
# div=1
# a=[4,5,3,2]
# for i in a:
#     div=i*div
# print(div)
# t=1
# a=11
# for i in range(1,11):
#     print(f"{a} * {i} is {a*i}")

# students = [

#     {"name": "ram", "math_grade": 43},

#     {"name": "hari", "math_grade": 65},

#     {"name": "sita", "math_grade": 90}

# ] 
# for i in students:
#     if i['math_grade']>=70:
#         i['status']='approved'
#     else:
#         i['status']='rejected'
# print(students)

# a= [1,2,3,4,5]
# b= [3,4,5,6,7]
# for i in a:
#     for x in b:
#         if i == x:
#          print(i)

# lst=[1,2,3,4]
# for i in lst:
#     if i == 1 or i==4:
#         print(i)

# lst=[1,2,3,4] 
# for i in lst:
#     if i == 1 or i==2 or i==4:
#         print(i)

# list= [1,2,3,4]
# list.insert(1,"e")
# print(list)

# b=[]
# c=[]
# a=[1,2,3,4,5]
# for i in a:
#     if i%2==0:
#       b.append(i)
#     else:
#         c.append(i)
# print(c)
# print(b)

# prime=False
# a=int(input("Enter a Number: "))
# for i in range(2,a):
#     if a%2==0:
#         prime=False
#     else:
#         prime=True
# if prime:
#     print(f"{a} is not a prime number")
# else:
#     print(f"{a} is a prime number")
# b=[]
# c=[]
# a=[1,2,3,4,"a","b"]
# for i in a:
#     if isinstance(i,str):
#         b.append(i)
#     else:
#         c.append(i)

# print(c)
# print(b)
# b=0
# c=0
# a=input("Enter a letter: ")
# for i in a:
#     if i.isdigit():
#         c=c+1
#     else:
#         b=b+1
# print(f" there are {b} letters")
# print(f"There are {c} digits")



# user = "Anish"
# password = "Anish123"

# a = input("Enter your Username: ")

# if a == user:
#     attempts = 3
#     while attempts > 0:
#         b = input("Enter your Password: ")

#         if b == password:
#             print(f"Welcome {user}")
#             break
#         else:
#             attempts -= 1
#             if attempts > 0:
#                 print(f"Wrong password. You have {attempts} attempts left.")
#             else:
#                 print("Account blocked. Too many wrong attempts.")
# else:
#     print("Invalid username.")

# a=int(input("ENter a number :"))
# if a%2==0:
#     print(f"The given number is even {a}")
# else:
#     print(f"The given number is odd {a}")
# a=int(input("Enter a number : "))
# fact=1
# for i in range(1,a+1):
#     fact*=i
# print(fact)

# a=[1,2,3,4,5,6,7,8]
# for i in a:
#     for x in range(1,11):
#         print(f"The table of {i} * {x} = {x*i}")
# lst=[1,2,3,4]
# for i in lst:
#     if i == 2 or i == 1:
#         print(i)
# b=1
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     if i%2==1:
#         b+=i
# print(b)
 
# b=1
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     if i%2==0:
#         b+=i
# print(b)
# count=0
# a=input("ENter a string")
# # print("The number of space is",a.count(""))
# for i in a:
#     if i ==" ":
#         count+=1
# print(count)
# b=[]
# list=[1,2,3,4]
# for i in list:
#     b.append(i**3)
# print(b)
# a = "programming"
# rev = ""

# for i in range(len(a)-1, -1, -1):
#     rev += a[i]

# print(rev)
# for i in range(50):
#     print(i)
#     if i == 7:
#         break
# a=input("ENter a string: ")
# for i in a:
#     print(i)

# a=["ram","shyam",1,2]
# for i in a:
#     if isinstance(i,str):
#         print(f"Hello {i}")

a=["ram","shyam"]
lst=[]
for i in a:
    lst.append("DR. "+i)
print(lst)
        

    



    
