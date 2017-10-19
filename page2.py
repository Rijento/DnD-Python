from Character import *
#from LevelUp import *
from random import *
from Races import *
from Classes import *
from Backgrounds import *
from Feats import *
from Features import *
from Armor import *
#from Weapons import *
import images
from Items import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SpellsPage(QGraphicsView):
    def __init__(self,char):
        super().__init__()
        self.char = char
        self.scene = QGraphicsScene()
        self.page = QPixmap(':/spells.jpg')
        self.setScene(self.scene)
        self.initUI()

    def initUI(self):
        font = QFont('URW Chancery L')
        font.setPointSize(18)
        font.setBold(True)
        self.scene.addPixmap(self.page)