#Write a python program to find prime numbers between 0 - 50

for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")