
"""
Crie uma variável recebendo dados. Esta variável deve reproduzir uma aplicação console se os dados digitados estão presentes:
- existe espaço
- existe caracter alfabético
- existe caracter alfanumérico
- existe caracter numérico

Utilizando o conceito de tipo primitivo Booleano.

"""

import time

var = input("Digite algo: ")

print("É somente espaço? ", var.isspace())
print("É caracter alfabético? ", var.isalpha())
print("É caracter alfa numérico? ", var.isalnum())
print("É caracter numérico? ", var.isnumeric())
print("Possui espaço? ", ' ' in var)
