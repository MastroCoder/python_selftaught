import os

lista = []

with open("sas.txt", "r") as arq:
    lista.append(arq.read())
a = lista[0]
print(a.split("\n"))
