# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
# define functions
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mult(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
# take user input
print("Select an operator")
print("1.Add")
print("2.Sub")
print("3.Mult")
print("4.Div")

choice = input("add/sub/mult/div: ")

num1 = int(input("First number:"))
num2 = int(input("Second number:"))

if choice == 'add':
    print(add(num1, num2))
elif choice == 'sub':
    print(sub(num1, num2))
elif choice == 'mult':
    print(mult(num1, num2))
elif choice == 'div':
    print(div(num1, num2))
else:
    print("Invalid input")
