# Name the constants for packaged price
Packaged_price=99
# discount_amount=060
# Get number of packages purchased
Quantity= int(input("Enter the number of packages purchased:"))
#calculate the total cost with discount
Total_cost= Quantity*Packaged_price
if 10<= Quantity<=19:
    discount_percentage=0.10
elif 20<= Quantity<=49:
    discount_percentage=0.20
elif 50<= Quantity<=99:
    discount_percentage=0.30
elif Quantity>=100:
    discount_percentage=0.40
else:
    discount_percentage=0
#Calculate Discount amount
discount_amount = (Total_cost*discount_percentage)
after_discount=Total_cost - discount_amount
print("the discount amount is ->$", discount_amount)
print("the total amount after discount is ->$", after_discount)