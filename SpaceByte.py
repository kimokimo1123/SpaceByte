from Planet import Planet
from SolarSystem import SolarSystem
from PySide2 import QtCore, QtGui, QtWidgets

class SpaceByte(QtWidgets.QWidget):
    tick_size = 5
    def increment_day(self):
        for planet in self.solar_system.planets:
            planet.rotate(self.tick_size)
        self.lcd.display(self.lcd.value() + self.tick_size)
        self.solar_system.update()

    def startButtonEvent(self):
        self.timer.start(10)

    def stopButtonEvent(self):
        self.timer.stop()
    
    def slider_value_changed(self, newValue):
        self.lcd.display(newValue)
        for planet in self.solar_system.planets:
            planet.set_days(newValue)
        self.solar_system.update()

    def scale_slider_value_changed(self, newValue):
        self.solar_system.scale = newValue
        self.solar_system.update()

    def tick_slider_value_changed(self, newValue):
        self.tick_size = newValue/10

    def __init__(self, parent=None):
        max_slider_days = 5000
        QtWidgets.QWidget.__init__(self, parent)
        startButton = QtWidgets.QPushButton('Start')
        startButton.resize(100, 30)
        startButton.clicked.connect(self.startButtonEvent)
        stopButton = QtWidgets.QPushButton('Stop')
        stopButton.resize(50, 60)
        stopButton.clicked.connect(self.stopButtonEvent)
        self.solar_system = SolarSystem()
        self.lcd = QtWidgets.QLCDNumber(7)
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(startButton)
        h_layout.addWidget(stopButton)
        h_layout.addWidget(self.lcd)
        buttons_box = QtWidgets.QWidget()
        buttons_box.setLayout(h_layout)
        buttons_box.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, 
            QtWidgets.QSizePolicy.Fixed)
        vLayout = QtWidgets.QVBoxLayout()
        vLayout.addWidget(buttons_box)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setRange(0, max_slider_days)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.slider_value_changed)
        vLayout.addWidget(self.slider)
        self.scale_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.scale_slider.setRange(500000, 20000000)
        self.scale_slider.setValue(7479894.5)
        self.scale_slider.valueChanged.connect(self.scale_slider_value_changed)
        vLayout.addWidget(self.scale_slider)
        self.tick_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.tick_slider.setRange(1, 200)
        self.tick_slider.setValue(10)
        self.tick_slider.valueChanged.connect(self.tick_slider_value_changed)
        vLayout.addWidget(self.tick_slider)
        vLayout.addWidget(self.solar_system)
        vLayout.setStretch(0,0)
        self.setLayout(vLayout)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.increment_day)
        self.setWindowTitle('SpaceByte')
        self.setWindowIcon(QtGui.QIcon('sun.gif'))