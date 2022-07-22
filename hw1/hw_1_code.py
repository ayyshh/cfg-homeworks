class CashRegister:

    def __init__(self):

        self.total_items = {} # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, price_and_item):
        self.total_items.update(price_and_item)

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, discount_amount):
        self.discount += discount_amount

    def get_total(self):
        total_before_discount = sum(self.total_items.values())
        return total_before_discount - self.discount

    def show_items(self):
        for item, price in self.total_items.items():
            print(f"{item} ... £{price:.2f}")

    def reset_register(self):
            self.total_items = {}
            self.total_price = 0
            self.discount = 0

#shop has two cash registers

first_register = CashRegister()
second_register = CashRegister()

# ADD
first_register.add_item({'Eggs', 1.50})
first_register.add_item({'Bread', 2.00})

#the customer may want to pt eggs back
first_register.remove_item({'Eggs', 1.50})

#discount on bread
first_register.apply_discount(0.50)

#cust wants total of shopping
first_register.get_total()

#cust wants to see all items they are buying
first_register.show_items()

#reset register
first_register.reset_register()