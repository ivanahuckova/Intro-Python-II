from product import Product


class Doge(Product):
    def __init__(self, name, price, eyes, legs, teeth, sunglasses=True, fluffy=True):
        super().__init__(name, price)
        self.eyes = eyes
        self.legs = legs
        self.teeth = teeth
        self.sunglasses = sunglasses
        self.fluffy = fluffy

    def __str__(self):
        return super().__str__() + "This fine Doge.. You know you want it!"
