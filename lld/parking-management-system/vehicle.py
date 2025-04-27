class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate


class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate)
        self.vehicle_type = "car"
class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate)
        self.vehicle_type = "motorcycle"

class EV(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate)
        self.vehicle_type = "ev"

class VehicleFactory:
    def __init__(self):
        self.vehicle_types = {
            "car": Car,
            "motorcycle": Motorcycle,
            "ev": EV
        }
    def build_vehicle(self, vehicle_type, license_plate):
        return self.vehicle_types[vehicle_type](license_plate)
