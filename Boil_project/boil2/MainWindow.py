from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from Dane import *
from ProduktySrodkiProdukcji import *
from Tabela import *
from wyniki import *
from main import  *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.dane = Dane.get_instance()
        self.ekran_powitalny()

    def ekran_powitalny(self):

        self.setMinimumWidth(300)
        self.ProduktySrodkiProdukcji = DanePoczatkowe(self)
        self.ProduktySrodkiProdukcji.buttondalej.clicked.connect(lambda : self.pobranie_danych())
        self.setCentralWidget(self.ProduktySrodkiProdukcji)
        self.show()

    def pobranie_danych(self):
        self.setMinimumWidth(640)
        self.setMinimumHeight(480)
        self.Tabela = Tabela(self)
        self.Tabela.buttondalej.clicked.connect(lambda : self.wyniki())
        self.setCentralWidget(self.Tabela)
        self.show()

    def wyniki(self):
        self.optymalizacja = Optymalizacja()
        self.optymalizacja.optymalizacja()
        self.setMinimumWidth(400)
        self.setMinimumHeight(150)
        self.Wyniki = Wyniki(self)
        self.setCentralWidget(self.Wyniki)
        self.show()

