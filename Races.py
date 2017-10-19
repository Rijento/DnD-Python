class Race(object):
    def __init__(self, name):
        self.name = name
        self.subraces = []
        self.description = ''

    def getRaceName(self):
        return self.name

    def addSubrace(self, subrace):
        self.subraces.append(subrace)
    def getSubraces(self):
        return self.subraces

    def setRaceDesc(self,desc):
        self.description = desc
    def getRaceDesc(self):
        return self.description

dwarf = Race('Dwarf')
dwarf.addSubrace('Hill')
dwarf.addSubrace('Mountain')
dwarf.setRaceDesc('Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal. Though they stand well under 5 feet tall, dwarves are so broad and compact that they can weigh as much as a human standing nearly two feet taller. their courage and endurance are also easily a match for any of the larger folk.\n')

elf = Race('Elf')
elf.addSubrace('High')
elf.addSubrace('Wood')
elf.addSubrace('Dark')
elf.setRaceDesc('Like the branches of a young tree, elves are flexible in the face of danger. They trust in diplomacy and compromise to resolve differences before they escalate to violence. They have been known to retreat from intrusions into their woodland homes, confidant thaty they can simply wait the invaders out. But when the need arises, elves reveal a stern martial side, demonstrating skill with sword, bow, and strategy.\n')

halfling = Race('Halfling')
halfling.addSubrace('Lightfoot')
halfling.addSubrace('Stout')
halfling.setRaceDesc('The diminutive halflings survive in a world full of larger creatures by avoiding notice or, barring that, avoiding offense. Standing about 3 feet tall, they appear relatively harmless and so have managed to survive for centuries in the shadow of empires and on the edges of wars and political strife.\n')

human = Race('Human')
human.addSubrace('Variant')
human.setRaceDesc('Humans are the most adaptable and ambiguous people among the common races. They have widely varying tastes, morals, and customs in the many different lands where they have settled. When they settle, though, they stay: they build cities to last for the ages, and kingdoms that can fersist for long centuries.\n')

dragonborn = Race('Dragonborn')
dragonborn.addSubrace('Black')
dragonborn.addSubrace('Blue')
dragonborn.addSubrace('Brass')
dragonborn.addSubrace('Bronze')
dragonborn.addSubrace('Copper')
dragonborn.addSubrace('Gold')
dragonborn.addSubrace('Green')
dragonborn.addSubrace('Red')
dragonborn.addSubrace('Silver')
dragonborn.addSubrace('White')
dragonborn.setRaceDesc('Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with fearful incomprehension. Some dragonborn are faithful servants to true dragons, others form the ranks of soldiers in great wars, and still others find themselves adrift, with no clear calling in life.\n')

gnome = Race('Gnome')
gnome.addSubrace('Forest')
gnome.addSubrace('Rock')
gnome.setRaceDesc('As far as gnomes are concerned, being alive is a wonderful thing, and they squeeze every ounce of enjoyment out of their three to five centuries of life. Humans might wonder about getting bored over the course of such a long life, and elves take plenty of time to savor the buties of the world in their long years, but gnomes seem to worry that even with all that time, they can\'t get enough of the things they want to do and see.\n')

halfelf = Race('Half-Elf')
halfelf.setRaceDesc( 'Walking in two worlds but truly belonging to neither, half-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tem[ered by the refined senses, love of nature, and artistic tastes of the elves. Some half-elves live among humans, and some live among the elves; many, however, choose lives of solitary wandering or join with other misfits and outcasts in the adventuring life.\n')

halforc = Race('Half-Orc')
halforc.setRaceDesc('Some half-orcs rise to become proud chiefs of orc tribes, their human blood giving them an edge over their full blooded orc rivals. Some venture into the world to prove their worth among humans and other more civilized races. Many of these become adventures, achieving greatness for their mighty deeds and notoriety for their barbaric customs and savage fury.\n')

tiefling = Race('Tiefling')
tiefling.setRaceDesc('Years of dealing with mistrust does leave its mark on most tieflings, and they respond to it in different ways. Some choose to live up to the wicked stereotype, but others are virtuous. Most are simply very aware of how people respond to them. After dealing with this mistrust throughout youth, a tiefling often developes the ability to overcome prejudice through charm or ingimidation.\n')

raceList = [dwarf,elf,halfling,human,dragonborn,gnome,halfelf,halforc,tiefling]