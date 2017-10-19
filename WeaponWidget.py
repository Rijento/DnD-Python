from Character import *
from Weapons import *
import images
from Items import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class WeaponWidget(QWidget):
    AddAnother = pyqtSignal(bool)
    def __init__(self,char,WEAPON = None):
        super().__init__()
        QFontDatabase.addApplicationFont(":/URWChanceryL.ttf")
        self.char = char
        self.resize(450,186)
        self.bg = QPixmap(':/weaponbg.jpg')
        self.initUI(WEAPON)
        self.weapon = WEAPON
        self.setMinimumHeight(186)
        self.addBool = True


    def initUI(self, WEAPON = None):
        sf = QFont()
        sf.setPointSize(18)

        sf.setFamily('URW Chancery L')

        bgl = QLabel(self)
        bgl.setPixmap(self.bg)

        weaponSelect = QComboBox(self)
        weaponSelect.setFont(sf)
        weaponSelect.setStyleSheet('background-color: rgb(230,230,230); border-style: solid; color:black; combobox-popup: 0;')
        weaponSelect.resize(280,40)
        weaponSelect.move(16,21)
        weaponSelect.setMaxVisibleItems(4)
        weaponSelect.addItem("Select Weapon")
        weaponSelect.addItem("Custom")
        for weapon in weaponList:
            weaponSelect.addItem(weapon.getName())

        weaponEdit = QLineEdit(self)
        weaponEdit.setAlignment(Qt.AlignCenter)
        weaponEdit.setFont(sf)
        weaponEdit.setStyleSheet('background-color: transparent; color: black')
        weaponEdit.resize(280,40)
        weaponEdit.move(16,21)
        weaponEdit.hide()

        weaponLabel = QLabel(self)
        weaponLabel.setAlignment(Qt.AlignCenter)
        weaponLabel.setFont(sf)
        weaponLabel.setStyleSheet('background-color: transparent; color: black')
        weaponLabel.resize(280,40)
        weaponLabel.move(16,21)
        weaponLabel.hide()

        typeLabel = QLabel(self)
        typeLabel.setFont(sf)
        typeLabel.font().setPointSize(14)
        typeLabel.setStyleSheet('background-color: transparent; color: black')
        typeLabel.resize(119,40)
        typeLabel.setAlignment(Qt.AlignCenter)
        typeLabel.move(313,22)
        typeLabel.hide()

        typeSelect = QComboBox(self)
        typeSelect.setFont(sf)
        typeSelect.setFont(sf)
        typeSelect.setStyleSheet('background-color: rgb(230,230,230); border-style: solid; color:black; combobox-popup: 0;')
        typeSelect.resize(119,40)
        typeSelect.move(313,22)
        typeSelect.addItem('Select Type')
        typeSelect.addItem('Bludgeoning')
        typeSelect.addItem('Piercing')
        typeSelect.addItem('Slashing')
        typeSelect.addItem('None')
        typeSelect.hide()

        rangeLabel = QLabel(self)
        rangeLabel.setFont(sf)
        rangeLabel.font().setPointSize(14)
        rangeLabel.setStyleSheet('background-color: transparent; color: black')
        rangeLabel.resize(119,40)
        rangeLabel.setAlignment(Qt.AlignCenter)
        rangeLabel.move(17,86)
        rangeLabel.hide()

        rangeEdit = QLineEdit(self)
        rangeEdit.setFont(sf)
        rangeEdit.font().setPointSize(14)
        rangeEdit.setStyleSheet('background-color: transparent; color: black')
        rangeEdit.resize(119,40)
        rangeEdit.setValidator(QRegExpValidator(QRegExp(r'[1-9][0-9]?|[1-9][0-9]{0,2}[\/][1-9][0-9]{0,3}')))
        rangeEdit.setAlignment(Qt.AlignCenter)
        rangeEdit.move(17,86)
        rangeEdit.hide()

        bonusLabel = QLabel(self)
        bonusLabel.setFont(sf)
        bonusLabel.font().setPointSize(14)
        bonusLabel.setStyleSheet('background-color: transparent; color: black')
        bonusLabel.resize(69,40)
        bonusLabel.setAlignment(Qt.AlignCenter)
        bonusLabel.move(152,86)
        bonusLabel.hide()

        damageLabel = QLabel(self)
        damageLabel.setFont(sf)
        damageLabel.setStyleSheet('background-color: transparent; color: black')
        damageLabel.resize(190,40)
        damageLabel.setAlignment(Qt.AlignCenter)
        damageLabel.move(240,86)
        damageLabel.hide()

        numSelect = QSpinBox(self)
        numSelect.setFont(sf)
        numSelect.setStyleSheet("QSpinBox{background-color: rgb(230,230,230); selection-color: black; selection-background-color: transparent;}"
                                "QToolTip{background-color:white;color:black;font-family:URW Chancery L;font-size: 16px}"
                                )
        numSelect.resize(50,40)
        numSelect.setToolTip("Number of Dice")
        numSelect.toolTip()
        numSelect.lineEdit().setStyleSheet('background-color: transparent; color: black')
        numSelect.lineEdit().setReadOnly(True)
        numSelect.setMinimum(0)
        numSelect.setAlignment(Qt.AlignCenter)
        numSelect.move(240,86)
        numSelect.hide()

        diceSelect = QComboBox(self)
        diceSelect.setFont(sf)
        diceSelect.setStyleSheet('background-color: rgb(230,230,230); border-style: solid; color:black; combobox-popup: 0;')
        diceSelect.resize(60, 40)
        diceSelect.move(300, 86)
        diceSelect.addItem('----')
        diceSelect.addItem('d4')
        diceSelect.addItem('d6')
        diceSelect.addItem('d8')
        diceSelect.addItem('d10')
        diceSelect.addItem('d12')
        diceSelect.setMaxVisibleItems(2)
        diceSelect.hide()

        bonusDamageSelect = QSpinBox(self)
        bonusDamageSelect.setFont(sf)
        bonusDamageSelect.setStyleSheet("QSpinBox{background-color: rgb(230,230,230); selection-color: black; selection-background-color: transparent;}"
                                        "QToolTip{background-color:white;color:black;font-family:URW Chancery L;font-size: 16px}"
                                        )
        bonusDamageSelect.resize(60,40)
        bonusDamageSelect.setToolTip("Bonus Damange")
        bonusDamageSelect.setPrefix("+ ")
        bonusDamageSelect.lineEdit().setStyleSheet('background-color: transparent; color: black')
        bonusDamageSelect.lineEdit().setReadOnly(True)
        bonusDamageSelect.setMinimum(0)
        bonusDamageSelect.setAlignment(Qt.AlignCenter)
        bonusDamageSelect.move(370, 86)
        bonusDamageSelect.hide()

        propertyEdit = QTextEdit(self)
        propertyEdit.setStyleSheet('background-color: transparent; color: black')
        propertyEdit.setFont(sf)
        propertyEdit.font().setPointSize(16)
        propertyEdit.resize(450, 60)
        propertyEdit.move(0, 127)
        propertyEdit.hide()

        propertyLabel = QLabel(self)
        propertyLabel.setStyleSheet('background-color: transparent; color: black')
        sf.setPointSize(16)
        propertyLabel.setAlignment(Qt.AlignTop)
        propertyLabel.setFont(sf)
        propertyLabel.font()
        propertyLabel.resize(450, 60)
        propertyLabel.move(0, 127)
        propertyLabel.hide()

        cancelButton = QPushButton(self)
        cancelButton.setText("Cancel")
        cancelButton.setStyleSheet("color: red; background-color: white;")
        cancelButton.resize(60, 20)
        sf.setPointSize(14)
        cancelButton.setFont(sf)
        cancelButton.move(170, 0)
        cancelButton.hide()

        deleteButton = QPushButton(self)
        deleteButton.setText("Delete")
        deleteButton.setStyleSheet("color: red; background-color: white;")
        deleteButton.resize(60, 20)
        sf.setPointSize(14)
        deleteButton.setFont(sf)
        deleteButton.move(170, 0)
        deleteButton.hide()

        saveButton = QPushButton(self)
        saveButton.setText("Save")
        saveButton.setStyleSheet("color: green; background-color: white;")
        saveButton.resize(60, 20)
        sf.setPointSize(14)
        saveButton.setFont(sf)
        saveButton.move(110, 0)
        saveButton.hide()

        def setWeapon(self, WEAPON):
            if (not(WEAPON in self.char.getWeapons())) or self.addBool == 0:
                self.weapon = WEAPON

                weaponSelect.setParent(None)
                weaponSelect.deleteLater()
                weaponEdit.setParent(None)
                weaponEdit.deleteLater()
                weaponLabel.setText(WEAPON.getName())
                weaponLabel.show()

                typeLabel.setText(WEAPON.getWeaponType())
                typeSelect.setParent(None)
                typeSelect.deleteLater()
                typeLabel.show()

                rangeLabel.setText(WEAPON.getWeaponRange())
                rangeEdit.setParent(None)
                rangeEdit.deleteLater()
                rangeLabel.show()

                p_bonus = [0,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6]
                s_mods = (-5,-5,-4,-4,-3,-3,-2,-2,-1,-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10)
                bonusLabel.setText('+ '+str(p_bonus[self.char.getLevel()] + s_mods[self.char.getScore(0)]))
                bonusLabel.show()

                damageLabel.setText(WEAPON.getWeaponDamage())
                bonusDamageSelect.setParent(None)
                bonusDamageSelect.deleteLater()
                numSelect.setParent(None)
                numSelect.deleteLater()
                diceSelect.setParent(None)
                diceSelect.deleteLater()
                damageLabel.show()

                propertyLabel.setText(WEAPON.getWeaponProperties())
                propertyEdit.setParent(None)
                propertyEdit.deleteLater()
                propertyLabel.show()

                cancelButton.setParent(None)
                cancelButton.deleteLater()
                saveButton.setParent(None)
                saveButton.deleteLater()
                deleteButton.show()

                self.char.addWeapon(WEAPON)
                self.AddAnother.emit(self.addBool)

        def addCustom():
            @pyqtSlot()
            def saveButtonPressed():
                if (weaponEdit.text()
                    and typeSelect.currentIndex() != 0
                    and rangeEdit.text()):
                    if (typeSelect.currentIndex() == 4 or diceSelect.currentIndex() == 0): #case for no damage
                        setWeapon(self, Weapon(
                            weaponEdit.text(),
                            "None",
                            rangeEdit.text() + " ft.",
                            "N/A",
                            propertyEdit.toPlainText()))
                    else:
                        setWeapon(self, Weapon(
                            weaponEdit.text(),
                            typeSelect.currentText(),
                            rangeEdit.text() + " ft.",
                            numSelect.text() + diceSelect.currentText() + bonusDamageSelect.text(),
                            propertyEdit.toPlainText()))
            @pyqtSlot()
            def cancelButtonPressed():
                weaponEdit.clear()
                typeSelect.setCurrentIndex(0)
                rangeEdit.clear()
                numSelect.setValue(0)
                diceSelect.setCurrentIndex(0)
                bonusDamageSelect.setValue(0)
                weaponEdit.hide()
                typeSelect.hide()
                rangeEdit.hide()
                numSelect.hide()
                diceSelect.hide()
                saveButton.hide()
                cancelButton.hide()
                bonusDamageSelect.hide()
                weaponSelect.setCurrentIndex(0)
                weaponSelect.show()
            weaponSelect.hide()

            weaponEdit.show()
            typeSelect.show()
            rangeEdit.show()
            numSelect.show()
            diceSelect.show()
            bonusDamageSelect.show()

            saveButton.show()
            saveButton.clicked.connect(saveButtonPressed)
            cancelButton.show()
            cancelButton.clicked.connect(cancelButtonPressed)

        @pyqtSlot(int)
        def handleIndexChange(index):
            if (index == 1):
                addCustom()
            if (index > 1):
                setWeapon(self, weaponList[index-2])

        weaponSelect.currentIndexChanged.connect(handleIndexChange)
        if (WEAPON != None):
            self.addBool = False
            setWeapon(self, WEAPON)

        @pyqtSlot(bool)
        def Another(boolean):
            if boolean:
                self.parentWidget().layout().addWidget(WeaponWidget(self.char))
                self.parentWidget().update()
        self.AddAnother.connect(Another)

        def delself(self):
            self.char.removeWeapon(self.weapon)
            self.setParent(None)
            del self
        deleteButton.clicked.connect(lambda: delself(self))

