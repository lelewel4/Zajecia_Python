from functions import liczby_zespolone

def start():
    real1 = float(input("Podaj czesc rzeczywista pierwszej liczby:\t"))               #podanie nie floata wyrzuci blad
    img1 = float(input("Podaj czesc urojona pierwszej liczby:\t"))
    znak = input("Podaj znak operacji:\t")
    real2 = float(input("Podaj czesc rzeczywista drugiej liczby:\t"))
    img2 = float(input("Podaj czesc urojona drugiej liczby:\t"))
    return real1, real2, znak, img1, img2

def check(command:str, complex1, complex2):
    if(command == '+'):
        add = complex1 + complex2
        print(str(add.real), str(add.img)+"j", "\n")
    elif(command == '-'):
        sub = complex1 - complex2
        print(str(sub.real), str(sub.img)+"j", "\n")
    elif(command == '/'):
        div = complex1 / complex2
        print(str(div.real), str(div.img)+"j", "\n")
    elif(command == "*"):
        mul = complex1 * complex2
        print(str(mul.real), str(mul.img) + "j", "\n")
    else:
        print("Podano zly znak")                                       #test znaku

if __name__ == '__main__':
    dane = start()
    complex1 = liczby_zespolone.Complex(int(dane[0]), int(dane[3]))
    complex2 = liczby_zespolone.Complex(int(dane[1]), int(dane[4]))
    check(dane[2], complex1, complex2)




