import sys
import random

from QMainWindowDesign import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class GameControl(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.game_state = False
		self.player_turn = bool(random.randint(0, 1))
		self.player_cross = self.player_turn

		self.btn_list = [
		                 self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4,
		                 self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8,
		                 self.ui.btn_9
		                 ]

		self.ui.btn_1.clicked.connect(lambda: self.make_turn(1))
		self.ui.btn_2.clicked.connect(lambda: self.make_turn(2))
		self.ui.btn_3.clicked.connect(lambda: self.make_turn(3))
		self.ui.btn_4.clicked.connect(lambda: self.make_turn(4))
		self.ui.btn_5.clicked.connect(lambda: self.make_turn(5))
		self.ui.btn_6.clicked.connect(lambda: self.make_turn(6))
		self.ui.btn_7.clicked.connect(lambda: self.make_turn(7))
		self.ui.btn_8.clicked.connect(lambda: self.make_turn(8))
		self.ui.btn_9.clicked.connect(lambda: self.make_turn(9))

		self.ui.btn_game_start.clicked.connect(lambda: self.game_start())

	def game_start(self) -> None:
		"""Начало игры\n
		   game_start(self) -> None"""

		self.restart_game()

	def restart_game(self) -> None:
		"""Подготовка к игре\n
		   restart_game(self) -> None"""

		self.set_btn_state(flag=True)
		self.del_btn_icon()

	def set_btn_state(self, btn_item: int = 1, flag:  bool = False) -> None:
		"""Устанавливает состояние для определенной кнопки поля или для всех кнопок сразу\n
		   set_btn_state(self, btn_item: int = 1, flag:  bool = False) -> None"""

		flag = not flag
		btn_item -= 1

		if btn_item == 0:
			for btn in self.btn_list:
				btn.setDisabled(flag)
		else:
			self.btn_list[btn_item].setDisabled(flag)

	def make_turn(self, btn_item: int) -> None:
		"""Совершить ход\n
		   make_turn(self, btn_item: int) -> None"""
		btn_item -= 1

		if self.player_turn == self.player_cross:
			self.btn_list[btn_item].setIcon(QIcon('icon/cross.png'))
		else:
			self.btn_list[btn_item].setIcon(QIcon('icon/circle.png'))

		self.player_turn = not self.player_turn
		self.btn_list[btn_item].setDisabled(True)

	def del_btn_icon(self, btn_item: int = 1) -> None:
		"""Удаляет иконку для определенной кнопки поля или для всех кнопок сразу\n
		   del_btn_icon(self, btn_item: int = 1) -> None"""

		btn_item -= 1

		if btn_item == 0:
			for btn in self.btn_list:
				btn.setIcon(QIcon())
		else:
			self.btn_list[btn_item].setIcon(QIcon())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = GameControl()
	window.show()

	sys.exit(app.exec())
