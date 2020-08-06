import sys
import math
from Planet import Planet
from SolarSystem import SolarSystem
from PySide2 import QtCore, QtGui, QtWidgets

class SpaceByte(QtWidgets.QWidget):
    def increment_day(self):
        for planet in self.solar_system.planets:
            planet.rotate_1_day()
        self.solar_system.update()

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
        self.solar_system = SolarSystem()
        self.solar_system.resize(1000, 1000)
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(startButton)
        h_layout.addWidget(stopButton)
        buttons_box = QtWidgets.QWidget()
        buttons_box.setLayout(h_layout)
        buttons_box.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, 
            QtWidgets.QSizePolicy.Fixed)
        vLayout = QtWidgets.QVBoxLayout()
        vLayout.addWidget(buttons_box)
        vLayout.addWidget(self.solar_system)
        vLayout.setStretch(0,0)
        self.angle = 0
        self.setLayout(vLayout)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.increment_day)
 

app = QtWidgets.QApplication(sys.argv)
spaceByte = SpaceByte()
spaceByte.setGeometry(500, 500, 500, 500)
spaceByte.show()
sys.exit(app.exec_())