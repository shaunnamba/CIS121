'''
#write a code to determine number of letters in word
word='Hello world'
count=0
for letter in word:
    if letter!=' ':
        count+=1
print(count)
'''
'''
#write a code to determine the number of vowels in word


def vowel_counter(passed_word):
    count=0
    for letter in passed_word:
        if letter=='a' or letter=='e' or letter=='o' or letter=='u' or letter=='i' or letter=='y':
            count+=1
    print(f"the vowel count in '{passed_word}' is {count}")

word1='hello world'
word2='apples and bananas'
word3='happy times'

vowel_counter('hello world')
vowel_counter('apples and bananas')
vowel_counter('happy times')
'''

def calc(number):
    number+=2
    number*=4
    return number  # to give something back

def add_ten(number):
    number+=10
    return number


result1= add_ten(calc(10))
result2=add_ten(result1)
print(result1)
result=10
for number in range(0,10):
    result=add_ten(result)

#starting with the value 10 add 2 then multiply by four take the result and add 2 to it, then multiply by four again.
#call he function calc 10 times
#call the function calc 10 times



#write a function that returns a product of two arguments
def product(num1,num2):
    product = num1*num2
    return product
print(product(4,3))