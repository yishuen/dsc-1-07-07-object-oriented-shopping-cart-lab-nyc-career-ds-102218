class ShoppingCart:

    def __init__(self, _employee_discount = None):
        self._total = 0
        self._items = []
        self._itemprices = []
        self._employee_discount = _employee_discount

    def get_total(self):
        return self._total

    def set_total(self, new):
        self._total = total

    total = property(get_total, set_total)

    def get_items(self):
        return self._items

    def set_items(self, new):
        self._items = items

    items = property(get_items, set_items)

    def get_employee_discount(self):
        return self._employee_discount

    employee_discount = property(get_employee_discount)

    def add_item(self, item, price, quantity = 1):
        self._total += price*quantity
        print(self._total)
        for i in range(quantity):
            self._items.append(item)
            self._itemprices.append(price)
        print(self._items)

    def mean_item_price(self):
        return self.total/len(self.items)

    def median_item_price(self):
        item_list = sorted(self._itemprices)
        print(item_list)
        x = len(item_list)
        if x % 2 == 0:
            return (item_list[x-1] + item_list[x])/2
        if x % 2 != 0:
            y = x/2 - 0.5
            return item_list[int(y)]

    def apply_discount(self):
        if self._employee_discount != None:
            return self.total*(100-self._employee_discount)/100
        else:
            print("Sorry, there is no discount to apply to your cart :(")

shopping_cart = ShoppingCart()
shopping_cart.add_item("rainbow sandals", 45.99)
shopping_cart.add_item("agyle socks", 10.50)
shopping_cart.add_item("jeans", 50.00, 3)
discount_shopping_cart = ShoppingCart(20)
print(discount_shopping_cart.add_item("rainbow sandals", 45.00)) # 45.00
print(discount_shopping_cart.add_item("agyle socks", 15.00)) # 60.00
print(discount_shopping_cart.apply_discount()) # 48.00
print(discount_shopping_cart.add_item("macbook air", 1000.00)) # 1060.00
print(discount_shopping_cart.apply_discount()) # 848.00
print(shopping_cart.apply_discount())
