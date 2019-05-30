# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, describtion, emoji, items):
        self.name = name
        self.describtion = describtion
        self.emoji = emoji
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return f"{self.name} - {self.describtion}"


# All the rooms
room = {
    'winterfell':   Room("Winterfell", "Winterfell is the seat and the ancestral home of the royal House Stark. It is a very large castle located at the center of the North, from where the head of House Stark rules over his or her people.", "🐺", ["wolf, snow"]),

    'riverrun':    Room("Riverrun", "Riverrun is the seat of House Tully, which was once occupied by House Frey. It is a large castle located in the central-western part of the Riverlands.", "⛲️", ["ship, book"]),

    'kings_landing': Room("Kings Landing", "King's Landing is the capital, and largest city, of the Seven Kingdoms. It enjoys a warm climate and life there is luxurious for those that can afford it.", "👑", ["money, gold"]),

    'eyrie':   Room("Eyrie", "The Eyrie is the principal stronghold of House Arryn. It is located in the Vale of Arryn near the east coast of Westeros. ", "🗻", ["boat, sword"]),

    'casterly_rock': Room("Casterly Rock", "Casterly Rock is the ancestral stronghold of House Lannister. It is located on the Western coast of Westeros on a rocky promontory overlooking the Sunset Sea.", "👫", ["sunglasses, gold"]),

    'pyke': Room("Pyke", "Pyke is the stronghold and seat of House Greyjoy, located on the island of the same name, which is one of the seven major Iron Islands. ", "⚓️", ["boat, ship"]),

    'highgarden': Room("Highgarden", "Highgarden was the seat of House Tyrell and is the regional capital of the Reach. Located on the banks of the river Mander, Highgarden sits astride the Roseroad, a major thoroughfare linking Oldtown and King's Landing.", "🏆", ["money, sword"]),

    'stormsend': Room("Storm's End", "Storm's End is the ancestral seat of House Baratheon. Lord Gendry Baratheon is the Lord of Storm's End. Storm's End is a formidable fortress, located on the southeastern coast of Westeros overlooking Shipbreaker Bay.", " 🌊", ["spear, ship"]),

    'sunspear': Room("Sunspear", "Sunspear is the capital of Dorne Dorne, southernmost of the Seven Kingdoms, located in the far southeast of the continent on the Summer Sea.", "☀️", ["boat, sword"])
}

# Link rooms together
room['winterfell'].n_to = room['riverrun']

room['pyke'].n_to = room['casterly_rock']
room['pyke'].e_to = room['riverrun']

room['riverrun'].n_to = room['highgarden']
room['riverrun'].s_to = room['winterfell']
room['riverrun'].w_to = room['pyke']
room['riverrun'].e_to = room['eyrie']

room['eyrie'].w_to = room['riverrun']
room['eyrie'].n_to = room['kings_landing']


room['casterly_rock'].s_to = room['pyke']
room['casterly_rock'].e_to = room['highgarden']

room['highgarden'].w_to = room['casterly_rock']
room['highgarden'].e_to = room['kings_landing']
room['highgarden'].s_to = room['riverrun']
room['highgarden'].n_to = room['sunspear']

room['kings_landing'].s_to = room['eyrie']
room['kings_landing'].n_to = room['stormsend']
room['kings_landing'].w_to = room['highgarden']

room['sunspear'].s_to = room['highgarden']
room['sunspear'].e_to = room['stormsend']

room['stormsend'].w_to = room['sunspear']
room['stormsend'].s_to = room['kings_landing']
