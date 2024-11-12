"""Input is the function which is used to take user input from the command line And  By Default it takes input as string"""

# takeInput = input("Enter Your Name: ")
# print("Hello " + takeInput)
# print(type(takeInput))

"""How TO Take input as a user and convert it into integer"""

# takeInput = int(input("Enter Your Age: "))
# print(type(takeInput))

# if takeInput % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
"""
Lets Take an Example of if else statement We Will Make A function Which takes age of the user as input and 
returns whether the person is eligible for voting or not.
if the age is odd then person will be sent to camp a or else b 
"""


def checkAge(age):
    if age <= 0 | age > 150:
        print("Please Enter The Valid Age")
    elif age < 18:
        print("You Are Not Eligible For Voting")
    elif age >= 18:
        print("You Are Eligible For Voting")
        if age % 2 == 0:
            print("You are given camp a for voting")
        else:
            print("You are given camp b for voting")


def main():
    while True:
        try:
            x = int(input("Enter Your Age: "))
            checkAge(x)
            break
        except ValueError:
            print("Please Enter The Valid Age")


if __name__ == "__main__":
    main()
