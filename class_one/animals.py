# classes

#  Vehicle -> LandVehicle -> Car
# Animal
# eyes, breed, fluff, gender, good_boye


class Animal:
    # dunder init
    def __init__(self, name, breed, gender):
        self.name = name
        self.breed = breed
        self.gender = gender

    def __str__(self):
        return f"\nName: {self.name} \nGender: {self.gender} \nBreed: {self.breed} \n"


a = Animal("Groot", "Tree", "Who Knows!?!")

# dog


class Dog(Animal):
    def __init__(self, name, breed, gender, eyes, fluff, good_boye=True):
        super().__init__(name, breed, gender)
        self.eyes = eyes
        self.fluff = fluff
        self.good_boye = good_boye

    def give_belly_rub(self):
        if self.good_boye:
            print("the good boye rolls on his back for the belly rub ")
        else:
            self.bark()

    def bark(self):
        print("Woof!! Woof!!")

    def __str__(self):
        return f"{super().__str__()}Number Of Eyes: {self.eyes}\nIs Fluffy: {self.fluff}\nIs a Good Boye: {self.good_boye}\n"


b = Dog("Fido", "Golden", "Male", 1, True, True)

print(a)
print(b)
b.bark()
b.give_belly_rub()
