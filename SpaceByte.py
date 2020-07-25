import sys
import math
from Planet import Planet
from PySide2 import QtCore, QtGui, QtWidgets

class Universe(QtWidgets.QWidget):
    scale = 7479894.5

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setPalette(QtGui.QPalette(QtGui.QColor(500, 500, 500)))
        self.setAutoFillBackground(True)
        self.planets =[]
        self.planets.append(Planet('Earth', 149597890, 149577002.3, 2499813.6534358, 0.01671022, 0))
        self.planets.append(Planet('Jupiter', 778412020, 777500023.9, 37669428.22, 0.04839266, 0))

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen()
        pen.setStyle(QtCore.Qt.SolidLine)
        pen.setWidth(3)
        pen.setBrush(QtCore.Qt.black)
        painter.setPen(pen)
        for planet in self.planets:
            painter.drawEllipse(QtCore.QPoint(200,200),planet.grosse_ha/self.scale,planet.kleine_ha/self.scale)

class SpaceByte(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        print('1123')
        hello = QtWidgets.QPushButton('Start')
        hello.resize(100, 30)
        biee = QtWidgets.QPushButton('Stop')
        biee.resize(50, 60)
        universe = Universe()
        universe.resize(500, 500)
        vLayout = QtWidgets.QVBoxLayout()
        vLayout.addWidget(hello)
        vLayout.addWidget(biee)
        vLayout.addWidget(universe)
        self.setLayout(vLayout)


        
        


app = QtWidgets.QApplication(sys.argv)
spaceByte = SpaceByte()
spaceByte.setGeometry(100, 100, 500, 355)
spaceByte.show()
sys.exit(app.exec_())