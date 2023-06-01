texto = open('intro.txt')
contagem = dict()
palavras = None
for linha in texto:
    linha.rstrip()
    palavras = linha.split()
    for item in palavras:
        contagem[item] = contagem.get(item, 0) + 1

maior = None
for item in contagem:
    if maior == None:
        maior = item
    else:
        if len(item) > len(maior):
            maior = item
print(f'a maior palavra é {maior}')

frequencia = None
frequente_nome = None
for k,v in contagem.items():
    if frequencia == None:
        frequencia = v
    else:
        if v > frequencia:
            frequencia = v
            frequente_nome = k
print(f'a palavra {frequente_nome} é a que mais aparece, {frequencia} vezes')