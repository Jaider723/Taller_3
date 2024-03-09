import os

lista_inicial = [1, 1991, "taller", 200, 3, "programación", 700, "utp", "POO"]

with open("lista_inicial.txt", "w") as archivo:
    for elemento in lista_inicial:
        archivo.write(str(elemento) + "\n")

numeros_enteros = []
for elemento in lista_inicial: 
    if isinstance(elemento, int):
        numeros_enteros.append(elemento)
with open("numeros_enteros.txt", "w") as archivo:
    for numero in numeros_enteros:
        archivo.write(str(numero) + "\n")
        
cadenas = []
for elemento in lista_inicial:
    if isinstance(elemento, str):
        cadenas.append(elemento)
with open("cadenas.txt", "w") as archivo:
    for cadena in cadenas:
        archivo.write(cadena + "\n")

lista_reemplazo = []
for elemento in lista_inicial:
    if isinstance(elemento, int) and elemento % 2 != 0:
        lista_reemplazo.append("reemplazo") 
    else:
        lista_reemplazo.append(elemento) 
with open("lista_reemplazada.txt", "w") as archivo:
    for elemento in lista_reemplazo:
        archivo.write(str(elemento) + "\n")


        
