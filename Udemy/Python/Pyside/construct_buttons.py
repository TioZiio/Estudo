
import math
from PySide6.QtCore import Slot , Qt
from PySide6.QtWidgets import QPushButton, QGridLayout
from window import Display, Labels, MainWindow
from variables import MEDIUM_FONT_SIZE
from regulares import Is_num_or_dot, Is_empty, Is_valid_number

class Buttons(QPushButton):
    """
        Classe responsável pela criação de Buttons
        Funções:
            config_style_buttons: Define as caracateristicas de um botão. Neste exemplo
                possui duas formas de definir o tamanho;
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config_style_buttons()
        
    def config_style_buttons(self):
        # Primeira forma de definir o tamanho, com chance de sobreescrever configurações anteriores.
        # Como foi definido alguns estilos no arquivo styles.py, pode ser sobreescrevido (talvez).
        # self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px;') 
        
        # Segunda forma de definir o tamanho, onde e pego a fonte específica e alterando,
        # sem sobreescrever, pq não esta sendo setado um novo stylo.
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(50,50) # Define especificamente o tamanho do bottun.

class Grid_Buttons(QGridLayout):
    """
        Classe responsável pela grade dos butões, logo , como se fosse no Exel.
        Variaveis:
            self._grid_mask: Possui todos os botões que estaram na calculadora. 
            self.display: Instancia da classe display
            self.label: Instancia da classe Labels
            self._equation: Conterá o valor esquerdo e operador do calculo, enviando para a label
            self._operator_left = Valor esquerdo da conta
            self._operator_right = Valor direito da conta
            self._op = representa o operador da conta
            self._equation_initial = representa uma string da label quando estiver vazia.
        Funções:
            _make_grid_buttons: Cria a garde de botões
            _add_button_to_grid: Cria os Widgets para cada caracter do _grid_mask
            _function_to_button: Configura sinal de click aos botões
            _hability_config_special_button: Atribui stylo aos botões
            _act_clicked_button: Adiciona funcionalidade e resposta doos botões, como limpar display
            _config_act_button_special:
            _create_slots_actions: Closure
            _clear: Funcionalidade do Botão "C" de limpeza
            _clicked_button_operator:
            _clicked_button_equal:
            _insert_value_button_to_display: Envia os valores para display
    """
    def __init__(
            self, display: Display, label: Labels, window: MainWindow,
             *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        
        self._grid_mask = [
            ['C','<','^','/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['' ,'0','.','='],
        ]
        self.display = display
        self.label = label
        self.window = window
        self._equation = ''
        self._operator_left = None
        self._operator_right = None
        self._op = None
        self._equation_initial = 'Wait ...'
        self.equation = self._equation_initial
        self._make_grid_buttons()

    @property 
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.label.setText(value)

    def apagarfrase(self):
        print(f'Log Signals: Passou aki o {type(self).__name__}')

    def _signals_keys_connect_button(self):
        self.display.sig_backspace.connect(self.display.backspace)
        self.display.sig_clear.connect(self.apagarfrase)
        self.display.sig_enter.connect(self.apagarfrase)
        self.display.sig_number_dot.connect(self.apagarfrase)

    # grid_buttons.addWidget(Buttons("0"), 0, 0)
    def _make_grid_buttons(self):
        # Função principal que cria, organiza e adiciona função para os botões.
        # Colocam em forma de Exel: ('Linha', row, 'Coluna', col, 'Value', row_values)

        self._signals_keys_connect_button() # sinais dos botões

        for row, row_values in enumerate(self._grid_mask):
            for col, keys in enumerate(row_values):
                button = self._hability_config_special_button(keys)
                self._add_button_to_grid(button, row, col)
                self._function_to_button(button)

    def _add_button_to_grid(self, _btn, _row, _col):
        # Adiciona os botões a grade como em uma planilha de Exel
        self.addWidget(_btn, _row, _col)

    def _function_to_button(self, _btn):
        # Aplica a capacidade dos botões de responder a clickes do mouse
        slot = self._create_slots_actions(
            self._insert_value_button_to_display,
            _btn,
        )
        self._act_clicked_button(_btn, slot)

    def _hability_config_special_button(self, keys):
        # Habilita a personalização do arquivo styles
        # Botões que não sejam numerais ou vazios, recebem personalização especial
        _btn = Buttons(keys)
        if not Is_num_or_dot(keys) and not Is_empty(keys):
            _btn.setProperty('cssClass', 'specialButton')
            self._config_act_button_special(_btn)
        return _btn
    
    def _act_clicked_button(self, _btn, slot): 
        # Adiciona função aos botões, como o botão de limpar a display
        _btn.clicked.connect(slot)

    def _config_act_button_special(self, _btn): #
        _btn_text = _btn.text()
        if _btn_text.upper() == 'C':
            slot = self._create_slots_actions(self._clear, False)
            self._act_clicked_button(_btn, slot)

        if _btn_text.upper() == '<':
            slot = self._act_clicked_button(_btn, self.display.backspace)
        
        elif _btn_text in '+-*/^':
            slot = self._create_slots_actions(self._clicked_button_operator, _btn)
            self._act_clicked_button(_btn, slot)

        elif _btn_text in '=':
            slot = self._create_slots_actions(self._clicked_button_equal, _btn)
            self._act_clicked_button(_btn, slot)
    
    # Encapsulamento / Closure:
    def _create_slots_actions(self, func, *args, **kwargs):
        @Slot()
        def inner(_):
            func(*args, **kwargs)
        return inner

    def _clear(self, verify=True):
        # Função do botão de limpar, é um slot
        # funciona tanto apertando o botão quanto apertando a tecla 'CTRL + C'
        if not verify:
            self._operator_left = None
            self._operator_right = None
            self._op = None
            self.equation = self._equation_initial
        self.display.clear()

    def _clicked_button_operator(self, _btn): #
        btn_text = _btn.text() # operador + - * /
        display_text = self.display.text() # Numero calculado
        self._clear()

        if not Is_valid_number(display_text) and self._operator_left is None: # Valor vazio em display
            self._msg_box('Not Value Inserted')
            return

        if self._operator_left is None:
            self._operator_left = float(display_text)
        
        self._op = btn_text
        self.equation = f'{self._operator_left} {self._op} ??'

    def _clicked_button_equal(self, _btn): #
        display_text = self.display.text()

        if not Is_valid_number(display_text):
            # self.equation = 'Invalid Value' # insere na label
            self._msg_box('Wait a segund number')
            return
        
        self._operator_right = float(display_text)
        self.equation = f'{self._operator_left} {self._op} {self._operator_right}'
        result = 'err'

        try:
            if '^' in self.equation and isinstance(self._operator_left, float):
                result = round(math.pow(self._operator_left, self._operator_right),3)
            else:
                result = round(eval(self.equation),3)
        except ZeroDivisionError as err:
            self.label.setText(
                f'{self._operator_left} {self._op} {self._operator_right} = {0.0}'
            )
        except OverflowError:
            # self.label.setText('Unsupported result') # insere na label
            self._msg_box('Buffer OverFlow')
        else:
            self._clear()
            self.label.setText(f'{self.equation} = {result}')
            self._operator_left = result
            self._operator_right = None

            if result == 'err':
                self._operator_left = None

    def _msg_box(self, _text):
        msg_box = self.window.make_msg_box()
        msg_box.setText(_text)
        msg_box.setWindowTitle('Error')
        msg_box.setIcon(msg_box.Icon.Information)
        msg_box.exec()

    def _insert_value_button_to_display(self, _btn):
        # Recebe e envia os valores para display, alem de validar expressoes diferentes de bool
        _btn_text = _btn.text()
        check_value_display = self.display.text() + _btn_text

        if not Is_valid_number(check_value_display):
            return

        self.display.insert(_btn_text) # Inserindo texto na display (caixa de entrada)
    