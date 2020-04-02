try:
    #value = 10/0  # except ZeroDivisionError
    number = int(input("Enter a number: "))  # except ValueError
    print(number)
except ValueError as err:
    print("Invalid Input: ")
    print(err)
except ZeroDivisionError as err:
    print("Divided by zero: ")
    print(err)
