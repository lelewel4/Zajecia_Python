from functions import wprowadzanie_danych
import json

#initialization
def init():
    data = wprowadzanie_danych.data_input()
    dictionary =  { 'Imie': data[0], 'Nazwisko': data[1], 'Data Urodzenia': data[2] }
    return dictionary

#writing
def write_json(dictionary:list[str], file:str):
    json_object = json.dumps(dictionary, indent=len(dictionary))
    with open(file, "w", encoding='utf-8') as outfile:
        outfile.write(json_object)

#reading
def read_json(file:str):
    with open(file, "r") as json_file:
        features = json.load(json_file)
    print("Zawartosc JSON:\n")
    for i in features:
        print(i,"\t", features[i])
    print("\n")

#adding
def add_json(file:str):
    data_input = input("Co chcesz dodac: [key],[value]\t")
    data_input = data_input.split(' ')
    new_data = {data_input[0]: data_input[1]}

    with open(file, "r") as json_file:
        features = json.load(json_file)

    features.update(new_data)
    write_json(features, file)

#subtracting
def sub_json(file:str):
    data_input = input("Co chcesz usunac: [key]\t")
    with open(file, "r") as json_file:
        features = json.load(json_file)
        features.pop(data_input)
        write_json(features, file)

def welcome(file:str):
    znak = input("\nCo chcesz wykonac: [+]dodawanie, [-]odejmowanie, [p]odczytanie JSONA:\t")
    if str(znak) == '+':
        return add_json(file)
    elif str(znak) == '-':
        return sub_json(file)
    elif str(znak) == 'p':
        return read_json(file)
    else:
        print("Podano zly znak")
        print(znak)
        exit()

if __name__ == '__main__':
    file = r'C:\PythonProjekty\Zajecia_Python\pliki\python.json'
    read_json(file)
    #write_json(init(), file)                #funckja do poczatkowej inicjalzizacji
    while(1):
        welcome(file)
