from SpaceByte import SpaceByte
import sys
from PySide2 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
spaceByte = SpaceByte()
<<<<<<< HEAD
spaceByte.setGeometry(0, 0, 1500, 1500)
=======
spaceByte.setGeometry(0, 0, 1500, 1000)
>>>>>>> parent of ef04ee9... background implemented
spaceByte.show()
sys.exit(app.exec_())