city_names=("Karachi", "Hyderabad", "Sukkur", "Mirpur Khas", "Lahore")
routes=[
    {"route_id": "100", "start_city": "Karachi", "end_city": "Hyderabad",
     "time": "08:00 AM", "fare": 1200, "max_seats": 40, "seats_left": 40},
    {"route_id": "120", "start_city": "Karachi", "end_city": "Sukkur",
     "time": "09:30 AM", "fare": 2000, "max_seats": 36, "seats_left": 36},
    {"route_id": "130", "start_city": "Hyderabad", "end_city": "Mirpur Khas",
     "time": "11:00 AM", "fare": 800, "max_seats": 32, "seats_left": 32},
    {"route_id": "140", "start_city": "Karachi", "end_city": "Lahore",
     "time": "07:00 PM", "fare": 5000, "max_seats": 45, "seats_left": 45},
    {"route_id": "150", "start_city": "Sukkur", "end_city": "Hyderabad",
     "time": "02:00 PM", "fare": 1500, "max_seats": 30, "seats_left": 30},
]

bookings=[]
used_ids=set()

def get_seat_status(route):
    if route["seats_left"]==0:
        return "Fully Booked"
    if route["seats_left"]<route["max_seats"]:
        return "Partially Booked"
    return "Available"

def display_routes(route_list, only_available=False):
    if not route_list:
        print("No routes found.")
        return
    print("\nNo. | Route | Journey | Depart | Fare | Seats | Status")

    for num, route in enumerate(route_list,start=1):
        if only_available and route["seats_left"]==0:
            continue

        journey=route["start_city"]+" -> " + route["end_city"]
        seats=f"{route['seats_left']}/{route['max_seats']}"
        print(f"{num} | {route['route_id']} | {journey} | {route['time']} | "
              f"Rs.{route['fare']} | {seats} | {get_seat_status(route)}")

def get_route(route_id):
    for route in routes:
        if route["route_id"]==route_id:
            return route
    return None

def get_number(prompt):
    text=input(prompt).strip()
    if text.isdecimal():
        return int(text)
    return None

def search_routes():
    text=input("Search by route ID or city: ").strip().lower()

    for route in routes:
        if route["route_id"].lower()==text:
            display_routes([route])
            break
    else:
        matches=[]
        for route in routes:
            if text in (route["start_city"].lower(), route["end_city"].lower()):
                matches.append(route)
        display_routes(matches)

def make_booking_id():
    number=1001
    while "B"+str(number) in used_ids:
        number+=1
    book_id="B"+str(number)
    used_ids.add(book_id)
    return book_id

def book_ticket():
    name=input("Passenger name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    age=get_number("Passenger age: ")

    if age is None or age<1 or age>120:
        print("Error: Age must be a whole number from 1 to 120.")
        return

    route=get_route(input("Route ID: ").strip().upper())

    if route is None:
        print("Error: That route does not exist.")
        return

    seats=get_number("Number of seats: ")

    if seats is None or seats<1:
        print("Error: Seats must be a whole number greater than 0.")
        return
    if seats>route["seats_left"]:
        print(f"Error: Only {route['seats_left']} seat(s) available.")
        return

    total=route["fare"]*seats
    book_id=make_booking_id()
    route["seats_left"]-=seats

    bookings.append({
        "booking_id":book_id,
        "name":name,
        "age":age,
        "route_id":route["route_id"],
        "seats":seats,
        "total":total,
        "status": "Confirmed",
    })

    print("\nBooking confirmed!")
    print(f"Booking ID:{book_id}")
    print(f"Passenger:{name}")
    print(f"Route:{route['route_id']} ({route['start_city']} -> {route['end_city']})")
    print(f"Seats booked:{seats}")
    print(f"Fare per seat:Rs. {route['fare']}")
    print(f"Total fare:Rs. {total}")
    print("Status:Confirmed")

def show_bookings():
    if not bookings:
        print("No bookings found.")
        return
    print("\nNo. | ID | Passenger | Route | Seats | Fare | Status")

    for num, booking in enumerate(bookings, start=1):
        print(f"{num} | {booking['booking_id']} | {booking['name']} | "
              f"{booking['route_id']} | {booking['seats']} | Rs.{booking['total']} | {booking['status']}")

def cancel_booking():
    book_id=input("Enter booking ID to cancel: ").strip().upper()
    for booking in bookings:
        if booking["booking_id"]==book_id:
            if booking["status"]!="Confirmed":
                print("Error: This booking is already cancelled.")
            else:
                route=get_route(booking["route_id"])
                route["seats_left"] +=booking["seats"]
                booking["status"] = "Cancelled"
                print(f"Booking {book_id} has been cancelled.")
                print(f"Seats restored: {booking['seats']}")
                print(f"Route {route['route_id']} available seats: {route['seats_left']}")
            break
    else:
        print("Error: No booking found with that ID.")

def check_availability():
    answer=input("Show only routes with seats left? (y/n): ").strip().lower()
    display_routes(routes, only_available=(answer == "y"))

def show_report():
    confirmed=0
    seats_booked=0
    revenue=0
    full_routes=0

    for route in routes:
        if route["seats_left"]==0:
            full_routes += 1

        for booking in bookings:
            if booking["route_id"]==route["route_id"] and booking["status"]=="Confirmed":
                confirmed+= 1
                seats_booked+=booking["seats"]
                revenue +=booking["total"]

    print("\nBOOKING REPORT")
    print(f"Total bookings created:{len(bookings)}")
    print(f"Confirmed bookings:{confirmed}")
    print(f"Cancelled bookings:{len(bookings) - confirmed}")
    print(f"Seats currently reserved:{seats_booked}")
    print(f"Confirmed revenue:Rs. {revenue:,}")
    print(f"Fully booked routes:{full_routes}")

def show_schedule():
    print("\nROUTE SCHEDULE BY DEPARTURE CITY")

    for city in city_names:
        print(city)
        has_departures = False
        for route in routes:
            if route["start_city"]==city:
                print(f"  {route['route_id']} -> {route['end_city']} | {route['time']}")
                has_departures = True

        if not has_departures:
            print(" No scheduled departures.")


def main():
    while True:
        print("\nSMART BUS RESERVATION SYSTEM")
        print("1.View Available Routes")
        print("2.Search for a Route")
        print("3.Book a Ticket")
        print("4.View My Bookings")
        print("5.Cancel a Booking")
        print("6.View Seat Availability")
        print("7.Generate Booking Report")
        print("8.Exit")
        print("9.View Route Schedule")

        choice=input("Enter your choice: ").strip()
        if choice=="1":
            display_routes(routes)
        elif choice=="2":
            search_routes()
        elif choice=="3":
            book_ticket()
        elif choice=="4":
            show_bookings()
        elif choice=="5":
            cancel_booking()
        elif choice=="6":
            check_availability()
        elif choice=="7":
            show_report()
        elif choice=="8":
            print("Thank you for using Smart Bus Reservation System.")
            break
        elif choice=="9":
            show_schedule()
        else:
            print("Error: Please enter a valid number from 1 to 9.")

main()