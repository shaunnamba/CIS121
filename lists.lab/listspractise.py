 #question 9
# def count(list_of_cards):
#     points=0
#     #iterate/loop through each of the cards
#     for card in list_of_cards:
#         if str(card) in ["10", "j", "q", "k"]:
#             points+=-1
#         elif str(card) in ["7", "8", "9"]:
#             points=0
#         elif str(card) in ["2", "3", "4", "5", "6"]:
#             points+=1
#     return points

# print(count([5,9,10,3,"j","a",4,8,5]))

def design_rug(width, length, pattern):
	result = "Your rug is:\n"
	for i in range(length -1):
		result += pattern * width
		if i < length - 1:
			result += "\t"
	return result