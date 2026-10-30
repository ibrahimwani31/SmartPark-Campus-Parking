
# SmartPark - Campus Parking Management System

import math
from datetime import datetime, timedelta

TOTAL_SLOTS = 6
RATE_PER_HOUR = 20
parking_lot = {}

def calculate_fee(entry_time, exit_time):
    """Return (duration_hours, billed_hours, total_fee)."""
    duration_hours = (exit_time - entry_time).total_seconds() / 3600
    billed_hours = max(1, math.ceil(duration_hours))
    return duration_hours, billed_hours, billed_hours * RATE_PER_HOUR

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

    # Find currently occupied slots
    occupied_slots = {
        details["slot"] for details in parking_lot.values()
    }

    # Find and assign the first available slot
    for slot in range(1, TOTAL_SLOTS + 1):
        if slot not in occupied_slots:
            parking_lot[vehicle] = {
                "slot": slot,
                "entry_time": datetime.now()
            }

            print(f"Vehicle {vehicle} parked in slot {slot}.")

            print(
                "Entry time:",
                parking_lot[vehicle]["entry_time"].strftime(
                    "%I:%M:%S %p"
                )
            )

            # Exit only after successfully parking the vehicle
            return

    print("Error: No available parking slot found.")


def remove_vehicle():
    """Remove a vehicle and calculate its parking bill."""

    vehicle = input(
        "Enter vehicle registration number to remove: "
    ).strip().upper()

    if not vehicle:
        print("Error: Registration number cannot be empty.")
        return

    if vehicle not in parking_lot:
        print(f"Error: Vehicle {vehicle} is not parked.")
        return

    # Retrieve the vehicle's parking information
    details = parking_lot[vehicle]
    slot = details["slot"]
    entry_time = details["entry_time"]

       # Record the departure time and calculate the bill
    exit_time = datetime.now()
    duration_hours, billed_hours, total_fee = calculate_fee(entry_time, exit_time)
    
    # Display the parking receipt
    print("\n========== SMARTPARK RECEIPT ==========")
    print(f"Vehicle number : {vehicle}")
    print(f"Parking slot   : {slot}")
    print(f"Entry time     : {entry_time.strftime('%I:%M:%S %p')}")
    print(f"Exit time      : {exit_time.strftime('%I:%M:%S %p')}")
    print(f"Duration       : {duration_hours:.2f} hours")
    print(f"Billable hours : {billed_hours}")
    print(f"Rate per hour  : Rs. {RATE_PER_HOUR}")
    print("---------------------------------------")
    print(f"TOTAL FEE      : Rs. {total_fee}")
    print("=======================================")

    # Remove the vehicle after generating the receipt
    parking_lot.pop(vehicle)

    print(f"Vehicle removed from slot {slot}.")


def display_vehicles():
    print("\n--- Parked Vehicles ---")

    if not parking_lot:
        print("No vehicles are parked.")
        return

    for vehicle, details in sorted(
        parking_lot.items(),
        key=lambda item: item[1]["slot"]
    ):
        slot = details["slot"]
        entry_time = details["entry_time"]

        print(f"Slot {slot}: {vehicle}")
        print(
            "Entry time:",
            entry_time.strftime("%I:%M:%S %p")
        )
def search_vehicle():
    vehicle = input(
        "Enter vehicle registration number to search: "
    ).strip().upper()

    if not vehicle:
        print("Error: Registration number cannot be empty.")
        return

    if vehicle in parking_lot:
        details = parking_lot[vehicle]

        slot = details["slot"]
        entry_time = details["entry_time"]

        print(f"Vehicle: {vehicle}")
        print(f"Parking slot: {slot}")
        print(
            "Entry time:",
            entry_time.strftime("%I:%M:%S %p")
        )
    else:
        print(f"Vehicle {vehicle} is not parked.")



def main():
    while True:
        print("\n===== SMARTPARK =====")
        print("1. Park a vehicle")
        print("2. Remove a vehicle")
        print("3. Display parked vehicles")
        print("4. Search for a vehicle")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            park_vehicle()
        elif choice == "2":
            remove_vehicle()
        elif choice == "3":
            display_vehicles()
        elif choice == "4":
            search_vehicle()
        elif choice == "5":
            print("Exiting SmartPark.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
