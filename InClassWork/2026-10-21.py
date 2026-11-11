class pet:
    # Name, Type, Hunger, Happiness, Bond
    # Play, Eat, Sleep,
    # Show Status

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hunger = 100
        self.happiness = 50
        self.bond = 0

    def sleep(time: int):
        if time <= 3:
            pet.happiness += 10
            pet.hunger -= 10
        elif time > 3 <= 6:
            pet.happiness += 25
            pet.hunger -= 25
        else:
            pet.happiness += 50
            pet.hunger -= 50
            pet.hunger

    def eat(food: str):
        special_foods = ["Apple", "Steak", "Chicken", "Bone"]
        bad_foods = ["Chocolate" "Grapes"]
        if food in special_foods:
            pet.hunger += 25
        elif food in bad_foods:
            pet.hunger = 0
        else:
            pet.hunger += 10
