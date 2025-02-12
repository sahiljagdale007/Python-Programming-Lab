number = int(input("Enter the given number:"))

reverse_number = 0

while number>0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number = number // 10

print("The reverse of given number is: ",reverse_number)
    