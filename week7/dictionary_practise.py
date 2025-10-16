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


menu={"burger":10,"fries":4,"soda":3}

def contents(menu):
    output=""
    for food, price in menu.items():
        output+=f"{food} costs {price}"
    return output
print(contents(menu))

                 
  


