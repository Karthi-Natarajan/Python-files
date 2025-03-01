#Extraction of middle digit

num = input("Enter a 4 digit number :")

num_value = 0

#manually converting String to Integer

for digit in num :
    num_value = num_value * 10 + (ord(digit)-ord('0'))
    

thousands = num_value // 1000
remaining =  num_value - (thousands * 1000)

hundreds = remaining // 100
remaining = remaining - (hundreds * 100)

tens = remaining // 10
remaining = remaining - (tens * 10)

print(hundreds * 10 + tens)


# In Built-in function

num =input("Enter the 4 digit number")
print(num[1:3])
