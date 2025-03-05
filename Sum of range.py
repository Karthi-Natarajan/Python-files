# Most Significant Digit

M = int(input("Enter the Number : "))
N = int(input("Enter the Number : "))

total=sum(range(M,N+1))

print("Sum : ",total)


# Without Built - in Function


M = int(input("Enter the Number : "))
N = int(input("Enter the Number : "))

total = 0
num = M

while num <= N:
    total += num
    num += 1

print("Sum : ",total)

