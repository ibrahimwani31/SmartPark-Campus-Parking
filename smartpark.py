# SmartPark: Campus Parking Management System
# Version 1 - Initial implementation

# Dictionary to store vehicle registration numbers and parking slots
parking_lot = {}

# Total parking spaces available
TOTAL_SLOTS = 5


def show_availability():
    """Display available and occupied parking spaces."""
    occupied = len(parking_lot)
    available = TOTAL_SLOTS - occupied

    print("\n--- Parking Status ---")
    print(f"Total spaces: {TOTAL_SLOTS}")
    print(f"Occupied spaces: {occupied}")
    print(f"Available spaces: {available}")


def park_vehicle():
    """Assign an available parking space to a vehicle."""
    vehicle = input("Enter vehicle registration number: ").strip().upper()

    if not vehicle:
        print("Error: Registration number cannot be empty.")
        return

    if vehicle in parking_lot:
        print("Error: This vehicle is already parked.")
        return

    if len(parking_lot) >= TOTAL_SLOTS:
        print("Sorry! The parking lot is full.")
        return

    # Assign the next available slot
    used_slots = set(parking_lot.values())
    slot = next(
        number for number in range(1, TOTAL_SLOTS + 1)
        if number not in used_slots
    )

    parking_lot[vehicle] = slot
    print(f"Vehicle parked successfully in slot {slot}.")


def remove_vehicle():
    """Remove a vehicle and free its parking space."""
    vehicle = input("Enter vehicle registration number: ").strip().upper()

    if vehicle in parking_lot:
        slot = parking_lot.pop(vehicle)
        print(f"Vehicle removed. Parking slot {slot} is now free.")
    else:
        print("Error: Vehicle not found.")


def search_vehicle():
    """Find the parking slot assigned to a vehicle."""
    vehicle = input("Enter vehicle registration number: ").strip().upper()

    if vehicle in parking_lot:
        print(f"Vehicle {vehicle} is parked in slot {parking_lot[vehicle]}.")
    else:
        print("Vehicle not found in the parking lot.")


def display_vehicles():
    """Display all currently parked vehicles."""
    print("\n--- Parked Vehicles ---")

    if not parking_lot:
        print("No vehicles are currently parked.")
        return

    for vehicle, slot in sorted(
        parking_lot.items(), key=lambda item: item[1]
    ):
        print(f"Slot {slot}: {vehicle}")


def main():
    """Run the SmartPark menu."""
    while True:
        print("\n========== SMARTPARK ==========")
        print("1. Park a vehicle")
        print("2. Remove a vehicle")
        print("3. Search for a vehicle")
        print("4. Display parked vehicles")
        print("5. Show parking availability")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            park_vehicle()
        elif choice == "2":
            remove_vehicle()
        elif choice == "3":
            search_vehicle()
        elif choice == "4":
            display_vehicles()
        elif choice == "5":
            show_availability()
        elif choice == "6":
            print("Thank you for using SmartPark!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
