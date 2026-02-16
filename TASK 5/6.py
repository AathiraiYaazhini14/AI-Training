class Order:
    def __init__(self, order_id, customer_name, amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer:", self.customer_name)
        print("Amount:", self.amount)


class Payment:
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print("Processing credit card payment of", amount)


class UPIPayment(Payment):
    def process_payment(self, amount):
        print("Processing UPI payment of", amount)


class CashOnDelivery(Payment):
    def process_payment(self, amount):
        print("Cash of", amount, "will be collected on delivery")



order1 = Order(101, "Arun", 2500)
order1.display()
payment = CreditCardPayment()
payment.process_payment(order1.amount)
