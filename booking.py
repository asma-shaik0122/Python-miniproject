# Taj Hotel Booking System

print("Welcome to Taj Hotel Booking System")

rooms = {
    "Luxury": 8000,
    "Deluxe": 5000,
    "Suite": 12000
}

services = {
    "Breakfast": 500,
    "Spa": 2000
}

total_amount = 0

while True:
    print("\nAvailable Rooms:")
    for room, price in rooms.items():
        print(f"{room} : ₹{price} per night")

    room_type = input("\nEnter room type: ")

    if room_type in rooms:
        nights = int(input("Enter number of nights: "))
        quantity = int(input("Enter number of rooms: "))

        cost = rooms[room_type] * nights * quantity
        total_amount += cost

        print(f"{room_type} booked! Cost: ₹{cost}")

        # Add services
        add_service = input("Do you want extra services? (yes/no): ")

        if add_service.lower() == "yes":
            print("\nAvailable Services:")
            for s, price in services.items():
                print(f"{s} : ₹{price}")

            service_choice = input("Enter service name: ")

            if service_choice in services:
                service_cost = services[service_choice] * quantity
                total_amount += service_cost
                print(f"{service_choice} added! Cost: ₹{service_cost}")
            else:
                print("Invalid service!")

    else:
        print("Invalid room type!")

    more = input("\nDo you want to book more? (yes/no): ")
    if more.lower() != "yes":
        break

print(f"\nTotal amount to pay: ₹{total_amount}")
print("Thank you for choosing Hotel Peace !")