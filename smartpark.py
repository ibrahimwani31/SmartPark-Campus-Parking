
# SmartPark - Campus Parking Management System
# Version 2: Added vehicle validation and removal

TOTAL_SLOTS = 5
parking_lot = {}


def park_vehicle():
    vehicle = input(
        "Enter vehicle registration number: "
    ).strip().upper()

    if not vehicle:
        print("Error: Registration number cannot be empty.")
        return

    if vehicle in parking_lot:
        print(f"Error: {vehicle} is already parked.")
        return

    if len(parking_lot) >= TOTAL_SLOTS:
        print("Parking lot is full.")
        return

    # Find the first available slot
    occupied_slots = set(parking_lot.values())

    for slot in range(1, TOTAL_SLOTS + 1):
        if slot not in occupied_slots:
            parking_lot[vehicle] = slot
            print(f"Vehicle {vehicle} parked in slot {slot}.")
            return


def remove_vehicle():
    vehicle = input(
        "Enter vehicle registration number to remove: "
    ).strip().upper()

    if not vehicle:
        print("Error: Registration number cannot be empty.")
        return

    if vehicle not in parking_lot:
        print(f"Error: Vehicle {vehicle} is not parked.")
        return

    slot = parking_lot.pop(vehicle)
    print(f"Vehicle {vehicle} removed from slot {slot}.")


def display_vehicles():
    print("\n--- Parked Vehicles ---")

    if not parking_lot:
        print("No vehicles are parked.")
        return

    for vehicle, slot in sorted(
        parking_lot.items(), key=lambda item: item[1]
    ):
        print(f"Slot {slot}: {vehicle}")


def main():
    while True:
        print("\n===== SMARTPARK =====")
        print("1. Park a vehicle")
        print("2. Remove a vehicle")
        print("3. Display parked vehicles")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            park_vehicle()
        elif choice == "2":
            remove_vehicle()
        elif choice == "3":
            display_vehicles()
        elif choice == "4":
            print("Exiting SmartPark.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
