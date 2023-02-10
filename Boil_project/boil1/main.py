import numpy as np
import math
from blokowanie import *

podaz = np.zeros([2])
popyt = np.zeros([3])
koszt_zakupu = np.zeros([2])
cena_sprzedazy = np.zeros([3])
jednostkowy_koszt_transportu = np.zeros(shape=(2, 3))

#podaz
podaz[0] = 20
podaz[1] = 30

#popyt
popyt[0] = 10
popyt[1] = 28
popyt[2] = 27

#koszt zakupu
koszt_zakupu[0] = 10
koszt_zakupu[1] = 12

#ceny sprzedazy
cena_sprzedazy[0] = 30
cena_sprzedazy[1] = 25
cena_sprzedazy[2] = 30

#jednostkowe koszty transportu
jednostkowy_koszt_transportu[0][0] = 8
jednostkowy_koszt_transportu[0][1] = 14
jednostkowy_koszt_transportu[0][2] = 17
jednostkowy_koszt_transportu[1][0] = 12
jednostkowy_koszt_transportu[1][1] = 9
jednostkowy_koszt_transportu[1][2] = 19

popyt_suma = 0
for i in popyt:
    popyt_suma += i
#print(popyt_suma)

podaz_suma = 0
for i in podaz:
    podaz_suma +=i
#print(podaz_suma)

flaga = 0

if flaga == 1:
    funkcja_blokowanie(popyt_suma, podaz_suma, popyt, podaz, jednostkowy_koszt_transportu, koszt_zakupu, cena_sprzedazy)
else:
    if podaz_suma == popyt_suma:
        zyski_jednostkowe = np.zeros(shape=(2, 3))
        optymalne_przewozy = np.zeros(shape=(2, 3))
    else:
        zyski_jednostkowe = np.zeros(shape=(3, 4))
        optymalne_przewozy = np.zeros(shape=(3, 4))
        podaz_falsz = popyt_suma
        popyt_falsz = podaz_suma
        popyt_dodaj = np.zeros([1])
        podaz_dodaj = np.zeros([1])
        popyt_dodaj[0] = popyt_falsz
        podaz_dodaj[0] = podaz_falsz
        popyt = np.append(popyt, popyt_dodaj, axis=0)
        podaz = np.append(podaz, podaz_dodaj, axis=0)

    def tabela_zyskow_jednostkowych(cena_sprzedazy, koszt_zakupu, jednostkowy_koszt_transportu):
        if popyt_suma == podaz_suma:
            for i in range(0, 2):
                for j in range(0, 3):
                        zyski_jednostkowe[i][j] = cena_sprzedazy[j] - koszt_zakupu[i] - jednostkowy_koszt_transportu[i][j]
        else:
            for i in range(0, 3):
                for j in range(0, 4):
                    if i < 2 and j < 3:
                        zyski_jednostkowe[i][j] = cena_sprzedazy[j] - koszt_zakupu[i] - jednostkowy_koszt_transportu[i][j]
                    else:
                        zyski_jednostkowe[i][j] = 0
        return zyski_jednostkowe

    zyski_jednostkowe = tabela_zyskow_jednostkowych(cena_sprzedazy, koszt_zakupu, jednostkowy_koszt_transportu)


    #print(tabela1)

    tabela1_pomocnicza = zyski_jednostkowe.copy()
    tabelazer = np.zeros(shape=(3, 4))

    x = 0
    y = 0

    while tabela1_pomocnicza.any() != 0:

        pomocnicze_maks = np.amax(tabela1_pomocnicza)
        if pomocnicze_maks == 0:
            pomocnicze_maks = np.amax((tabela1_pomocnicza[tabela1_pomocnicza != 0]))
        result = np.where(tabela1_pomocnicza == pomocnicze_maks)
        listOfCordinates = list(zip(result[0], result[1]))

        for cord in listOfCordinates:
            x = cord[0]
            y = cord[1]

        if popyt_suma == podaz_suma:
            if podaz[x] < popyt[y]:
                optymalne_przewozy[x][y] = podaz[x]
                popyt[y] -= podaz[x]
                podaz[x] = 0
                tabela1_pomocnicza[x][0] = 0
                tabela1_pomocnicza[x][1] = 0
                tabela1_pomocnicza[x][2] = 0

            else:
                optymalne_przewozy[x][y] = popyt[y]
                podaz[x] -= popyt[y]
                popyt[y] = 0
                tabela1_pomocnicza[0][y] = 0
                tabela1_pomocnicza[1][y] = 0

        else:
            if podaz[x] < popyt[y]:
                optymalne_przewozy[x][y] = podaz[x]
                popyt[y] -= podaz[x]
                podaz[x] = 0
                tabela1_pomocnicza[x][0] = 0
                tabela1_pomocnicza[x][1] = 0
                tabela1_pomocnicza[x][2] = 0

            else:
                optymalne_przewozy[x][y] = popyt[y]
                podaz[x] -= popyt[y]
                popyt[y] = 0
                tabela1_pomocnicza[0][y] = 0
                tabela1_pomocnicza[1][y] = 0
                tabela1_pomocnicza[2][y] = 0


    while podaz.any() != 0 or popyt.any() != 0:
        for i in range(0, 3):
            if podaz[i] != 0:
                x = i
                break

        for i in range(0, 4):
            if popyt[i] != 0:
                y = i
                break

        if podaz[x] < popyt[y]:
            optymalne_przewozy[x][y] = podaz[x]
            popyt[y] -= podaz[x]
            podaz[x] = 0

        else:
            optymalne_przewozy[x][y] = popyt[y]
            podaz[x] -= popyt[y]
            popyt[y] = 0


    tabela1_kopia = np.zeros((3,4))
    tabela1_kopia = zyski_jednostkowe.copy()



    def liczenie_liczb_dualnych(tabela1):

        if popyt_suma == podaz_suma:
            beta = np.zeros([3])
            alfa = np.zeros([2])
            for i in range(0, 3):
                beta[i] = None

            for i in range(0, 2):
                alfa[i] = None
        else:
            beta = np.zeros([4])
            alfa = np.zeros([3])

            for i in range(0, 4):
                beta[i] = None

            for i in range(0, 3):
                alfa[i] = None


        #zalozenie
        alfa[0] = 0


        while any(np.isnan(alfa)) or any(np.isnan(beta)):
            if popyt_suma == podaz_suma:
                for i in range(0,2):
                    for j in range(0,3):
                        if not np.isnan(alfa[i]) and np.isnan(beta[j]):
                            if optymalne_przewozy[i, j] != 0:
                                beta[j] = tabela1[i, j] - alfa[i]
                        elif np.isnan(alfa[i]) and not np.isnan(beta[j]):
                            if optymalne_przewozy[i, j] != 0:
                                alfa[i] = tabela1[i, j] - beta[j]
                        else:
                            continue
                print(alfa, beta)
            else:
                for i in range(0,3):
                    for j in range(0,4):
                        if not np.isnan(alfa[i]) and np.isnan(beta[j]):
                            if optymalne_przewozy[i, j] != 0:
                                beta[j] = tabela1[i, j] - alfa[i]
                        elif np.isnan(alfa[i]) and not np.isnan(beta[j]):
                            if optymalne_przewozy[i, j] != 0:
                                alfa[i] = tabela1[i, j] - beta[j]
                        else:
                            continue


        return alfa, beta


    tabela3 = np.zeros(shape=(3,4))
    for i in range(0,3):
        for j in range(0, 4):
            tabela3[i][j] = 9999

    def tablica3(tabela1_kopia, alfa, beta):
        if popyt_suma == podaz_suma:
            for i in range(0,2):
                for j in range(0, 3):
                    if optymalne_przewozy[i][j] != 0:
                        tabela3[i][j] = None
                    else:
                        tabela3[i][j] = tabela1_kopia[i][j] - alfa[i] - beta[j]
        else:
            for i in range(0,3):
                for j in range(0, 4):
                    if optymalne_przewozy[i][j] != 0:
                        tabela3[i][j] = None
                    else:
                        tabela3[i][j] = tabela1_kopia[i][j] - alfa[i] - beta[j]
        return tabela3


    ź = 0
    alfa, beta = liczenie_liczb_dualnych(zyski_jednostkowe)

    #PETLA GLOWNA

    while tabela3.max() > 0:


        ź += 1

        tabela3 = tablica3(tabela1_kopia, alfa, beta)
        wartosc = 0

        zmienna = False



        for i in range(0, 3):
            for j in range(0, 4):
                if tabela3[i,j] > wartosc:
                    wartosc = tabela3[i, j]
                    zmienna = True
        yyy = 0
        xxx = 0
        for i in range(0, 3):
            for j in range(0, 4):
                if tabela3[i,j] == wartosc:
                    yyy = i
                    xxx = j

        nan_1x = []
        nan_1y = []

        nan_2x = []
        nan_2y = []

        for i in range(0, 3):
            for j in range(0, 4):
                if math.isnan(tabela3[i][j]) and yyy == i:
                    nan_1x.append(j)
                    nan_1y.append(i)

        for i in range(0, 3):
            for j in range(0, 4):
                if math.isnan(tabela3[i][j]) and xxx == j:
                    nan_2x.append(j)
                    nan_2y.append(i)

        pp = []
        qq = []

        for i in range(0, len(nan_1x)):
            for j in range(0, len(nan_2x)):
                if math.isnan(tabela3[nan_2y[j]][nan_1x[i]]):
                    pp.append(xxx)
                    qq.append(yyy)
                    pp.append(nan_2x[j])
                    qq.append(nan_2y[j])
                    pp.append(nan_2y[j])
                    qq.append(nan_1x[i])
                    pp.append(nan_1x[i])
                    qq.append(nan_1y[i])
                    p = nan_2y[j]
                    q = nan_1x[i]

        if len(qq) == 0 and len(pp) == 0:
            break
        elif optymalne_przewozy[qq[1], pp[1]] < optymalne_przewozy[qq[3], pp[3]]:
            temp = optymalne_przewozy[qq[1], pp[1]]
        else:
            temp = optymalne_przewozy[qq[3], pp[3]]

        optymalne_przewozy[qq[0], pp[0]] += temp
        optymalne_przewozy[qq[1], pp[1]] -= temp
        optymalne_przewozy[qq[2], pp[2]] += temp
        optymalne_przewozy[qq[3], pp[3]] -= temp
        alfa, beta = liczenie_liczb_dualnych(zyski_jednostkowe)
        tabela3 = tablica3(tabela1_kopia, alfa, beta)


    koszt_transportu = 0
    zakup = 0
    koszt_calkowity = 0
    przychod = 0
    for i in range(0, 2):
        for j in range(0, 3):
            zakup += koszt_zakupu[i] * optymalne_przewozy[i][j]
            koszt_transportu += jednostkowy_koszt_transportu[i][j] * optymalne_przewozy[i][j]
            przychod += cena_sprzedazy[j] * optymalne_przewozy[i][j]

    koszt_calkowity = zakup + koszt_transportu
    zysk = przychod - koszt_calkowity

    f = open("wyniki.txt", "w")
    f.write("ZYSKI JEDNOSTKOWE:\n")
    f.write(str(zyski_jednostkowe))
    f.write("\nOPTYMALNE PRZEWOZY:\n")
    f.write(str(optymalne_przewozy))
    f.write("\nKOSZT CALKOWITY: ")
    f.write(str(koszt_calkowity))
    f.write("\nPRZYCHOD: ")
    f.write(str(przychod))
    f.write("\nZYSK: ")
    f.write(str(zysk))
    f.close()

    print("ZYSK JEDNOSTKOWY: \n", zyski_jednostkowe, "\n")
    print("DOCHOD OPTYMALNY: \n", optymalne_przewozy, "\n")
    print("KOSZT CALKOWITY: ", koszt_calkowity)
    print("PRZYCHÓD: ", przychod, )
    print("ZYSK POŚREDNIKA: ", zysk)