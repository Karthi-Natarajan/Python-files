n = 5  

# Upper half
for i in range(n):
    print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))

# Lower half 
for i in range(n - 2, -1, -1):
    print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))
