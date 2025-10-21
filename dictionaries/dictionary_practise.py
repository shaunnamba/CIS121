# def get_names(names_dict):
#     result=[]
#     for key in names_dict:
#         names=names_dict[key]
#         result.append(names)
#     return result
# print(get_names({"01475": "steve", "87469":"alice","654123":"bob"}))

# def find_oldest(people):
#     oldest=-1
#     name=""
#     for key in people:
#         age=people[key]
#         if age > oldest:
#             oldest=age
#             name=key
#     return name
    
# print(find_oldest({"emma":71,"jack":45,"olivia":82}))


# def letter_count(word):
#     count_dict={}
#     for letter in word:
#         if letter in count_dict:
#             count_dict[letter]+=1
#         else:
#             count_dict[letter]=1
#     return count_dict
# print(letter_count("hello"))

# receipt={"Side Salad":6,"Chicken":12, "Cookie":3}

# def total_cost(receipt):
#     sum=0
#     for item in receipt:
#         sum+=receipt[item]
#     return sum
# print(total_cost(receipt))


# menu={"burger":10,"fries":4,"soda":3}

# def contents(menu):
#     output=""
#     for food, price in menu.items():
#         output+=f"{food} costs {price}"
#     return output
# print(contents(menu))

# def is_isogram(word):
#    for i in range(len(word)):
#       for j in range(i+1,len(word)):
#         if word[i]==word[j]:
#             return False
# return True
        
# print(is_isogram("algorissm"))

# def find_unique(numbers):
#     for i in range(len(numbers)):
#         unique=True
#         for j in range(len(numbers)):
#             if i!=j and numbers[i]==numbers[j]:
#                 unique=False
#                 break
#         if unique:
#             return numbers[i]
        
# print(find_unique([1,2,2,3,3]))

# def return_unique(numbers):
#     result=[]
    
#     for j in range(len(numbers)):
#         unique=True
#         for i in range(len(numbers)):
#             if i!=j and numbers[i]==numbers[j]:
#                 unique=False
#                 break
#         if unique:
#             result.append(numbers[j])
#     return result
# print(return_unique([1,9,9,8,2,2]))

# def get_names(names_dict):
#     result=[]
#     for id in names_dict:
#         names=names_dict[id]
#         result.append(names)
#     return result
# print(get_names({"01475": "steve", "87469":"alice","654123":"bob"}))

# def find_oldest(people):
#     oldest=-1
#     name=""
#     for names in people:
#         age=people[names]
#         if age>oldest:
#             oldest=age
#             name=names
#     return name
# print(find_oldest({"emma":71,"jack":45,"olivia":82}))

# def letter_count(word):
#     result={}
#     for letter in word:
#         if letter in result:
#             result[letter]+=1
#         else:
#             result[letter]=1
#     return result
# print(letter_count("hello"))

# def min_grade(exams):
#     min_score=None
#     course=""
#     for key in exams:
#         score=exams[key]
#         if min_score is None or score<min_score:
#             min_score=score
#             course=key
#     return course
# print(min_grade({"physics":82,"math":65,"hist":75,"bio":95}))
                 
# def find_youngest(people):
#     youngest=None
#     name=""
#     for names in people:
#         age=people[names]
#         if youngest is None or age<youngest:
#             youngest=age
#             name=names
#     return name
# print(find_youngest({"emma":71,"jack":45,"olivia":82}))
 
# receipt={"side salad":6,"Chicken parm":12,"cookie":3}

# def total_cost(receipt):
#     sum=0
#     for food in receipt:
#         sum+=receipt[food]
#     return sum
# print(total_cost(receipt))

# menu={"burger":10, "fries":4,"soda":3}

# def cost(menu):
#     output=""
#     for food,price in menu.items():
#         output+=f"{food} cost {price} \n"
#     return output
# print(cost(menu))


# def count_repetitions(elements):
#     output={}
#     for i in elements:
#         if i in output:
#             output[i]+=1
#         else:
#             output[i]=1
#     return output
# print(count_repetitions(["cat","cat","cow","cow","cow"]))
        
# def item_purchase(store,wallet):
#     afford=[]
#     for item,price in store.items():
#         if price<=wallet:
#             afford.append(item)
#     return afford

# def total_sales(sales):
#     sum=0
#     for items in sales:
#         sum+=sales[items]
#     return sum
# print(total_sales({"laptop":5,"phone":10,"tablet":3}))

# def high_earners(employee_salaries,given):
#     result=[]
#     for name,salary in employee_salaries.items():
#         if salary>=given:
#             result.append(name)
#     return result
# print(high_earners({"alice":50000,"bob":75000,"charlie":100000},60000))

# calories={"apple":95,"banana":105,"orange":62,"grape":3,"pear":102}

# def total_calories(fruits):
#     total=0
#     for fruit in fruits:
#         if fruit in calories:
#             total+=calories[fruit]
#     return total
# print(total_calories(["apple","banana","orange"]))

def majority_element(nums):
    numbers=None
    count=0
    for num in nums:
        if count==0:
            numbers=num
        if num==numbers:
            count+=1
        else:
            count-=1
    return numbers
print(majority_element([3,3,2,2,2,2,3]))








