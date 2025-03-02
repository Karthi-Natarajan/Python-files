# ATM Withdrawal Calculation

def multiply(num, factor):
    result = 0
    for _ in range(factor):
        result += num
    return result
def add(a,b,c):
    while b > 0:
        a += 1
        b -= 1
    while c > 0:
        a += 1
        c -= 1
    return a

n100 = int(input("Enter number of 100 INR notes: "))
n500 = int(input("Enter number of 500 INR notes: "))
n1000 = int(input("Enter number of 1000 INR notes: "))

amt1=multiply(n100,100)
amt2=multiply(n500,500)
amt3=multiply(n1000,1000)

total =add(amt1,amt2,amt3)

print("The total amount : " ,total)

