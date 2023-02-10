from MainWindow import *
import sys
from Dane import *
from pulp import LpMaximize, LpProblem, lpSum, LpVariable


class Optymalizacja:
    def __init__(self):
        self.dane = Dane.get_instance()
    def optymalizacja(self):
        model = LpProblem(name="Dobór_optymalnego_asortymentu", sense=LpMaximize)
        produkty = [self.dane.wstawione_dane["Produkt "+str(i)] for i in range(self.dane.produkty)]
        zyski_jednostkowe = self.dane.wstawione_dane["Zysk"]
        gorne_ograniczenie = self.dane.wstawione_dane["<="]
        dolne_ograniczenie = self.dane.wstawione_dane[">="]
        rowne_ograniczenie = self.dane.wstawione_dane["="]
        limit_fabryki = self.dane.wstawione_dane["Limit fabryki"]
        liczby = [i for i in range(self.dane.produkty)]
        nazwy = ["x" + str(liczba) for liczba in liczby]

        zmienne = [LpVariable(nazwa, None, cat="Integer") for nazwa in nazwy]
        print(zmienne)
        model += lpSum(float(zyski_jednostkowe[i]) * zmienne[i] for i in range(0, self.dane.produkty))

        for i in range(self.dane.srodki_produkcji):
            model += lpSum([float(produkty[j][i]) * zmienne[j] for j in range(len(zmienne))]) <= limit_fabryki[i]

        for i in range(self.dane.produkty):
            if gorne_ograniczenie[i] != 0:
                model += lpSum([zmienne[i]]) <= gorne_ograniczenie[i]

        for i in range(self.dane.produkty):
            model += lpSum([zmienne[i]]) >= dolne_ograniczenie[i]

        for i in range(self.dane.produkty):
            if rowne_ograniczenie[i] != 0:
                model += lpSum([zmienne[i]]) == rowne_ograniczenie[i]

        print(model)
        model.solve()
        zoptymalizowane = []
        for v in model.variables():
            zoptymalizowane.append(v.varValue)

        for i in range(self.dane.produkty):
            self.dane.ilosc_produktow[i] = zoptymalizowane[i]
        for var in model.variables():
            print(f"{var.name}: {var.value()}")
        self.dane.wartosc_funkcji_celu = model.objective.value()

        print(self.dane.wartosc_funkcji_celu)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())