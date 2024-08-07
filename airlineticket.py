import sqlite3
import requests
import math

class AirlineTicketApplication:
    def process_ticket_booking(self, passenger_name, ticket_class, number_of_tickets):
        total_cost = self.calculate_total_cost(ticket_class, number_of_tickets)
        is_eligible_for_discount = self.check_discount_eligibility(total_cost)
        
        if is_eligible_for_discount:
            total_cost = self.apply_discount(total_cost)
        
        # Added arithmetic operation
        total_cost = math.ceil(total_cost)  # Round up to nearest integer
        
        booking = Booking(passenger_name, ticket_class, number_of_tickets, total_cost)
        is_booking_successful = self.save_booking_to_database(booking)
        
        if is_booking_successful:
            self.call_confirmation_api(booking)
        else:
            print("Booking failed. Please try again.")

    def calculate_total_cost(self, ticket_class, number_of_tickets):
        if ticket_class.lower() == "economy":
            price_per_ticket = 100.00
        elif ticket_class.lower() == "business":
            price_per_ticket = 200.00
        elif ticket_class.lower() == "firstclass":
            price_per_ticket = 300.00
        else:
            raise ValueError("Invalid ticket class: " + ticket_class)
        
        # Added arithmetic operation
        return price_per_ticket * number_of_tickets * 1.1  # Added 10% tax

    def check_discount_eligibility(self, total_cost):
        return total_cost > 500.00

    def apply_discount(self, total_cost):
        return total_cost * 0.9  # 10% discount

    def save_booking_to_database(self, booking):
        conn = sqlite3.connect('airline.db')
        sql = '''INSERT INTO bookings (passenger_name, ticket_class, number_of_tickets, total_cost)
                 VALUES (?, ?, ?, ?)'''
        try:
            cur = conn.cursor()
            cur.execute(sql, (booking.passenger_name, booking.ticket_class, booking.number_of_tickets, booking.total_cost))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        finally:
            conn.close()

    def call_confirmation_api(self, booking):
        api_url = "https://api.example.com/confirmBooking"
        request_payload = {
            "name": booking.passenger_name,
            "totalCost": booking.total_cost
        }
        
        response = requests.post(api_url, json=request_payload)
        
        if response.status_code == 200:
            print("Booking confirmed.")
        else:
            print("Failed to confirm booking.")

    # Added method with HTTP GET request
    def get_current_exchange_rate(self, base_currency, target_currency):
        api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                return data['rates'].get(target_currency)
            else:
                print(f"Failed to get exchange rate. Status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error occurred while fetching exchange rate: {e}")
            return None

if __name__ == "__main__":
    app = AirlineTicketApplication()
    app.process_ticket_booking("John Doe", "Economy", 2)
    
    # Example of using the new exchange rate method
    usd_to_eur_rate = app.get_current_exchange_rate("USD", "EUR")
    if usd_to_eur_rate:
        print(f"Current USD to EUR exchange rate: {usd_to_eur_rate}")
