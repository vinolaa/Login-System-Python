import sys
from janela_cadastro import *
from cadastro_handler import *
from janela_login import *
from login_handler import *
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    carrega = carregarTelaLogin()
    carrega.show()
    qt.exec_()
