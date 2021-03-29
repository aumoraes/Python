from src.insufficient_amount import InsufficientAmount
import requests
class Wallet:
    def __init__(self, amount=0):
        self._balance = amount
    
    def balance(self):
        return self._balance
    
    def add_cash(self, amount):
        self._balance = self._balance + amount
    
    def spend_cash(self, amount):
        if amount > self._balance:
            raise InsufficientAmount("Valor solicitado maior que o disponivel em conta")
        else: 
            self._balance = self._balance - amount
    
    
    def request_month_report(self):
        return requests.get("https://google.com", False)
    
    
    