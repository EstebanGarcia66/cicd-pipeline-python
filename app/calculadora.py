# app/calculadora.py
"""Funciones principales de la aplicacio"""


def sumar(a, b):
    """Funcion Suma"""
    return a + b


def restar(a, b):
    """Funcion Resta"""
    return a - b


def multiplicar(a, b):
    """Funcion Multiplicacion"""
    return a * b


def dividir(a, b):
    """Funcion Division"""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
