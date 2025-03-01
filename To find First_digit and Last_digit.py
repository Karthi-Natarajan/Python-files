# To  print First_digit and Last_digit

num = input("Enter a 3 digit number: ")
num_value = 0
for digit in num :
    num_value = num_value*10 + (ord(digit) - ord('0'))

last_digit = num_value
while last_digit >= 10:
    last_digit -= 10

first_digit = num_value
while first_digit >= 10:
    first_digit //= 10

print(first_digit,last_digit)

#In Built-in function

num = int(input("Enter a 3 digit number: "))
print ( num % 10 , num // 100 )
