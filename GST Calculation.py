# Calculate CGST and SGST for a product

price = input("Enter the price :")
price = int(price) if "." not in price else float(price)
cgst = 0
sgst =0
i =0
while i < 9 :
    cgst += price / 100
    sgst += price/100
    i+=1
total = price
j = 0
while j < 2:
    total += cgst
    j+=1
def rounding_off(num):
    return int(num * 100) / 100

print("CGST : ",rounding_off(cgst),"SGST :",rounding_off(sgst),"Total :",rounding_off(total))


# IN Built-in function

price = int(input("enter the price "))
cgst = price * 0.09
sgst = price * 0.09
total = price +cgst+sgst
print(f"CGST :{cgst : .2f},SGST : {sgst : .2f},Total : {total : .2f}")
