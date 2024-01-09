class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
            self.total += price

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.total - self._get_price_of_last_transaction()
            self.total -= last_item_price
            self.items.pop()
        else:
            self.total = 0.0

    def _get_price_of_last_transaction(self):
        if self.items:
            return self._get_price_of_item(self.items[-1])
        return 0.0

    def _get_price_of_item(self, item):
        return round(1.76, 2)
