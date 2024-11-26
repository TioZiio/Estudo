
from time import sleep
from random import randint, shuffle, choice
from functools import partial
from thread import Ui_MainWidget

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal, Slot, QThread, QTimer

def random_number():
    numb = [str(n) for n in range(1, 21)]
    shuffle(numb)
    value = str(choice(numb))
    return [numb, value]

def modo_um_a_um():
    # Modo antigo... O número passa um a um:
    # _valor = randint(1, 20)
    # value = '0'
    # self.started.emit(value)
    # sleep(1.5)
    # for i in range(1,(_valor + 1)):
    #     value = str(i)
    #     sleep(0.4)
    #     self.progressed.emit(value)
    # self.finished.emit(value)
    ...

class WorkPlayer(QObject):

    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWorkPlayer(self):
        _values = random_number()
        self.started.emit(_values[1])
        sleep(1.5)
        for i in _values[0]:
            sleep(0.8)
            self.progressed.emit(i)
            if i == _values[1]:
                break
        self.finished.emit(_values[1])

class WorkEnemy(QObject):

    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWorkEnemy(self):
        _values = random_number()
        self.started.emit(_values[1])
        sleep(1.5)
        for i in _values[0]:
            sleep(0.8)
            self.progressed.emit(i)
            if i == _values[1]:
                break
        self.finished.emit(_values[1])

class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.start_game()

        self.d20_p.clicked.connect(self.D20_player)
        self.d20_e.clicked.connect(self.D20_enemy)

    def start_game(self):
        self._player = 'Arthur'
        self._enemy = 'Goblin'

        self._d20Player = 0
        self._d20Enemy = 0

        self._verify_Player = False
        self._verify_Enemy = False

        self.player.setText('Arthur')
        self.enemy.setText('Goblin')
        self.winner.setText('Game') # new game

    def D20_player(self):
        """
        Para instancias do Work e Thread, e necessario objetos e não variaveis.
        Quando é criado uma nova thread o python tenta esquecer a Thread antiga,
            gerando um erro. Por isso precisa ser um objeto (self).
        
        Explicando cada objeto:
            self.player = Representa a Label 01 - Player;
            self._player = Representa o nome do jogador, aprensetado na Label;
            self.d20_p = Representa o Botão 01 - Player;
            _d20Player = Representa o valor final sorteado do Player;
            _verify_Player = Representa que o Player possui um valor, e pode ser comparado;
        """
        self._workPlayer = WorkPlayer()
        self._threadPlayer = QThread()

        self.all_thread(
            self._workPlayer, self._threadPlayer, self._workPlayer.doWorkPlayer,
            self.player, self._player, self.d20_p, '_d20Player', '_verify_Player'
        )

    def D20_enemy(self):
        """
        Explicando cada objeto:
            self.enemy = Representa a Label 02 - Enemy;
            self._enemy = Representa o nome do monstro, aprensetado na Label;
            self.d20_e = Representa o Botão 02 - Enemy;
            _d20Enemy = Representa o valor final sorteado do montros;
            _verify_Enemy = Representa que o Enemy possui um valor, e pode ser comparado;
        """
        self._workEnemy = WorkEnemy()
        self._threadEnemy = QThread()

        self.all_thread(
            self._workEnemy, self._threadEnemy, self._workEnemy.doWorkEnemy,
            self.enemy, self._enemy, self.d20_e, '_d20Enemy', '_verify_Enemy'
        )

    def all_thread(self, _work, _thread, doWork, _display, _user, _d20b, _d20l, _verify):
        # Mover o work da Thread principal para a aoutra Thread:
        _work.moveToThread(_thread)

        # doWork para conectar o work na Thread:
        _thread.started.connect(doWork)

        # Finaliza a Thread:
        _work.finished.connect(_thread.quit)

        # Apaga os processos da memória:
        _thread.finished.connect(_thread.deleteLater)
        _work.finished.connect(_thread.deleteLater)

        # Passando os processoas a serem executados pela thread:
        _work.started.connect(self.work_started(_display, _user, _d20b))
        _work.progressed.connect(partial(self.work_progressed, _display))
        _work.finished.connect(partial(
            self.work_finished, _display, _user,
            _d20l, _d20b, _verify
        ))
        # Inicia a Thread:
        _thread.start()

    @Slot()
    def work_started(self, _display, _user, d20b):
        # Quando o botão e clicado e é criado uma nova Thread. 
        # Clicar novamente mata a Thread anterior e matando todo o sistema
        d20b.setDisabled(True) # Desabilita o botão.
        _display.setText(f'D20 {_user}')

    @Slot()
    def work_progressed(self, _display, value):
        _display.setText(value)

    @Slot()
    def work_finished(self, _display, _user, _d20l, _d20b, _verify, value):
        _display.setText(f'D20 {_user}:\n{value}')
        setattr(self, _d20l, int(value))
        _d20b.setDisabled(False)
        setattr(self, _verify, True)
        self.check_and_calculate()

    def check_and_calculate(self):
        if self._verify_Player and self._verify_Enemy:
            self.calculo()

    def calculo(self):
        if self._d20Player == 0 and self._d20Enemy == 0:
            return
        else:
            if self._d20Player > self._d20Enemy:
                self.winner.setText(f'Ganhou\n{self._player}')
            elif self._d20Player == self._d20Enemy:
                self.winner.setText('Deu empate')
            else:
                self.winner.setText(f'Ganhou\n{self._enemy}')
            QTimer.singleShot(4000, self.start_game)
        
        self._d20Player = 0; self._d20Enemy = 0

if __name__ == '__main__':
    app = QApplication()
    main_widget = MainWidget()

    main_widget.show()
    app.exec()
