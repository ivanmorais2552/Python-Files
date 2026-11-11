class FortniteBot:  # Class

    max_health = 100  # Class Level Variable (Scope)

    def __init__(self, bot_name):  # Constructor
        self.name = bot_name  # Attribute
        self.health = 100  # Attribute

    def take_damage(self, amount):  # method
        self.health -= amount

        # from FortniteBot import Fortnite Bot
