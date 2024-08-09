
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
            keyPressEvent: Função responsável pela escolha de quais teclas seram permitidas
                    durante a execução da calculadora. Apenas as teclas selecionadas funcionaram
                    enquanto a calculadora estiver aberta.
    """
    # Configura variaveis a capacidade que enviar sinais.
    sig_enter = Signal()
    sig_backspace = Signal()
    sig_clear = Signal()
    sig_number_dot = Signal(str)
    sig_operator = Signal(str)
    sig_invert = Signal()

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
        # Função que define quais teclas podem ser trasmitidas para a calculadora.
        # Apesar de todas as teclas emitirem sinal quando a calculadora esta aberta, apenas
        #       algumas consiguiram ser realmente efetivadas.
        # Essa função deve ser chamada assim para funcionar o evento de sinais.

        text = event.text().strip() # Diz qual tecla foi clicada.
        key = event.key() # Define quais teclas seram escolhidas.
        teclas = Qt.Key # Instancia de Qt.Key

        is_enter = key in [teclas.Key_Enter, teclas.Key_Return]
        is_backspace = key in [teclas.Key_Backspace, teclas.Key_Delete]
        is_clear = key in [teclas.Key_C]
        is_operator = key in [
            teclas.Key_Plus, teclas.Key_Minus, teclas.Key_Asterisk, teclas.Key_Slash, teclas.Key_P
        ]
        is_invert = key in [teclas.Key_N]

        if is_enter or text == '=':
            self.sig_enter.emit() # Emiti um sinal
            return event.ignore

        if is_backspace:
            self.sig_backspace.emit() # Emiti um sinal
            return event.ignore

        if is_clear or text.upper() == 'C':
            self.sig_clear.emit() # Emiti um sinal
            return event.ignore

        if is_operator:
            if text.upper() == 'P':
                text = '^'
            self.sig_operator.emit(text) # Emiti um sinal
            return event.ignore

        if is_clear or text.upper() == 'N':
            self.sig_invert.emit() # Emiti um sinal
            return event.ignore

        if Is_empty(text):
            return event.ignore
        
        if Is_num_or_dot(text):
            self.sig_number_dot.emit(text)
            return event.ignore

        # return super().keyPressEvent(event) -> Libera para todas as teclas serem permitidas.

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