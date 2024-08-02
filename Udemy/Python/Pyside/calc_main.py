
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from window import MainWindow, Entry, Labels
from variables import WINDOW_ICON_PATH
from styles import setup_Theme

if __name__ == '__main__':

    app = QApplication(sys.argv)
    setup_Theme()
    window = MainWindow()
    
    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Labels
    labels = Labels('Testando')
    window.add_widget_layout(labels)

    # Entry
    entry = Entry()
    window.add_widget_layout(entry)

    # Não permite aumentar a tela
    window.adjust_interface()
    window.show()
    app.exec()