from Character import *
from random import *
from Races import *
import images
from Classes import *
from Backgrounds import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class characterCreator(QMainWindow):
    def __init__(self, char):
        super().__init__()

        self.font = QFont()
        fontid = QFontDatabase.addApplicationFont(":/URWChanceryL.ttf")
        self.font.setFamily(QFontDatabase.applicationFontFamilies(fontid)[0])
        self.font.setPointSize(16)


        self.icon = QIcon(':/icon.png')

        self.tabs = QTabWidget()
        self.tabs.setFont(self.font)
        self.setCentralWidget(self.tabs)


        self.raceTab = QWidget()
        self.classTab = QWidget()
        self.backgroundTab = QWidget()
        self.alignmentTab = QWidget()
        self.tbifTab = QWidget() #Traits bonds ideals flaws
        self.appearanceTab = QWidget()
        self.skillsTab = QWidget()
        self.statsTab = QWidget()


        self.char = char


        self.initUITemp()
    

    def setFirstLevel(self):
        def rollStats():
            pool = [0,0,0,0,0,0]
            def d6():
                return randint(1,6)
            for i in range(len(pool)):
                temp = [d6(),d6(),d6(),d6(),d6()]
                temp.remove(min(temp))
                temp.remove(min(temp))
                pool[i] = str(sum(temp))
            return pool

        baseScores = [0,0,0,0,0,0]
        if(self.char.getRace() == "Dwarf"):
            self.char.setSpeed(25)
            if self.char.getCharSubrace() == 'Mountain':
                baseScores = [2,0,2,0,0,0]
                self.char.addFeature(darkvision)
                self.char.addFeature(dwarvenResilience)
                self.char.addFeature(dwarvenCombatTraining)
                self.char.addFeature(stonecunning)
                self.char.addFeature(dwarvenArmorTraining)
            else:
                baseScores = [0,0,2,1,0,0]
                self.char.addHealth(1)
                self.char.addFeature(darkvision)
                self.char.addFeature(dwarvenResilience)
                self.char.addFeature(dwarvenCombatTraining)
                self.char.addFeature(stonecunning)
                self.char.addFeature(dwarvenToughness)

        elif(self.char.getRace() == "Elf"):
            self.char.setSpeed(30)
            self.char.addFeature(keenSenses)
            self.char.addFeature(feyAncestry)
            self.char.addFeature(trance)

            if self.char.getCharSubrace() == 'High':
                baseScores = [0,2,0,1,0,0]
                self.char.addFeature(darkvision)
                self.char.addFeature(cantripElf)
                self.char.addFeature(elfWeaponTraining)
            elif self.char.getCharSubrace() == 'Wood':
                baseScores = [0,2,0,0,1,0]
                self.char.setSpeed(35)
                self.char.addFeature(darkvision)
                self.char.addFeature(elfWeaponTraining)
                self.char.addFeature(maskOfTheWild)
            else:
                baseScores = [0,2,0,0,0,1]
                self.char.addFeature(superiorDarkvision)
                self.char.addFeature(drowMagic)
                self.char.addFeature(sunlightSensitivity)
                self.char.addFeature(drowWeaponTraining)

        elif(self.char.getRace() == "Halfling"):
            self.char.setSpeed(25)
            self.char.addFeature(lucky)
            self.char.addFeature(brave)
            self.char.addFeature(halflingNimbleness)
            if self.char.getCharSubrace() == 'Lightfoot':
                baseScores = [0,2,0,0,0,1]
                self.char.addFeature(naturallyStealthy)
            else:
                baseScores = [0,2,1,0,0,0]
                self.char.addFeature(stoutResilience)

        elif(self.char.getRace() == "Human"):
            baseScores= [1,1,1,1,1,1]
            self.char.setSpeed(30)

        elif(self.char.getRace() == "Dragonborn"):
            baseScores = [2,0,0,0,0,1]
            self.char.setSpeed(30)
            if self.char.getCharSubrace() == 'Black':
                self.char.addFeature(draconicAncestryBlack)
                self.char.addFeature(breathWeaponBlack)
                self.char.addFeature(damageResistanceBlackDrag)
            elif self.char.getCharSubrace() == 'Blue':
                self.char.addFeature(draconicAncestryBlue)
                self.char.addFeature(breathWeaponBlue)
                self.char.addFeature(damageResistanceBlueDrag)
            elif self.char.getCharSubrace() == 'Brass':
                self.char.addFeature(draconicAncestryBrass)
                self.char.addFeature(breathWeaponBrass)
                self.char.addFeature(damageResistanceBrassDrag)
            elif self.char.getCharSubrace() == 'Bronze':
                self.char.addFeature(draconicAncestryBronze)
                self.char.addFeature(breathWeaponBronze)
                self.char.addFeature(damageResistanceBronzeDrag)
            elif self.char.getCharSubrace() == 'Copper':
                self.char.addFeature(draconicAncestryCopper)
                self.char.addFeature(breathWeaponCopper)
                self.char.addFeature(damageResistanceCopperDrag)
            elif self.char.getCharSubrace() == 'Gold':
                self.char.addFeature(draconicAncestryGold)
                self.char.addFeature(breathWeaponGold)
                self.char.addFeature(damageResistanceGoldDrag)
            elif self.char.getCharSubrace() == 'Green':
                self.char.addFeature(draconicAncestryGreen)
                self.char.addFeature(breathWeaponGreen)
                self.char.addFeature(damageResistanceGreenDrag)
            elif self.char.getCharSubrace() == 'Red':
                self.char.addFeature(draconicAncestryRed)
                self.char.addFeature(breathWeaponRed)
                self.char.addFeature(damageResistanceRedDrag)
            elif self.char.getCharSubrace() == 'Silver':
                self.char.addFeature(draconicAncestrySilver)
                self.char.addFeature(breathWeaponSilver)
                self.char.addFeature(damageResistanceSilverDrag)
            elif self.char.getCharSubrace() == 'White':
                self.char.addFeature(draconicAncestryWhite)
                self.char.addFeature(breathWeaponWhite)
                self.char.addFeature(damageResistanceWhiteDrag)

        elif(self.char.getRace() == "Gnome"):
            self.char.setSpeed(25)
            self.char.addFeature(darkvision)
            self.char.addFeature(gnomeCunning)
            if self.char.getCharSubrace() == 'Forest':
                baseScores = [0,1,0,2,0,0]
                self.char.addFeature(naturalIllusionist)
                self.char.addFeature(speakWithSmallBeasts)
            else: 
                baseScores = [0,0,0,2,0,0]
                self.char.addFeature(artificersLore)
                self.char.addFeature(tinkerGnome)

        elif(self.char.getRace() == "Half-Elf"):
            baseScores = [0,0,0,0,0,2]
            self.char.setSpeed(30)
            self.char.addFeature(darkvision)
            self.char.addFeature(feyAncestry)

        elif(self.char.getRace() == "Half-Orc"):
            baseScores = [2,0,1,0,0,0]
            self.char.setSpeed(30)
            self.char.addFeature(darkvision)
            self.char.addFeature(menacing)
            self.char.addFeature(relentlessEndurance)
            self.char.addFeature(savageAttacks)

        elif(self.char.getRace() == "Tiefling"):
            baseScores = [0,0,0,1,0,2]
            self.char.setSpeed(30)
            self.char.addFeature(darkvision)
            self.char.addFeature(hellishResistance)
            self.char.addFeature(InfernalLegacy)

        #Class stuff
        if(self.char.getClasses()[0].name == "Barbarian"):
            self.char.addHealth(12)
            self.char.addSavingthrow(STR)
            self.char.addSavingthrow(CON)
            self.char.addFeature(rageL1)
            self.char.addFeature(unarmoredDefenseBarbarian)
        elif(self.char.getClasses()[0].name == "Bard"):
            self.char.addHealth(8)
            self.char.addSavingthrow(DEX)
            self.char.addSavingthrow(CHA)
            self.char.addFeature(spellcastingBardL1)
            self.char.addFeature(bardicInspirationL1)
        elif(self.char.getClasses()[0].name == "Cleric"):
            self.char.addSavingthrow(WIS)
            self.char.addSavingthrow(CHA)
            self.char.addHealth(8)
        elif(self.char.getClasses()[0].name == "Druid"):
            self.char.addHealth(8)
            self.char.addSavingthrow(INT)
            self.char.addSavingthrow(WIS)
            self.char.addFeature(druidic)
            self.char.addFeature(druidicSpellcastingL1)
        elif(self.char.getClasses()[0].name == "Fighter"):
            self.char.addHealth(10)
            self.char.addSavingthrow(STR)
            self.char.addSavingthrow(CON)
            self.char.addFeature(secondWind)
            self.char.addFeature(fightingStyle)
        elif(self.char.getClasses()[0].name == "Monk"):
            self.char.addHealth(8)
            self.char.addSavingthrow(STR)
            self.char.addSavingthrow(DEX)
            self.char.addFeature(unarmoredDefenseMonk)
            self.char.addFeature(martialArtsMonkL1)
        elif(self.char.getClasses()[0].name == "Paladin"):
            self.char.addHealth(10)
            self.char.addSavingthrow(WIS)
            self.char.addSavingthrow(CHA)
            self.char.addFeature(divineSensePaladin)
            self.char.addFeature(PaladinLayOnHandsL1)
        elif(self.char.getClasses()[0].name == "Ranger"):
            self.char.addHealth(10)
            self.char.addSavingthrow(STR)
            self.char.addSavingthrow(DEX)
            self.char.addFeature(favoredEnemyRangerL1)
            self.char.addFeature(naturalExplorerRangerL1)
        elif(self.char.getClasses()[0].name == "Rogue"):
            self.char.addHealth(8)
            self.char.addSavingthrow(DEX)
            self.char.addSavingthrow(INT)
            self.char.addFeature(expertiseRogueL1)
            self.char.addFeature(sneakAttackRogueL1)
            self.char.addFeature(thievesCant)
        elif(self.char.getClasses()[0].name == "Sorcerer"):
            self.char.addHealth(6)
            self.char.addFeature(spellcastingSorcererL1)
            self.char.addFeature(sorcerousOrigin)
        elif(self.char.getClasses()[0].name == "Warlock"):
            self.char.addHealth(8)
            self.char.addSavingthrow(WIS)
            self.char.addSavingthrow(CHA)
            self.char.addFeature(otherworldlyPatron)
            self.char.addFeature(pactMagicWarlockL1)
        elif(self.char.getClasses()[0].name == "Wizard"):
            self.char.addHealth(6)
            self.char.addSavingthrow(INT)
            self.char.addSavingthrow(WIS)
            self.char.addFeature(spellcastingWizardL1)
            self.char.addFeature(arcaneRecovery)

        self.button = QPushButton("Finalize",self)
        self.button.move(375,200)
        self.button.setFont(self.font)
        self.button.setVisible(True)
        statpool = rollStats()
        spl = QLabel("Stat Pool:\nInput one of the following into each box above.\n"+', '.join(statpool)+"\n(Racial bonuses added automatically)",self)
        spl.setWordWrap(True)
        spl.resize(350,150)
        spl.move(250,300)
        spl.setFont(self.font)
        spl.setVisible(True)

        strl = QLabel('STR',self)
        strl.setFont(self.font)
        strl.setAlignment(Qt.AlignHCenter)
        strl.setMaximumWidth(100)
        strl.setMinimumWidth(100)
        strl.move(25,50)
        strl.setVisible(True)
        strle = QLineEdit(self)
        strle.setFont(self.font)
        strle.setAlignment(Qt.AlignHCenter)
        strle.setMaximumWidth(125)
        strle.move(25,100)
        strle.setValidator(QRegExpValidator(QIntValidator(3,18)))
        strle.setVisible(True)

        dexl = QLabel('DEX',self)
        dexl.setFont(self.font)
        dexl.setAlignment(Qt.AlignHCenter)
        dexl.setMaximumWidth(100)
        dexl.setMinimumWidth(100)
        dexl.move(175,50)
        dexl.setVisible(True)
        dexle = QLineEdit(self)
        dexle.setFont(self.font)
        dexle.setAlignment(Qt.AlignHCenter)
        dexle.setMaximumWidth(100)
        dexle.move(175,100)
        dexle.setValidator(QRegExpValidator(QIntValidator(3,18)))
        dexle.setVisible(True)

        conl = QLabel('CON',self)
        conl.setFont(self.font)
        conl.setAlignment(Qt.AlignHCenter)
        conl.setMaximumWidth(100)
        conl.setMinimumWidth(100)
        conl.move(325,50)
        conl.setVisible(True)
        conle = QLineEdit(self)
        conle.setFont(self.font)
        conle.setAlignment(Qt.AlignHCenter)
        conle.setMaximumWidth(100)
        conle.move(325,100)
        conle.setValidator(QRegExpValidator(QIntValidator(3,18)))
        conle.setVisible(True)

        intl = QLabel('INT',self)
        intl.setFont(self.font)
        intl.setAlignment(Qt.AlignHCenter)
        intl.setMaximumWidth(100)
        intl.setMinimumWidth(100)
        intl.move(475,50)
        intl.setVisible(True)
        intle = QLineEdit(self)
        intle.setFont(self.font)
        intle.setAlignment(Qt.AlignHCenter)
        intle.setMaximumWidth(100)
        intle.move(475,100)
        intle.setValidator(QRegExpValidator(QIntValidator(3,18)))
        intle.setVisible(True)

        wisl = QLabel('WIS',self)
        wisl.setFont(self.font)
        wisl.setAlignment(Qt.AlignHCenter)
        wisl.setMaximumWidth(100)
        wisl.setMinimumWidth(100)
        wisl.move(625,50)
        wisl.setVisible(True)
        wisle = QLineEdit(self)
        wisle.setFont(self.font)
        wisle.setAlignment(Qt.AlignHCenter)
        wisle.setMaximumWidth(100)
        wisle.move(625,100)
        wisle.setValidator(QRegExpValidator(QIntValidator(3,18)))
        wisle.setVisible(True)

        chal = QLabel('CHA',self)
        chal.setFont(self.font)
        chal.setAlignment(Qt.AlignHCenter)
        chal.setMaximumWidth(100)
        chal.setMinimumWidth(100)
        chal.move(775,50)
        chal.setVisible(True)
        chale = QLineEdit(self)
        chale.setFont(self.font)
        chale.setAlignment(Qt.AlignHCenter)
        chale.setMaximumWidth(100)
        chale.move(775,100)
        chale.setValidator(QRegExpValidator(QIntValidator(3,18)))
        chale.setVisible(True)

        self.button.clicked.connect(lambda:self.char.setScore(STR,int(strle.text())+int(baseScores[STR])))
        self.button.clicked.connect(lambda:self.char.setScore(DEX,int(dexle.text())+int(baseScores[DEX])))
        self.button.clicked.connect(lambda:self.char.setScore(CON,int(conle.text())+int(baseScores[CON])))
        self.button.clicked.connect(lambda:self.char.setScore(INT,int(intle.text())+int(baseScores[INT])))
        self.button.clicked.connect(lambda:self.char.setScore(WIS,int(wisle.text())+int(baseScores[WIS])))
        self.button.clicked.connect(lambda:self.char.setScore(CHA,int(chale.text())+int(baseScores[CHA])))
        self.button.clicked.connect(lambda:self.char.addLevel(self.char.getClasses()[0]))
        self.button.clicked.connect(lambda:self.close())


    def initUITemp(self):
        self.resize(900, 450)
        self.tabs.addTab(self.raceTab, "Test")

        test = QLabel(self.raceTab)
        test.setText("test")
        test.move(50,50)

        self.show()

    def initUI(self):
        self.setWindowIcon(self.icon)




        self.lbl = QLabel("Select a Race", self.raceTab)
        self.lbl.move(50, 250)
        self.lbl.setFont(self.font)
        self.lbl.setAlignment(Qt.AlignLeft)
        self.lbl.resize(200,150)
        self.lbl.setWordWrap(True)

        self.lbl3 = QLabel("",self.raceTab)
        self.lbl3.move(450,50)
        self.lbl3.setFont(cf)
        self.lbl3.setWordWrap(True)

        # self.button = QPushButton("Finalize",self.raceTab)
        # self.button.setVisible(False)
        # self.button.setFont(cf)
        # self.button2 = QPushButton("Finalize",self.raceTab)
        # self.button2.setFont(cf)
        # self.button2.setVisible(False)

        self.button.move(350,50)
        self.button2.move(350,150)
        
        Race = QComboBox(self.raceTab)
        Race.setFont(self.font)
        Race.addItem("Select a Race")
        Race.addItem(dwarf.getRaceName())
        Race.addItem(elf.getRaceName())
        Race.addItem(halfling.getRaceName())
        Race.addItem(human.getRaceName())
        Race.addItem(dragonborn.getRaceName())
        Race.addItem(gnome.getRaceName())
        Race.addItem(halfelf.getRaceName())
        Race.addItem(halforc.getRaceName())
        Race.addItem(tiefling.getRaceName())
        Race.move(50, 50)
        
        subRace = QComboBox(self.raceTab)
        subRace.setFont(self.font)
        subRace.setVisible(False)
        subRace.addItem("%:ERROR:%")
        subRace.activated.connect(lambda: self.button.setVisible(1))
        subRace.move(200,50)

        Class = QComboBox(self.classTab)
        Class.setFont(self.font)
        Class.setVisible(0)
        Class.addItem("Select a Class")
        Class.addItem(barbarian.name)
        Class.addItem(bard.name)
        Class.addItem(cleric.name)
        Class.addItem(druid.name)
        Class.addItem(fighter.name)
        Class.addItem(monk.name)
        Class.addItem(paladin.name)
        Class.addItem(ranger.name)
        Class.addItem(rogue.name)
        Class.addItem(sorcerer.name)
        Class.addItem(warlock.name)
        Class.addItem(wizard.name)
        Class.move(50,150)

        alignLbl = QLabel(self.classTab)
        alignLbl.setFont(self.font)
        alignLbl.setText("Alignment:")
        alignLbl.move(50, 250)
        alignLbl.setVisible(0)

        alignCreed = QComboBox(self.alignmentTab)
        alignCreed.setVisible(0)
        alignCreed.setFont(self.font)
        alignCreed.addItem("Select Creed")
        alignCreed.addItem("Lawfull")
        alignCreed.addItem("Neutral")
        alignCreed.addItem("Chaotic")
        alignCreed.move(50, 250)

        alignFaction = QComboBox(self.alignmentTab)
        alignFaction.setVisible(0)
        alignFaction.setFont(self.font)
        alignFaction.addItem("Select Faction")
        alignFaction.addItem("Good")
        alignFaction.addItem("Neutral")
        alignFaction.addItem("Evil")

        alignDesc = QLabel(self.alignmentTab)
        alignDesc.setVisible(0)
        alignDesc.setFont(self.font)
        alignDesc.move(300,50)

        background = QComboBox(self)
        background.setVisible(False)
        background.addItem("Drop Down 4")
        background.move(200,150)
        

        
        self.resize(900, 450)
        self.setWindowTitle('Race and Class Selection')
        self.show()

        def onActivated(text):
            if(text == "Dwarf"):
               subRace.setVisible(True) 
               self.lbl.setText("Race Description\n" + (dwarf.getRaceDesc()))
               subRace.clear()
               subRace.addItem("Select a Subrace")
               subRace.addItem("Hill")
               subRace.addItem("Mountain")
            elif(text == "Elf"):
               subRace.setVisible(True)
               self.lbl.setText("Race Description\n" + (elf.getRaceDesc()))
               subRace.clear()
               subRace.addItem("Select a Subrace")
               subRace.addItem("High")
               subRace.addItem("Wood")
               subRace.addItem("Dark")
            elif(text == "Halfling"):
               subRace.setVisible(True)
               self.lbl.setText("Race Description\n" + (halfling.getRaceDesc()))
               subRace.clear() 
               subRace.addItem("Select a Subrace")
               subRace.addItem("Lightfoot")
               subRace.addItem("Stout")
            elif(text == "Human"):
               subRace.setVisible(True)
               self.lbl.setText("Race Description\n" + (human.getRaceDesc()))
               subRace.clear()
               subRace.addItem("Select a Subrace")
               subRace.addItem("None")
               #subRace.addItem("Variant")
            elif(text == "Dragonborn"):
               subRace.setVisible(True) 
               self.lbl.setText("Race Description\n" + (dragonborn.getRaceDesc()))
               subRace.clear()
               subRace.addItem("Select a Subrace")
               subRace.addItem("Black")
               subRace.addItem("Blue")
               subRace.addItem("Brass")
               subRace.addItem("Bronze")
               subRace.addItem("Copper")
               subRace.addItem("Gold")
               subRace.addItem("Green")
               subRace.addItem("Red")
               subRace.addItem("Silver")
               subRace.addItem("White")
            elif(text == "Gnome"):
               subRace.setVisible(True) 
               self.lbl.setText("Race Description\n" + (gnome.getRaceDesc()))
               subRace.clear()
               subRace.addItem("Select a Subrace")
               subRace.addItem("Forest")
               subRace.addItem("Rock")
            elif(text == "Half-Elf"):
               subRace.setVisible(True) 
               self.lbl.setText("Race Description\n" + (halfelf.getRaceDesc()))
               subRace.clear()
               subRace.addItem("Select a Subrace")
               subRace.addItem("None")
            elif(text == "Half-Orc"):
               subRace.setVisible(True) 
               self.lbl.setText("Race Description\n" + (halforc.getRaceDesc()))
               subRace.clear()
               subRace.addItem("Select a Subrace")
               subRace.addItem("None")
            elif(text == "Tiefling"):
               subRace.setVisible(True) 
               self.lbl.setText("Race Description\n" + (halforc.getRaceDesc()))
               subRace.clear()
               subRace.addItem("None")
            else:
                self.lbl.setText("Select a Subrace")
            self.lbl.adjustSize()

        def onActivated2(text):
            if(text == "Barbarian"):
               self.lbl.setText("Class Description:\n" + (barbarian.getClassDesc()))
            elif(text == "Bard"):
               self.lbl.setText("Class Description:\n" + (bard.getClassDesc()))
            elif(text == "Cleric"):
               self.lbl.setText("Class Description\n" + (cleric.getClassDesc()))
            elif(text == "Druid"):
               self.lbl.setText("Class Description\n" + (druid.getClassDesc()))
            elif(text == "Fighter"):
               self.lbl.setText("Class Description\n" + (fighter.getClassDesc()))
            elif(text == "Monk"):
               self.lbl.setText("Class Description\n" + (monk.getClassDesc()))
            elif(text == "Paladin"):
               self.lbl.setText("Class Description\n" + (paladin.getClassDesc()))
            elif(text == "Ranger"):
               self.lbl.setText("Class Description\n" + (ranger.getClassDesc()))
            elif(text == "Rogue"):
               self.lbl.setText("Class Description\n" + (rogue.getClassDesc()))
            elif(text == "Sorcerer"):
               self.lbl.setText("Class Description\n" + (sorcerer.getClassDesc()))
            elif(text == "Warlock"):
               self.lbl.setText("Class Description\n" + (warlock.getClassDesc()))
            elif(text == "Wizard"):
               self.lbl.setText("Class Description\n" + (wizard.getClassDesc()))
            else:
               self.lbl.setText("Select a Class")

        def onActivated3(text):
            if(text == "None"):
                self.lbl3.setText('N/A')
            
            self.lbl.adjustSize()
            self.lbl3.adjustSize()

        def button1pressed():
            if((Race.currentIndex() > 0) and (subRace.currentIndex() > 0)):
                self.char.setRace(Race.currentText())
                Race.setVisible(0)

                self.char.setSubrace(subRace.currentText())
                subRace.setVisible(0)

        def button2pressed():
            if(Class.currentIndex > 0):
                self.char.addClass(classList[Class.currentIndex()-1])
                Class.setVisible(0)

        Race.activated[str].connect(onActivated)
        subRace.activated[str].connect(onActivated3)

        Class.activated[str].connect(onActivated2)
        Class.activated.connect(lambda: self.button2.setVisible(1))

        self.button.clicked.connect(button1pressed)
        self.button.clicked.connect(lambda: self.button.setVisible(0))
        self.button.clicked.connect(lambda: self.lbl.setText('Select a Class'))
        self.button.clicked.connect(lambda: Class.setVisible(1))

        self.button2.clicked.connect(button2pressed)
        self.button2.clicked.connect(lambda:self.lbl.setVisible(0))
        self.button2.clicked.connect(lambda:self.button2.setVisible(0))
        self.button2.clicked.connect(lambda:self.setFirstLevel())

        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
