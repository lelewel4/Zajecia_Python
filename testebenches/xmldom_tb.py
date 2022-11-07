from functions import xmlsax

if __name__ == '__main__':                          #weryfikacja zmian wykonanych za pomoca DOM, wyswietlenie SAX
    handler = xmlsax.ColorHandler()
    parser = xmlsax.xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(r'C:\PythonProjekty\Zajecia_Python\pliki\xmlpythonafter.xml')

