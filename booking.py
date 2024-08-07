class Booking:
    def __init__(self, passenger_name, ticket_class, number_of_tickets, total_cost):
        self.passenger_name = passenger_name
        self.ticket_class = ticket_class
        self.number_of_tickets = number_of_tickets
        self.total_cost = total_cost

    def __str__(self):
        return f"Booking{{passenger_name='{self.passenger_name}', ticket_class='{self.ticket_class}', number_of_tickets={self.number_of_tickets}, total_cost={self.total_cost}}}"
