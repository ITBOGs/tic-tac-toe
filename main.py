import sys
import random

from QMainWindowDesign import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt5.QtGui import QIcon, QPixmap


class GameControl(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.game_state = False
		self.player_turn = bool(random.randint(0, 1))
		self.player_cross = self.player_turn
		self.count_win_bot = 0
		self.count_win_player = 0
		self.score_bot = 0
		self.score_player = 0

		self.btn_list = [
			self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4,
			self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8,
			self.ui.btn_9
		]

		self.table = [
			[-1, -1, -1],
			[-1, -1, -1],
			[-1, -1, -1]
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

		self.scene_1 = QGraphicsScene()
		self.scene_2 = QGraphicsScene()
		self.scene_3 = QGraphicsScene()
		self.scene_4 = QGraphicsScene()
		self.scene_5 = QGraphicsScene()
		self.ui.scene.setScene(self.scene_1)
		self.ui.scene_2.setScene(self.scene_2)
		self.ui.scene_3.setScene(self.scene_3)
		self.ui.scene_4.setScene(self.scene_4)
		self.ui.scene_5.setScene(self.scene_5)

		pixmap = QPixmap('icon/icon-tic-tac-toe.png')

		self.pixmapitem = self.scene_1.addPixmap(pixmap)
		self.pixmapitem.setScale(0.2)

		pixmap = QPixmap('icon/man.png')
		scene_2_pixmapitem = self.scene_2.addPixmap(pixmap)
		scene_2_pixmapitem.setScale(0.07)

		pixmap = QPixmap('icon/robot.png')
		scene_3_pixmapitem = self.scene_3.addPixmap(pixmap)
		scene_3_pixmapitem.setScale(0.07)

		pixmap = QPixmap('icon/question-sign.png')
		scene_4_pixmapitem = self.scene_4.addPixmap(pixmap)
		scene_5_pixmapitem = self.scene_5.addPixmap(pixmap)
		scene_4_pixmapitem.setScale(0.07)
		scene_5_pixmapitem.setScale(0.07)

	def game_start(self) -> None:
		"""Начало игры\n
		   game_start(self) -> None"""

		self.restart_game()
		self.refresh_score()
		self.ui.btn_game_start.setText('Перезапустить')

	def restart_game(self) -> None:
		"""Подготовка к игре\n
		   restart_game(self) -> None"""

		self.set_btn_state(flag=True)
		self.del_btn_icon()

		self.player_cross = not self.player_cross
		self.player_turn = self.player_cross

		self.table = [  # Таблица полностью отражена от настоящего поля
			[-1, -1, -1],
			[-1, -1, -1],
			[-1, -1, -1]
		]

		btn_style = """
		QPushButton {
		    background-color: transparent;
		    border: none;
		}
		
		QPushButton:hover{
		    background-color: #c0c0c0;
		}
		
		QPushButton:pressed {
		    background-color: #888;
		}"""

		for i in self.btn_list:
			i.setStyleSheet(btn_style)

		self.scene_1.clear()
		self.scene_4.clear()
		self.scene_5.clear()

		if self.player_turn:
			pixmap = QPixmap('icon/man.png')
			pixmapitem = self.scene_1.addPixmap(pixmap)
			pixmapitem.setScale(0.2)

			pixmap = QPixmap('icon/cross.png')
			pixmapitem = self.scene_4.addPixmap(pixmap)
			pixmapitem.setScale(0.05)

			pixmap = QPixmap('icon/circle.png')
			pixmapitem = self.scene_5.addPixmap(pixmap)
			pixmapitem.setScale(0.05)

		else:
			pixmap = QPixmap('icon/robot.png')
			pixmapitem = self.scene_1.addPixmap(pixmap)
			pixmapitem.setScale(0.2)

			pixmap = QPixmap('icon/cross.png')
			pixmapitem = self.scene_5.addPixmap(pixmap)
			pixmapitem.setScale(0.05)

			pixmap = QPixmap('icon/circle.png')
			pixmapitem = self.scene_4.addPixmap(pixmap)
			pixmapitem.setScale(0.05)

	def set_btn_state(self, btn_item: int = 1, flag: bool = False) -> None:
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
			self.table[btn_item // 3][btn_item % 3] = 1
		else:
			self.btn_list[btn_item].setIcon(QIcon('icon/circle.png'))
			self.table[btn_item // 3][btn_item % 3] = 0

		self.player_turn = not self.player_turn
		self.btn_list[btn_item].setDisabled(True)

		self.scene_1.clear()
		pixmap = QPixmap('icon/man.png') if self.player_turn else QPixmap('icon/robot.png')
		pixmapitem = self.scene_1.addPixmap(pixmap)
		pixmapitem.setScale(0.2)

		self.check_win()

	def check_win(self) -> None:
		"""Проверка выигрыша"""

		for y in range(3):  # горизонтально
			flag = not (-1 in self.table[y])

			for x in range(2):
				f = self.table[y][x] == self.table[y][x + 1]
				flag = flag and f

			if flag:
				self.set_win(y * 3 + 1, y * 3 + 2, y * 3 + 3)
				return

		for x in range(3):  # вертикально
			flag = True

			for y in range(2):
				f = self.table[y][x] == self.table[y + 1][x]
				f = f and self.table[y][x] != -1 and self.table[y + 1][x] != -1
				flag = flag and f

			if flag:
				self.set_win(x + 1, 3 + x + 1, 6 + x + 1)
				return

		if self.table[0][0] == self.table[1][1] == self.table[2][2] and self.table[0][0] != -1:
			self.set_win(1, 5, 9)
			return

		if self.table[0][2] == self.table[1][1] == self.table[2][0] and self.table[0][2] != -1:
			self.set_win(7, 5, 3)
			return

	def set_win(self, btn_win_1: int, btn_win_2: int, btn_win_3: int) -> None:
		self.btn_list[btn_win_1 - 1].setStyleSheet("background-color: #5aff51; border: None")
		self.btn_list[btn_win_2 - 1].setStyleSheet("background-color: #5aff51; border: None")
		self.btn_list[btn_win_3 - 1].setStyleSheet("background-color: #5aff51; border: None")

		for i in self.btn_list:
			i.setDisabled(True)

		if self.player_cross and self.table[btn_win_1 // 3][(btn_win_1-1) % 3] == 1:
			self.score_player += 1
		elif not self.player_cross and self.table[btn_win_1 // 3][(btn_win_1-1) % 3] == 0:
			self.score_player += 1
		else:
			self.score_bot += 1

		self.refresh_score()

	def refresh_score(self):
		self.ui.lb_3_score.setText(f"Побед: {self.score_player}")
		self.ui.lb_4_score.setText(f"Побед: {self.score_bot}")

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
