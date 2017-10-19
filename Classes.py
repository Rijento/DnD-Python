class Class(object):
    def __init__(self, name):
        self.name = name
        self.description = ''
        self.level = 0;
        
    def getClassName(self):
        return self.name

    def setClassDesc(self, desc):
        self.description = desc
    def getClassDesc(self):
        return self.description

    def __eq__(self,other):
        if isinstance(other, type(self)):
            return self.name == other.name
        return False;
    def __str__(self):
        return self.name+'   '+str(self.level)

barbarian = Class('Barbarian')
barbarian.setClassDesc('A Fierce Warrior of primitive background who can enter a battle rage.')

bard = Class('Bard')
bard.setClassDesc('An inspiring magician whose power echoes the music of creation.')

cleric = Class('Cleric')
cleric.setClassDesc('A priestly champion who wields divine magic in service of a higher power.')

druid = Class('Druid')
druid.setClassDesc('A priest of the Old Faith, wielding the powers of nature and adopting animal forms.')

fighter = Class('Fighter')
fighter.setClassDesc('A master of martial combat, skilled with a variety of weapons and armor.')

monk = Class('Monk')
monk.setClassDesc('A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection.')

paladin = Class('Paladin')
paladin.setClassDesc( 'A holly warrior bound to a sacred oath')

ranger = Class('Ranger')
ranger.setClassDesc('A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization.')

rogue = Class('Rogue')
rogue.setClassDesc('A scoundrel who uses stealth and trickery to overcome obstacles and enemies.')

sorcerer = Class('Sorcerer')
sorcerer.setClassDesc('A spellcaster who draws on inherent magic from a gift or bloodline.')

warlock = Class('Warlock')
warlock.setClassDesc('A wielder of magic that is derived from a bargain with an extraplanar entity')

wizard = Class('Wizard')
wizard.setClassDesc('A scholarly magic user capable of manipulating the structures of reality.')

classList = [barbarian,bard,cleric,druid,fighter,monk,paladin,ranger,rogue,sorcerer,warlock,wizard]