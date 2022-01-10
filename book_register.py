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
Escritura

"""

# Modelo de Clase, llamado "Libro", que pasa a ser mapeado como una TABLA de la DB.
# Los ATRIBUTOS (title, year, gender, isbn, read), son mapeados como COLUMNAS de la DB.
# Y las INSTANCIAS (TIPOS DE DATOS) de estos atributos (CharField, DateTimeField, IntegerField), pasan a ser mapeados como FILAS

class Libro(Model):
    anio_de_edicion = DateTimeField()
    anio_de_publicacion = DateTimeField()
    autor = CharField()
    coleccion = CharField()
    edicion_en_coleccion = CharField()
    edicion = CharField()   
    editorial = CharField()
    escritura = CharField()     # Ejemplo: Novela, cuento, ensayo, poesia, etc.
    generos = CharField()
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

# Funcion que CONECTA (db.connect()) y CREA LAS TABLAS (db.create_tables([Tabla1, Tabla2,])) SAFE=TRUE para evitar que crashee
# el programa, ya que si la base de datos ya existe el programa crashea al correrlo una vez ya creada la base de datos.

def create_n_connect():
    db.connect()
    db.create_tables([Libro], safe=True)        


# Funcion del menu, variable "choice" inicializada en NADA.
# Mientras la opcion sea diferente de 'q':
# Hacemos un ciclo for que itere los elementos de nuestro diccionario ordenado, y con el __doc__, que esta en el VALOR
# muestre el docstring de ese valor, que es el docstring que esta en la funcion (menu_loop: DocString: """Show Menu""")
# Imprimimos esas llaves y valores (docstrings), de nuestro diccionario ordenado.
# Pedimos la opcion al usuario, via un input, y convertimos la opcion a minusculas con lower y sin espacios antes o despues (strip)
# Si la opcion esta en el menu
# Entramos a la opcion del menu elegida:   MENU[OPCION]()   Accedemos a esa opcion via index [] del dict.

def menu_loop():
    """Mostrar Menú"""
    choice = None
    while choice != 'q':
        for key, value in menu.items():
            print(f'{key}) {value.__doc__}')
        choice = input('\nOpción: ').lower().strip()
        if choice in menu:
            menu[choice]()
