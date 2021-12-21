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
# prints the number of times a letter is repeated before it changes to a different letter 
def compressed(word):
    index = 0
    compress = '' 
    len_of_word = len(word)
    
    while index != len_of_word:
        count = 1

         ####                               checking if both values are true  
        while (index < len_of_word - 1) and (word[index] == word[index + 1]):
            # adding 1 to count to count the number of times a word was repeated and adding 1 to index to move to the next index number
            count = count + 1
            index = index + 1
        if count == 1:
            # adding a letter that was only used once
            compress += str(word[index])
        else:
            compress += str(word[index] + str(count))
        # index number added by one to grab the next letter
        index = index + 1 
    return compress

print(compressed(user_choice_of_letters)) 

# 4 bonus challenge: Palindrome 
user_input = input('Can you do a Palindrome!? ')
def is_palindrome(word):
    # reversing the word
    reversed_word = word[::-1]
    # checking if orignal value is the same as the reversed value 
    if word == reversed_word:
        print(word, "is a palindrome!")
    else:
        print(word, "is not a palindrome :(")

is_palindrome(user_input)