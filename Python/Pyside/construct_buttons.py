
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
            self.window: Instancia da MainWindow (Janela principal)
            self._equation: Conterá o valor esquerdo e operador do calculo, enviando para a label
            self._equation_initial = representa uma string da label quando estiver vazia.
            self._operator_left = Valor esquerdo da conta
            self._operator_right = Valor direito da conta
            self._op = representa o operador da conta
        Funções:
            _signals_keys_connect_button: Função que recebe sinais de clicke do usuário em teclas
                    especificas, como (0-9), (/*-+.).
            _make_grid_buttons: Cria a garde de botões.
            _hability_config_special_button: Atribui stylo aos botões.
            _add_button_to_grid: Cria os Widgets para cada caracter do _grid_mask.
            _function_to_button: Configura sinal de click aos botões.
            _act_clicked_button: Adiciona funcionalidade e resposta doos botões, como limpar display.
            _special_button_config: Função responsável por atribuir funcionalidades para cada botão
                    especial. Dentre eles estão os ( + - * / < C . ).
            _insert_value_button_to_display: Envia os valores para display.
            _create_slots_actions: Closure.
            _clear: Funcionalidade do Botão "C" de limpeza.
            _invert_number: Altera os valores digitados em números negativos.
            _config_operator: Consiste em adicionar o operador a conta. Evitando possiveis erros.
            _config_equal: Configura o butão de igual para que seja o finalizador da conta,
                    trasendo o resultado da conta.
            _msg_box: Para cada erro ou aviso por motivos do User esquecer algum digito ou operador,
                    aperecerá uma janela de aviso com o problema ocorrido.
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
            ['N','0','.','='],
        ]
        self.display = display
        self.label = label
        self.window = window
        self._equation = ''
        self._equation_initial = 'Wait ...'
        self._operator_left = None
        self._operator_right = None
        self._op = None
        
        self.equation = self._equation_initial
        self._make_grid_buttons()

    @property 
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.label.setText(value)

    def _signals_keys_connect_button(self): 
        # Função que conecta os sinais a respectivas funções.
        # Esses sinais são definidos de acordo com cada tecla cliacada.
        # As teclas foram definidas no arquivo window, função KeyPressEvent
        self.display.sig_enter.connect(self._config_equal)
        self.display.sig_backspace.connect(self.display.backspace)
        self.display.sig_clear.connect(self._clear)
        self.display.sig_number_dot.connect(self._insert_value_button_to_display)
        self.display.sig_operator.connect(self._config_operator)
        self.display.sig_invert.connect(self._invert_number)

    def _make_grid_buttons(self):
        # Função principal que cria, organiza e adiciona função para os botões.
        # Colocam em forma de Exel: ('Linha', row, 'Coluna', col, 'Value', row_values)

        self._signals_keys_connect_button() # sinais dos botões

        for row, row_values in enumerate(self._grid_mask):
            for col, button_text in enumerate(row_values):
                button = self._hability_config_special_button(button_text)
                self._add_button_to_grid(button, row, col)
                self._function_to_button(button, button_text)

    def _hability_config_special_button(self, _btn_text):
        # Habilita a personalização do arquivo styles
        # Botões que não sejam numerais ou vazios, recebem personalização especial
        _btn = Buttons(_btn_text)
        if not Is_num_or_dot(_btn_text) and not Is_empty(_btn_text):
            _btn.setProperty('cssClass', 'specialButton')
            self._special_button_config(_btn)
        return _btn

    def _add_button_to_grid(self, _btn, _row, _col):
        # Adiciona os botões a grade como em uma planilha de Exel
        self.addWidget(_btn, _row, _col)

    def _function_to_button(self, _btn, _btn_text):
        # Aplica a capacidade dos botões de responder a clickes do mouse
        slot = self._create_slots_actions(
            self._insert_value_button_to_display,
            _btn_text,
        )
        self._act_clicked_button(_btn, slot)
    
    def _act_clicked_button(self, _btn, slot): 
        # Adiciona função aos botões, como o botão de limpar o display
        _btn.clicked.connect(slot)

    def _special_button_config(self, _btn): 
        # Configura os botões especiais da calculadora (+-*/C.N<).
        # Recebe a classe do botão e atribui um slot que contêm uma funcionalidade
        # Se a funcionalidade precisar de argumento, use da função _create_slots_actions
        #       para  criar um slot separa capaz de receber argumentos.
        _btn_text = _btn.text()
        if _btn_text.upper() == 'C':
            self._act_clicked_button(
                _btn, 
                self._create_slots_actions(self._clear, False)
            )

        elif _btn_text.upper() == '<':
            self._act_clicked_button(_btn, self.display.backspace)

        elif _btn_text.upper() == 'N':
            self._act_clicked_button(_btn, self._invert_number)
        
        elif _btn_text in '+-*/^':
            self._act_clicked_button(
                _btn,
                self._create_slots_actions(self._config_operator, _btn_text)
            )

        elif _btn_text == '=':
            self._act_clicked_button(_btn, self._config_equal)
    
    @Slot()
    def _insert_value_button_to_display(self, _btn_text):
        # Recebe e envia os valores para display.
        check_value_display = self.display.text() + _btn_text

        if not Is_valid_number(check_value_display):
            return

        self.display.insert(_btn_text) # Inserindo texto na display (caixa de entrada)

    # Encapsulamento / Closure:
    @Slot()
    def _create_slots_actions(self, func, *args, **kwargs):
        @Slot(bool)
        def inner(_):
            func(*args, **kwargs)
        return inner

    @Slot()
    def _clear(self, verify=False):
        # Função do botão de limpar, é um slot
        # funciona tanto apertando o botão quanto apertando a tecla 'C'
        if not verify:
            self._operator_left = None
            self._operator_right = None
            self._op = None
            self.equation = self._equation_initial
        self.display.clear()

    @Slot()
    def _invert_number(self):
        # Função que recebe do display o valor digitado e o converte em um número negativo.
        # Depois devolve ao display.
        display_text = self.display.text() # Texto do Display
        self._clear(True)

        if not Is_valid_number(display_text) and Is_empty(display_text): # Valor vazio em display
            self._msg_box('Not Value Inserted')
            return

        new_number = -float(display_text)
        self.display.setText(str(new_number))

    @Slot()
    def _config_operator(self, _btn_text):
        # Função capaz de definir o operador da conta, validando sempre se há um valor digitado.
        # O valor digitado e passado para self._operator_left e depois é atribuido um opeardor.
        display_text = self.display.text() # Numero calculado
        self._clear(True)

        if not Is_valid_number(display_text) and self._operator_left is None: # Valor vazio em display
            self._msg_box('Not Value Inserted')
            return

        if self._operator_left is None:
            self._operator_left = float(display_text)
        
        self._op = _btn_text
        self.equation = f'{self._operator_left} {self._op} ??'

    @Slot()
    def _config_equal(self):
        # Esta função consiste em validar se o segundo valor (self._operator_right) foi digitado.
        # Caso estekja válido, e feito o calculo usando eval() e retornando o resultado.
        # Eval() - Executa uma string como em um terminal python (Tomar cuidado em usar).
        display_text = self.display.text()

        if self._operator_left is None or self._op is None:
            self._msg_box('Values or operators not Inserted')
            return 

        if not Is_valid_number(display_text):
            self._msg_box('Wait a number')
            return
        
        self._operator_right = float(display_text) # Converte str em float para o calculo.
        self.equation = f'{self._operator_left} {self._op} {self._operator_right}'
        result = 'err' # Já atribui um valor para que, caso de erro geral.

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
            self._msg_box('Buffer OverFlow')
        else:
            self.display.clear()
            self.label.setText(f'{self.equation} = {result}')
            self._operator_left = result
            self._operator_right = None

            if result == 'err':
                self._operator_left = None

    def _msg_box(self, _text):
        # Pequena Janela de aviso. Recebe string para avisar o User de um mal uso da calculadora.
        msg_box = self.window.make_msg_box()
        msg_box.setText(_text)
        msg_box.setWindowTitle('Error')
        msg_box.setIcon(msg_box.Icon.Information)
        msg_box.exec()
    