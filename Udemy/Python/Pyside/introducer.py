
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget


app = QApplication(sys.argv)

button = QPushButton('EXIT')
button.setStyleSheet('font-size: 40px')
button.show()

central_widgets = QWidget()
layout = QVBoxLayout()
layout.addWidget(button)

app.exec()
