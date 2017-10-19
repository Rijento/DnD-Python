from Character import *
#from LevelUp import *
from Races import *
from Classes import *
from Backgrounds import *
from Feats import *
from Features import *
from Armor import *
from Weapons import *
from WeaponWidget import *
import images
from Items import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CharacterPage(QGraphicsView):
    def __init__(self,char):
        super().__init__()
        self.font = QFont()
        self.fontid = QFontDatabase.addApplicationFont(":/URWChanceryL.ttf")
        self.font.setFamily(QFontDatabase.applicationFontFamilies(self.fontid)[0])
        self.char = char
        self.scene = QGraphicsScene()
        self.page1 =  QPixmap(':/pg1.jpg')
        self.setScene(self.scene)
        self.initUI()

    def initUI(self):
        self.scene.clear()
        self.scene.addPixmap(self.page1)
        def setCName():
            cname = QLabel(self.char.getCharName())
            self.font.setPointSize(30)
            cname.setFont(self.font)
            cname.setAlignment(Qt.AlignCenter)
            cname.setStyleSheet('background-color:transparent;')
            cname.resize(545,60)
            cname.move(110,150)
            self.scene.addWidget(cname)

        def setCClassLevel():
            classLevel = QLabel('     '.join(str(clss) for clss in self.char.getClasses()))
            self.font.setPointSize(20)
            classLevel.setFont(self.font)
            classLevel.resize(700,30)
            classLevel.move(695,138)
            classLevel.setStyleSheet('background-color:transparent')
            self.scene.addWidget(classLevel)

        def setCRace():
            self.font.setPointSize(20)
            rLabel = QLabel(self.char.getCharSubrace()+' '+self.char.getRace())
            rLabel.setFont(self.font)
            rLabel.resize(290,30)
            rLabel.move(695,205)
            rLabel.setStyleSheet('background-color:transparent')
            self.scene.addWidget(rLabel)

        def setCAllignment():
            self.font.setPointSize(20)
            aLabel = QLabel(self.char.getAlignment())
            aLabel.setFont(self.font)
            aLabel.resize(290,30)
            aLabel.move(985,205)
            aLabel.setStyleSheet('background-color:transparent')
            self.scene.addWidget(aLabel)

        def setArmorClass():
            af = QFont('URW Chancery L')
            af.setPointSize(18)
            af.setBold(True)

            def swap(index = 0):
                if armorSelect.isVisible() and index != 0:
                    #set player armor, display name and stats
                    self.char.setArmor(armorList[index-1])
                    self.char.addItem(armorItems[index-1])
                    self.scene.itemAt(90,1621,QTransform()).setParent(None)
                    setItems()
                    armorSelect.setVisible(0)
                    currentArmor.setText(self.char.getArmor().getArmorName())
                    currentArmor.setVisible(1)
                    delBtn.setVisible(1)
                    setArmorStats()
                    armorSelect.setCurrentIndex(0)
                elif index == -1:
                    self.char.setArmor(None)
                    setArmorStats()
                    armorSelect.setVisible(1)
                    currentArmor.setVisible(0)
                    delBtn.setVisible(0)




            armorSelect = QComboBox()
            armorSelect.setStyleSheet('background-color:white; color:black; combobox-popup: 0;')
            armorSelect.setMaxVisibleItems(8)
            armorSelect.setDuplicatesEnabled(False)
            armorSelect.addItem('Select Your Armor')
            for armor in armorList:
                armorSelect.addItem(armor.getArmorName())
            armorSelect.setMaximumWidth(225)
            armorSelect.setMaximumHeight(30)
            armorSelect.resize(225,30)
            armorSelect.setFont(af)
            armorSelect.currentIndexChanged.connect(swap)
            armorSelect.move(768,314)
            armorSelect.setVisible(0)
            #self.scene.addWidget(armorSelect)
                
            currentArmor = QLabel()
            currentArmor.setStyleSheet('background-color:transparent')
            currentArmor.setMaximumWidth(225)
            currentArmor.setMaximumHeight(30)
            currentArmor.resize(225,30)
            currentArmor.setFont(af)
            currentArmor.move(768,314)
            currentArmor.setVisible(0)
            self.scene.addWidget(currentArmor)

            delBtn = QPushButton('✘')
            delBtn.setFont(af)
            delBtn.setStyleSheet('background-color:white; color:red;')
            delBtn.resize(30,30)
            delBtn.setMaximumWidth(30)
            delBtn.setMaximumHeight(30)
            delBtn.move(1008,314)
            delBtn.clicked.connect(lambda:swap(-1))
            delBtn.setVisible(0)
            self.scene.addWidget(delBtn)

            acb = QLabel()
            acb.setStyleSheet('background-color:transparent;font-family:URW Chancery L;font-size: 25px')
            acb.setMaximumHeight(70)
            acb.resize(70,70)
            acb.setAlignment(Qt.AlignCenter)
            acb.move(589,339)
            self.scene.addWidget(acb)

            dmb = QLabel()
            dmb.setStyleSheet('background-color:transparent')
            dmb.setMaximumHeight(40)
            dmb.resize(80,40)
            dmb.setAlignment(Qt.AlignCenter)
            dmb.move(728,358)
            dmb.setFont(af)
            self.scene.addWidget(dmb)

            ab = QLabel()
            ab.setStyleSheet('background-color:transparent')
            ab.setMaximumHeight(40)
            ab.resize(80,40)
            ab.move(833,358)
            ab.setAlignment(Qt.AlignCenter)
            ab.setFont(af)
            self.scene.addWidget(ab)

            if self.char.getShield():
                shieldbtn = QPushButton('2')
            else:
                shieldbtn = QPushButton('0')
            shieldbtn.setFont(af)
            shieldbtn.setStyleSheet('QToolTip{background-color:white;color:black;font-family:URW Chancery L;font-size: 16px;}\nQPushButton{background-color:transparent; color:black;};')
            shieldbtn.setToolTip('Press To Equip a Shield')
            shieldbtn.resize(80,40)
            shieldbtn.setFlat(1)
            shieldbtn.setMaximumWidth(80)
            shieldbtn.setMaximumHeight(40)
            shieldbtn.move(938,358)
            shieldbtn.clicked.connect(lambda: shieldbtn.setText('2') if shieldbtn.text() == '0' else shieldbtn.setText('0'))
            shieldbtn.clicked.connect(lambda: self.char.setShield(True) if shieldbtn.text() == '2' else self.char.setShield(False))
            self.scene.addWidget(shieldbtn)

            mb = QLineEdit('0')
            mb.setStyleSheet('background-color:transparent')
            mb.setMaximumHeight(40)
            mb.resize(80,40)
            mb.setAlignment(Qt.AlignCenter)
            mb.setFont(af)
            mb.setValidator(QIntValidator())
            mb.move(1043,358)
            self.scene.addWidget(mb)

            def setArmorStats():
                mods = ('ERR','-5','-4','-4','-3','-3','-2','-2','-1','-1','0','0','1','1','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10')
                if self.char.getArmor():
                    if self.char.getArmor().getArmorWeight() == 'light':
                        dmb.setText(mods[self.char.getScore(DEX)])
                    elif self.char.getArmor().getArmorWeight() == 'medium':
                        if int(mods[self.char.getScore(DEX)]) > 2:
                            dmb.setText('2')
                        else:
                            dmb.setText(mods[self.char.getScore(DEX)])
                    else:
                        dmb.setText('0')
                    ab.setText(str(self.char.getArmor().getArmorAC()))
                else:
                    if Class('Barbarian') in self.char.getClasses():
                        dmb.setText(mods[self.char.getScore(DEX)])
                        ab.setText(str(int(mods[self.char.getScore(CON)])+10))
                    elif Class('Monk') in self.char.getClasses() and not self.char.getShield():
                        dmb.setText(mods[self.char.getScore(DEX)])
                        ab.setText(str(int(mods[self.char.getScore(WIS)])+10))
                    else:
                        dmb.setText(mods[self.char.getScore(DEX)])
                        ab.setText('0')
                
                acb.setText(str(int(dmb.text())+int(ab.text())+int(shieldbtn.text())+int(mb.text())))

            shieldbtn.clicked.connect(setArmorStats)
            mb.editingFinished.connect(setArmorStats)

            setArmorStats()

            if self.char.getArmor():
                currentArmor.setText(self.char.getArmor().getArmorName())
                currentArmor.setVisible(1)
                delBtn.setVisible(1)
            else:
                armorSelect.setVisible(1)
            self.scene.addWidget(armorSelect)

        def dispHealth():
            self.font.setPointSize(45)

            maxLabel = QLabel()
            maxLabel.setText(str(self.char.getMaxHealth()))
            maxLabel.setFont(self.font)
            maxLabel.setAlignment(Qt.AlignCenter)
            maxLabel.setStyleSheet('background-color:transparent')
            maxLabel.resize(183,85)
            maxLabel.move(588,681)
            self.scene.addWidget(maxLabel)

            curEdit = QLineEdit()
            curEdit.setText(str(self.char.getCurrHealth()))
            self.font.setPointSize(25)
            curEdit.setFont(self.font)
            curEdit.setStyleSheet('background-color:transparent;border:none')
            curEdit.setAlignment(Qt.AlignCenter)
            curEdit.resize(75, 80)
            curEdit.move(620,534)
            curEdit.setValidator(QIntValidator(0, self.char.getMaxHealth()))
            curEdit.editingFinished.connect(lambda:self.char.setCurrHealth(int(curEdit.text())))
            self.scene.addWidget(curEdit)

            tempEdit = QLineEdit()
            tempEdit.setText(str(self.char.getTempHealth()))
            self.font.setPointSize(25)
            tempEdit.setFont(self.font)
            tempEdit.setStyleSheet('background-color:transparent;border:none')
            tempEdit.setAlignment(Qt.AlignCenter)
            tempEdit.resize(75, 80)
            tempEdit.move(888,534)
            tempEdit.setValidator(QIntValidator())
            tempEdit.editingFinished.connect(lambda:self.char.setTempHealth(int(tempEdit.text())))
            self.scene.addWidget(tempEdit)

            totalLabel = QLabel()
            totalLabel.setText(str(self.char.getTempHealth() + self.char.getCurrHealth()))
            self.font.setPointSize(25)
            totalLabel.setFont(self.font)
            totalLabel.setStyleSheet('background-color:transparent;border:none')
            totalLabel.setAlignment(Qt.AlignCenter)
            totalLabel.resize(75, 80)
            totalLabel.move(754,534)
            self.scene.addWidget(totalLabel)

            tempEdit.editingFinished.connect(lambda:totalLabel.setText(str(self.char.getTempHealth() + self.char.getCurrHealth())))
            curEdit.editingFinished.connect(lambda:totalLabel.setText(str(self.char.getTempHealth() + self.char.getCurrHealth())))

            deathPass1 = QRadioButton()
            deathPass1.setChecked(self.char.getDeathPass(0))
            deathPass1.setStyleSheet('QRadioButton::indicator{width: 22px;height: 22px;}')
            deathPass1.setAttribute(120,True)
            deathPass1.setAutoExclusive(False)
            deathPass1.move(895,687)
            deathPass1.toggled.connect(lambda:self.char.setDeathPass(0, deathPass1.isChecked()))
            self.scene.addWidget(deathPass1)
            deathPass2 = QRadioButton()
            deathPass2.setChecked(self.char.getDeathPass(1))
            deathPass2.setStyleSheet('QRadioButton::indicator{width: 22px;height: 22px;}')
            deathPass2.setAttribute(120,True)
            deathPass2.setAutoExclusive(False)
            deathPass2.move(928,687)
            deathPass2.toggled.connect(lambda:self.char.setDeathPass(1, deathPass2.isChecked()))
            self.scene.addWidget(deathPass2)
            deathPass3 = QRadioButton()
            deathPass3.setChecked(self.char.getDeathPass(2))
            deathPass3.setStyleSheet('QRadioButton::indicator{width: 22px;height: 22px;}')
            deathPass3.setAttribute(120,True)
            deathPass3.setAutoExclusive(False)
            deathPass3.move(961,687)
            deathPass3.toggled.connect(lambda:self.char.setDeathPass(2, deathPass3.isChecked()))
            self.scene.addWidget(deathPass3)

            deathFail1 = QRadioButton()
            deathFail1.setChecked(self.char.getDeathFail(0))
            deathFail1.setStyleSheet('QRadioButton::indicator{width: 22px;height: 22px;}')
            deathFail1.setAttribute(120,True)
            deathFail1.setAutoExclusive(False)
            deathFail1.move(895,726)
            deathFail1.toggled.connect(lambda:self.char.setDeathFail(0, deathFail1.isChecked()))
            self.scene.addWidget(deathFail1)
            deathFail2 = QRadioButton()
            deathFail2.setChecked(self.char.getDeathFail(1))
            deathFail2.setStyleSheet('QRadioButton::indicator{width: 22px;height: 22px;}')
            deathFail2.setAttribute(120,True)
            deathFail2.setAutoExclusive(False)
            deathFail2.move(928,726)
            deathFail2.toggled.connect(lambda:self.char.setDeathFail(1, deathFail2.isChecked()))
            self.scene.addWidget(deathFail2)
            deathFail3 = QRadioButton()
            deathFail3.setChecked(self.char.getDeathFail(2))
            deathFail3.setStyleSheet('QRadioButton::indicator{width: 22px;height: 22px;}')
            deathFail3.setAttribute(120,True)
            deathFail3.setAutoExclusive(False)
            deathFail3.move(961,726)
            deathFail3.toggled.connect(lambda:self.char.setDeathFail(2, deathFail3.isChecked()))
            self.scene.addWidget(deathFail3)

        def dispWeapons():
            weaponScroll = QScrollArea()
            weaponScroll.resize(469, 545)
            weaponScroll.move(565, 1007)
            weaponScroll.setStyleSheet('background-color:transparent')
            weaponWidget = QWidget()
            weaponWidget.setFixedWidth(452)
            weaponLayout = QVBoxLayout()
            weaponLayout.setSpacing(0)
            weaponLayout.setContentsMargins(0,0,0,0)
            weaponWidget.setLayout(weaponLayout)
            @pyqtSlot(int)
            def Another(boolean):
                if (boolean):
                    weaponLayout.addWidget(WeaponWidget(self.char))

            for weapon in self.char.getWeapons():
                temp = WeaponWidget(self.char, weapon)
                temp.AddAnother.connect(Another)
                weaponLayout.addWidget(temp)
            weaponLayout.addWidget(WeaponWidget(self.char))

            weaponScroll.setWidget(weaponWidget)
            weaponScroll.setWidgetResizable(True)
            weaponScroll.setFixedHeight(545)

            self.scene.addWidget(weaponScroll)

        def setFeats():
            featBox = QVBoxLayout()
            featBox.setSpacing(0)
            featBox.setContentsMargins(0,0,0,0)
            featScrl = QScrollArea()
            featScrl.resize(453,415)
            featScrl.setStyleSheet('background-color:transparent')
            featScrl.setFrameStyle(0)
            featScrl.move(1055,505)
            for feat in self.char.getFeats():
                featL = QLabel(feat.getFeatName())
                featL.setMaximumWidth(435)
                featL.setMaximumHeight(30)
                featL.setFont(self.font)
                featL.font().setPointSize(18)
                featL.setToolTip(feat.getFeatDesc())
                featL.setStyleSheet('QToolTip{background-color:white;color:black;font-family:URW Chancery L;font-size: 16px}')
                featL.toolTip()
                featL.setAlignment(Qt.AlignBaseline)
                featL.setAttribute(120,True)
                featBox.addWidget(featL)
            featWidget = QWidget()
            featWidget.setFixedWidth(435)
            featWidget.setLayout(featBox)
            featScrl.setWidget(featWidget)
            self.scene.addWidget(featScrl)

        def setSpeedBox():
            sf = QFont('URW Chancery L')
            sf.setPointSize(35)
            sf.setBold(True)
            sbLabel = QLabel(str(self.char.getSpeed()))
            sbLabel.resize(200,130)
            sbLabel.move(1300,325)
            sbLabel.setAlignment(Qt.AlignCenter)
            sbLabel.setStyleSheet('background-color:transparent')
            sbLabel.setFont(sf)
            self.scene.addWidget(sbLabel)

        def setInitiativeBox():
            ibf = QFont('URW Chancery L')
            ibf.setPointSize(35)
            ibf.setBold(True)
            ibEdit = QLineEdit()
            ibEdit.setPlaceholderText('N/A')
            ibEdit.resize(130,130)
            ibEdit.move(1155,325)
            ibEdit.setAlignment(Qt.AlignCenter)
            ibEdit.setStyleSheet('background-color:transparent;border:none')
            ibEdit.setValidator(QIntValidator())
            ibEdit.setFont(ibf)
            self.scene.addWidget(ibEdit)

        def setFeatures():
            ff = QFont('URW Chancery L')
            ff.setPointSize(18)
            ff.setBold(True)
            featureBox = QVBoxLayout()
            featureBox.setSpacing(0)
            featureBox.setContentsMargins(0,0,0,0)
            featureScrl = QScrollArea()
            featureScrl.resize(450,955)
            featureScrl.setStyleSheet('background-color:transparent')
            featureScrl.setFrameStyle(0)
            featureScrl.move(1055,990)
            for feature in self.char.getFeatures():
                featureL = QLabel(feature.getFeatureName())
                featureL.setMaximumWidth(435)
                featureL.setMaximumHeight(30)
                featureL.setFont(ff)
                featureL.setToolTip(feature.getFeatureDesc())
                featureL.setStyleSheet('QToolTip{background-color:white;color:black;font-family:URW Chancery L;font-size: 16px}')
                featureL.setAlignment(Qt.AlignBaseline)
                featureL.setAttribute(120,True)
                featureBox.addWidget(featureL)
            featureWidget = QWidget()
            featureWidget.setFixedWidth(435)
            featureWidget.setLayout(featureBox)
            featureScrl.setWidget(featureWidget)
            self.scene.addWidget(featureScrl)

        def setCurrency():
            cf = QFont()
            cf.setPointSize(25)
            cf.setFamily('URW Chancery L')
            def updateCurrency(coin,num):
                if not num:
                    num = 0
                else:
                    num = int(num)
                self.char.setMoney(coin,num)

            cp = QLineEdit(str(self.char.getMoney()[CP]))
            cp.setFont(cf)
            cp.resize(110,60)
            cp.setStyleSheet('background-color:transparent;border:none')
            cp.editingFinished.connect(lambda: updateCurrency(CP,cp.text()))
            cp.setAlignment(Qt.AlignCenter)
            cp.setValidator(QIntValidator())
            cp.move(575,1627)
            self.scene.addWidget(cp)
            sp = QLineEdit(str(self.char.getMoney()[SP]))
            sp.setFont(cf)
            sp.resize(110,60)
            sp.setStyleSheet('background-color:transparent;border:none')
            sp.editingFinished.connect(lambda: updateCurrency(SP,sp.text()))
            sp.setAlignment(Qt.AlignCenter)
            sp.setValidator(QIntValidator())
            sp.move(575,1693)
            self.scene.addWidget(sp)
            gp = QLineEdit(str(self.char.getMoney()[GP]))
            gp.setFont(cf)
            gp.resize(110,60)
            gp.setStyleSheet('background-color:transparent;border:none')
            gp.editingFinished.connect(lambda: updateCurrency(GP,gp.text()))
            gp.setAlignment(Qt.AlignCenter)
            gp.setValidator(QIntValidator())
            gp.move(575,1762)
            self.scene.addWidget(gp)
            pp = QLineEdit(str(self.char.getMoney()[PP]))
            pp.setFont(cf)
            pp.resize(110,60)
            pp.setStyleSheet('background-color:transparent;border:none')
            pp.editingFinished.connect(lambda: updateCurrency(PP,pp.text()))
            pp.setAlignment(Qt.AlignCenter)
            pp.setValidator(QIntValidator())
            pp.move(575,1828)
            self.scene.addWidget(pp)

        def setItems():
            itf = QFont('URW Chancery L')
            itf.setPointSize(18)
            itf.setBold(True)

            itemBox = QHBoxLayout()
            itemBox.setSpacing(0)
            itemBox.setContentsMargins(0,0,0,0)
            itemBox.setSizeConstraint(QLayout.SetFixedSize)

            nameBox = QVBoxLayout()
            nameBox.setSpacing(0)
            nameBox.setContentsMargins(0,0,0,0)
            nameBox.setSizeConstraint(QLayout.SetFixedSize)
            legend = QLabel('Name')
            legend.resize(215,30)
            legend.setMaximumWidth(215)
            legend.setMinimumWidth(215)
            legend.setMaximumHeight(30)
            legend.setMinimumHeight(30)
            legend.setFont(itf)
            legend.setAlignment(Qt.AlignHCenter)
            legend.setStyleSheet('background-color:transparent')
            nameBox.addWidget(legend)

            quantityBox = QVBoxLayout()
            quantityBox.setSpacing(0)
            quantityBox.setContentsMargins(0,0,0,0)
            legend = QLabel('Amount')
            legend.resize(85,30)
            legend.setMaximumWidth(85)
            legend.setMinimumWidth(85)
            legend.setMaximumHeight(30)
            legend.setMinimumHeight(30)
            legend.setFont(itf)
            legend.setAlignment(Qt.AlignHCenter)
            legend.setStyleSheet('background-color:transparent')
            quantityBox.addWidget(legend)

            weightBox = QVBoxLayout()
            weightBox.setSpacing(0)
            weightBox.setContentsMargins(0,0,0,0)
            legend = QLabel('Weight')
            legend.resize(97,30)
            legend.setMaximumWidth(97)
            legend.setMinimumWidth(97)
            legend.setMaximumHeight(30)
            legend.setMinimumHeight(30)
            legend.setFont(itf)
            legend.setAlignment(Qt.AlignHCenter)
            legend.setStyleSheet('background-color:transparent')
            weightBox.addWidget(legend)

            delBox = QVBoxLayout()
            delBox.setSpacing(0)
            delBox.setContentsMargins(0,0,0,0)
            legend = QLabel('')
            legend.resize(30,30)
            legend.setMaximumWidth(30)
            legend.setMinimumWidth(30)
            legend.setMaximumHeight(30)
            legend.setMinimumHeight(30)
            legend.setStyleSheet('background-color:transparent')
            delBox.addWidget(legend)

            def updateWeight(LEdit):
                index = quantityBox.indexOf(LEdit)-1
                if LEdit.isModified():
                    self.char.getItems()[index].setItemQuantity(int(LEdit.text()))
                    weightBox.itemAt(index+1).widget().setText(str(self.char.getItems()[index].getItemWeight())+' lb.')
            
            def addCustomItem():
                name = QLineEdit()
                name.setPlaceholderText('Enter Item Name')
                name.setMaximumHeight(30)
                name.setFont(itf)
                name.setAlignment(Qt.AlignHCenter)
                name.setStyleSheet('background-color:transparent;border:none')
                nameBox.addWidget(name)

                quantity = QLabel('1')
                quantity.resize(85,30)
                quantity.setMaximumWidth(85)
                quantity.setMaximumHeight(30)
                quantity.setFont(itf)
                quantity.setAlignment(Qt.AlignHCenter)
                quantity.setStyleSheet('background-color:transparent;border: none')
                quantityBox.addWidget(quantity)

                weight = QLineEdit()
                weight.setPlaceholderText('# of lbs')
                weight.resize(100,30)
                weight.setMaximumWidth(97)
                weight.setMaximumHeight(30)
                weight.setFont(itf)
                weight.setAlignment(Qt.AlignHCenter)
                weight.setValidator(QDoubleValidator())
                weight.setStyleSheet('background-color:transparent')
                weightBox.addWidget(weight)

                delBtn = QPushButton('✔')
                delBtn.setFont(itf)
                delBtn.setStyleSheet('background-color:white; color:green;')
                delBtn.resize(30,30)
                delBtn.setMaximumWidth(30)
                delBtn.setMaximumHeight(30)
                delBox.addWidget(delBtn)
                delBtn.clicked.connect(lambda: self.char.addItem(Item(name.text(),float(weight.text()))))
                delBtn.clicked.connect(lambda: __setItem__(Item(name.text(),float(weight.text()))))
                delBtn.clicked.connect(addItemDropdown)
                last = nameBox.count()-1
                delBtn.clicked.connect(lambda: nameBox.takeAt(last).widget().setParent(None))
                delBtn.clicked.connect(lambda: quantityBox.takeAt(last).widget().setParent(None))
                delBtn.clicked.connect(lambda: weightBox.takeAt(last).widget().setParent(None))
                delBtn.clicked.connect(lambda: delBox.takeAt(last).widget().setParent(None))
            
            def addNewItem(index):
                last = nameBox.count()-1
                nameBox.takeAt(last).widget().setVisible(0)
                quantityBox.takeAt(last).widget().setParent(None)
                weightBox.takeAt(last).widget().setParent(None)
                delBox.takeAt(last).widget().setParent(None)
                if index == 1:
                    addCustomItem()
                else:
                    item = itemList[index-2]
                    self.char.addItem(item)
                    __setItem__(item)
                    addItemDropdown()


            def delItem(index):
                nameBox.takeAt(index).widget().setParent(None)
                quantityBox.takeAt(index).widget().setParent(None)
                weightBox.takeAt(index).widget().setParent(None)
                delBox.takeAt(index).widget().setParent(None)
                item = self.char.getItems()[index-1]
                self.char.removeItem(item)               

            def __setItem__(item):
                name = QLabel(item.getItemName())
                name.resize(215,30)
                name.setMaximumWidth(215)
                name.setMaximumHeight(30)
                name.setFont(itf)
                name.setAlignment(Qt.AlignHCenter)
                name.setStyleSheet('background-color:transparent')
                nameBox.addWidget(name)

                quantity = QLineEdit(str(item.getItemQuantity()))
                quantity.resize(85,30)
                quantity.setMaximumWidth(85)
                quantity.setMaximumHeight(30)
                quantity.setFont(itf)
                quantity.setAlignment(Qt.AlignHCenter)
                quantity.setStyleSheet('background-color:transparent;border: none')
                quantity.setValidator(QIntValidator())
                quantityBox.addWidget(quantity)
                quantity.editingFinished.connect(lambda: updateWeight(quantity))

                weight = QLabel(str(item.getItemWeight())+' lb.')
                weight.resize(100,30)
                weight.setMaximumWidth(97)
                weight.setMaximumHeight(30)
                weight.setFont(itf)
                weight.setAlignment(Qt.AlignHCenter)
                weight.setStyleSheet('background-color:transparent')
                weightBox.addWidget(weight)

                delBtn = QPushButton('✘')
                delBtn.setFont(itf)
                delBtn.setStyleSheet('background-color:white; color:red;')
                delBtn.resize(30,30)
                delBtn.setMaximumWidth(30)
                delBtn.setMaximumHeight(30)
                delBox.addWidget(delBtn)
                delBtn.clicked.connect(lambda: delItem(delBox.indexOf(delBtn)))

            def addItemDropdown():
                newItem = QComboBox()
                newItem.addItem('Add an Item')
                newItem.addItem('Custom')
                for item in itemList:
                    newItem.addItem(item.getItemName())
                newItem.resize(215,30)
                newItem.setVisible(0);
                newItem.setMaximumWidth(215)
                newItem.setMaximumHeight(30)
                newItem.setStyleSheet('background-color:white; color:black; combobox-popup: 0;')
                newItem.setFont(itf)
                newItem.setMaxVisibleItems(8)
                nameBox.addWidget(newItem)
                newItem.currentIndexChanged.connect(addNewItem)
                quantityBox.addWidget(QLabel(' '))
                weightBox.addWidget(QLabel(' '))
                delBox.addWidget(QLabel(' '))
                newItem.setVisible(1)

            for item in self.char.getItems():
                __setItem__(item)
            addItemDropdown()

            nameWidget = QWidget()
            nameWidget.setLayout(nameBox)

            quantityWidget = QWidget()
            quantityWidget.setLayout(quantityBox)

            weightWidget = QWidget()
            weightWidget.setLayout(weightBox)

            delWidget = QWidget()
            delWidget.setLayout(delBox)

            itemBox.addWidget(nameWidget)
            itemBox.addWidget(quantityWidget)
            itemBox.addWidget(weightWidget)
            itemBox.addWidget(delWidget)

            itemWidget = QWidget()
            itemWidget.setLayout(itemBox)

            itemScroll = QScrollArea()
            itemScroll.resize(445,334)
            itemScroll.move(80,1611)
            itemScroll.setStyleSheet('background-color:transparent; color:black')
            itemScroll.setWidget(itemWidget)
            itemScroll.setObjectName("Items")

            self.scene.addWidget(itemScroll)        

        def setPBonus():
            bonus = ['ERR','+2','+2','+2','+2','+3','+3','+3','+3','+4','+4','+4','+4','+5','+5','+5','+5','+6','+6','+6','+6']
            bf = QFont('URW Chancery L')
            bf.setPointSize(25)
            bf.setBold(True)
            pbLabel = QLabel(bonus[self.char.getLevel()])
            pbLabel.resize(80,50)
            pbLabel.move(125,322)
            pbLabel.setAlignment(Qt.AlignCenter)
            pbLabel.setStyleSheet('background-color:transparent')
            pbLabel.setFont(bf)

            self.scene.addWidget(pbLabel)

        def setStats():
            sf = QFont()
            sf.setPointSize(25)
            sf.setFamily('URW Chancery L')

            strength = QLabel(str(self.char.getScore(STR)))
            strength.setFont(sf)
            strength.resize(80,45)
            strength.setStyleSheet('background-color:transparent')
            strength.setAlignment(Qt.AlignCenter)
            strength.move(125,535)
            self.scene.addWidget(strength)

            dexterity = QLabel(str(self.char.getScore(DEX)))
            dexterity.setFont(sf)
            dexterity.resize(80,45)
            dexterity.setStyleSheet('background-color:transparent')
            dexterity.setAlignment(Qt.AlignCenter)
            dexterity.move(125,711)
            self.scene.addWidget(dexterity)

            constitution = QLabel(str(self.char.getScore(CON)))
            constitution.setFont(sf)
            constitution.resize(80,45)
            constitution.setStyleSheet('background-color:transparent')
            constitution.setAlignment(Qt.AlignCenter)
            constitution.move(125,887)
            self.scene.addWidget(constitution)

            intelligence = QLabel(str(self.char.getScore(INT)))
            intelligence.setFont(sf)
            intelligence.resize(80,45)
            intelligence.setStyleSheet('background-color:transparent')
            intelligence.setAlignment(Qt.AlignCenter)
            intelligence.move(125,1063)
            self.scene.addWidget(intelligence)

            wisdom = QLabel(str(self.char.getScore(WIS)))
            wisdom.setFont(sf)
            wisdom.resize(80,45)
            wisdom.setStyleSheet('background-color:transparent')
            wisdom.setAlignment(Qt.AlignCenter)
            wisdom.move(125,1239)
            self.scene.addWidget(wisdom)

            charisma = QLabel(str(self.char.getScore(CHA)))
            charisma.setFont(sf)
            charisma.resize(80,45)
            charisma.setStyleSheet('background-color:transparent')
            charisma.setAlignment(Qt.AlignCenter)
            charisma.move(125,1415)
            self.scene.addWidget(charisma)

        def setStatMods():
            sf = QFont()
            sf.setPointSize(18)
            sf.setFamily('URW Chancery L')
            mods = ('ERR','-5','-4','-4','-3','-3','-2','-2','-1','-1','+0','+0','+1','+1','+2','+2','+3','+3','+4','+4','+5','+5','+6','+6','+7','+7','+8','+8','+9','+9','+10')
            
            strMod = QLabel(mods[int(self.char.getScore(STR))])
            strMod.setFont(sf)
            strMod.resize(80,45)
            strMod.setStyleSheet('background-color:transparent')
            strMod.setAlignment(Qt.AlignCenter)
            strMod.move(125,475)
            self.scene.addWidget(strMod)

            dexMod = QLabel(mods[int(self.char.getScore(DEX))])
            dexMod.setFont(sf)
            dexMod.resize(80,45)
            dexMod.setStyleSheet('background-color:transparent')
            dexMod.setAlignment(Qt.AlignCenter)
            dexMod.move(125,651)
            self.scene.addWidget(dexMod)

            conMod = QLabel(mods[int(self.char.getScore(CON))])
            conMod.setFont(sf)
            conMod.resize(80,45)
            conMod.setStyleSheet('background-color:transparent')
            conMod.setAlignment(Qt.AlignCenter)
            conMod.move(125,827)
            self.scene.addWidget(conMod)

            intMod = QLabel(mods[int(self.char.getScore(INT))])
            intMod.setFont(sf)
            intMod.resize(80,45)
            intMod.setStyleSheet('background-color:transparent')
            intMod.setAlignment(Qt.AlignCenter)
            intMod.move(125,1003)
            self.scene.addWidget(intMod)

            wisMod = QLabel(mods[int(self.char.getScore(WIS))])
            wisMod.setFont(sf)
            wisMod.resize(80,45)
            wisMod.setStyleSheet('background-color:transparent')
            wisMod.setAlignment(Qt.AlignCenter)
            wisMod.move(125,1179)
            self.scene.addWidget(wisMod)

            chaMod = QLabel(mods[int(self.char.getScore(CHA))])
            chaMod.setFont(sf)
            chaMod.resize(80,45)
            chaMod.setStyleSheet('background-color:transparent')
            chaMod.setAlignment(Qt.AlignCenter)
            chaMod.move(125,1355)
            self.scene.addWidget(chaMod)

        def setSkills():
            def addCircle(x,y):
                self.scene.addEllipse(x,y,15,15,QColor('black'),QColor('black'))
            def addDiamond(x,y):
                diamondPoly = QPolygonF()
                diamondPoly.append(QPoint(0,8))
                diamondPoly.append(QPoint(8,0))
                diamondPoly.append(QPoint(16,8))
                diamondPoly.append(QPoint(8,16))
                diamond = QGraphicsPolygonItem(diamondPoly)
                diamond.setBrush(QColor('black'))
                diamond.setX(x)
                diamond.setY(y)
                self.scene.addItem(diamond)

            x,y = 267,484
            for throw in self.char.getSavingthrows():
                if throw:
                    addDiamond(x,y)
                y += 176

            if 'Athletics' in self.char.getSkills():
                addCircle(267,510)
            if 'Acrobatics' in self.char.getSkills():
                addCircle(267,687)
            if 'Sleight of Hand' in self.char.getSkills():
                addCircle(267,711)
            if 'Stealth' in self.char.getSkills():
                addCircle(267,736)
            if 'Arcana' in self.char.getSkills():
                addCircle(267,1039)
            if 'History' in self.char.getSkills():
                addCircle(267,1064)
            if 'Investigation' in self.char.getSkills():
                addCircle(267,1088)
            if 'Nature' in self.char.getSkills():
                addCircle(267,1113)
            if 'Religion' in self.char.getSkills():
                addCircle(267,1137)
            if 'Animal Handling' in self.char.getSkills():
                addCircle(267,1216)
            if 'Insight' in self.char.getSkills():
                addCircle(267,1240)
            if 'Medicine' in self.char.getSkills():
                addCircle(267,1264)
            if 'Perception' in self.char.getSkills():
                addCircle(267,1289)
            if 'Survival' in self.char.getSkills():
                addCircle(267,1314)
            if 'Deception' in self.char.getSkills():
                addCircle(267,1392)
            if 'Intimidation' in self.char.getSkills():
                addCircle(267,1416)
            if 'Performance' in self.char.getSkills():
                addCircle(267,1441)
            if 'Persuasion' in self.char.getSkills():
                addCircle(267,1465)

        def setInspBtn():
            btn = QFont()
            btn.setPointSize(35)
            ibtn = QPushButton('')
            ibtn.setFont(btn)
            ibtn.setAttribute(120,True)
            ibtn.setFlat(1)
            ibtn.resize(80,50)
            ibtn.move(125,395)
            self.scene.addWidget(ibtn)
            def inspBtnPressed(self):
                if ibtn.text() == '':
                    ibtn.setText('✔')
                else:
                    ibtn.setText('')
            ibtn.clicked.connect(inspBtnPressed)

        setCName()
        setCClassLevel()
        setCRace()
        setCAllignment()
        setPBonus()
        dispHealth()
        setArmorClass()
        dispWeapons()
        setSpeedBox()
        setInitiativeBox()
        setFeats()
        setFeatures()
        setItems()
        setCurrency()
        setStats()
        setStatMods()
        setSkills()
        setInspBtn()