'''
larger=int(input())
smaller=int(input())
count=-1
while larger >smaller:
    larger/=2
    count+=1
    print(larger)
print(count)
'''
'''
#question 2
user_word= input("")
result_word=""
for letter in range(1,len(user_word),2):
    print(user_word[letter])
    '''
#question 3
'''
for number in range(37, 1051):
    if number%2==0:
        print(number)
'''
'''
word=""
user_letter=""
while user_letter !='done':
    user_letter=input("Enter a letter(or type done): ")
    word+=user_letter
print(word)
'''

'''
count=0
while True:
    user_num=int(input("enter an integer: "))
    if user_num<0:
        break
    count+=user_num
print(count)
'''
'''
num=int(input("Enter a number: "))

for i in range(1, num+1):
    if num% i==0:
        print(i, end=" ")
'''

width=int(input("Enter a width: "))
length=int(input("Enter a length: "))
pattern=(input("Enter a pattern: "))

for i in range(length):
    for w in range(width):
        print(pattern, end="")
    print()

'''
user_num=int(input("Enter a number: "))
largest=-1
while True:
    user_num=int(input("Enter a number: "))
    if user_num<0:
        break
    if user_num%2==0:
        if user_num>largest:
            largest=user_num
print(largest)
'''
'''
count=0
user_num=int(input("Enter number: "))
for i in range(1, user_num+1):
    square=i**2
    print(square, end=", ")
    count+=square
print(count)
'''   

    