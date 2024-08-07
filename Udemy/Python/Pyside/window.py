
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QMessageBox
)
from variables import *
from regulares import Is_empty, Is_num_or_dot

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

    def make_msg_box(self):
        return QMessageBox(self)

class Display(QLineEdit):
    """
        Classe responsável pela criação da unica Display (recebe dados) da calculadora;
        Funções:
            config_style_display: Recebe as configurações e características da caixa de entrada;
    """

    sig_enter = Signal()
    sig_backspace = Signal()
    sig_clear = Signal()
    sig_number_dot = Signal(str | int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style_display()
        self.setPlaceholderText('Digite numeros ...') # Frase fixa dentro da display

    def config_style_display(self):
        self.setStyleSheet(f'font-size: {FONT_SIZE_DISPLAY}px;') # Tamanho da fonte
        self.setMinimumHeight(BIG_FONT_SIZE) # Tamanho da altura
        self.setMinimumWidth(MINIMUM_WIDTH) # Tamanho da largura
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # Define a indentação da display
        self.setTextMargins(*TEXT_MARGIN_DISPLAY) # Margem das 4 bordas; [left, top, right, bottom]

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip() 
        key = event.key()
        teclas = Qt.Key

        is_enter = key in [teclas.Key_Enter, teclas.Key_Return]
        is_backspace = key in [teclas.Key_Backspace, teclas.Key_Delete]
        is_clear = key in [teclas.Key_C]

        if is_enter or text == '=':
            print(text)
            self.sig_enter.emit() # Emiti um sinal
            return event.ignore

        if is_backspace:
            print(text)
            self.sig_backspace.emit() # Emiti um sinal
            return event.ignore

        if is_clear or text.lower() == 'c':
            print(text)
            self.sig_clear.emit() # Emiti um sinal
            return event.ignore

        if Is_empty(text):
            return event.ignore
        
        if Is_num_or_dot(text):
            print(text)
            self.sig_number_dot.emit(text)
            return event.ignore

        # return super().keyPressEvent(event)
        # retorna para todas as teclas, sem o return, apenas as tecla selecionadas, seram ativadas 

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