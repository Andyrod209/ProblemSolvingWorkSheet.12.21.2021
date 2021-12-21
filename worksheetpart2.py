# 1 happy number
def happy_number(number):
    # using a while loop to keep on multiplying 
    not_one = True
    while not_one is True:
        # figure out how to end the loop if it goes to 1
        index_zero = int(number[0]) * int(number[0])
        index_one = int(number[1]) * int(number[1])
        total = (index_one) + (index_zero)
        print(total)

    # loop_number = True
    # while (loop_number):
    #     if
calling_function = happy_number('19')

