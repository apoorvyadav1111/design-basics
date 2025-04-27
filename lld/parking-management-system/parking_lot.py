from vehicle import Vehicle, EV, Motorcycle, Car
class ParkingSpace:
    def __init__(self, id, is_available):
        self.id = id
        self.is_available = is_available
        self.vehicle = None
    
    def park(self, vehicle):
        if self.is_available:   
            self.is_available = False
            self.vehicle = vehicle
            return True
        else:
            return False

    def unpark(self):
        if self.is_available:
            return False
        self.is_available = True
        self.vehicle = None
        return True
    
    def get_vehicle(self):
        return self.vehicle
    
    def get_id(self):
        return self.id
    
    def is_space_available(self):
        return self.is_available
    
    
class EVParkingSpace(ParkingSpace):
    def __init__(self, id, is_available):
        super().__init__(id, is_available)

class CarParkingSpace(ParkingSpace):
    def __init__(self, id, is_available):
        super().__init__(id, is_available)

class MotorcycleParkingSpace(ParkingSpace):
    def __init__(self, id, is_available):
        super().__init__(id, is_available)

class ParkingLot:
    def __init__(self, car_capacity, motorcycle_capacity, ev_capacity):
        self.car_capacity = car_capacity
        self.motorcycle_capacity = motorcycle_capacity
        self.ev_capacity = ev_capacity
        self.car_parking_spaces = [CarParkingSpace(i, True) for i in range(car_capacity)]
        self.motorcycle_parking_spaces = [MotorcycleParkingSpace(i, True) for i in range(motorcycle_capacity)]
        self.ev_parking_spaces = [EVParkingSpace(i, True) for i in range(ev_capacity)]
        self.free_slots = {
            "car": car_capacity,
            "motorcycle": motorcycle_capacity,
            "ev": ev_capacity
        }
        
    
    def park_vehicle(self, vehicle):
        if isinstance(vehicle, EV):
            for space in self.ev_parking_spaces:
                if space.park(vehicle):
                    self.free_slots["ev"] -= 1
                    return space
        elif isinstance(vehicle, Motorcycle):
            for space in self.motorcycle_parking_spaces:
                if space.park(vehicle):
                    self.free_slots["motorcycle"] -= 1
                    return space
        for space in self.car_parking_spaces:
            if space.park(vehicle):
                self.free_slots["car"] -= 1
                return space
        return None
    
    def unpark_vehicle(self, vehicle, parking_space):
        if parking_space.unpark():
            if isinstance(vehicle, EV):
                self.free_slots["ev"] += 1
            elif isinstance(vehicle, Motorcycle):
                self.free_slots["motorcycle"] += 1
            else:
                self.free_slots["car"] += 1
            return True
        return False
    

    def free_slots_count(self):
        return sum(self.free_slots.values())
    
    def find_vehicle(self, license_plate):
        for space in self.ev_parking_spaces:
            if not space.is_space_available() and space.get_vehicle().license_plate == license_plate:
                return space
        for space in self.motorcycle_parking_spaces:
            if not space.is_space_available() and space.get_vehicle().license_plate == license_plate:
                return space
        for space in self.car_parking_spaces:
            if not space.is_space_available() and space.get_vehicle().license_plate == license_plate:
                return space
        return None
    
    
class ParkingLotManager:
    def __init__(self):
        self.parking_lot = ParkingLot(100, 100, 100)
        self.vehicles_to_parking_spot = {}
    
    def park_vehicle(self, vehicle):
        if vehicle in self.vehicles_to_parking_spot:
            return False
        parking_spot = self.parking_lot.park_vehicle(vehicle)
        if parking_spot:
            self.vehicles_to_parking_spot[vehicle] = parking_spot
            return True
        return False
        
    
    def unpark_vehicle(self, vehicle):
        if vehicle not in self.vehicles_to_parking_spot:
            return False
        parking_spot = self.vehicles_to_parking_spot[vehicle]
        if self.parking_lot.unpark_vehicle(vehicle):
            del self.vehicles_to_parking_spot[vehicle]
            return True
        return False
    def find_vehicle(self, vehicle):
        return vehicle in self.vehicles_to_parking_spot
    
    def free_slots_count(self):
        return self.parking_lot.free_slots_count()


