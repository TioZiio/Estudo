
from PySide6.QtCore import Slot 
from PySide6.QtWidgets import QPushButton, QGridLayout
from window import Entry
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
            self.entry: Instancia da classe Entry
            self.label: Instancia da classe Labels
            self._equation: Conterá o valor a esquerda do calculo, enviando para o calculo e entry
        Funções:
            _make_grid_buttons: Cria a garde de botões
            _hability_style_button: Atribui stylo aos botões
            _add_button_to_grid: Cria os Widgets para cada caracter do _grid_mask
            _function_to_button: Configura sinal de click aos botões
            _connect_button_entry: Closure
            _insert_value_button_to_entry: Envia os valores para entry
    """
    def __init__(self, entry: Entry, label, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._grid_mask = [
            ['C','<','^','/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['' ,'0','.','='],
        ]
        self.entry = entry
        self.label = label
        self._equation = ''
        self._make_grid_buttons()

    @property 
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.label.setText(value)

    # grid_buttons.addWidget(Buttons("0"), 0, 0)
    def _make_grid_buttons(self):
        # Função principal que cria, organiza e adiciona função para os botões.
        # Colocam em forma de Exel: ('Linha', row, 'Coluna', col, 'Value', row_values)
        for row, row_values in enumerate(self._grid_mask):
            for col, keys in enumerate(row_values):
                button = self._hability_style_button(keys)
                self._add_button_to_grid(button, row, col)
                self._function_to_button(button)

    def _hability_style_button(self, keys):
        # Habilita a personalização do arquivo styles
        # Botões que não sejam numerais ou vazios, recebem personalização especial
        _btn = Buttons(keys)
        if not Is_num_or_dot(keys) and not Is_empty(keys):
            _btn.setProperty('cssClass', 'specialButton')
        return _btn

    def _add_button_to_grid(self, _btn, _row, _col):
        # Adiciona os botões a grade como em uma planilha de Exel
        self.addWidget(_btn, _row, _col)

    def _function_to_button(self, _btn):
        # Aplica a capacidade dos botões de responder a clickes do mouse
        slot_button = self._connect_button_entry(
            self._insert_value_button_to_entry,
            _btn,
        )
        _btn.clicked.connect(slot_button)

    # Encapsulamento / Closure:
    def _connect_button_entry(self, func, *args, **kwargs):
        @Slot(bool)
        def inner(_):
            func(*args, **kwargs)
        return inner

    def _insert_value_button_to_entry(self, button):
        # Recebe e envia os valores para entry, alem de validar expressoes diferentes de bool
        _button = button.text()
        check_value_entry = self.entry.text() + _button

        if not Is_valid_number(check_value_entry):
            return

        self.entry.insert(_button) # Inserindo texto na entry (caixa de entrada)
    