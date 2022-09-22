from janela_usuario import *
from login_handler import *
from cadastro_handler import *
from janela_login import *
from PyQt5.QtWidgets import QMainWindow

class carregarTelaUsuario(QMainWindow, JanelaUsuario):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.pushButton.clicked.connect(self.press_cadastro)
        self.pushButton_2.clicked.connect(self.relatorio_popup)
        self.pushButton_3.clicked.connect(self.press_logout)


    def abrir_cadastro(self):
        tela_cadastro = carregarTelaCadastro(self)
        tela_cadastro.show()


    def press_cadastro(self):
        self.abrir_cadastro()

    
    def press_logout(self):
        self.close()

    
    def relatorio_popup(self):
        usuario_logado = ''
        email_usuario = ''
        senha_usuario = ''

        with open('dados.json', 'r') as f:
            data = json.load(f)
        
        for u in data['Pessoas']:
            if u['username'] == JanelaMain().lineEdit.text:
                usuario_logado = u['username']
                email_usuario = u['email']
                senha_usuario = u['password']

        w = QMessageBox()
        w.setWindowTitle("RELATORIO!")
        w.setText(f'Usuario logado: {usuario_logado}\nEmail cadastrado: {email_usuario}\nSenha cadastrada: {senha_usuario}')
        w.setStandardButtons(QMessageBox.Ok)
        w.setIcon(QMessageBox.Warning)

        w.exec_()
