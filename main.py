#condisionales 
 
#if condicion:
#   pedazo de codigo 


#if 2 < 5:
    #print("2es menor que 5")

#if 2 > 5:
    #print("2 es mayor que 5")
    
    
#preguntale al usuario cuantios años tiene , si el usuario tie
#imprime un mensaje "eres mayor de edad "

'''
edad = int (input ("cuantos años tienes? "))

if edad >= 18:
    print("eres mayor de edad ")
    
else:
    print("eres menor")
    '''
    
    #preguntale al usuario la edad , si el usuario tien de 0 a 17 dile que es meno , y si tiene de 18 a 59 años 
    #imprime eres mayor de edad y si tiene mas de 60 dile que es adulto mayor 
'''
edad = int (input("cuantos años tienes?"))

if edad >= 0 and edad <= 17 :
        print("eres menor de edad ")
        
elif edad >= 18 and edad <= 59:
        print("eres mayor de edad ")
        
else: 
    print("eres de la atersera edad")
'''
        
'''     
ciclo wile 
imprimir los numeros del 0 al 9 
'''
'''
i = 0
while i <= 10: 
    print(i)
    i=i + 1
else:
    print("buen dia ya salio del while   ")
'''
'''
#for variable in codigo:
    #codigo 
    
#imprime los numeros del 0 al 9 
for numeros in range(10):
    print(numeros"")
    '''

#listas [1,2,3,4,5]
#lista => [1,2,3,4,5]

#indices         0 1 2 3 4 5 6 7 8
'''
lista_numeros = [1,2,3,4,5,6,7,8,9]
num = lista_numeros[8]
print(num)
lista_numeros[8] = 100
num = lista_numeros[8]
print(num)

print(lista_numeros)

tamaño = len(lista_numeros)
print(tamaño)

#append #agrega numeros a la lista 
#agregar valor 99 al final de la lista 
lista_numeros.append(99)
print(lista_numeros)
#sacar el tamaño de la lista de nuevo
tamaño = len(lista_numeros)
print(tamaño)


for numero in lista_numeros:
    print(numero)
print("terminamos de imprimir los elementos de la lista")
'''
#(ejercicio , te voy a dar una lista y vas a tener que crear una lista 
# nuevaque va a tener los mismos valores de la lista pero multiplicados
# por dos)

#[1,2,3,4,5]
# y me vas a regresar [2,4,6,8,10])
'''
lista = [1,2,3,4,5]

lista_nueva = []

for num in lista:
    valor_nuevo = num *2
    lista_nueva.append(valor_nuevo)
print(lista_nueva)
'''





'''   
#funciones 

def suma_tres_numeros( a, b, c):
    valor = a + b + c 
    return valor 

def imprimir(num):
    print(num)

def fin_del_programa():
    print("adios")
suma = suma_tres_numeros(1, 2, 3)
imprimir(suma)

suma_ = 4 + 5 + 6
print(suma)
'''