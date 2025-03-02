# Age Calculation

def subtract(x,y):
    while y >0:
        x -= 1
        y -=1
    return x
def  compare_date(curr_d,curr_m,bir_d,bir_m):
    if curr_m < bir_m:
        return True
    if curr_m == bir_m and curr_d == bir_d:
        return True
    return False

birth_d = int(input("Enter birth day: "))
birth_m = int(input("Enter birth month: "))
birth_y = int(input("Enter birth year: "))


curr_d = int(input("Enter current day: "))
curr_m = int(input("Enter current month: "))
curr_y = int(input("Enter current year: "))

age = subtract(curr_y ,birth_y)

if compare_date(curr_d,curr_m,birth_d,birth_m):
    age=subtract(age, 1)

print("Age",age)


# In Built-in Function

from datetime import date

d,m,y = map(int, input("Enter the Date(DD MM YYYY) : ").split())

today = date.today( )

age = today.year - y - ((today.month, today.day) < (m,d))

print("Age : ",age)
