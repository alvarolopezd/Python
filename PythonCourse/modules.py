# Propios modulos
# Modulos de teceros descargados de intenet - https://pypi.org
# Modulos que Python proporciona - https://docs.python.org/3/py-modindex.html


# MODULO OFICIAL
import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=70)) # Pasar de minutos a horas y minutos


# TOMAR PARTES DE UN MODULO
from datetime import timedelta

print(timedelta(minutes=80))

# MI PROPIO MODULO
import mymath

mymath.add(1,2)
mymath.substract(1,2)


# INSTALAR MODULOS DE TERCEROS
# En cmd se puede ver la version del Python y de pip poniendo python --version y pip --version
# Para actualizar pip -> https://www.neoguias.com/como-instalar-pip-python/#Como_actualizar_PIP_para_Python
# https://pypi.org/project/colorama/ y poner en cmd el comando que sale del software del tecero 
# pip install colorama

#from colorama import Fore, Style, init
#init(convert=True)

#print(Fore.Red + "Hello World")

# Flash - para crear aplicaciones web
# Django - crearcion de aplicaciones
# tkinter - diseñar interfaces graficas de escritorio 






