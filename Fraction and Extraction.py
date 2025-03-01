# Fraction Extraction and Summation

def extract_part(num):
    integer_part=0
    while num >=1:
        num -=1
        integer_part +=1
    return num

num1 = float(input("Enter the number :"))
num2 = float(input("Enter the number :"))

frac1 = extract_part(num1)
frac2 = extract_part(num2)

fraction_part  = frac1 + frac2

print(int(fraction_part * 1000) / 1000)
