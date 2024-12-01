class Customer:
    def __init__(self,name, balance):
        self.name=name
        self.__balance=balance
        
    @property
    def balance(self):
        return self.__balance
        
    @balance.setter
    def balance(self,balance):
        if balance < 0:
            self.__balance=0
        elif balance > 10000:
            self.__balance=10000
        else:
            self.__balance=balance
            
        
        
customer1= Customer("Shubham",1000)
print(customer1.balance)
customer1.balance= 1100
print(customer1.balance)
