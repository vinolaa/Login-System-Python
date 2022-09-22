from PyQt5.QtWidgets import QMainWindow
from janela_login import *
from cadastro_handler import *
from usuario_handler import *
from PyQt5.QtWidgets import QMessageBox
import os.path


class carregarTelaLogin(QMainWindow, JanelaMain):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.pushButton.clicked.connect(self.press_entrar)
        self.pushButton_2.clicked.connect(self.press_esqueci)
        self.pushButton_3.clicked.connect(self.abrir_cadastro)


    def abrir_cadastro(self):
        cadastro = carregarTelaCadastro(self)
        cadastro.show()


    def abrir_usuario(self):
        usuario = carregarTelaUsuario(self)
        usuario.show()


    def press_esqueci(self):
        self.esqueci_popup()


    def press_entrar(self):
        with open('dados.json', 'r') as f:
            data = json.load(f)


        username_input = self.lineEdit.text()
        aux = False
        id = NULL

        for u in data['Pessoas']:
            if u['username'] == username_input:
                aux = True
                id = u['id']
        
        if aux:
            password_input = self.lineEdit_2.text()
            if data["Pessoas"][id]['password'] == password_input:
                self.logado_popup()
                self.fechar_a()
                self.abrir_usuario()
            else:
                self.senha_incorreta_popup()
                self.registrar_log()
        else:
            self.usuario_nao_encontrado_popup()
            self.registrar_log()


    def criar_arquivo_log(self):
        file = open('invalid_logins.txt', mode='a+', encoding='utf-8')
        file.write('-=-\nEste é um arquivo log que contém todas as tentativas inválidas de login.\nPor favor, não editar este arquivo.\nCaso necessário, copie dados importantes e apague o arquivo.\n-=-\n\n')
        file.close()


    def registrar_log(self):
        if os.path.exists('invalid_logins.txt'):
            log_file = open('invalid_logins.txt', 'a+')
            log_try = [
                f"username: {self.lineEdit.text()}\npassword: {self.lineEdit_2.text()}\n\n"
            ]
            log_file.write(log_try[0])
            log_file.close()
        else:
            self.criar_arquivo_log()
            log_file = open('invalid_logins.txt', 'a+')
            log_try = [
                f"username: {self.lineEdit.text()}\npassword: {self.lineEdit_2.text()}\n\n"
            ]
            log_file.write(log_try[0])
            log_file.close()


    def usuario_nao_encontrado_popup(self):
        w = QMessageBox()
        w.setWindowTitle("AVISO!")
        w.setText('Usuário não encontrado.')
        w.setIcon(QMessageBox.Warning)

        botao_nova_conta = w.addButton('Criar conta', QMessageBox.YesRole)
        botao_nova_conta.clicked.connect(lambda: self.abrir_cadastro())
        botao_tentar_novamente = w.addButton('Tentar novamente', QMessageBox.DestructiveRole)

        w.exec_()


    def senha_incorreta_popup(self):
        w = QMessageBox()
        w.setWindowTitle("FALHA NA CONEXÃO!")
        w.setText('Senha incorreta. Por favor, tente novamente.')
        w.setStandardButtons(QMessageBox.Ok)
        w.setIcon(QMessageBox.Warning)

        w.exec_()


    def area_usuario_popup(self):
        w = QMessageBox()
        w.setWindowTitle('DESENVOLVIMENTO!')
        w.setText('Área de usuário em construção.')
        w.setStandardButtons(QMessageBox.Ok)
        w.setIcon(QMessageBox.Warning)

        w.exec_()


    def logado_popup(self):
        w = QMessageBox()
        w.setWindowTitle("SUCESSO!")
        w.setText('Logado com sucesso.')
        w.setStandardButtons(QMessageBox.Ok)
        w.setIcon(QMessageBox.Warning)

        w.exec_()


    def esqueci_popup(self):
        w = QMessageBox()
        w.setWindowTitle("AVISO!")
        w.setText('Função em desenvolvimento.')
        w.setStandardButtons(QMessageBox.Ok)
        w.setIcon(QMessageBox.Warning)

        w.exec_()


    def fechar_a(self):
        self.close()
    
