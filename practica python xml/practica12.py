from lxml import etree
doc = etree.parse(r'C:\Users\edgar\OneDrive\Escritorio\Administracion org de datos\practica python xml\books.xml')
print(etree.tostring(doc, pretty_print=True, xml_declaration=True, encoding="utf-8"))
raiz=doc.getroot()
print(raiz.tag)
print(len(raiz))
libro=raiz[0]
print(libro.tag)
print(libro[0].text)
print(libro.attrib["category"])
precio=doc.find("book/price")
for precio in precio:
    print(precio.text)
libros=doc.findall("book")
libros[1].set("category","INFANCIA")
print(libros[1].attrib["category"])