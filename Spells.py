class Spell(object):
    def __init__(self,name,level,cTime,Range,duration,damage):
        self.name = name
        self.level = level
        self.cTime = cTime
        self.Range = Range
        self.duration = duration
        self.damage = damage
        self.prepaired = False

    def __str__(self):
        return self.name.ljust(30)+self.cTime.center(15)+self.range.center(8)+self.damage.center(7)+self.duration.ljust(30)
    
    def getSpellName(self):
        return self.name
    def getSpellLevel(self):
        return self.level
    def getCastTime(self):
        return self.cTime
    def getSpellRange(self):
        return self.Range
    def getSpellDuration(self):
        return self.duration
    def getSpellDamage(self):
        return self.damage

    def getPrepaired(self):
        return self.prepaired
    def setPrepaired(self, boolean):
        self.prepaired = boolean