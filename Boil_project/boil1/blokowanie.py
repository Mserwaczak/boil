import math

import numpy as np
def funkcja_blokowanie(popyt_suma, podaz_suma, popyt, podaz, jednostkowy_koszt_transportu, koszt_zakupu, cena_sprzedazy):
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

        D = 1
        O = 1

        # D = int(input("Podaj numer zablokowanego dostawcy: "))
        # O = int(input("Podaj numer zablokowanego odbiorcy: "))

        zyski_jednostkowe[D][O] = None

        # print(zyski_jednostkowe)

        def tabela_zyskow_jednostkowych(cena_sprzedazy, koszt_zakupu, jednostkowy_koszt_transportu):
            for i in range(0, 3):
                for j in range(0, 4):
                    if i < 2 and j < 3:
                        if i == D and j == O:
                            continue
                        else:
                            zyski_jednostkowe[i][j] = cena_sprzedazy[j] - koszt_zakupu[i] - jednostkowy_koszt_transportu[i][j]
                    else:
                        zyski_jednostkowe[i][j] = 0
            return zyski_jednostkowe


        zyski_jednostkowe = tabela_zyskow_jednostkowych(cena_sprzedazy, koszt_zakupu, jednostkowy_koszt_transportu)
        # print(zyski_jednostkowe)
        tabela1_pomocnicza = zyski_jednostkowe.copy()
        tabelazer = np.zeros(shape=(3, 4))

        x = 0
        y = 0

        tabela1_pomocnicza[D][O] = None
        optymalne_przewozy[D][O] = None

        while np.isnan(tabela1_pomocnicza[D][O]) or tabela1_pomocnicza.any() != 0 :
            # print(tabela1_pomocnicza)
            pomocnicze_maks = np.nanmax(tabela1_pomocnicza)

            # print(pomocnicze_maks)
            if pomocnicze_maks == 0:
                pomocnicze_maks = np.nanmax((tabela1_pomocnicza[tabela1_pomocnicza != 0]))
            print(pomocnicze_maks)
            if np.isnan(pomocnicze_maks):
                 break
            result = np.where(tabela1_pomocnicza == pomocnicze_maks)
            listOfCordinates = list(zip(result[0], result[1]))

            for cord in listOfCordinates:
                x = cord[0]
                y = cord[1]

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


        # print(optymalne_przewozy)
        while podaz.any() != 0 or popyt.any() != 0:
            # for i in range(0, 3):
            #     if podaz[i] != 0:
            #         x = i
            #         break
            #
            # for i in range(0, 4):
            #     if popyt[i] != 0:
            #         y = i
            #         break

            for i in range(0,3):
                for j in range(0,4):
                    if podaz[i] != 0 and popyt[j] != 0 and i != D:
                        x = i
                    if popyt[j] != 0 and podaz[i] != 0 and j != O:
                        y = j
                        if optymalne_przewozy[x][y] == 0:
                            break
                else:
                    continue
                break


            print(x, y)
            print(podaz[x])
            print(popyt[y])

            if podaz[x] < popyt[y]:
                optymalne_przewozy[x][y] = podaz[x]
                popyt[y] -= podaz[x]
                podaz[x] = 0
                # print(optymalne_przewozy, "\n \n", zyski_jednostkowe, "\n \n", tabela1_pomocnicza, "\n \n", popyt, "\n \n", podaz, "\n \n",
                # "\n PIERWSZY \n")

            else:
                optymalne_przewozy[x][y] = popyt[y]
                podaz[x] -= popyt[y]
                popyt[y] = 0
            print(optymalne_przewozy)
        tabela1_kopia = np.zeros((3, 4))
        tabela1_kopia = zyski_jednostkowe.copy()

        def liczenie_liczb_dualnych(tabela1):

            tabela1[D][O] = 0

            beta = np.zeros([4])
            alfa = np.zeros([3])

            for i in range(0, 4):
                beta[i] = None

            for i in range(0, 3):
                alfa[i] = None

            # print(alfa)
            # print(beta)

            # print("----------------------------------------------")

            # zalozenie
            alfa[0] = 0

            while any(np.isnan(alfa)) or any(np.isnan(beta)):
                for i in range(0, 3):
                    for j in range(0, 4):
                        if not np.isnan(alfa[i]) and np.isnan(beta[j]):
                            if optymalne_przewozy[i, j] != 0:
                                beta[j] = tabela1[i, j] - alfa[i]
                        elif np.isnan(alfa[i]) and not np.isnan(beta[j]):
                            if optymalne_przewozy[i, j] != 0:
                                alfa[i] = tabela1[i, j] - beta[j]
                        else:
                            continue

            return alfa, beta

        alfa, beta = liczenie_liczb_dualnych(zyski_jednostkowe)

        print("Alfa: ",alfa, "\nBeta", beta)

        print("ZYSK JEDNOSTKOWY: \n", zyski_jednostkowe, "\n")
        print("DOCHOD OPTYMALNY: \n", optymalne_przewozy, "\n")
        # print("KOSZT CALKOWITY: ", koszt_calkowity)
        # print("PRZYCHÓD: ", przychod, )
        # print("ZYSK POŚREDNIKA: ", zysk)
