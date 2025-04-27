from parking_lot import ParkingLotManager
from vehicle import Car, Motorcycle, EV
from vehicle import VehicleFactory


def main():
    all_vehicles = {}
    parking_lot_manager = ParkingLotManager()
    vehicle_factory = VehicleFactory()

    while True:
        print()
        print("1. Create vehicle")
        print("2. Remove vehicle")
        print("3. List vehicles")
        print("4. Park vehicle")
        print("5. Unpark vehicle")
        print("6. Get parking status")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("1. Car")
            print("2. Motorcycle")
            print("3. EV")
            vehicle_type_int = int(input("Enter the type of vehicle: "))
            vehicle_type = ""
            if vehicle_type_int == 1:
                vehicle_type = "car"
            elif vehicle_type_int == 2:
                vehicle_type = "motorcycle"
            elif vehicle_type_int == 3:
                vehicle_type = "ev"
            else:
                print("Invalid vehicle type")
                continue
            license_plate = input("Enter the license plate: ")
            vehicle = vehicle_factory.build_vehicle(vehicle_type, license_plate)
            if license_plate in all_vehicles:
                print("Vehicle already exists")
            else:
                all_vehicles[license_plate] = vehicle
        elif choice == 2:
            license_plate = input("Enter the license plate: ")
            if license_plate in all_vehicles:
                del all_vehicles[license_plate]
            else:
                print("Vehicle not found")
        elif choice == 3:
            for license_plate, vehicle in all_vehicles.items():
                print(license_plate + " " + vehicle.vehicle_type)
        elif choice == 4:
            license_plate = input("Enter the license plate: ")
            if license_plate in all_vehicles:
                if parking_lot_manager.find_vehicle(license_plate):
                    print("Vehicle already parked")
                else:
                    if parking_lot_manager.park_vehicle(all_vehicles[license_plate]):
                        print("Vehicle parked")
                    else:
                        print("Unable to park vehicle")
            else:
                print("Vehicle not found")
        elif choice == 5:
            license_plate = input("Enter the license plate: ")
            if license_plate in all_vehicles:
                if parking_lot_manager.unpark_vehicle(all_vehicles[license_plate]):
                    print("Vehicle unparked")
                else:
                    print("Vehicle already parked")
            else:
                print("Vehicle not found")
        elif choice == 6:
            print(parking_lot_manager.free_slots_count())
        elif choice == 7:
            break

if __name__ == "__main__":
    main()  