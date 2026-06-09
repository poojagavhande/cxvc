#if else program in python


"""

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

"""


"""
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


"""



"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")
"""


"""
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

"""

"""
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
"""



"""
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
"""

"""
ch = input("Enter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
"""

"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is largest")
elif b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")
"""


"""
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
"""



"""
num = int(input("Enter a number: "))

if 1 <= num <= 100:
    print("Within range")
else:
    print("Out of range")
"""



#loop


"""
for i in range(1, 11):
    print(i)
"""


"""
for i in range(10, 0, -1):
    print(i)

"""
"""
for i in range(2, 21, 2):
    print(i)

"""

"""
for i in range(1, 21, 2):
   print(i)


"""
"""
sum =0

for i in range(1, 101):
    sum += i

print("Sum =", sum)

"""


"""
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
"""
"""
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

"""
"""
text = input("Enter a string: ")

for ch in text:
    print(ch)
"""




"""
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)
"""




"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
"""





  #while loop


"""   
 i = 1

 while i <= 10:
    print(i)
    i += 1
"""

"""
i = 10

while i >= 1:
    print(i)
    i -= 1

"""


"""
i = 2

while i <= 20:
    print(i)
    i += 2
"""


"""
i = 1

while i <= 20:
    print(i)
    i += 2
"""




"""
i = 1
sum = 0

while i <= 100:
    sum += i
    i += 1

print("Sum =", sum)

"""



"""
num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
"""



"""
num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Digits =", count)
"""



"""
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reverse =", rev)
"""



"""
num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial =", fact)


"""


password = "admin123"

while True:
    user = input("Enter password: ")

    if user == password:
        print("Correct Password")
        break
    else:
        print("Wrong Password")



