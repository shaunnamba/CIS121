'''
#in python a list starts with [ and end with]
x=[]#nothing in list
lyst=['apple','banana', 3, False, 4.5, 'grapes']
#print the element of the list in position 1.

#print the portion of the list without strings
print(lyst[2:5])
x='appl'
x+='e'
print(x)
#lyst.append(element) will add an element to the end of the lyst.

print(lyst)
lyst.insert(3,'pro')
'''

#question 8
'''
def pool_time(user_grade, user_time):
    time_output=""
    if user_grade== "K":
        user_grade==0
    
    if int(user_grade)>=0 and int(user_grade)<=3:
        if user_time=='Morning':
            time_output="9AM"
        else:
            time_output="1PM"
    if int(user_grade)>=4 and int(user_grade)<=8:
        if user_time=="Morning":
             time_output="10AM"
        else:
            time_output="2PM"
    if int(user_grade)>=9 and int(user_grade)<=12:
        if user_time=='Morning':
            time_output="11AM"
        else:
            time_output="3PM"
    return time_output
    
print(pool_time(3, 'afternoon'))
'''

#question knuts
'''
def convert_knuts(knuts):
    output= ""
    galleon = knuts//493
    remaining_knuts= knuts-(galleon*493)
    sickles=remaining_knuts//29
    remaining_knuts=remaining_knuts-(sickles*29)

    if galleon>0:
        output=output+ f"Galleon: {galleon}"
    if sickles>0:
        output=output+ f"Galleon: {sickles}"
    if remaining_knuts>0:
        output=output+ f"Galleon: {remaining_knuts}"

    return output

user_input=int(input("Enter number of knuts: "))
print(f'for{user_input} knuts I van buy {convert_knuts(user_input)}')
'''

'''
lyst=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(lyst)
'''

 #Line 70 prints 'nes' from wednesday
'''
print(lyst[2][3:6])
'''

#this appends new day to the list
'''
lyst.append('Saturday')
lyst.append('Sunday')
print(lyst)
'''
#immunitable object(cant move it or change it(strings))
'''
word="apfel"
print(word)
word[2]='p'
print(word)
'''
#mutable object(lists)
'''
workday=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
print(workday)
workday[4]='Funday'
print(workday)
'''

#Write a function that takes a string as an argument, and returns a list containing
#all of the words in that string.
# the_word='Peter Piper picked a peck of pickled pepprs.'
# result= ['Peter', 'Piper' ,'picked', 'a', 'peck',  'of', 'pickled',  'peppers.']
# def get_list_with_vowels(user_word):
#     word=[]
#     #collect a word
#     built_word=''
#     vowel_count=0
#     for letter in user_word:
#         if letter ==' ':
#             #add built_word into the list if amount of vowels >= 2
#             if vowel_count>=2:
#                 word.append(built_word)
#             built_word=''
#             vowel_count=0
#             #once we have a full word, lets add it to the list of words
#         else:
#             built_word+=letter
#             if letter in 'aeiou':
#                 vowel_count+=1
#     if vowel_count>=2:
#         word.append(built_word)
#     return word















# phonebook={'matt':5073891439, 'ashley':12345}
# print(phonebook)
# #to add something to a dictionary we use name_of dictioanry[key]=value
# phonebook['waters']=789
# print(phonebook)
# #to look up a value in a dictionary we use  the name_of_dict[key]
# print(phonebook['matt'])
# for person in phonebook:
#     print(person,phonebook[person])


# def sting_to_dictionary(word):
#     string_as_list=word.split()
#     word_dictionary={}
#     for word in string_as_list:
#         if word in word_dictionary:
#            word_dictionary[word]=word_dictionary[word]+1
#         else:
#              word_dictionary[word]=1
#     return word_dictionary



#Write a function that takes a string as an argument, and returns a dictionary containing
#all of the number of times each word was used in that string.



# def get_list_alt(word):
#     words=[]
#     built_word=''
#     for index in range(len(word)):
#         if word[index]==' ' or index==len(word)-1:
#             words.append(built_word)
#             built_word=''
#         elif index ==len(word)-1:
#             built_word+=word[index]
#             words.append(built_word)
#         else:
#             built_word+=word[index]
#     return words

#print(get_list(the_word))
# print(get_list_alt(the_word))
  



'''
def skip_letter(word):
    result=[]
    for i in range(1,len(word),2):
        result.append(word[i])
    return result

print(skip_letter("banana sunday"))
'''

'''
def output_even(smaller_num, larger_num):
    result=[]
    for numbers in range(smaller_num, larger_num+1):
        if numbers%2==0:
            result.append(numbers)
    return result
print(output_even(37,1050))

def output_odd(smaller_num, larger_num):
    result=[]
    for numbers in range(smaller_num, larger_num+1):
        if numbers%2==1:
            result.append(numbers)
    return result
print(output_odd(37,1050))
'''

'''
def hailstone_seq(n):
    result=[n]
    while n !=1:
        if n%2==0:
           n= n//2
        else:
           n= n*3+1
        result.append(n)
    return result

print(hailstone_seq(25))
'''
'''
def find_factors(num):
    result=[]
    for numbers in range(1,num+1):
        if num%numbers==0:
            result.append(numbers)
    return result
print(find_factors(17))
'''
'''
def ascending_order(num1,num2,num3):
    if num1<=num2 and num1<=num3:
        if num2<=num3:
            return [num1,num2,num3]
        else:
            return [num1,num3,num2]
    elif  num2<=num1 and num2<=num3:
        if num1<=num3:
            return [num2,num1,num3]
        else:
            return [num2,num3,num1]
    else:
        if num1<=num2:
            return [num3,num1,num2]
        else:
            return [num3,num2,num1]
print(ascending_order(2,24,1))

def descending_order(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        if num2<=num3:
            return [num1,num3,num3]
        else:
            return [num1,num2,num3]
    elif  num2>=num1 and num2>=num3:
        if num1<=num3:
            return [num2,num3,num1]
        else:
            return [num2,num1,num3]
    else:
        if num1<=num2:
            return [num3,num2,num1]
        else:
            return [num3,num1,num2]
print(descending_order(2,3,1))
'''


'''
def count(cards):
    points=0
    for card in cards:
        if str(card) in ['2','3','4','5','6']:
            points+=1
        elif str(card) in ['7','8','9']:
            points+=0
        else:
            str(card) in['10','j','q','k']
            points+=-1
    return points
print(count([5,9,10,3,"j","a",4,8,5]))
'''


'''
def war_of_numbers(numbers):
    odd=0
    even=0
    for number in numbers:
        if number%2==0:
            even+=number
        else:
            odd+=number
    if odd>even:
        return "odds"
    else:
        return "evens"
print(war_of_numbers([2,8,7,5]))
'''
    



# def add_lists(lyst1,lyst2):
#     result=[]
#     for i in range(len(lyst1)):
#         result.append(lyst1[i] +lyst2[i])
#     return result
# print(add_lists([1,3,3,1],[4,3,6,1]))

# def largest_even(numbers):
#     largest=-1
#     for number in numbers:
#         if number%2==0:
#             if number>largest:
#                 largest=number
#     return largest
# print(largest_even([3,7,2,1,7,9,10,13]))

# def largest_odd(numbers):
#     largest=-1
#     for number in numbers:
#         if number%2==1:
#             if number>largest:
#                 largest=number
#     return largest
# print(largest_odd([3,7,2,1,7,9,10,13]))

# def progress_days(miles):
#     progress=0
#     for number in range(1,len(miles)):
#         if miles[number]>miles[number-1]:
#             progress+=1
#     return progress
# print(progress_days([3,4,1,2]))

# def lag_days(miles):
#     progress=0
#     for number in range(1,len(miles)):
#         if miles[number]<miles[number-1]:
#             progress+=1
#     return progress
# print(lag_days([5,3,2,1]))

# def buttons(events):
#     blank="nothing"
#     for event in events:
#         if event==blank:
#             blank="nothing"
#         else:
#             blank=event
#     return blank
# print(buttons(["dislike","like"]))

# def get_indices(lyst,item):
#     result=[]
#     for numbers in range(1,len(lyst)):
#         if lyst[numbers]==item:
#             result.append(numbers)
#     return result
        
# print(get_indices([1,5,5,2,7],7))


# def list_of_multiples(num,length):
#     result=[]
#     for i in range(1,length+1):
#         result.append(i*num)
#     return result
# print(list_of_multiples(7,5))


def is_acronym(s,words):
    acronym=""
    for word in words:
        acronym+=word[0]
    return acronym==s
print(is_acronym("abc",["alice","bob","charlie"]))




