def get_discount_rate(promo_code):
    if promo_code == "SAVED10":
       return 0.10
       if promo_code == "HALFOFF":
          return 0.50
       else :
            return 0

def apply_discout(item_name, original_price, promo_code):
    discount_rate = get_discount_rate(promo_code)
    discount_amount = original_price * discount_rate
    final_price = original_price - discount_amount
    return final_price


item_name = input("Enter the name of the item: ")
original_price = float(input("Enter the original price: "))
promo_code = input("Enter promo code: ")


final_result = apply_discount(item_name, original_price, promo_code)
print(final_result)

