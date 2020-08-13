from PySide2 import QtCore, QtGui, QtWidgets
from Planet import Planet


class SolarSystem(QtWidgets.QWidget):
    scale = 10000000

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setPalette(QtGui.QPalette(QtGui.QColor(100, 100, 100)))
        self.setAutoFillBackground(True)
        self.oImage = QtGui.QImage("background.jpg")
        sImage = self.oImage.scaled(QtCore.QSize(self.width(),self.height()))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))                        
        self.setPalette(palette)
        self.planets =[]
        self.planets.append(Planet('Mercury', 57909175, 56671636.48, 11907903.61, 0.20563069, 0, 4.147727272727273, QtGui.QColor.fromRgb(217, 197, 180), 10))
        self.planets.append(Planet('Venus', 108208930, 108206447.8, 732923.9709, 0.00677323, 0, 1.622222222222222, QtGui.QColor.fromRgb(186, 187, 188), 10))
        self.planets.append(Planet('Earth', 149597890, 149577002.3, 2499813.6534358, 0.01671022, 0, 0.9993428978206111, QtGui.QColor.fromRgb(2, 0, 254), 10))
        self.planets.append(Planet('Mars', 227936640, 226939989.1, 21292092.63, 0.09341233, 0, 0.5312954876273654, QtGui.QColor.fromRgb(255, 0, 0), 10))
        self.planets.append(Planet('Jupiter', 778412020, 777500023.9, 37669428.22, 0.04839266, 0, 0.0843150843150843, QtGui.QColor.fromRgb(204, 153, 102), 20))
        self.planets.append(Planet('Saturn', 1426725400, 1424632080, 77258036.45, 0.05415060, 0, 0.0339503302018417365, QtGui.QColor.fromRgb(229,183,59), 20))
        self.planets.append(Planet('Uranus', 2870972200, 2867776762, 135417184.1, 0.04716771, 0, 0.0119032089746935, QtGui.QColor.fromRgb(31,117,254), 15))
        self.planets.append(Planet('Neptun', 4498252900, 4498087098, 38621414.63, 0.00858587, 0, 0.00606836470040575, QtGui.QColor.fromRgb(0,72,186), 15))

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setStyle(QtCore.Qt.SolidPattern)
        for planet in self.planets:
            brush.setColor((planet.get_color()))
            painter.setBrush(brush)
            painter.drawEllipse(
                planet.get_x()/self.scale+self.width()/2, 
                planet.get_y()/self.scale+self.height()/2,
                planet.diameter,
                planet.diameter)
        brush.setColor(QtCore.Qt.yellow)   
        painter.setBrush(brush)
        painter.drawEllipse(
            2499815/self.scale+self.width()/2, 
            self.height()/2,
            20,
            20)     
        painter.end()
    
    def resizeEvent(self, newSize):
        sImage = self.oImage.scaled(QtCore.QSize(self.width(),self.height()))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))                        
        self.setPalette(palette)