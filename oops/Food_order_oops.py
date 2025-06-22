from abc import ABC, abstractmethod

# ------------------------------
# 1. CLASS and OBJECT
# ------------------------------
class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# ------------------------------
# 2. ENCAPSULATION
# ------------------------------
class Order:
    def __init__(self):
        self.__items = []  # private

    def add_item(self, item: FoodItem):
        self.__items.append(item)

    def get_total(self):
        return sum(item.price for item in self.__items)

    def get_items(self):
        return [item.name for item in self.__items]

# ------------------------------
# 3. INHERITANCE
# ------------------------------
class User:
    def __init__(self, name):
        self.name = name

    def place_order(self):
        print(f"{self.name} placed a regular order.")

class PremiumUser(User):
    def place_order(self):
        print(f"{self.name} placed an order with 10% discount.")

# ------------------------------
# 4. POLYMORPHISM
# ------------------------------
class DineInOrder:
    def serve(self):
        print("Order will be served at the table.")

class DeliveryOrder:
    def serve(self):
        print("Order will be delivered to your home.")

def process_order(order_type):
    order_type.serve()

# ------------------------------
# 5. ABSTRACTION
# ------------------------------
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI.")

class Card(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

def make_payment(gateway: PaymentGateway, amount):
    gateway.pay(amount)

# ------------------------------
# 6. DESTRUCTOR
# ------------------------------
class Session:
    def __init__(self, user):
        self.user = user
        print(f"Session started for {user}")

    def __del__(self):
        print(f"Session ended for {self.user}")

# ------------------------------
# MAIN EXECUTION
# ------------------------------
if __name__ == "__main__":
    print("\n--- Creating Food Items ---")
    pizza = FoodItem("Pizza", 250)
    burger = FoodItem("Burger", 150)

    print("\n--- Adding Items to Order (Encapsulation) ---")
    order = Order()
    order.add_item(pizza)
    order.add_item(burger)
    print("Items in order:", order.get_items())
    print("Total bill:", order.get_total())

    print("\n--- User Types (Inheritance) ---")
    user1 = User("Rahul")
    user2 = PremiumUser("Shubham")
    user1.place_order()
    user2.place_order()

    print("\n--- Order Serving (Polymorphism) ---")
    process_order(DineInOrder())
    process_order(DeliveryOrder())

    print("\n--- Payment (Abstraction) ---")
    make_payment(UPI(), order.get_total())
    make_payment(Card(), order.get_total())

    print("\n--- Session (Destructor) ---")
    session = Session("Shubham")
    del session
