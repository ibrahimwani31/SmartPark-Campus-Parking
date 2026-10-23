# SmartPark - Campus Parking Management System
# Version 1: Basic parking system

TOTAL_SLOTS = 5
parking_lot = {}




def park_vehicle():
    vehicle = input("Enter vehicle registration number: ").strip().upper()

    # Reject empty registration numbers
    if not vehicle:
        print("Error: Registration number cannot be empty.")
        return

    # Reject duplicate registration numbers
    if vehicle in parking_lot:
        print(f"Error: {vehicle} is already parked.")
        return

    # Check parking capacity
    if len(parking_lot) >= TOTAL_SLOTS:
        print("Parking lot is full.")
        return

    # Assign the next available slot
    occupied_slots = set(parking_lot.values())

    for slot in range(1, TOTAL_SLOTS + 1):
        if slot not in occupied_slots:
            parking_lot[vehicle] = slot
            print(f"Vehicle {vehicle} parked in slot {slot}.")
            return




def display_vehicles():
    print("\n--- Parked Vehicles ---")

    if not parking_lot:
        print("No vehicles are parked.")
        return

    for vehicle, slot in parking_lot.items():
        print(f"Slot {slot}: {vehicle}")


def main():
    while True:
        print("\n===== SMARTPARK =====")
        print("1. Park a vehicle")
        print("2. Display parked vehicles")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            park_vehicle()
        elif choice == "2":
            display_vehicles()
        elif choice == "3":
            print("Exiting SmartPark.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()


# SmartPark - Campus Parking Management System
# Version 1: Basic parking system

TOTAL_SLOTS = 5
parking_lot = {}




def park_vehicle():
    vehicle = input("Enter vehicle registration number: ").strip().upper()

    # Reject empty registration numbers
    if not vehicle:
        print("Error: Registration number cannot be empty.")
        return

    # Reject duplicate registration numbers
    if vehicle in parking_lot:
        print(f"Error: {vehicle} is already parked.")
        return

    # Check parking capacity
    if len(parking_lot) >= TOTAL_SLOTS:
        print("Parking lot is full.")
        return

    # Assign the next available slot
    occupied_slots = set(parking_lot.values())

    for slot in range(1, TOTAL_SLOTS + 1):
        if slot not in occupied_slots:
            parking_lot[vehicle] = slot
            print(f"Vehicle {vehicle} parked in slot {slot}.")
            return




def display_vehicles():
    print("\n--- Parked Vehicles ---")

    if not parking_lot:
        print("No vehicles are parked.")
        return

    for vehicle, slot in parking_lot.items():
        print(f"Slot {slot}: {vehicle}")


def main():
    while True:
        print("\n===== SMARTPARK =====")
        print("1. Park a vehicle")
        print("2. Display parked vehicles")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            park_vehicle()
        elif choice == "2":
            display_vehicles()
        elif choice == "3":
            print("Exiting SmartPark.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
