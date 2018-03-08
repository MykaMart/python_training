age = 24
print("My age is " + str(age) + " years old.")
#                        ^ js => age.tostring()

print("My age is {0} years old.".format(age))

longmonth = "31"

print("There are " + longmonth + " days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}.".format(31, "January", "March", "May", "July", "August", "October", "December"))

# String Replacement Fields
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}.".format(31, "January", "March", "May", "July", "August", "October", "December"))

print("""January: {2}
February: {0}
March: {2}
April: {1}
June: {1}
July: {2}
August: {2}
September: {2}
October: {2}
November: {1}
December: {0}""".format(28, 30, 31))

# Python 2 Only

print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d, and cubed is %4d" %(i, i**2, i**3))
#              ^2 spaces width used for formatting     ^4 spaces width used for formatting

print("Pi is approximately %12.50f" % (22/7))
#                              ^spaces width after the decimal point


# Width using Python 3 replacement fields

for i in range(1, 12):
    print("No. {0:2} squared is {1:4}, and cubed is {2:4}".format(i, i**2, i**3))

print("Pi is approximately {0:12.50}".format(22/7))

print("--------------------------------------------")

#Left Justified width
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4}, and cubed is {2:<4}".format(i, i**2, i**3))


#Replacement positions can be inferred

for i in range (1, 12):
    print("no. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))

