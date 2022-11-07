import xml.dom.minidom

domtree = xml.dom.minidom.parse(r'C:\PythonProjekty\Zajecia_Python\pliki\xmlpythonbefore.xml')
fruits = domtree.documentElement
group = fruits.getElementsByTagName('fruit')

for fruit in group:
    print(f"\n-- Fruit {fruit.getAttribute('id')} --")

    name = fruit.getElementsByTagName('name')[0].childNodes[0].nodeValue
    color = fruit.getElementsByTagName('color')[0].childNodes[0].nodeValue
    shape = fruit.getElementsByTagName('shape')[0].childNodes[0].nodeValue
    taste = fruit.getElementsByTagName('taste')[0].childNodes[0].nodeValue

    print(f"Name: {name}")
    print(f"Color: {color}")
    print(f"Shape: {shape}")
    print(f"Taste: {taste}")

#podmiana
group[0].getElementsByTagName('name')[0].childNodes[0].nodeValue = "Python_lab"
group[1].getElementsByTagName('color')[0].childNodes[0].nodeValue = "Nowy_kolor"
group[2].setAttribute("id", "989")

domtree.writexml(open(r'C:\PythonProjekty\Zajecia_Python\pliki\xmlpythonafter.xml', 'w'))