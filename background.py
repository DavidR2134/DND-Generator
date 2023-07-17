import random
from Sibling import Sibling

class Background:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.parents = self.setParents()
        if self.parents != "You do not know who your parents were.":
            self.birthplace = self.setBirthplace()
            self.siblings = self.setSiblings()
        else:
            self.birthplace = "You do not know where you were born"
            self.siblings = "You do not know if you have any siblings"

    def setParents(self):
        s = ""
        r = random.randint(1,100)
        parents = {
                tuple(range(1, 96)) : "You know who your parents are or were.",
                tuple(range(96, 101)) : "You do not know who your parents were."
            }

        for key, value in parents.items():
            if r in key:
                s += value
                break

        if r >= 96:
            return s


        if self.race == "half-orc":
            #r = random.randint(1,8)
            r = 8
            half_orc_parents = {
                tuple(range(1,4)) : " One parent was an orc and the other was a human",
                tuple(range(4,6)) : " One parent was an orc and the other was a half-orc",
                tuple(range(6,8)) : " One parent was a human and the other was a half-orc",
                8 : " Both parents were half-orcs"
            }   

            for key, value in half_orc_parents.items():
                if r == key:
                    s += value
                    break
                elif r in key:
                    s += value
                    break
                                
        elif self.race == "tiefling":
            r = random.randint(1,8)
            tiefling_parents = {
                tuple(range(1,5)) : " Both parents were humans their infernal heritage dormant until you came along",
                tuple(range(5,7)) : " One parent was a tiefling and the other was a human",
                tuple(range(7,8)) : " One parent was a tiefling and the other was a devil",
                tuple(range(8,9)) : " One parent was a human and the other was a devil",
            }

            for key, value in tiefling_parents.items():
                if r in key:
                    s += value
                    break
            

        return s
            
                
    def setBirthplace(self):
        birthplace = {
            tuple(range(1,51))   : f"{self.name} was born at home",
            tuple(range(51,56))   : f"{self.name} was born at the home of a family friend",
            tuple(range(56,64))   : f"{self.name} was born in the home of a healer or midwife",
            tuple(range(64,66))   : f"{self.name} was born in a carriage cart or wagon",
            tuple(range(66,69))   : f"{self.name} was born in a barn shed or other outbuilding",
            tuple(range(69,71))   : f"{self.name} was born in a cave",
            tuple(range(71,73))   : f"{self.name} was born in a field",
            tuple(range(73,75))   : f"{self.name} was born in a forest",
            tuple(range(75,78))   : f"{self.name} was born in a temple",
            tuple(range(78,79))   : f"{self.name} was born on a battlefield",
            tuple(range(79,81))   : f"{self.name} was born in a alley or the street",
            tuple(range(81,83))   : f"{self.name} was born in a brothel tavern or inn",
            tuple(range(83,85))   : f"{self.name} was born in a castle keep tower or palace",
            tuple(range(85,86))   : f"{self.name} was born in a sewer or rubbish heap",
            tuple(range(86,89))   : f"{self.name} was born among people of a different race",
            tuple(range(89,92))   : f"{self.name} was born onboard a boat or a ship",
            tuple(range(92,94))   : f"{self.name} was born in a prison or in the headquarters of a secret organization",
            tuple(range(94,96))   : f"{self.name} was born in a sages library",
            tuple(range(96,97))   : f"{self.name} was born in the Feywild",
            tuple(range(97,98))   : f"{self.name} was born in the Shadowfell",
            tuple(range(98,99))   : f"{self.name} was born on the Astral Plane or the Ethereal Plane",
            tuple(range(99,100))   : f"{self.name} was born on an Inner Plane of your choice",
            tuple(range(100,101))   : f"{self.name} was born on an Outer Plane of your choice"
        }

        r = random.randint(1,100)

        for key, value in birthplace.items():
            if r in key:
                return value

    def setSiblings(self):
        r = random.randint(1,10)
        siblings = 0

        s = []

        print(r)

        if self.race.lower() == "elf" or self.race.lower() == "dwarf":
            r -= 2

        if r <= 2:
            return s
        elif r == 3 or r == 4:
            siblings += random.randint(1,3)
        elif r == 5 or r == 6:
            siblings += (random.randint(1,4) + 1)
        elif r == 7 or r == 8:
            siblings += (random.randint(1,6) + 2)
        elif r == 9 or r == 10:
            siblings += (random.randint(1,8) + 3)


        for i in range(siblings):
            s.append(Sibling(self.race))

        return s

    
    