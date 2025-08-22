class Passenger:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Ticket:
    def __init__(self, passenger, seat_class, seat_preference, food_choice, source, destination, flight_company, transit):
        self.passenger = passenger
        self.seat_class = seat_class
        self.seat_preference = seat_preference
        self.food_choice = food_choice
        self.source = source
        self.destination = destination
        self.flight_company = flight_company
        self.transit = transit
        self.special_request = None

    def process_special_requests(self):
        if self.passenger.age < 18:
            self.special_request = "WIP (With Immediate Person)"
        elif self.passenger.gender == "Female":
            prefer_sitting_with_female = input("Do you prefer sitting with another female? (yes/no): ").strip().lower()
            if prefer_sitting_with_female == "yes":
                self.special_request = "Sit with another female"

    def display_ticket(self):
        print("\nTicket Details:")
        print(f"Passenger Name: {self.passenger.name}")
        print(f"Age: {self.passenger.age}")
        print(f"Gender: {self.passenger.gender}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Preferred Flight Company: {self.flight_company}")
        print(f"Transit Required: {self.transit}")
        print(f"Class: {self.seat_class}")
        print(f"Seat Preference: {self.seat_preference}")
        print(f"Food Choice: {self.food_choice}")
        if self.special_request:
            print(f"Special Request: {self.special_request}")

class FlightManager:
    def book_ticket(self):
        print("Welcome to Flight Ticket Booking!")

        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (Male/Female): ").strip()

        passenger = Passenger(name, age, gender)

        source = input("Enter your source location: ").strip()
        destination = input("Enter your destination: ").strip()

        print("Available flight options: Flight1, Flight2, Flight3")
        flight_company = input("Enter your preferred flight company (or type 'Any'): ").strip()
        transit = input("Do you need a transit flight? (yes/no): ").strip().lower()

        seat_class = input("Choose seat class (Business/Economy): ").strip()
        seat_preference = input("Choose seat preference (Aisle/Middle/Window): ").strip()
        wants_food = input("Do you want food? (yes/no): ").strip().lower()
        food_choice = None
        if wants_food == "yes":
            food_choice = input("Choose food type (Veg/Non-Veg): ").strip()

        ticket = Ticket(passenger, seat_class, seat_preference, food_choice, source, destination, flight_company, transit)
        ticket.process_special_requests()

        return ticket

# Main Function
if __name__ == "__main__":
    flight_manager = FlightManager()
    ticket = flight_manager.book_ticket()
    ticket.display_ticket()
