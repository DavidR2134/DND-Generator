class DictionaryHolder:
    def __init__(self):
        self.classes_and_stats = None
        self.races_and_stats = None
        self.parents = None
        self.half_orc_parents = None
        self.tiefling_parents = None
        self.birthplace = None
        self.family = None
        self.familyLifestyle = None
        self.childhoodHome = None
        self.childhoodMemories = None

    
    #Initialized Dictionary only when called
    #Dictionaries used in Character.py
    def load_classes_and_stats(self):
        self.classes_and_stats = {
            "Fighter" : ["Strength", "Constitution"],
            "Barbarian" : ["Strength", "Constitution"],
            "Bard" : ["Wisdom", "Charisma"],
            "Cleric" : ["Wisdom" , "Constitution"],
            "Paladin" : ["Strength", "Charisma"],
            "Druid" : ["Wisdom", "Constitution"],
            "Ranger" : ["Dexterity", "Wisdom"],
            "Monk" : ["Dexterity", "Wisdom"],
            "Rouge" : ["Dexterity", "Charisma"],
            "Sorcerer" : ["Charisma", "Constitution"],
            "Warlock" : ["Charisma", "Constitution"],
            "Wizard" : ["Intellegence", "Dexterity"]
        }

    def load_races_and_stats(self):
        self.races_and_stats = {
            "dwarf" : [0,0,2,0,0,0],
            "dragonborn" : [2,0,0,0,0,1],
            "elf" : [0,2,0,0,0,0],
            "gnome" : [0,0,0,2,0,0],
            "halfling" : [0,2,0,0,0,0],
            "half-orc" : [2,0,1,0,0,0],
            "tiefling" : [0,0,0,1,0,2]
        }

    
    #Load Dictionary and search for value needed
    def get_value_from_classes_and_stats(self, key):
        if self.classes_and_stats == None:
            self.load_classes_and_stats()
        
        return self.classes_and_stats.get(key)

    def get_value_from_races_and_stats(self, key):
        if self.races_and_stats == None:
            self.load_races_and_stats()

        return self.races_and_stats.get(key)
    
    #Dictionaries used in background.py
    def load_parents(self):
        self.parents = {
                tuple(range(1, 96)) : "You know who your parents are or were.",
                tuple(range(96, 101)) : "You do not know who your parents were."
            }
        
    def load_half_orc_parents(self):
        self.half_orc_parents = {
                tuple(range(1,4)) : " One parent was an orc and the other was a human",
                tuple(range(4,6)) : " One parent was an orc and the other was a half-orc",
                tuple(range(6,8)) : " One parent was a human and the other was a half-orc",
                8 : " Both parents were half-orcs"
            }  
        
    def load_tiefling_parents(self):
        self.tiefling_parents = {
                tuple(range(1,5)) : " Both parents were humans their infernal heritage dormant until you came along",
                tuple(range(5,7)) : " One parent was a tiefling and the other was a human",
                tuple(range(7,8)) : " One parent was a tiefling and the other was a devil",
                tuple(range(8,9)) : " One parent was a human and the other was a devil",
            }
        
    def load_birthplace(self):
        self.birthplace = {
            tuple(range(1,51))   : " was born at home",
            tuple(range(51,56))   : " was born at the home of a family friend",
            tuple(range(56,64))   : " was born in the home of a healer or midwife",
            tuple(range(64,66))   : " was born in a carriage cart or wagon",
            tuple(range(66,69))   : " was born in a barn shed or other outbuilding",
            tuple(range(69,71))   : " was born in a cave",
            tuple(range(71,73))   : " was born in a field",
            tuple(range(73,75))   : " was born in a forest",
            tuple(range(75,78))   : " was born in a temple",
            tuple(range(78,79))   : " was born on a battlefield",
            tuple(range(79,81))   : " was born in a alley or the street",
            tuple(range(81,83))   : " was born in a brothel tavern or inn",
            tuple(range(83,85))   : " was born in a castle keep tower or palace",
            tuple(range(85,86))   : " was born in a sewer or rubbish heap",
            tuple(range(86,89))   : " was born among people of a different race",
            tuple(range(89,92))   : " was born onboard a boat or a ship",
            tuple(range(92,94))   : " was born in a prison or in the headquarters of a secret organization",
            tuple(range(94,96))   : " was born in a sages library",
            tuple(range(96,97))   : " was born in the Feywild",
            tuple(range(97,98))   : " was born in the Shadowfell",
            tuple(range(98,99))   : " was born on the Astral Plane or the Ethereal Plane",
            tuple(range(99,100))   : " was born on an Inner Plane of your choice",
            tuple(range(100,101))  : " was born on an Outer Plane of your choice"
        }

    def load_family(self):
        self.family = {
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
    
    def load_familyLifestyle(self):
        self.familyLifestyle = {
            tuple(range(3,4)) : ("Wretched", -40),
            tuple(range(4,6)) : ("Squalid", -20),
            tuple(range(6,9)) : ("Poor", -10),
            tuple(range(9,13)) : ("Modest", 0),
            tuple(range(13,16)) : ("Comfortable", 10),
            tuple(range(16,18)) : ("Wealthy", 20),
            tuple(range(18,19)) : ("Aristocratic", 40)
        }

    def load_childhoodHome(self):
        self.childhoodHome = {
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
    
    def load_childhoodMemories(self):
        self.childhoodMemories = {
            tuple(range(-25,4)) : "You are still haunted by your childhood, when you were treated badly by your peers.",
            tuple(range(4,6)) : "You spent most of your childhood alone, with no close friends.",
            tuple(range(6,9)) : "Others saw you as being different or strange, and so you had few companions.",
            tuple(range(9,13)) : "You had few close friends and lived an ordinary childhood.",
            tuple(range(13,16)) : "You had several friends, and your childhood was generally a happy one.",
            tuple(range(16,18)) : "You always found it easy to make friends, and loved being around people.",
            tuple(range(18,25)) : "Everyone knew who you were, and you had friends everywhere you went."
        }

    def get_value_from_birthplace(self, key):
        if self.birthplace == None:
            self.load_birthplace()
        
        for k,v in self.birthplace.items():
            if key in k:
                return v
        
    
