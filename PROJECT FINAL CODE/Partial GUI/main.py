from PyQt5.QtWidgets import QApplication
import sys

from ui import window
 
app = QApplication(sys.argv)
UIWindow = window.windowUI()
UIWindow.main_win.show()

sys.exit(app.exec_())

# After editing the ui file in the Qt Designer, enter into the
# terminal the ff. command to update the UI_MainWindow.py file:
# pyuic5 ui\MainWindow.ui -o ui\UI_MainWindow.py