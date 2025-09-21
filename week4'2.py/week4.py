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
    result_word+=word[i]
    '''
#question 3
'''
for number in range(37, 1051):
    if number%2==0:
        print(number)
'''
word=""
user_letter=""
while user_letter !='done':
    user_letter=input("Enter a letter(or type done): ")
    if user_letter!="done":
        word+=user_letter
print(word)


    
