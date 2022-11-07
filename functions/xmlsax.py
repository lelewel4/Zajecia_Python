import xml.sax

class ColorHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if name == "fruit":
            print(f"\n-- Fruit {attrs['id']} --")

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "color":
            self.color = content
        elif self.current == "shape":
            self.shape = content
        elif self.current == "taste":
            self.taste = content

    def endElement(self, name):
        if self.current == "name":
            print(f"Name: {self.name}")
        elif self.current == "color":
            print(f"Color: {self.color}")
        elif self.current == "shape":
            print(f"Shape: {self.shape}")
        elif self.current == "taste":
            print(f"Taste: {self.taste}")
        self.current = ""

if __name__ == '__main__':
    handler = ColorHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(r'C:\PythonProjekty\Zajecia_Python\pliki\xmlpythonbefore.xml')



