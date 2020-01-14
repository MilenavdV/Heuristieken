class Connection:
    def __init__(self, origin, destination, time):
        self.origin = origin
        self.destination = destination
        self.time = time

    def __str__(self):
        return f"Trein van {self.origin} naar {self.destination} van {self.time} minuten"

    def text(self):
        return f"{self.origin}-{self.destination}"
