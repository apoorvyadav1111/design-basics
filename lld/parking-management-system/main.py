from parking_lot import ParkingLot, VehicleFactory

parking_lot = ParkingLot(10, 10, 10)


def main():
    all_vehicles = []
    vehicle_factory = VehicleFactory()
    while True:
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
            license_plate = input("Enter the license plate: ")
            vehicle = vehicle_factory.build_vehicle(vehicle_type, license_plate)
            all_vehicles.append(vehicle)
        elif choice == 2:
            license_plate = input("Enter the license plate: ")
            for vehicle in all_vehicles:
                if vehicle.license_plate == license_plate:
                    all_vehicles.remove(vehicle)
                    break
        elif choice == 3:
            for index, vehicle in enumerate(all_vehicles):
                print(str(index) + ". " + vehicle.vehicle_type + " " + vehicle.license_plate)
        elif choice == 4:
            vehicle_index = int(input("Enter the index of the vehicle from 0 to " + str(len(all_vehicles) - 1) + ": "))
            parking_lot.park_vehicle(all_vehicles[vehicle_index])
        elif choice == 5:
            license_plate = input("Enter the license plate: ")
            for vehicle in all_vehicles:
                if vehicle.license_plate == license_plate:
                    parking_lot.unpark_vehicle(vehicle)
                    all_vehicles.remove(vehicle)
                    break
        elif choice == 6:
            print(parking_lot.free_slots_count())
        elif choice == 7:
            break

if __name__ == "__main__":
    main()  