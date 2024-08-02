
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QPushButton, QVBoxLayout, QWidget, QGridLayout, QMainWindow
)


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widgets = QWidget() # Tela de fundo;
        self.setCentralWidget(self.central_widgets)
        self.setWindowTitle('The Fist')

        # Buttons
        self.button = self.make_buttons('Button 1', '80px')
        self.button2 = self.make_buttons('Button 2', '80px')
        self.button3 = self.make_buttons('Button 3', '80px')

        # Layout
        self.layout = QGridLayout()
        self.central_widgets.setLayout(self.layout)
        
        buttons_list = [
            (self.button, 1, 1, 1, 2),
            (self.button2, 2, 1, 1, 2),
            (self.button3, 3, 1, 1, 1),
        ]
        for info in buttons_list:
            self.make_layout(*info)

        # Status Bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Loading')
        self.menu = self.menuBar().addMenu('Vai vai')

        # Sinal de click de button
        self.primeira_acao = self.menu.addAction('Ja foi')
        self.primeira_acao.triggered.connect(self.mudar_status_bar)

        # Sinal de marcação
        self.segunda_acao = self.menu.addAction('Passei')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.completou)

        # Sinal de passar o mouse
        self.terceira_acao = self.menu.addAction('Passei')
        self.terceira_acao.setCheckable(True)
        self.terceira_acao.hovered.connect(self.completou)

        # Signal são responsaveis por observar ações, como triggered, toggled e hovered, clicked
        # Sinal do click do mouse
        self.button3.clicked.connect(self.completou)
    
    @Slot()
    def mudar_status_bar(self):
        self.status_bar.showMessage('Eira carai')

    @Slot()
    def completou(self):
        print('Marcou? ', self.segunda_acao.isChecked())

    
    def make_buttons(self, texto, tamanho):
        btn = QPushButton(texto)
        btn.setStyleSheet(f'font-size: {tamanho}')
        btn.show() # Ativa o button;
        return btn

    def make_layout(self, btn, x=1, y=1, wd=1, hg=1):
        layt = self.layout.addWidget(btn, x, y, wd, hg)
        return layt

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Window()
    janela.show()
    app.exec()