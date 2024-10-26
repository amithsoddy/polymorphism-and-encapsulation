class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print(self.__maxprice)
    def setprice(self,price):
        self.__maxprice=price
c=computer()
c.sell()
c.__maxprice=1000
c.sell()
c.setprice(1000)
c.sell()
