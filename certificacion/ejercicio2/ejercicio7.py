fh = open('C:\\Users\\edgar\\OneDrive\\Escritorio\\Administracion org de datos\\certificacion\\mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())

