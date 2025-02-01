#payment 
class Payment:
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print("Credit card payment of amount "+str(amount))

class PaypalPayment(Payment):
    def process_payment(self, amount):
        print("Paypal payment of amount "+str(amount))

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        print("Bitcoin payment of amount "+str(amount))

bitcoinObj = BitcoinPayment()
bitcoinObj.process_payment(100)
paypalObj = PaypalPayment()
paypalObj.process_payment(200)
creditcardObj = CreditCardPayment()
creditcardObj.process_payment(300)