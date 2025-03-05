# Fractional Part of Sum

def multiply (num,factor):
    result = 0
    for _ in range(factor):
         result += num
    return result

days = int(input("Enter the number of days : "))

hours = multiply(days,24)
minutes = multiply(hours,60)
seconds = multiply (minutes,60)

print(f"hours : {hours},\n Minutes : {minutes},\n Seconds : {seconds}")


