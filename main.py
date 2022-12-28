import sys

from QMainWindowDesign import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


class GameControl(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = GameControl()
	window.show()

	sys.exit(app.exec())
