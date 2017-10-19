import shelve
import os
statList = ['Strength','Dexterity','Constitution','Intelagence','Wisdom','Charisma']
skillList = ['Athletics','Acrobatics','Sleight of Hand','Stealth','Arcana','History','Investigation','Nature','Religion','Animal Handling','Insight','Medicine','Perception','Survival','Deception','Intimidation','Performance','Persuasion']
languageList = ['Dwarvish','Elvish','Giant','Gnomish','Goblin','Halfling','Orc','Abyssal','Celestial','Draconic','Deep Speech','Infernal','Primordial','Sylvan','Undercommon']
STR,DEX,CON,INT,WIS,CHA = 0,1,2,3,4,5
CP,SP,GP,PP = 0,1,2,3 #coin types: copper, sliver, gold, and platinum respectively
class Character(object):
    def __init__(self, Name, path = ''):
        self.db = shelve.open(os.path.join(path,Name),'c',writeback = True)
        if not bool(self.db):
            self.db['name'] = Name
            self.db['alignment'] = ''
            self.db['race'] = ''
            self.db['subrace'] = ''
            self.db['size'] = ''
            self.db['speed'] = ''
            self.db['classes'] = []
            self.db['background'] = ''
            self.db['languages'] = ['Common']
            self.db['savingthrows'] = [False,False,False,False,False,False]
            self.db['skills'] = []
            self.db['spells'] = []
            self.db['features'] = []
            self.db['armor'] = None
            self.db['shield'] = 0
            self.db['weapons'] = []
            self.db['items'] = []
            self.db['money'] = [0,0,0,0]
            self.db['feats'] = []
            self.db['scores'] = [0,0,0,0,0,0]
            self.db['level'] = 0
            self.db['maxhealth'] = 0
            self.db['currhealth'] = 0
            self.db['temphealth'] = 0
            self.db['deathpasses'] = [False, False, False]
            self.db['deathfails'] = [False, False, False]

    def getCharName(self):
        return self.db['name']

    def setAlignment(self,alignment):
        self.db['alignment'] = alignment
    def getAlignment(self):
        return self.db['alignment']

    def setRace(self, race):
        self.db['race'] = race
    def getRace(self):
        return self.db['race']

    def setSubrace(self, subrace):
        self.db['subrace']= subrace
    def getCharSubrace(self):
        return self.db['subrace']

    def setSize(self,size):
        self.db['size'] = size
    def getSize(self):
        return self.db['size']

    def setSpeed(self,speed):
        self.db['speed'] = speed
    def getSpeed(self):
        return self.db['speed']

    def addClass(self,Class):
        if Class in self.db['classes']:
            return;
        self.db['classes'].append(Class)
        self.db.sync()
    def getClasses(self):
        return self.db['classes']

    def setBackground(self,background):
        self.db['background'] = background
    def getBackground(self):
        return self.db['background']

    def addLanguage(self,language):
        self.db['languages'].append(language)
        self.db.sync()
    def getLanguages(self):
        return self.db['languages']

    def addSavingthrow(self, stat):
        self.db['savingthrows'][stat] = True
    def getSavingthrow(self, stat):
        return self.db['savingthrows'][stat]
    def removeSavingthrow(self, stat):
        self.db['savingthrows'][stat] = False
    def getSavingthrows(self):
        return self.db['savingthrows']

    def addSkill(self, skill):
        self.db['skills'].append(skill)
        self.db.sync()
    def getSkills(self):
        return self.db['skills']

    def addSpell(self,spell):
        self.db['spells'].append(spell)
        self.db.sync()
    def getSpells(self):
        return self.db[spells]

    def addFeature(self, feature):
        if feature in self.db['features']:
            self.db['features'].remove(feature)
        self.db['features'].append(feature)
        #self.db.sync()
    def removeFeature(self, feature):
        self.db['features'].remove(feature)
        self.db.sync()
    def getFeatures(self):
        return self.db['features']

    def setArmor(self, armor):
        self.db['armor'] = armor
    def getArmor(self):
        return self.db['armor']

    def setShield(self, shield):
        self.db['shield'] = shield
    def getShield(self):
        return self.db['shield']

    def addWeapon(self, weapon):
        if(not(weapon in self.db["weapons"])):
            self.db['weapons'].append(weapon)
    def removeWeapon(self, weapon):
        if(weapon in self.db["weapons"]):
            self.db['weapons'].remove(weapon)
    def getWeapons(self):
        return self.db['weapons']


    def addItem(self, item):
        self.db['items'].append(item)
        self.db.sync()
    def removeItem(self, item):
        self.db['items'].remove(item)
        self.db.sync()
    def getItems(self):
        return self.db['items']

    def setMoney(self,coin,amnt):
        self.db['money'][coin] = amnt
    def getMoney(self):
        return self.db['money']

    def addFeat(self, feat):
        self.db['feats'].append(feat)
        self.db.sync()
    def getFeats(self):
        return self.db['feats']

    def setScore(self, stat, score):
        self.db['scores'][stat] = score
    def getScore(self,stat):
        return self.db['scores'][stat]
    def getScores(self):
        return self.db['scores']

    def addLevel(self, Class):
        for clss in self.db['classes']:
            if Class.name == clss.name:
                clss.level += 1;
                self.db['level'] += 1
        self.db.sync()
    def getLevel(self):
        return self.db['level']

    def addHealth(self, hp):
        self.db['maxhealth'] += hp
    def getMaxHealth(self):
        return self.db['maxhealth']

    def setCurrHealth(self,hp):
        self.db['currhealth'] = hp
    def getCurrHealth(self):
        return self.db['currhealth']

    def setTempHealth(self,hp):
        self.db['temphealth'] = hp
    def getTempHealth(self):
        return self.db['temphealth']

    def setDeathPass(self, index, boolean):
        self.db['deathpasses'][index] = boolean
    def getDeathPass(self, index):
        return self.db['deathpasses'][index]

    def setDeathFail(self, index, boolean):
        self.db['deathfails'][index] = boolean
    def getDeathFail(self, index):
        return self.db['deathfails'][index]


    def CLOSE(self):
        self.db.close()