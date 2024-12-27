import random

class Sibling:
    def __init__(self, race):
        self.race = race
        self.sex = self.getSex()
        self.name = self.getName()
        self.age_compared = self.ageCompared()
        self.occupation = self.getOccupation()
        self.relationship = self.setRelationship()
        self.status = self.setStatus()
        if self.status == "Dead":
            self.cause_of_death = self.setCauseOfDeath()
    
    def getName(self):
        fileName = f"RaceNames/{self.race}, {self.sex} .csv"
        r = random.randint(3,51)

        with open(fileName, 'r') as f:
            count = 0
            for line in f:
                s = line.split(',')
                name = s[1]
                count += 1
                if count == r:
                    return name.strip()

    def getSex(self):
        r = random.randint(0,1)
        if r == 0:
            return "MALE"
        else:
            return "FEMALE"
        
    def ageCompared(self):
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)

        total = r1 + r2

        ageOrder = {
            tuple(range(2,3)) : "Twin, triplet, or quadruplet",
            tuple(range(3,8)) : "Older",
            tuple(range(8,13)) : "Younger" 
        }

        for key, value in ageOrder.items():
            if total in key:
                return value
            
    def getOccupation(self):
        classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rouge", "Sorcerer", "Warlock", "Wizard"]
        occupations = {
            tuple(range(1,6)) : "Academic",
            tuple(range(6,11)) : "Adventurer",
            tuple(range(11,12)) : "Aristocrat",
            tuple(range(12,27)) : "Artisan or Guild Member",
            tuple(range(27,32)) : "Criminal",
            tuple(range(32,37)) : "Entertainer",
            tuple(range(37,39)) : "Exile, hermit, or refugee",
            tuple(range(39,44)) : "Explorer or wanderer",
            tuple(range(44,56)) : "Farmer or herder",
            tuple(range(56,61)) : "Hunter or trapper",
            tuple(range(61,76)) : "Laborer",
            tuple(range(76,81)) : "Merchant",
            tuple(range(81,86)) : "Politician or bureaucrat",
            tuple(range(86,91)) : "Priest",
            tuple(range(91,96)) : "Sailor",
            tuple(range(96,101)) : "Soldier"
        }

        r = random.randint(1,100)

        for key, value in occupations.items():
            if r in key:
                if value == "Adventurer":
                    roll = random.randint(0,11)
                    return f"Adventurer: {classes[roll]}"
                else:
                    return value
                
    def setRelationship(self):
        relationship = {
            tuple(range(3,5)) : "Hostile",
            tuple(range(5,11)) : "Friendly",
            tuple(range(11,13)) : "Indifferent"
        }

        roll1 = random.randint(1,4)
        roll2 = random.randint(1,4)
        roll3 = random.randint(1,4)

        total = roll1 + roll2 + roll3

        for key, value in relationship.items():
            if total in key:
                return value
            
    def setStatus(self):
        status = {
            tuple(range(3,4)) : "Dead",
            tuple(range(4,6)) : "Missing or Unknown",
            tuple(range(6,9)) : "Alive, but doing poorly due to injury, financial trouble, or relationship difficulties",
            tuple(range(9,13)) : "Alive and well",
            tuple(range(13,16)) : "Alive and quite successful",
            tuple(range(16,18)) : "Alive and infamous",
            tuple(range(18,19)) : "Alive and famous",
        }

        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        roll3 = random.randint(1,6)

        total = roll1 + roll2 + roll3

        for key, value in status.items():
            if total in key:
                    return value
            
    def setCauseOfDeath(self):
        cause_of_death = {
            tuple(range(1,2)) : "Unknown",
            tuple(range(2,3)) : "Murdered",
            tuple(range(3,4)) : "Killed in battle",
            tuple(range(4,5)) : "Accident related to class or occupation",
            tuple(range(5,6)) : "Accident unrelated to class or occupation",
            tuple(range(6,8)) : "Natural Causes, such as disease or old age",
            tuple(range(8,9)) : "Apparent suicide",
            tuple(range(9,10)) : "Torn apart by an animal or a natural disaster",
            tuple(range(10,11)) : "Consumed by a monster",
            tuple(range(11,12)) : "Executed for a crime or tortured to death",
            tuple(range(12,13)) : "Bizzare event such as being hit by a meteorite, struck down by an angry god, or killed by a hatching slaad egg"
        }
        roll = random.randint(1,12)
        for k, v in cause_of_death.items():
            if roll in k:
                return v