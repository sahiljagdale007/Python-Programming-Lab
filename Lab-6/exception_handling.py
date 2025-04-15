# Program Name: Divide by Zero (Simple Version)

# try:
#     a = int(input("Enter numerator: "))
#     b = int(input("Enter denominator: "))
#     print("Result:", a / b)
#     
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
#     
    

# Program Name: Divide by Zero (with try, except, finally)

# try:
#     a = int(input("Enter numerator: "))
#     b = int(input("Enter denominator: "))
#     print("Result:", a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print("Program execution completed.")


# Program Name: Basic File Handling

# Writing to a file
try:
    file = open("example.txt", "w")  # "w" means write mode
    file.write("My name is sahil ashok jagdale. This is the name of father\n")
    file.write("Learning Python is fun!")
except Exception as e:
    print("An error occurred while writing to the file:", e)
finally:
    file.close()
    print("File writing completed.")

# Reading from a file
try:
    file = open("example.txt", "r")  # "r" means read mode
    content = file.read()
    print("\nFile content:")
    print(content)
except Exception as e:
    print("An error occurred while reading the file:", e)
finally:
    file.close()
    print("File reading completed.")

# Program Name: Temperature Measurement

# try:
#     temp_celsius = float(input("Enter temperature in Celsius: "))
#     temp_fahrenheit = (temp_celsius * 9/5) + 32
#     print(f"Temperature in Fahrenheit: {temp_fahrenheit}")
# except ValueError:
#     print("Invalid input! Please enter a number.")
# finally:
#     print("Temperature measurement completed.")


#program

# Program Name: Add String and Integer

# try:
#     s = input("Enter a name: ")
#     n = int(input("Enter an age: "))
#     result = s + n  # This will cause an error
#     print("Result:", result)
# except TypeError:
#     print("Error: Cannot add a string and an integer directly!")
# except ValueError:
#     print("Error: Please enter a valid integer.")
# finally:
#     print("Program completed.")

# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6, 7]
# lst = [0, *lst_one, *lst_two]
# print(lst)