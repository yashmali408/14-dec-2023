

#1 clss Defination 
class Parent():
    #1.1 property=variable
    bloodGroup='' # Difine property

    #1.2 constructor is special Function/Methode
    def __init__(self):
        self.bloodGroup="B+ve" # property value initialization
        pass

    #1.3 method = Function
    def myMethod(self):
        print(f"My Blood group is {self.bloodGroup}")
        pass
    pass    



#2 create class object 
ceo = Parent()
#2.1 call the method with clss object
ceo.myMethod()
