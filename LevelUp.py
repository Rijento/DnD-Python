from Character import *
from Feats import *
from Features import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class LevelUp(QWidget):
    def __init__(self,char):
        super().__init__()
        self.char = char
        self.icon = QIcon('icon.png')
        self.char.addLevel()

    def addFeatures(self):
        #go through races
        #go through classes # if neccessary subclasses
        #

    def improveHealth(self):

    def statImprovement(self):

    def addFeats(self):