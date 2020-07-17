import sys
import math
from PySide2 import QtCore, QtGui, QtWidgets

class Universe(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setPalette(QtGui.QPalette(QtGui.QColor(250, 250, 250)))
        self.setAutoFillBackground(True)
    
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.white)
        painter.save()
        painter.translate(0, self.height())
        painter.drawPie(QtCore.QRect(-35, -35, 70, 70), 0, 90 * 16)
        painter.restore()
        painter.setPen(QtCore.Qt.white)
        painter.drawLine(10,10,200,300)
        painter.setBrush(QtCore.Qt.CrossPattern)
        painter.drawEllipse(10,10,110,90)

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