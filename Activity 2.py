class comp:
    def __init__(self):
        self.__max = 900
        
    def sell(self):
        print ("Selling price: {}".format(self.__max))

    def setmax(self, price):
        self.__max  = price

c = comp()
c.sell()

c.__max = 1000
c.sell()

c.setmax(1000)
c.sell()