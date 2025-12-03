# Question No 1

num1=int(input("Enter a Number1: "))
num2=int(input("Enter a Number2: "))
num3=int(input("Enter a Number3: "))

if num1 == num2 == num3:
    print("The numbers are equal")
elif num1 > num2 and num1 > num3:
    print(f"Number 1 is greater {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Number 2 is greater {num2}")
elif num3 > num2 and num3 > num1:
    print(f"Number 3 is greater {num3}")
else:
    print(f"The vaule you have is {num1},{num2},{num3}")

    #Question no 2

month = int(input("Enter a month from (1-12):"))
dict={
   1 : "January", 
   2 : "February", 
   3 : "March", 
   4 : "April", 
   5 : "May", 
   6 : "June", 
   7 : "July", 
   8 : "August", 
   9 : "September", 
   10 : "October", 
   11 : "November",
   12 : "December"

}
if month in dict:
    print(dict[month])


    # Question no 3

num1=int(input("ENter a Number"))
num2=int(input("ENter second a Number"))
num=num1
num1=num2
num2=num
print(f'num 1:{num1}')
print(f'num 2:{num2}')

    # Question no 4

age=int(input("Enter your age:"))
is_membership =eval(input("Do you have membership enter True or False"))
if is_membership :
    if age>13 and age<=60:
        print("The price of the ticket is 150")
    elif age<=12 and age>1:
        print("You can get a Ticket for free")
else:
    if age<=12 and age>1:
        print("You can get a Ticket for free")
    elif age>=60 and age<110:
        print("The price for ticker is 100")
    elif age>=13 and age<61:
        print("The price for ticker is 200")
    else:
        print("Invalid")

#     # Question no 5

units = int(input("Enter electricity usage in units: "))

if units < 100:
    cost = units * 5

elif units <= 300:
    cost = 100 * 5
    cost += (units - 100) * 8

else: 
    cost = 100 * 5
    cost += 200 * 8
    cost += (units - 300) * 10

print(f"Total electricity bill: Rs {cost}")
        
        # Question 6
player1=input("Input Rock Paper or Scissors").lower()
player2=input("Input Rock Paper or Scissors").lower()
if player1==player2:
    print("its a tie")
elif player1 == "rock":
    if player2=='scissors':
        print('player1 won the game')
    else:
        print('player2 won the game')
elif player1 == "paper":
    if player2=='rock':
           print('player1 won the game')
    else:
        print('player2 won the game')

elif player1=='scissors':
    if player2=='paper':
           print('player1 won the game')
    else:
        print('player2 won the game')
else:
    print('invalid input enter (paper, scissors and rock only)')

      # Question 7
class1=int(input("Enter total students of class 1"))
class2=int(input("Enter total students of class 2"))
class3=int(input("Enter total students of class 3"))
total = class1+ class2+ class3
seat = total/2
print(f"The total seat needed is {seat}")

      # Question 8
lift = 5
floor=int(input("Enter a floor:"))
if lift<floor:
    print("The lift needs to go up")
elif lift>floor:
    print("The lift needs to go down")
elif lift==floor:
    print("The lift needs to be at current location")

else:
    print("Invalid")
    
 # Question 9
num=int(input("Enter a Number"))
if num>0:
    if num%2==0:
        print("The Number is even")
    else:
        print("The Number is odd")
else:
    print("The number is neagtive")

 # Question 10
num1=int(input("Enter a Number"))
num2=int(input("Enter a Number"))
if num1 == num2:
    if num1>0:
        print("The number is positive and equal")
    elif num1 == 0:
        print("The number is zero and equal")
    else:
        print("The number is Negative and equal")
elif num1<num2:
    print("The num2 is greater tha num1 and equal")
elif num2<num1:
    print("The num1 is greater tha num2 and equal")
else:
    print("Invalid")

#  Question 11

a=int(input("Enter a Number"))
if a% 5==0 and a % 3 == 0:
  print("fizz buzz")
elif a% 5==0:
  print("fizz")
elif a% 3==0:
  print("Buzz")
else:
  print(a)

# Question 12
import random 
a=[0,1,2,3,4,5]
b=random.choice(a)
if b == 0:
    print("Flamingos turn pink from eating shrimp.")
elif b ==1:
    print("The only food that doesn't spoil is honey.") 
elif b ==2:
    print("Shrimp can only swim backwards.") 
elif b ==3:
    print("A taste bud's life span is about 10 days.") 
elif b ==4:
    print("It is impossible to sneeze while sleeping.") 
else:
    print("It is illegal to sing off-key in North Carolina.") 

# Question 13
membership=eval(input("Do you have membership True or False"))
a=int(input("Enter the Total amount:"))
if membership==True:
  if a>=10000:
    discount=0.2*a
    print("The total cost after discount is",a - discount)
  else: 
     print(f"No discount{a}")
else:
   if a>=10000:
    discount=0.1*a
    print("The total cost after discount is",a-discount) 
   else:
       print(f"No discount{a}")

# Question 14
weight=int( input("Enter Your weight"))
planet=int(input("enter a Number for planet"))
if planet ==1:
  des=weight*0.38
  print(f"Mercury{des}")
elif planet == 2:
  des=weight*0.91
  print(f"Venus{des}")
elif planet == 3:
  des=weight*0.38
  print(f"Mars{des}")
elif planet == 4:
  des=weight*2.53
  print(f"Jupiter{des}")
elif planet == 5:
  des=weight*1.07
  print(f"Satrun{des}")
elif planet == 6:
  des=weight*0.89
  print(f"Uranus{des}")
elif planet == 7:
  des=weight*1.14
  print(f"Neptune{des}")
else:
  print("Invaild")

# Question 15

a=int(input("Enter your marks 1: "))
b=int(input("Enter your marks 2: "))
c=int(input("Enter your marks 3: "))
d=int(input("Enter your marks 4: "))

total=a+b+c+d
percentage=total/4
if percentage>=70 and percentage<=100:
  print("distinction")
elif percentage>=60 and percentage<=70:
  print("first")
elif percentage>=40 and percentage<=60:
  print("Pass")
elif percentage>=0 and percentage<=39: 
  print("fail")
else:
  print("Invaild")

#   Question 16
a=int(input("Enter your bike price"))
if a>=100000:
  print("The tax for ",0.15*a)
elif a>50000 and a<=100000:
  print("Tax",0.10*a)
elif a<=5000 and a>=0:
  print("Tax",0.5*a)
else:
  print("Invalid")
b= int(input("enter your salary"))
if a>=11:
  print("Bonus ",b*100/10)
elif a>6 and a<=10:
  print("Bonus",b*100/8)
elif a<=6 and a>=0:
  print("Bonus",b*100/5)
else:
  print("Invalid")

# Question 17
a= int(input("enter your work year"))
b= int(input("enter your salary"))
if a>=11:
  print("Bonus ",b*100/10)
elif a>6 and a<=10:
  print("Bonus",b*100/8)
elif a<=6 and a>=0:
  print("Bonus",b*100/5)
else:
  print("Invalid")

# Question 18
sub=int(input("Enter your marks:"))
if sub>=90 and sub<=100:
    print("congrates")
elif sub<=89 and sub>=50:
    print("suggest improvement")
elif sub<=49 and sub>=1:
    print("Retake the program")
else:
    print("Invalid marks")

# Question 19
age=int(input("Enter yoyr age:"))

if age>=18:
    degree=eval(input("Do you have a degree enter True or False:"))
    work=int(input("Enter your experince:"))
    if degree == True:
        if work>=3:
            print("High Eligible")
        elif work<=2 and work>=1:
            print("Eligible")
        else:
            print("Under Review")
else:
    print("Not Eligible")
Notes
 random.randint(0,5)
 random.ranrage(0,5)
# Question 20

age = int(input("Enter your age: "))

if age >= 18 and age <= 30:
    gender = input("Enter M for male and F for female: ").lower()

    if gender == "m":
        print("Your wage is 700")
    elif gender == "f":
        print("Your wage is 750")
    else:
        print("Invalid gender input")

elif age > 30 and age <= 40:
    gender = input("Enter M for male and F for female: ").lower()

    if gender == "m":
        print("Your wage is 800")
    elif gender == "f":
        print("Your wage is 850")
    else:
        print("Invalid gender input")

else:
    print("You can't work now")

    # Question 21
iscardvalid = True
balance=50000
pin=int(input("Enter your pin: "))
if iscardvalid:
    if pin == 123:
        option=int(input("Enter a Number 1. Withdraw2. Check Balance 2. Exit"))
        if option == 1:
            amt=int(input("enter a amount : "))
            print(balance-amt)
        elif option == 2:
            print(f"Your current balance is {balance}") 
        elif option == 3:
            print("Thanks for visiting!")
    else:
        print("The pin was Invalid, Please Try again !")
else:
    print("The card was not vaild!!")

# Question 22
print("Welcome To the Magic Forest!!")
place=input("want to go north or south : ").lower()
if place == 'south':
    print("Game over")
elif place == 'north':
    a=input('''want to "cross the river" or "follow the path"''').lower()
    if a == 'cross the river':
        print("Game Over")
    elif a == 'follow the path':
        b=input("fairy,ogre,or elf").lower()
    else:
        print("Please insert a correct value ")
        if b == 'elf':
            print("You win!")
        elif b =='fairy' or b=='ogre' :
            print("Game over")
        else:
            print("Please insert a correct value ")
else:
    print("Please insert a correct value ")
#  Question 23 
print("Welcome To the haunted House!!")
place=input("want to go Upstairs or Downstairs : ").lower()
if place == 'downstairs':
    print("Game over")
elif place == 'upstairs':
    a=input('''"enter the room" or "stay outside"''').lower()
    if a == 'enter the room':
        print("Game Over")
    elif a == 'stay outside':
        b=input("""ghost", "vampire", or "werewolf""").lower()
    else:
        print("Please insert a correct value ")
        if b == 'werewolf':
            print("You win!")
        elif b =='ghost' or b=='vampire' :
            print("Game over")
        else:
            print("Please insert a correct value ")
else:
    print("Please insert a correct value ")