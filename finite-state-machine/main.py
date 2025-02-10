from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from GUI_Main import Ui_MainWindow
from statesWindow import Ui_statesWindow
from estopWindow import Ui_estopWindow
from shutdownWindow import Ui_shutdownWindow
from state_machine_3 import StateMachine
from state_bridge import guistate

sb = guistate()
sm = StateMachine(sb)
sm.run_cycle()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

