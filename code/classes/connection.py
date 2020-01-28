class Connection:
    def __init__(self, origin, destination, time):
        self.origin = origin
        self.destination = destination
        self.time = time

    def text(self):
        # text description of connection, used in code
        return f"{self.origin}-{self.destination}"

    def __str__(self):
        # string method
        return f"Trein van {self.origin} naar {self.destination} van {self.time} minuten"
