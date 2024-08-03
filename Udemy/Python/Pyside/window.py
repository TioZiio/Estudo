
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit)
from variables import *

class MainWindow(QMainWindow):
    """
        Classe responsável pela criação da janela principal
        Variaveis:
            self.central_widget: variavel que recebe os Widgets;
            self.main_layout: variavel que especifiva o tipo de layout;
        Funções:
            adjust_interface: Atualiza e organiza o tamanho da janela com base nos Widgets;
            add_widget_layout: Adiciona e atualiza os Widgets na janela;
    """
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.central_widget = QWidget()
        # QVBoxLayout e um dos tipos que existe. Neste tipo, os Widgets são adicionados
        # um abaixo do outro, como cascata; 
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        # Titulo da Interface;
        self.setWindowTitle('Calculadora')

    def adjust_interface(self):
        self.adjustSize() # Ajusta a interface de acordo com os widgets presentes
        self.setFixedSize(self.width(), self.height()) # Tamanho da intarface não muda mais;

    def add_widget_layout(self, widget: QWidget):
        self.main_layout.addWidget(widget)

class Entry(QLineEdit):
    """
        Classe responsável pela criação da unica entry (recebe dados) da calculadora;
        Funções:
            config_style_entry: Recebe as configurações e características da caixa de entrada;
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style_entry()
        self.setPlaceholderText('Digite numeros ...') # Frase fixa dentro da entry

    def config_style_entry(self):
        self.setStyleSheet(f'font-size: {FONT_SIZE_ENTRY}px;') # Tamanho da fonte
        self.setMinimumHeight(BIG_FONT_SIZE) # Tamanho da altura
        self.setMinimumWidth(MINIMUM_WIDTH) # Tamanho da largura
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # Define a indentação da Entry
        self.setTextMargins(*TEXT_MARGIN_ENTRY) # Margem das 4 bordas; [left, top, right, bottom]

class Labels(QLabel):
    """
        Classe responsável peal criação da caixa de texto do resultado dos calculos
        Funções:
            config_style_labels: Recebe as configurações e características da caixa de texto;
    """
    def __init__(self, text: str, parent: QWidget | None = None):
        super().__init__(text, parent)
        self.config_style_labels()

    def config_style_labels(self):
        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px;') # Tamanho da fonte
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # Alinha o texto a direita