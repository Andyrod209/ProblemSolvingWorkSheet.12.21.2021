# 1 happy number
def happy_number(number):
    count = 1
    not_one = True 
    while not_one is True:
        index_zero = int(number[0]) * int(number[0])
        index_one = int(number[1]) * int(number[1])
        
        total = index_zero + index_one 
        number = total
        number = str(number)
        if number == '1' or number == '10' or number == '100' or number == '1000' or number == '10000':
            print(f'{user_number} is a happy number!')
            break
        elif number == number:
            count += 1
            if count == 15:
                print(f'{user_number} is a sad number')
                break

        
            
user_number = input('pick a number... ')  
calling_function = happy_number(user_number)




    
