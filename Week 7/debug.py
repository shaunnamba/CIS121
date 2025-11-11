'''
total=0
user_number=input("enter a number or type q to end")

while user_number!='q':
    total+=int(user_number)
    user_number=input("enter a number or type qto end")

print(f'total ={total}'
'''

def string_to_list_with_vowels(word):
    words=[]
    built_word=''
    vowel_count=0
    for letter in word:
        if letter== ' ':
            words.append(built_word)
        else:
            built_word= ''
            built_word+=letter
    return words

my_word= 'peter piper picked a peck of pickles pepprs'
print(string_to_list_with_vowels(my_word))