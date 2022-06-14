class Base:
    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name

class Child(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age = age

    def getAge(self):
        return self.age

class GrandChild(Child):
    def __init__(self,name,age, address):
        Child.__init__(self,name,age)
        self.address = address

    def getAddress(self):
        return self.address



a = GrandChild('Omar gandu', '25','narayanganj')
print("Name = "+a.getname())
print("Age = "+a.getAge())
print("Address = "+a.getAddress())
