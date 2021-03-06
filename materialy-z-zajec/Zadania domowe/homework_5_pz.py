"""Zadanie 5 (zmienione)

Napisz program, który obliczy cenę telefonu po zaaplikowaniu zniżek:

- 10% dla osób poniżej 20 roku życia, 15% dla osób powyżej 70 roku życia
- rodzina pracowników - 12% przy cenie poniżej 3000, 20% przy cenie równej lub powyżej 3000 zł
- punkty z programu lojalnościowego: 10 zł za każde 100 punktów

Zapytaj użytkownika o cenę telefonu, datę urodzenia, czy jest rodziną pracownika oraz ile ma punktów
w programie lojalnościowym

Stwórz dwa warianty programu. Wariant 1 programu zakłada, że aplikujemy wszystkie przysługujące zniżki,
wariant 2 programu zakłada, że wybieramy tę najkorzystniejszą
"""
import math

cena_telefonu = float(input("Podaj cenę telefonu w zł: "))
wiek = int(input("Podaj wiek: "))
rodzina_pracownika = input("Czy jesteś rodziną pracownika, wybierz tak lub nie: T/N? ")
punkty = int(input("Ile masz punktów w programie lojalnościowym?"))


#  1 sposób

# wiek
if 20 >= wiek:
    rabat_1 = cena_telefonu * 0.1
    print(rabat_1)

elif wiek > 70:
    rabat_1 = cena_telefonu * 0.15
    # print(rabat_1)

else:
    rabat_1 = 0
    # print(rabat_1)

# rodzina pracownika
if rodzina_pracownika == "T":
    if cena_telefonu < 3000:
        rabat_2 = cena_telefonu * 0.12
        # print(rabat_2)
    else:
        rabat_2 = cena_telefonu * 0.2
        # print(rabat_2)
else:
    rabat_2 = 0
    # print(rabat_2)

#  punkty z programu lojalnościowego

if punkty >= 10:
    # zaokrąglenie do 10

    rabat_pkty = (punkty - (punkty % 10)) / 10
    new_rabat_pkty = math.floor(rabat_pkty)
    # print(new_rabat_pkty)
else:
    rabat_pkty = new_rabat_pkty = 0
    # print(new_rabat_pkty)

n_telefon = cena_telefonu - rabat_1 - rabat_2 - new_rabat_pkty
print(f" Cena telefonu po zniżkach: {round(n_telefon, 2)} zł. ")

#  2 sposób

# wiek
if 20 >= wiek:
    nowa_cena_1 = cena_telefonu * 0.9
    # print(nowa_cena_1)

elif wiek > 70:
    nowa_cena_1 = cena_telefonu * 0.85
    # print(nowa_cena_1)

else:
    nowa_cena_1 = cena_telefonu
    # print(nowa_cena_1)

# rodzina pracownika
if rodzina_pracownika == "T":
    if cena_telefonu < 3000:
        nowa_cena_2 = cena_telefonu * 0.88
        # print(nowa_cena_2)
    else:
        nowa_cena_2 = cena_telefonu * 0.80
        # print(nowa_cena_2)
else:
    nowa_cena_2 = cena_telefonu
    # print(nowa_cena_2)

#  punkty z programu lojalnościowego

if punkty >= 10:
    # zaokrąglenie do 10

    rabat_pkty = (punkty - (punkty % 10)) / 10
    new_rabat_pkty = math.floor(rabat_pkty)
    nowa_cena_3 = cena_telefonu-new_rabat_pkty
    # print(nowa_cena_3)
else:
    nowa_cena_3 = cena_telefonu
    # print(nowa_cena_3)

lista = [nowa_cena_1, nowa_cena_2, nowa_cena_3]
print(f" Cena telefonu po zniżkach: {round(min(lista),2)} zł. ")
