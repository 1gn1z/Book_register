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

#------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Vamos a hacer una lista (ordenada alfabeticamente) de todos los criterios para registrar los libros (autor, editorial, etc.)

año de edición 
año de publicacion original
Autor(es)
coleccion 
edición (1a, 1a reimpresion)
edicion en coleccion (x ejemplo: colección: Mitos Bolsillo - Primera edición en Mitos Bolsillo, Primera reimpresión)

editorial
ilustrado por
isbn
leido?
Libro original?
Tipo de libro (cómic, manga, novela, libro de cuentos, etc.)
Título del libro
Título original
Traducción de

"""
class Libro(Model):
    anio_de_edicion = DateTimeField()
    anio_de_publicacion = DateTimeField()
    autor = CharField()
    coleccion = CharField()
    edicion_en_coleccion = CharField()
    edicion = CharField()   
    editorial = CharField()
    ilustrador = CharField()
    isbn = CharField()
    leido = CharField()
    libro_original = CharField()
    Tipo_de_libro = CharField()
    titulo_libro = CharField()
    titulo_original = CharField()
    tradducion = CharField()
    registro = DateTimeField(default = datetime.datetime.now().strftime("%A, %d %B %Y %I:%M%p"))  # Aqui se agrega el strftime en peewee

    class Meta:
        database = db


