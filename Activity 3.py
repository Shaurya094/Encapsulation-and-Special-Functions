x = input("Enter x coordinates: ")
y = input("Enter y coordinates: ")

class point:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

p1 = point(x, y)
print(p1)
