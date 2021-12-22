# # 1 happy number
# def happy_number(number):
#     not_one = True 
#     while not_one is True:
#         # numbers multiply to the their square root and then add up to each other
#         index_zero = int(number[0]) * int(number[0])
#         index_one = int(number[1]) * int(number[1])
#         total = (index_one) + (index_zero)
#         # made total a string because i kept on getting an error
#         total = str(total)
#         print(total)
    
#         if total == 1 or total == 10 or total == 100 or total == 1000 or total == 10000:
#             print(f'{number} is a happy Number!') 

#         else:
        
#             while not_one is True:
#                 total_index_zero = int(total[0]) * int(total[0])
#                 total_index_one = int(total[1]) * int(total[1])
#                 total = total_index_zero + total_index_one
#                 print(total)
#                 break

#             # added while loop to add numbers that hasn't got to one yet
            
# user_number = input('pick a number... ')  
# calling_function = happy_number(user_number)



number = '19'
not_one = True
while not_one is True:
    index_zero = int(number[0]) * int(number[0])
    index_one = int(number[1]) * int(number[1])
    total = index_zero + index_one 
    number = total
    number = str(number)
