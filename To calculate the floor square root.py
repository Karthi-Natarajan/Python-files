# To calculate the floor square root

def floorsqrt(n):
    res = 1
    while res*res <=n:
        res+=1
    return res-1
n = int(input("Enter the number : "))
result = floorsqrt(n)
print("ans : ",result)



#Using Binary Search

def flsqrt(n):
    lo=1
    hi=n
    res=0

    while lo <= hi:
        mid = lo+(hi-lo)//2

        if mid*mid <= n:
            res = mid
            lo += mid
        else:
            hi -=mid
    return res

n = int(input("Enter the number : "))
result = flsqrt(n)
print("ans : ",result)
        
