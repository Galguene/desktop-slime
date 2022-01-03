import sys
import random
import time
import math
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (QDialog, QPushButton, QVBoxLayout, QSplashScreen, QApplication)
from screeninfo import get_monitors

width = get_monitors()[0].width
height = get_monitors()[0].height


class Update(QtCore.QRunnable):
    def run(self):
        while 1:
            self.ran1 = random.randrange(1, 4)
            if self.ran1 == 1 or self.ran1 == 3:
                main.idle()
            if self.ran1 == 2:
                main.bounce()


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.b1 = QPushButton('Goodbye Slime')
        self.b1.clicked.connect(qApp.quit)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.b1)
        self.current_pix = QtGui.QPixmap('Sprites/Idle1.png')
        self.splash = QSplashScreen(self.current_pix, QtCore.Qt.WindowStaysOnTopHint)
        self.x = width/2
        self.y = height
        self.splash.move(self.x, self.y)
        self.splash.show()

    def idle(self):
        for i in range(1, 5):
            new_pix = QtGui.QPixmap(f'./Sprites/Idle{i}.png')
            self.splash = QSplashScreen(new_pix, QtCore.Qt.WindowStaysOnTopHint)
            self.splash.update()
            time.sleep(1 / 24)
        for i in range(3, 0, -1):
            new_pix = QtGui.QPixmap(f'./Sprites/Idle{i}.png')
            self.splash = QSplashScreen(new_pix, QtCore.Qt.WindowStaysOnTopHint)
            self.splash.update()
            time.sleep(1 / 24)

    def bounce(self):
        anim = True
        frame = 0
        s = math.pi / 12
        ran = random.randrange(-1, 2)
        while anim:
            s += math.pi / 12
            self.x = self.splash.x() + ran*25
            self.y = self.splash.y() - int(math.sin(s) * 25)
            self.splash.move(self.x, self.y)
            self.splash.update()
            if frame == 22:
                anim = False
            frame += 1
            time.sleep(1 / 24)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    runnable = Update()
    main = Dialog()
    main.show()
    QtCore.QThreadPool.globalInstance().start(runnable)
    sys.exit(app.exec())
