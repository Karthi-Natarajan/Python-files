# Sum of Digits

num = int(input("Enter the number : "))
count =0
while num > 0:
    count += num%10
    num //= 10

print("sum_digits",count)


# In Built-in function

num = input("Enter the number : ")
sum_digit=sum(int(digit) for digit in str(num))
print("sum_digits",sum_digit)
