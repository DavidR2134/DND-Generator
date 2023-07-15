import random

class Character:
    def __init__(self):
        self.race = self.getRace()
        self.name = self.getName()


    def getRace(self):
        races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Hafling", "Half-Orc", "Tiefling", "Human"]

        humanRaces = ["Arabic", "Celtic", "Chinese", "Egyptian", "English", "French", "German", "Greek", "Indian", "Japanese", "Mesoamerican", "NigeriaCongo", "Norse", "Polynesian", "Roman", "Slavic", "Spanish"]


        r = random.randint(0, len(races) - 1)

        if races[r] == "Human":
            r = random.randint(0, len(humanRaces) - 1)
            print(f"You are a {humanRaces[r]} Human.")
        else:
            print(f"You are a {races[r]}")

    def getName(self):
        print("Here's where the name goes")



if __name__ == "__main__":
    app = Character()