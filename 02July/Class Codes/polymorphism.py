class PaymentMethod:
    def process_payment(self, amount):
        pass


class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        return f'This payment is done by using CreditCard of Rs.{amount}'


class UPI(PaymentMethod):
    def process_payment(self, amount):
        return f'This payment is done by using UPI of Rs.{amount}'


def make_payment(payment_method, amount):
    print(payment_method.process_payment(amount))


credit_card = CreditCard()
UPI = UPI()

make_payment(UPI, 100)
make_payment(credit_card, 100)
