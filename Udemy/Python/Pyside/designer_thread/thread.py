# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thread.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(400, 300)
        font = QFont()
        font.setPointSize(15)
        MainWidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(MainWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.d20_p = QPushButton(MainWidget)
        self.d20_p.setObjectName(u"d20_p")

        self.gridLayout.addWidget(self.d20_p, 2, 0, 1, 1)

        self.d20_e = QPushButton(MainWidget)
        self.d20_e.setObjectName(u"d20_e")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setUnderline(False)
        self.d20_e.setFont(font1)
        self.d20_e.setAutoExclusive(False)

        self.gridLayout.addWidget(self.d20_e, 2, 1, 1, 1)

        self.player = QLabel(MainWidget)
        self.player.setObjectName(u"player")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setItalic(True)
        font2.setUnderline(False)
        self.player.setFont(font2)
        self.player.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.player, 1, 0, 1, 1)

        self.enemy = QLabel(MainWidget)
        self.enemy.setObjectName(u"enemy")
        self.enemy.setFont(font2)
        self.enemy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.enemy, 1, 1, 1, 1)

        self.winner = QLabel(MainWidget)
        self.winner.setObjectName(u"winner")
        self.winner.setMaximumSize(QSize(16777215, 100))
        font3 = QFont()
        font3.setPointSize(35)
        self.winner.setFont(font3)
        self.winner.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.winner, 0, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Treino_designer", None))
        self.d20_p.setText(QCoreApplication.translate("MainWidget", u"D20", None))
        self.d20_e.setText(QCoreApplication.translate("MainWidget", u"D20", None))
        self.player.setText(QCoreApplication.translate("MainWidget", u"PLAYER", None))
        self.enemy.setText(QCoreApplication.translate("MainWidget", u"ENEMY", None))
        self.winner.setText(QCoreApplication.translate("MainWidget", u"Game", None))
    # retranslateUi

