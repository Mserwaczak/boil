from Dane import *
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QTableWidget
import pprint


class Tabela(QWidget):

    def __init__(self, parent=None):
        super(Tabela, self).__init__(parent)
        self.dane = Dane.get_instance()
        self.initUI()

    def initUI(self):

        self.layout = QGridLayout()
        self.createTable()
        self.createTable2()

        buttonHBox = QHBoxLayout()
        self.buttondalej = QPushButton("Dalej")
        self.buttondalej.clicked.connect(self.pobierz_dane)
        buttonHBox.addWidget(self.buttondalej)

        self.layout.addLayout(buttonHBox, 2, 0)
        self.setLayout(self.layout)



    def createTable(self):
        vbox = QVBoxLayout()
        self.tabela = QTableWidget()

        self.tabela.setColumnCount(self.dane.produkty + 1)
        self.tabela.setRowCount(self.dane.srodki_produkcji)

        self.kolumny = ['Limit fabryki']

        for i in range(self.dane.produkty):
            naglowek = 'Produkt ' + str(i)
            self.kolumny.append(naglowek)

        self.tabela.setHorizontalHeaderLabels(self.kolumny)


        vbox.addWidget(self.tabela)
        self.layout.addLayout(vbox, 0, 0)



    def createTable2(self):
        vbox = QVBoxLayout()

        self.tabela2 = QTableWidget()
        self.tabela2.setColumnCount(4)
        self.tabela2.setRowCount(self.dane.produkty)


        self.kolumny2 = ['Zysk', ">=", "<=", "="]

        self.tabela2.setHorizontalHeaderLabels(self.kolumny2)

        vbox.addWidget(self.tabela2)
        self.layout.addLayout(vbox, 1, 0)

    def pobierz_dane(self):
        kolumny = []
        for i in self.kolumny:
            kolumny.append(i)

        for i in self.kolumny2:
            kolumny.append(i)

        for i in kolumny:
            self.dane.wstawione_dane[i] = []

        for i in range(self.dane.srodki_produkcji):
            for j in range(len(self.kolumny)):
                self.dane.wstawione_dane[self.kolumny[j]].append(float(self.tabela.item(i, j).text()))

        for i in range(self.dane.produkty):
            for j in range(len(self.kolumny2)):
                self.dane.wstawione_dane[self.kolumny2[j]].append(float(self.tabela2.item(i, j).text()))

        pprint.pprint(self.dane.wstawione_dane)
