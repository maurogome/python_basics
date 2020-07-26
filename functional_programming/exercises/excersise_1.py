def apply_tax(price, tax):
    return price + price * tax / 100

def apply_discount(price, discount):
    return price - price * discount / 100

def basket(basket, tax=15):
    subtotal = 0
    for price, discount in basket.items():
        subtotal += apply_discount(price, discount)

    total = apply_tax(subtotal, tax)

    return subtotal, total


if __name__ == "__main__":
    shopping_cart = {1000:20,500: 10,100: 1}
    subtotal, total = basket(shopping_cart, 12)

    print(f'Price before tax: ${subtotal}')
    print(f'Final price: ${total}')