from Character import *
from Creator import *
from page1 import *
from page2 import *
from page3 import *
from WeaponWidget import *
#from LevelUp import *
from random import *
from Races import *
from Classes import *
from Backgrounds import *
from Feats import *
from Features import *
from Armor import *
from Weapons import *
from Items import *
import images
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import ctypes

FILE_ATTRIBUTE_HIDDEN = 0x02

if os.name != 'nt':
    path = r'.Characters' 
else:
    path = r'Characters'
 
if not os.path.exists(path):
    os.makedirs(path)
    
if os.name == 'nt':
    ret = ctypes.windll.kernel32.SetFileAttributesW(path,FILE_ATTRIBUTE_HIDDEN)
    if not ret: 
        raise ctypes.WinError()

class characterSelect(QWidget):
    def __init__(self):
        super().__init__()
        f = QFont()
        f.setFamily('URW Chancery L')
        f.setPointSize(16)
        self.icon = QIcon(':/icon.png')
        self.name = ''
        self.le = QLineEdit()
        self.le.setPlaceholderText('Character Name')
        self.le.setAlignment(Qt.AlignCenter)
        self.le.setFont(f)
        self.btn = QPushButton('Done')
        self.btn.setFont(f)
        self.layout = QVBoxLayout(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Character Select')
        self.setWindowIcon(self.icon)
        self.layout.addWidget(self.le)
        self.layout.addWidget(self.btn)
        self.btn.clicked.connect(self.setName)        
        self.show()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setName(self):
        self.name = self.le.text()
        self.close()


class CharacterSheet(QMainWindow):
    def __init__(self,char):
        super().__init__()
        self.char = char
        self.title = 'Character Sheet'
        self.window = QTabWidget()
        self.setCentralWidget(self.window)
        self.page1 = CharacterPage(char)
        self.page2 = SpellsPage(char)
        self.page3 = NotesPage(char)
        self.icon = QIcon(':/icon.png')
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.window.addTab(self.page1, 'Character')
        self.window.addTab(self.page2, 'Spellcasting')
        self.window.addTab(self.page3, 'Notes & Misc')
        clf = QFont()
        clf.setFamily('URW Chancery L')
        clf.setPointSize(20)
        self.window.setFont(clf)



        self.show()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = characterSelect()
    app.exec_()
    Player = Character(str(first.name),path)
    if Player.getLevel() == 0:
        second = characterCreator(Player)
        app.exec_()
    sheet = CharacterSheet(Player)
    app.exec_()

    
    Player.CLOSE()
    sys.exit()