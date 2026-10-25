from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay():
        pass


class CreditCardPayment(Payment):
    def pay(self,amount):
        if(amount > 0):
            print(f"Credit Card: Payment of {amount} successful.")
        else:
            print("Failed to pay.")


class PayPalPayment(Payment):
    def pay(self, amount):
        if(amount > 0):
            print(f"PayPal: Payment of {amount} successful.")
        else:
            print("Failed to pay.")

def process_payment(payment, amount):
    if(amount < 0):
        print("Error: Amount must be greater than zero.")
    
    payment.pay(amount)


process_payment(CreditCardPayment(), 10)
process_payment(PayPalPayment(), 10)