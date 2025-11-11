#write a program that takes integers from the user and adds them together
#until they type done. return the sum

# total=0
# user_input=input('Enter a number or type done')
# while user_input!='done':
#     user_number=float(user_input)
#     total+=user_number
#     user_input=input('enter a number or type done')

# print(f'total= {total}')




from random import randint
#var_name=open('whatever your file name is .ext','w')
my_file=open('numbers.txt','w')

for index in range(0,100):
    number=randint(50,250)
    my_file.write(f'{number}\n')

my_file.close()
