class vehicle:
    def set_vehicle_make(self, make, model):
        self.vehicle_make = make
        self.vehicle_model = model

    def get_vehicle_make(self):
        print(f"the car make is: {self.vehicle_make}")
        print(f"the car model is: {self.vehicle_model}")

class car(vehicle):

    def set_cardoor(self, door):
        self.cardoor = door

    def get_cardoor(self):
        print(f"the number of cardoors: {self.cardoor}")
        print(f"the car make is: {self.vehicle_make}")
        print(f"the car model is: {self.vehicle_model}")

class truck(vehicle):

    def setbedlength(self, length):
        self.bed_length = length

    def get_bedlength(self):
        print(f"the bed length is: {self.bed_length}")
        print(f"the truck make is: {self.vehicle_make}")
        print(f"the truck model is: {self.vehicle_model}")

def new_car():
    input_car = input("please enter amount of doors")
    input_make = input("please enter make")
    input_model = input('please enter model')
    cars = car()
    cars.set_cardoor(input_car)
    cars.set_vehicle_make(input_make,input_model)
    cars.get_cardoor()

def new_truck():
    input_truck = input("please enter bed length")
    input_make = input("please enter make")
    input_model = input('please enter model')
    trucks = truck()
    trucks.setbedlength(input_truck)
    trucks.set_vehicle_make(input_make,input_model)
    trucks.get_bedlength()

input_choice = input("please enter whether you want a car or truck")
if input_choice == "car":
    new_car()
elif input_choice == "truck":
    new_truck()
