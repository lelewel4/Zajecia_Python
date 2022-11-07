class Complex(object):
    def __init__(self, real, img=0.0):
        self.real = real
        self.img = img

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.img * other.img, self.real * other.img + self.img * other.real)

    def __opposite__(self):
        self.real =self.real
        self.img = self. img if self.img<0 else self.img * -1

    def __truediv__(self, other):
        other.__opposite__()
        x = self.real * other.real - self.img * other.img
        y = self.img * other.real + self.real * other.img
        z = other.real**2 + other.img**2
        self.new_real = x / z
        self.new_img = y / z
        return Complex(self.new_real, self.new_img)

if __name__ == '__main__':
    i = Complex(2, 10)
    k = Complex(3, 5)

    add = i + k
    #print(add.real, add.img)
    if(add.real == 5) and (add.img == 15):                                      #wartosci ktorych jestesmy pewni ze sa poprawne
        print("Dodawanie poprawne")
        print(str(add.real), str(add.img)+"j","\n")
    else:
        print("Dodawanie niepoprawne, wynik:\t", add.real, add.img)

    sub = i - k
    #print(sub.real, sub.img)
    if(sub.real == -1) and (sub.img == 5):
        print("Odejmowanie poprawne")
        print(str(sub.real), str(sub.img)+"j","\n")
    else:
        print("Odejmowanie niepoprawne, wynik:\t", sub.real, sub.img)

    mul = i * k
    #print(mul.real, mul.img)
    if(mul.real == -44) and (mul.img == 40):
        print("Mnozenie poprawne")
        print(str(mul.real), str(mul.img)+"j","\n")
    else:
        print("Mnozenie niepoprawne, wynik:\t", mul.real, mul.img)

    if(k != 0):
        div = i / k
        #print(div.real, div.img)
        if (div.real == 28/17) and (div.img == 10/17):
            print("Dzielenie poprawne")
            print(str(div.real), str(div.img)+"j","\n")
        else:
            print("Dzielenie niepoprawne, wynik:\t", div.real, div.img)
    else:
        print("Nie mozna dzielic przez 0")




