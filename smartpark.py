
# SmartPark - Campus Parking Management System
# Version 1: Basic parking system

TOTAL_SLOTS = 5
parking_lot = {}


def park_vehicle():
    vehicle = input("Enter vehicle registration number: ").strip().upper()

    if len(parking_lot) >= TOTAL_SLOTS:
        print("Parking lot is full.")
        return

    slot = len(parking_lot) + 1
    parking_lot[vehicle] = slot

    print(f"Vehicle {vehicle} parked in slot {slot}.")


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
