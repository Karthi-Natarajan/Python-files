# Fractional Part of Sum

def multiply (num,factor):
    result = 0
    for _ in range(factor):
         result += num
    return result

def subtract(a,b):
    while b > 0 :
        a -= 1
        b -= 1
    return a

def extract_integer(num):
    integer_part = 0
    while num >=1:
        integer_part += 1
        num -= 1
    return integer_part

def fraction_part(a,b):
    total = a+b
    int_part = extract_integer(total)
    frac_part = subtract(total,int_part)
    return frac_part
    

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

fract = fraction_part(a,b)

print("Fractional part:", round(fract, 4))
