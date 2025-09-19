# Created by Shaun Namba
'''''
light_color= input("Enter a light color: ")
if light_color=="green":
    print("Go")
elif light_color=="yellow":
    print("Yield")
elif light_color=="red":
    print("Stop")
else:
    print("Invalid color")
    '''
# question 5
'''
num1= int(input("Enter first number: "))
num2=int(input("Enter second nummber: "))
num3=int(input("Enter third number: "))
if num1<=num2<=num3:
    print(num3,num2,num1)
elif
    '''
# Question 7
'''
kunts=int(input("Number of kunts: "))
sickle =int(kunts /29)
Kunts= kunts-(sickle*29)
'''

# question 8 and 9
'''
# question 8 and 9
num1=int(input())
num2=int(input())
num3=int(input())
if num1>=num2 and num1>=num3:
    largest= num1
elif num2>=num1 and num2>=num3:
    largest=num2
else:
    largest=num3
print(largest)Elf
'''
# Question 10
'''
race=input('')
char_class=input('')
health_points= -1

if race=='Elf':
    if char_class=='Warrior':
        health_points=150
    elif char_class=='Bard':
        health_points=75
    elif char_class=='Wizard':
        health_points=25
    else:
        health_points= 'None'
    print(health_points) 
elif race=="Ogre":
    if char_class=='Warrior':
        health_points=100
    elif char_class=='Bard':
        health_points=100
    elif char_class=='Wizard':
        health_points=50
    else:
        health_points="None"
    print(health_points)
'''
# Question 11
'''
from random import randint
value = randint(0,1)
guess= input('')
if guess==0:
    results='tails'
else:
    results='heads'
if guess==results:
    print("Correct")
else:
    print("Incorect")
'''
'''
# question 12
num1=int(input("Pick a number"))
num2=int(input("Pick a number"))
num3=int(input("Pick a number"))
if num1==num2==num3:
    print("Nmbers entered three times")
elif num1==num2 or num1==num3 or num3==num2:
    print("Number entered two times")
else:
    print('Unique')
'''
'''
grade= int(input("Enter your grade: "))
time= input("Enter time: ")
if grade=="k"or grade==1 or grade==2 or grade==3:
    if time=='morning':
        print("9am")
    else:
        print("1pm")
elif grade==4 or grade==5 or grade==6 or grade==7 or grade==8:
     if time=='morning':
        print("10am")
     else:
        print("2pm")
else:
     if time=='morning':
        print("11am")
     else:
        print("3pm")
'''
'''
pick1=int(input("pick side: "))
pick2=int(input("pick side: "))
pick3=int(input("pick side: "))
if pick1==pick2==pick3:
    print("equilateral")
elif pick1==pick2 or pick2==pick3 or pick3==pick1:
    print("isosceles")
else:
    print("scalene")
'''
age=int(input())
athletism=input("goal?: ")
if age>=20 and age<=39:
    if athletism=='above average':
        print("47-72")
    else:
        print("73-93")
elif age<=59:
    if athletism=='above average':
        print("46-71")
    else:
        print("72-94")
else:
    if athletism=='above average':
        print("45-70")
    else:
        print("71-97")





