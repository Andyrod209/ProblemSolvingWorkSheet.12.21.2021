# 1 writing a Reverse a string
normal_string = "Master Cheif"
print(normal_string)
# using :: with -1 moves to the back of the string
reversed_string = normal_string[::-1]
print(reversed_string) 

# 2 Capitalize letter 
user_name = input('What is your full name? ')
# using title() will make the first letter of each word capitlize
user_name = user_name.title()
print(user_name)

#  compress a srting of characters
user_choice_of_letters = input('Type as many letters as you want... ')
user_choice_of_letters