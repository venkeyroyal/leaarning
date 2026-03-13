class Vehicle:
    def __init__(self,name):
        self.name=name

    def start(self):
        print(self.name,"started")

    def stop(self):
        print(self.name,"stopped")


class Car(Vehicle):
    def drive(self):
        print(self.name,"is driving")


class Bike(Vehicle):
    def ride(self):
        print(self.name,"is riding")


c = Car("Car")
c.start()
c.drive()
c.stop()

b = Bike("Bike")
b.start()
b.ride()
b.stop()