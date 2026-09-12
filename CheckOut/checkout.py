
def calculate_sub_total(prices, quantities):
    sub_total = 0.0
    for count in range(len(prices)):
        sub_total += prices[count] * quantities[count]
    return sub_total


def calculate_discount(prices, quantities, discount_percentage):
    sub_total = calculate_sub_total(prices, quantities)
    return (sub_total * discount_percentage) / 100


def calculate_vat(prices, quantities):
    sub_total = calculate_sub_total(prices, quantities)
    return (sub_total * 17.5) / 100


def calculate_bill_total(prices, quantities, discount_percentage):
    sub_total = calculate_sub_total(prices, quantities)
    discount = calculate_discount(prices, quantities, discount_percentage)
    vat = calculate_vat(prices, quantities)
    return sub_total - discount + vat


def calculate_balance(bill_total, amount_paid):
    return amount_paid - bill_total
