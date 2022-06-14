class Dog:
    _animal ='dog'



    def __init__(self,breed):
        self.breed = breed

    def setcolor(self,color):
        self.color = color

    def getcolor(self):
        return self.color
        return self.breed



Rodger = Dog("Pug")
Rodger.setcolor("Brown")
print(Rodger._animal)
