import sys
from PyQt5.QtWidgets import QApplication

from TelaVeiculo import TelaVeiculo

app = QApplication(sys.argv )

TelaVeiculo = TelaVeiculo( "cadastro de Veículo")
TelaVeiculo.show()
sys.exit( app.exec_())