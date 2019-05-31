from room import room


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f"{self.name} is in {self.current_room}"

    def getItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)


player = Player("Ivana", room["winterfell"])
