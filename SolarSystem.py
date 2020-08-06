from PySide2 import QtCore, QtGui, QtWidgets
from Planet import Planet


class SolarSystem(QtWidgets.QWidget):
    scale = 7479894.5

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setPalette(QtGui.QPalette(QtGui.QColor(100, 100, 100)))
<<<<<<< HEAD
        self.setAutoFillBackground(False)
        self.oImage = QtGui.QImage("background.jpg")
        sImage = self.oImage.scaled(QtCore.QSize(self.width(),self.height()))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))                        
        self.setPalette(palette)
        self.planets =[]
        self.planets.append(Planet('Mercury', 57909175, 56671636.48, 11907903.61, 0.20563069, 0, 4.147727272727273, QtCore.Qt.gray))
        self.planets.append(Planet('Venus', 108208930, 108206447.8, 732923.9709, 0.00677323, 0, 1.622222222222222, QtCore.Qt.yellow))
        self.planets.append(Planet('Earth', 149597890, 149577002.3, 2499813.6534358, 0.01671022, 0, 0.9993428978206111, QtCore.Qt.blue))
        self.planets.append(Planet('Mars', 227936640, 226939989.1, 21292092.63, 0.09341233, 0, 0.5312954876273654, QtCore.Qt.red))
        self.planets.append(Planet('Jupiter', 778412020, 777500023.9, 37669428.22, 0.04839266, 0, 0.0843150843150843, QtGui.QColor.fromRgb(204, 153, 102)))
        self.planets.append(Planet('Saturn', 1426725400, 1424632080, 77258036.45, 0.05415060, 0, 0.0339503302018417365, QtGui.QColor.fromRgb(229,183,59)))
        self.planets.append(Planet('Uranus', 2870972200, 2867776762, 135417184.1, 0.04716771, 0, 0.0119032089746935, QtGui.QColor.fromRgb(31,117,254)))
        self.planets.append(Planet('Neptun', 4498252900, 4498087098, 38621414.63, 0.00858587, 0, 0.00606836470040575, QtGui.QColor.fromRgb(0,72,186)))
=======
        self.setAutoFillBackground(True)
        self.planets =[]
        self.planets.append(Planet('Mercury', 57909175, 56671636.48, 11907903.61, 0.20563069, 0, 4.090909090909091))
        self.planets.append(Planet('Venus', 108208930, 108206447.8, 732923.9709, 0.00677323, 0, 1.6))
        self.planets.append(Planet('Earth', 149597890, 149577002.3, 2499813.6534358, 0.01671022, 0, 0.9863013698630137))
        self.planets.append(Planet('Mars', 227936640, 226939989.1, 21292092.63, 0.09341233, 0, 0.5240174672489083))
        self.planets.append(Planet('Jupiter', 778412020, 777500023.9, 37669428.22, 0.04839266, 0, 0.0831600831600832))
        self.planets.append(Planet('Saturn', 1426725400, 1424632080, 77258036.45, 0.05415060, 0, 0.0334852571853781))
        self.planets.append(Planet('Uranus', 2870972200, 2867776762, 135417184.1, 0.04716771, 0, 0.0117401513175059))
        self.planets.append(Planet('Neptun', 4498252900, 4498087098, 38621414.63, 0.00858587, 0, 0.0059852364168385))
>>>>>>> parent of ef04ee9... background implemented

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen()
        pen.setStyle(QtCore.Qt.SolidLine)
<<<<<<< HEAD
        pen.setWidth(5)
=======
        pen.setWidth(3)
        pen.setBrush(QtCore.Qt.black)
        painter.setPen(pen)
>>>>>>> parent of ef04ee9... background implemented
        for planet in self.planets:
            pen.setBrush(planet.get_color())
            painter.setPen(pen)
            painter.drawPoint(
                (planet.get_x()/self.scale+self.width()/2), 
                (planet.get_y()/self.scale+self.height()/2))
        painter.end()