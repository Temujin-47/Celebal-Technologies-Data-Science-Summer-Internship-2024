# Simple Calculator

# Add
def add(num1, num2):
    return num1 + num2

# Subtract


def sub(num1, num2):
    return num1 - num2

# Multiplication


def mul(num1, num2):
    return num1 * num2

# Division


def div(num1, num2):
    return num1 / num2


# Menu
while True:
    select = int(input(
        "Select operations form 1.Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Exit :"))

    if select == 5:
        print("Exit initiated!")
        break

    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if select == 1:
        print(number_1, "+", number_2, "=",
              add(number_1, number_2))

    elif select == 2:
        print(number_1, "-", number_2, "=",
              sub(number_1, number_2))

    elif select == 3:
        print(number_1, "*", number_2, "=",
              mul(number_1, number_2))

    elif select == 4:
        print(number_1, "/", number_2, "=",
              div(number_1, number_2))
    else:
        print("Invalid input")
