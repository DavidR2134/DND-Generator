import random
from background import Background

class Character:
    def __init__(self):
        self.race = self.getRace()
        self.sex = self.getSex()
        self.name = self.getName()
        self.adventuringClass = self.getClass()
        self.stats = self.getStats()
        self.back = Background(self.name, self.race)


    def getRace(self):
        races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Halfling", "Half-Orc", "Tiefling", "Human"]

        humanRaces = ["Arabic", "Celtic", "Chinese", "Egyptian", "English", "French", "German", "Greek", "Indian", "Japanese", "Mesoamerican", "Niger-Congo", "Norse", "Polynesian", "Roman", "Slavic", "Spanish"]


        r = random.randint(0, len(races) - 1)

        if races[r] == "Human":
            r = random.randint(0, len(humanRaces) - 1)
            return f"HUMAN {humanRaces[r].upper()}"
        else:
            return races[r].upper()
        
    def getName(self):
        fileName = f"RaceNames\{self.race}, {self.sex} .csv"
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
        
    def getClass(self):
        r = random.randint(0,11)
        classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rouge", "Sorcerer", "Warlock", "Wizard"]

        return classes[r]
    
    def getStats(self):
        #Define stats and classes most important two stats
        s = ["Strength", "Dexterity", "Constitution", "Intellegence", "Wisdom", "Charisma"]
        classes_and_stats = {
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

        races_and_stats = {
            "dwarf" : [0,0,2,0,0,0],
            "dragonborn" : [2,0,0,0,0,1],
            "elf" : [0,2,0,0,0,0],
            "gnome" : [0,0,0,2,0,0],
            "halfling" : [0,2,0,0,0,0],
            "half-orc" : [2,0,1,0,0,0],
            "tiefling" : [0,0,0,1,0,2]
        }

        rolls = []
        statsDict = {}

        #Create stats - roll 4d6 and take sum of highest 3
        for i in range(len(s)):
            total = []
            
            for j in range(4):
                r = random.randint(1,6)
                total.append(r)
            
            total.sort()
            total.pop(0)
            rolls.append(sum(total))
        
        #Sort rolls
        rolls.sort()
    
        #Take highest and second highest rolls for important class rolls and leave remainder
        #for 4 other random stats
        most_importantStat = rolls[-1]
        rolls.pop()
        next_mostImportantStat = rolls[-1]
        rolls.pop()

        for i in range(len(s)):
            if i == s.index(classes_and_stats[self.adventuringClass][0]):
                statsDict[s[i]] = most_importantStat
            elif i == s.index(classes_and_stats[self.adventuringClass][1]):
                statsDict[s[i]] = next_mostImportantStat
            else:
                statsDict[s[i]] = rolls[random.randint(0,len(rolls) - 1)]
                rolls.pop(rolls.index(statsDict[s[i]]))

        #Add Racial Bonuses to final stats
        if self.race.lower()[:5] != "human":
            for i in range(6):
                statsDict[s[i]] = statsDict[s[i]] + races_and_stats[self.race.lower()][i]
        else:
            for i in range(6):
                statsDict[s[i]] += 1

        return statsDict

        

        

if __name__ == "__main__":
    app = Character()
    print(f"You are {app.name}, a {app.sex.lower()} {app.race.lower()} who is a {app.adventuringClass}!")
    print(app.stats)

    if len(app.back.siblings) != 40:
        print(f"{app.back.parents} {app.back.birthplace}\n{app.back.name} has {len(app.back.siblings)} siblings.")
        for sibling in app.back.siblings:
            print(sibling.name + ": " + sibling.sex + ", " + sibling.age_compared + ", " + sibling.occupation + ", " + sibling.relationship + '\n' + sibling.status)
            if sibling.status == "Dead":
                print(f"CAUSE OF DEATH: {sibling.cause_of_death}")
            print()
    else:
        print(f"{app.back.parents} {app.back.birthplace}\n{app.back.siblings} ")