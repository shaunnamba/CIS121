# def ascending_order(num1,num2=5,num3=25):
 
#     if num1>num2:
#         num1,num2=num2,num1
#     if num1>num3:
#         num1,num3=num3,num1
#     if num2>num3:
#         num2,num3=num3,num2
#     return [num1,num2,num3]

#15
# def is_negative(num):
#     if num<0:
#         return True
#     else:
#         return False
# def is_odd(num):
#     if num%2==1:
#         return True
#     else:
#         return False
    
    
# def report_negative_odds(lyst):
#     result=[]
#     for nums in lyst:
#         if is_negative(nums) and is_odd(nums):
#             result.append(nums)
#     return result
# print(report_negative_odds([100,-57,12,1,-36,-15]))

#9
# def get_indices(lyst,value=0):
#     result=[]
#     for i in range(len(lyst)):
#         if lyst[i]==value:
#             result.append(i)
#     return result
# print(get_indices([1,0,5,0,7],7))

#14
def is_two_digit_number(num):
    return num>=10 and num<=99
def report_two_digit_numbers(lyst):
    result=[]
    for num in lyst:
        if is_two_digit_number(num):
            result.append(num)
    return result
print(report_two_digit_numbers([100,23,4,57,189]))




