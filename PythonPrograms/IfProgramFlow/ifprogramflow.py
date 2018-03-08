# name = input("Please enter your name: ")
# age = input("How old are you, {0}? ".format(name))
# print(age)
# #                                           ^ in this case age is a string

# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print("{0} is {1} years old.".format(name, age))
# #                                           ^ in this case age is an integer
#
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {} years.".format(18 - age))

print("Please guess a number between 1 and 10: ")
guess = int(input())


#intro to elif

# if guess < 5:
#     print("Please guess higher.")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you've guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly!")
# elif guess > 5:
#     print("Please guess lower.")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you've guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly!")
# else:
#     print("You got it on your first guess!")

#Removing duplicate code

if guess != 5:
    if guess < 5:
        print("Please guess higher.")
    else:
        print("Please guess lower.")

    guess = int(input())
    if guess == 5:
        print("Well done, you've guessed it!")
    else:
        print("Sorry, you have not guessed correctly!")
else:
    print("You got it on your first guess!")