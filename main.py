class House:
    def __init__(self):
        self.numberOfFloors =0
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors

house_1 = House()
print(house_1.numberOfFloors)
house_1.setNewNumberOfFloors(10)
print(house_1.numberOfFloors)