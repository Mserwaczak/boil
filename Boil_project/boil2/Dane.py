class Dane():

    _instance = None

    @staticmethod
    def get_instance():
        if Dane._instance == None:
            Dane()
        return Dane._instance

    def __init__(self):
        if Dane._instance != None:
            raise Exception("Wyjatek")
        else:
            Dane._instance = self

        self.srodki_produkcji = -1
        self.produkty = -1
        self.wstawione_dane = {}
        self.wartosc_funkcji_celu = 0
        self.ilosc_produktow = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]