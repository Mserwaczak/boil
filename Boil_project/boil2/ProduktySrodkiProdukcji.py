from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from Dane import *


class DanePoczatkowe(QWidget):

    def __init__(self, parent=None):
        super(DanePoczatkowe, self).__init__(parent)
        self.dane = Dane.get_instance()
        self.initUI()

    def initUI(self):

        self.layout = QGridLayout()
        buttonHBox = QHBoxLayout()
        buttonHBox1 = QHBoxLayout()
        buttonHBox2 = QHBoxLayout()
        self.buttondalej = QPushButton("Dalej")

        self.buttonliczbaproduktow=QPushButton("Liczba Produktów")
        self.buttonliczbaproduktow.clicked.connect(self.on_click)

        self.buttonsrodkiprodukcji=QPushButton("Środki produkcji")
        self.buttonsrodkiprodukcji.clicked.connect(self.on_click2)

        buttonHBox.addWidget(self.buttonliczbaproduktow)
        buttonHBox1.addWidget(self.buttonsrodkiprodukcji)
        buttonHBox2.addWidget(self.buttondalej)

        self.layout.addLayout(buttonHBox, 0, 0)
        self.layout.addLayout(buttonHBox1, 1, 0)
        self.layout.addLayout(buttonHBox2, 2, 0)

        self.setLayout(self.layout)


    def getInteger(self):
        i, okPressed = QInputDialog.getInt(self, "Produkty", "Ilość produktów:", 0, 0, 100, 1)
        if okPressed:
            self.dane.produkty =i
            print(self.dane.produkty)

    def getInteger2(self):
        i, okPressed = QInputDialog.getInt(self, "Środki produkcji", "Środki produkcji:", 0, 0, 100, 1)
        if okPressed:
            self.dane.srodki_produkcji = i
            print(self.dane.srodki_produkcji)


    @pyqtSlot()
    def on_click(self):
       self.getInteger()

    @pyqtSlot()
    def on_click2(self):
        self.getInteger2()


    def get_data(self):
        self.dane.produkty = float(self.produkty)
        self.dane.srodki_produkcji = float(self.srodki_produkcji)

