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
user_word= input("")
for letter in range(1,len(user_word),1):
    print(user_word[letter])