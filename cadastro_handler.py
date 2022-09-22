from PyQt5.QtWidgets import QMainWindow
from janela_cadastro import *
import json
from PyQt5.QtWidgets import QMessageBox


class carregarTelaCadastro(QMainWindow, JanelaCadastro):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.pushButton.clicked.connect(self.press_cadastrar)


    def fechar(self):
        self.close()

    
    def erro_campo(self):
        w = QMessageBox()
        w.setWindowTitle("AVISO!")
        w.setText('Volte e preencha todos os campos.')
        w.setStandardButtons(QMessageBox.Ok)
        w.setIcon(QMessageBox.Warning)

        w.exec_()


    def usuario_invalido(self):
        w = QMessageBox()
        w.setWindowTitle("AVISO!")
        w.setText('Nome de usuário já cadastrado.')
        w.setStandardButtons(QMessageBox.Ok)
        w.setIcon(QMessageBox.Warning)

        w.exec_()


    def sucesso_cadastro(self):
        w = QMessageBox()
        w.setWindowTitle("SUCESSO!")
        w.setText('Conta cadastrada.')
        w.setStandardButtons(QMessageBox.Ok)
        w.setIcon(QMessageBox.Information)

        w.exec_()


    def press_cadastrar(self):
        if not self.lineEdit.text() or not self.lineEdit_2.text() or not self.lineEdit_3.text():
            self.erro_campo()
        else:
            with open('dados.json', 'r') as f:
                data = json.load(f)
            
            username_try = self.lineEdit.text()
            aux = False
            for u in data['Pessoas']:
                if u['username'] == username_try:
                    aux = True
            
            if aux:
                self.usuario_invalido()
            else:
                with open("dados.json") as json_file:
                    data = json.load(json_file)
                    temp = data["Pessoas"]
                    id_to_add = (len(data["Pessoas"]))
                    y = {"id": id_to_add, 
                    "username": self.lineEdit.text(), 
                    "email": self.lineEdit_3.text(), 
                    "password": self.lineEdit_2.text()}
                    temp.append(y)
                self.write_json(data)
                self.sucesso_cadastro()
                self.fechar()
                

    def write_json(self, data, filename="dados.json"):
	    with open(filename, "w") as f:
		    json.dump(data, f, indent=4) 
