
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from window import MainWindow, Display, Labels
from construct_buttons import Buttons, Grid_Buttons
from variables import WINDOW_ICON_PATH
from styles import setup_Theme

if __name__ == '__main__':

    app = QApplication(sys.argv)
    setup_Theme()
    window = MainWindow()
    
    # -Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # -Labels
    label = Labels('Wait ...')
    window.add_widget_layout(label)

    # -display
    display = Display()
    window.add_widget_layout(display)

    # -Grid Buttons
    # Como já existe um layout em execução (QVBoxLayout), precisa adicionar o novo layout,
    # para isso usa-se o função addLayout no proprio main_layout.
    grid_buttons = Grid_Buttons(display, label, window)
    window.main_layout.addLayout(grid_buttons)

    # Não permite aumentar a tela
    window.adjust_interface()
    window.show()
    app.exec()