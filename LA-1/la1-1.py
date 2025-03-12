#Write a python program to count vowles in string of your name

name = input("Enter your name: ")
vowels = "aeiouAEIOU"
count = 0

for char in name:
    if char in vowels:
        count += 1

print("Number of vowels:", count)