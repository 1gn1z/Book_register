#--------------------------------------------------------
# Importaciones

# Importamos todo peewee
from peewee import *

# Para usar el diccionario ordenado para implementar menú con letras y no con números.
from collections import OrderedDict

import sys

# Para usar horas y fechas en python
import datetime

# Para pedir el password de forma segura (no se ven las letras al escribir el password)
import getpass

#--------------------------------------------------------

# Creamos la base de datos (Book_register.db) y la guardamos en una variable:
db = SqliteDatabase('Book_register.db')