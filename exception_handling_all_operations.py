try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Division:", a/b)

    l = [10,20,30]
    index = int(input("Enter list index: "))
    print("Value:", l[index])

    name = {"name":"Venky"}
    key = input("Enter dictionary key: ")
    print("Value:", name[key])

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid number")

except IndexError:
    print("Error: List index out of range")

except KeyError:
    print("Error: Key not found")

except Exception as e:
    print("Unknown Error:", e)

else:
    print("Program executed successfully")

finally:
    print("Program finished")