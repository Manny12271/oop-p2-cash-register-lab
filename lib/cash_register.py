class CashRegister:
    def __init__(self, discount=0):
        # Validate discount
        if not isinstance(discount, int) or not (0 <= discount <= 100):
            print("Not valid discount")
            self.discount = 0
        else:
            self.discount = discount

        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self, show_message=True):
        """Apply discount to total; optionally print the result."""
        if self.discount == 0 or not self.previous_transactions:
            if show_message:
                print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        self.total = round(self.total, 2)

        if show_message:
            total_display = int(
                self.total) if self.total.is_integer() else self.total
            print(f"After the discount, the total comes to ${total_display}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        self.total = round(self.total, 2)

        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])
