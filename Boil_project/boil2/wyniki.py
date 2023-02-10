from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from Dane import *


class Wyniki(QWidget):
    def __init__(self, parent=None):
        super(Wyniki, self).__init__(parent)
        self.dane = Dane.get_instance()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.nazwa = QLabel(f"Wartość funkcji celu: {self.dane.wartosc_funkcji_celu}")

        for i in range(self.dane.produkty):
            label = QLabel(f"Produkt {i}: {self.dane.ilosc_produktow[i]}")
            self.layout.addWidget(label)

        self.layout.addWidget(self.nazwa)
        self.setLayout(self.layout)
