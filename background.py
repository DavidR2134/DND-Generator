import random, math
from DictionaryHolder import DictionaryHolder
from Sibling import Sibling

class Background:
    def __init__(self, name, race, stats):
        self.name = name
        self.race = race
        self.stats = stats
        self.parents = self.setParents()
        self.raised = self.childhood()
        self.d = DictionaryHolder()
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
        r = random.randint(1,100)

        return f"{self.name}{self.d.get_value_from_birthplace(r)}"

        
    def setSiblings(self):
        r = random.randint(1,10)
        siblings = 0

        s = []

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

    def childhood(self):
        s = ""
        family = {
            tuple(range(1,2)) : "None",
            tuple(range(2,3)) : "Institution, such as an asylum",
            tuple(range(3,4)) : "Temple",
            tuple(range(4,6)) : "Orphanage",
            tuple(range(6,8)) : "Guardian",
            tuple(range(8,16)) : "Paternal or maternal aunt, uncle, or both; or extended family such as a tribe or clan",
            tuple(range(16,26)) : "Paternal or maternal grandparent(s)",
            tuple(range(26,36)) : "Adoptive family (same or different race)",
            tuple(range(36,56)) : "Single father or stepfather",
            tuple(range(56,76)) : "Single mother or stepmother",
            tuple(range(76,101)) : "Mother and father"
        }

        familyLifestyle = {
            tuple(range(3,4)) : ("Wretched", -40),
            tuple(range(4,6)) : ("Squalid", -20),
            tuple(range(6,9)) : ("Poor", -10),
            tuple(range(9,13)) : ("Modest", 0),
            tuple(range(13,16)) : ("Comfortable", 10),
            tuple(range(16,18)) : ("Wealthy", 20),
            tuple(range(18,19)) : ("Aristocratic", 40)
        }

        childhoodHome = {
            tuple(range(-40,1)) : "the streets",
            tuple(range(1,21)) : "Rundown Shack",
            tuple(range(21,31)) : "No permanent residence; you moved around a lot",
            tuple(range(31,41)) : "Encampment or village in the wilderness",
            tuple(range(41,51)) : "Apartment in a rundown neighborhood",
            tuple(range(51,71)) : "Small house",
            tuple(range(71,91)) : "Large house",
            tuple(range(91,111)) : "Mansion",
            tuple(range(111,152)) : "Palace or castle"
        }

        childhoodMemories = {
            tuple(range(-25,4)) : "You are still haunted by your childhood, when you were treated badly by your peers.",
            tuple(range(4,6)) : "You spent most of your childhood alone, with no close friends.",
            tuple(range(6,9)) : "Others saw you as being different or strange, and so you had few companions.",
            tuple(range(9,13)) : "You had few close friends and lived an ordinary childhood.",
            tuple(range(13,16)) : "You had several friends, and your childhood was generally a happy one.",
            tuple(range(16,18)) : "You always found it easy to make friends, and loved being around people.",
            tuple(range(18,25)) : "Everyone knew who you were, and you had friends everywhere you went."
        }

        roll = random.randint(1,100)
        
        for key, value in family.items():
            if roll in key:
                s += ("You were raised by a " + value)
        
        
        rolls = []

        for i in range(3):
            rolls.append(random.randint(1,6))
        
        roll = sum(rolls)

        for key,value in familyLifestyle.items():
            if roll in key:
                s = s + ". You lived a " + value[0] + " life. "
                mod = value[1]
                roll = random.randint(1,100)
                roll += mod

                for k, v in childhoodHome.items():
                    if roll in k:
                        if v == "the streets":
                            s = s + f"{self.name} grew up in " + v + ". "
                        else:
                            s = s + f"{self.name} grew up in a " + v + ". "

        
        rolls = []
        for i in range(3):
            rolls.append(random.randint(1,6))
        
        mod = math.floor(((self.stats['Charisma'] - 10) / 2 ))


        roll = sum(rolls) + mod 

        for key,value in childhoodMemories.items():
            if roll in key:
                s = s + " " + value

        return s
    
    
    