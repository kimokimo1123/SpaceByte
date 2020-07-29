import sys
import math
import PySide2
from Planet import Planet
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QPainter, QPixmap, QPainterPath
from PySide2.QtCore import QObject, QPointF, QPropertyAnimation, Property

class Universe(QtWidgets.QWidget):
    scale = 7479894.5*1.5

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setPalette(QtGui.QPalette(QtGui.QColor(100, 100, 100)))
        self.setAutoFillBackground(True)
        self.planets =[]
        self.planets.append(Planet('Mercury', 57909175, 56671636.48, 11907903.61, 0.20563069, 0))
        self.planets.append(Planet('Venus', 108208930, 108206447.8, 732923.9709, 0.00677323, 0))
        self.planets.append(Planet('Earth', 149597890, 149577002.3, 2499813.6534358, 0.01671022, 0))
        self.planets.append(Planet('Mars', 227936640, 226939989.1, 21292092.63, 0.09341233, 0))
        self.planets.append(Planet('Jupiter', 778412020, 777500023.9, 37669428.22, 0.04839266, 0))
        self.planets.append(Planet('Saturn', 1426725400, 1424632080, 77258036.45, 0.05415060, 0))
        self.planets.append(Planet('Uranus', 2870972200, 2867776762, 135417184.1, 0.04716771, 0))
        self.planets.append(Planet('Neptun', 4498252900, 4498087098, 38621414.63, 0.00858587, 0))

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen()
        pen.setStyle(QtCore.Qt.SolidLine)
        pen.setWidth(1)
        pen.setBrush(QtCore.Qt.black)
        painter.setPen(pen)
        painter.drawPoint(self.width()/2,self.height()/2)
        for planet in self.planets:
            painter.drawEllipse(QtCore.QPoint(self.width()/2,self.height()/2),planet.grosse_ha/self.scale,planet.kleine_ha/self.scale)

class SpaceByte(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        hello = QtWidgets.QPushButton('Start')
        hello.resize(100, 30)
        biee = QtWidgets.QPushButton('Stop')
        biee.resize(100, 60)
        universe = Universe()
        universe.resize(1000, 1000)
        vLayout = QtWidgets.QVBoxLayout()
        vLayout.addWidget(hello)
        vLayout.addWidget(biee)
        vLayout.addWidget(universe)
        self.setLayout(vLayout)


app = QtWidgets.QApplication(sys.argv)
spaceByte = SpaceByte()
spaceByte.setGeometry(0, 0, 1000, 1000)
spaceByte.show()
sys.exit(app.exec_())