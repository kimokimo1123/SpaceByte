from SpaceByte import SpaceByte
import sys
from PySide2 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
spaceByte = SpaceByte()
spaceByte.setGeometry(0, 0, 500, 500)
spaceByte.show()
sys.exit(app.exec_())