import sys
import math
from Planet import Planet
from PySide2 import QtCore, QtGui, QtWidgets

class Universe(QtWidgets.QWidget):
    scale = 7479894.5

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
        pen.setWidth(3)
        pen.setBrush(QtCore.Qt.black)
        painter.setPen(pen)
        for planet in self.planets:
            painter.drawPoint(
                ((planet.grosse_ha/self.scale*math.cos(math.radians(planet.winkel_fi)))+self.height()/2), 
                ((planet.kleine_ha/self.scale*math.sin(math.radians(planet.winkel_fi)))+self.width()/2))
        

class SpaceByte(QtWidgets.QWidget):
    def Drawplanet(self):
        self.universe.planets[0].winkel_fi += 4.090909090909091
        self.universe.planets[1].winkel_fi += 1.6
        self.universe.planets[2].winkel_fi += 0.9863013698630137
        self.universe.planets[3].winkel_fi += 0.5240174672489083
        self.universe.planets[4].winkel_fi += 0.0831600831600832
        self.universe.planets[5].winkel_fi += 0.0334852571853781
        self.universe.planets[6].winkel_fi += 0.0117401513175059
        self.universe.planets[7].winkel_fi += 0.0059852364168385
        self.universe.update()

    def startButtonEvent(self):
        print ("Start Button clicked")
        self.timer.start(2)

    def stopButtonEvent(self):
        print ("Stop Button clicked")
        self.timer.stop()
        self.close()

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        startButton = QtWidgets.QPushButton('Start')
        startButton.resize(100, 30)
        startButton.clicked.connect(self.startButtonEvent)
        stopButton = QtWidgets.QPushButton('Stop')
        stopButton.resize(50, 60)
        stopButton.clicked.connect(self.stopButtonEvent)
        self.universe = Universe()
        self.universe.resize(1000, 1000)
        vLayout = QtWidgets.QVBoxLayout()
        vLayout.addWidget(startButton)
        vLayout.addWidget(stopButton)
        vLayout.addWidget(self.universe)
        self.angle = 0
        self.setLayout(vLayout)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Drawplanet)
 

app = QtWidgets.QApplication(sys.argv)
spaceByte = SpaceByte()
spaceByte.setGeometry(1500, 500, 1000, 1000)
spaceByte.show()
sys.exit(app.exec_())