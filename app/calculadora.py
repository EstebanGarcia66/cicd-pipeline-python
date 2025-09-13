"""Funciones principales de la aplicacio"""
# app/calculadora.py

def sumar(a, b):
    return a + b
"""Funcion Suma"""

def restar(a, b):
    return a - b
"""Funcion Resta"""

def multiplicar(a, b):
    return a * b
"""Funcion Multiplicacion"""

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
"""Funcion Division"""
