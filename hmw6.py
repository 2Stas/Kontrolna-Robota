class MusicalInstrument:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def info(self):
        return f"Model: {self.model}, Price: {self.price}"


class Violin(MusicalInstrument):
    def __init__(self, model, price, color):
        super().__init__(model, price)
        self.color = color

    def info(self):
        return f"{super().info()}, Color: {self.color}"


class Guitar(MusicalInstrument):
    def __init__(self, model, price, guitar_type):
        super().__init__(model, price)
        self.guitar_type = guitar_type

    def info(self):
        return f"{super().info()}, Type: {self.guitar_type}"


instruments = [
    Violin("Yamaha V5", 800, "Brown"),
    Violin("Stentor 1500", 600, "Red"),
    Violin("Stradivarius Replica", 10000, "Natural"),
    Violin("Cremona SV-75", 700, "Black"),
    Guitar("Fender Stratocaster", 1200, "Electric"),
    Guitar("Gibson Les Paul", 2500, "Electric"),
    Guitar("Yamaha C40", 300, "Acoustic")
]

print("List of instruments:")
for instrument in instruments:
    print(instrument.info())

most_instrument = instruments[0]
for instrument in instruments:
    if instrument.price > most_instrument.price:
        most_instrument = instrument

print("\nThe most expensive instrument is:")
print(most_instrument.info())
