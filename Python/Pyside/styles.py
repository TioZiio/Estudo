
import qdarktheme
from variables import (
    DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR)


# Existe 3 modos, o normal, hover, pressed.;
# Hover ocorre ao passar o mouse por cima;
# Pressed ao precionar p button;
qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""
# Explicação sobre a variavel qss:
# QPushButton - É o metodo do Pyside6
# [cssClass="specialButton"] - Propriedade específica do QPushButton que foram criadas.
#      |-> Tanto cssCLass quanto specialButton são variaveis definida por mim;

def setup_Theme():
    """
        Função responsavel por definir stylos na janela, background, bordas e o qss.
    """
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss = qss
    )