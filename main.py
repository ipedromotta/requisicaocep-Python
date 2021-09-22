from PyQt5 import QtWidgets
from funcionalidades import Telas, Consulta

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    telas = Telas()
    telas.tela_buscador.btn_buscar.clicked.connect(lambda: Consulta.consultar(telas))
    telas.tela_buscador.show()
    app.exec()
