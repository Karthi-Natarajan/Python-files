# Most Significant Digit

num = int(input("Enter the Number : "))

while num > 10:
    num //= 10

print("MSB : ",num)



