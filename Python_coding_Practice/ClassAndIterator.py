class Vehicle:
    def purpose(self):
        print("Runs on petrol and diesel")

class Bike(Vehicle):

     def feature(self):
            self.purpose()
            print("Has two Wheels!")

class Car(Vehicle):

    def feature(self):
        self.purpose()
        print("Has Four Wheels!")

b = Bike()
b.feature()

models = ["Ford", "Maruti", "Mercedes", "Audi", "KIA"]

itr = iter(models)

print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())


