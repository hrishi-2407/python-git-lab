class Calculator():

    def __init__(self, a, b):
        self.a = a 
        self.b = b

    def add(self):
        return self.a + self.b
    
calci = Calculator(2, 3)

add_result = calci.add()
print("Addition Result:", add_result)