def data_input():
    data = input("podaj: Imie [spacja] Nazwisko [spacja] Date_Urodzenia w formacie [DD.MM.RRRR]:\t")
    data = data.split(' ')
    if len(data[2]) != 10:
        print("Podano zly format daty urodzenia")
        exit()
    else:
        data_bday = data[2].split(".")
        if int(data_bday[0]) > 31:
            print("Blad w podaniu dnia:\t", data_bday[0])
            exit()
        elif int(data_bday[1]) > 12:
            print("Blad w podaniu miesiaca:\t", data_bday[1])
            exit()
        elif int(data_bday[2]) > 2023 and data_bday < 1900:
            print("Blad w podaniu roku:\t", data_bday[2])
            exit()
    return(data)

if __name__ == '__main__':
    data = data_input()
    print("Imie:\t", data[0])
    print("Naziwsko:\t", data[1])
    print("Data urodzenia:\t", data[2])
