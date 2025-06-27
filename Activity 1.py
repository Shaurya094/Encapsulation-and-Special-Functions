class  Set:
    def __init__(self):
        self.__c = "Shaurya"
    def get (self):
        print (self.__c)

class Get(Set):
    def __init__(self):
        Set.__init__(self)
        print ("This is a private variable.")
        print(self.__c)

obj = Set()
obj.get()