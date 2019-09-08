
def discount_value(price, discount):
    discount_amount = (price / 100)* discount
    discounted_price = price - discount_amount
    return discounted_price


final_price = 0
price = int(input("Enter the price:"))
while price != 0:
    discount = int(input("Enter the discount:"))
    disc = discount_value(price, discount)
    print("Item discounted price is:", disc)
    final_price = final_price + disc
    price = int(input("Enter the price:"))


print("Total amount to pay is:", final_price)
