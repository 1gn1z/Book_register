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
    paginas = IntegerField()        # Dato de tipo entero
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


# Funcion para agregar un libro a la base de datos.

# Pedimos los datos (autor, titulo, etc.) mediante inputs
# Confirmation, para preguntar al usuario si los datos del libro son correctos.
# Si la confirmacion NO es correcta, osea, si el usuario pone 'n', devuelve la funcion, para que despliegue "add_book" desde el principio
# SINO
# SAVE, esta variable pregunta al usuario, via un input, que si quiere guardar el libro en el registro.
# Si SAVE es igual a 'y', osea, si el usuario SI quiere guardar el registro
# Guardamos el registro con BOOK.CREATE, y dentro del parentesis asignamos los INPUTS que nos paso el usuario a las
# INSTANCIAS (CharField, IntegerField, etc.) (FILAS) del registro.

Libro.registro = Libro.registro     # Asignacion GLOBAL para usarla dentro de la funcion "agregar_libro"

def agregar_libro():
    """Agregar un libro"""
    print('Agregar un libro al registro: ')
    titulo_libro = input('Título del libro:\n').capitalize()      # Capitalize para que la primera letra del titulo se guarde en mayuscula
    titulo_original = input('Título original:\n').capitalize()     # Capitalize para que la primera letra del titulo se guarde en mayuscula
    autor = input('Nombre del autor:\n').title()    # Devuelve en mayusculas LA PRIMERA LETRA DE CADA PALABEA, ideal para los autores

    while True:     # Mientras sea True (bucle indenifido)
        try:        # Intenta
            anio_de_publicacion = int(input('Año de publicación:\n'))
            anio_de_edicion = int(input('Año de edición:\n'))
            paginas = int(input('Número de páginas:\n'))        # Número de páginas del libro
        except ValueError:      # Si hay error de valor es xq el usuario ingreso letras en lugar de números
            print('Debes ingresar un número entero:\n')
        else:
            editorial = input('Editorial del libro:\n')
            edicion = input('Edición (por ejemplo: 1a edición, 1a reimpresión, etc:\n')
            escritura = input('Escritura (por ejemplo: cuento, ensayo, novela, etc:)\n')
            coleccion = input('Colección:\n')
            genero = input('Genero(s) del libro:\n')
            isbn = input('ISBN del libro:\n')
            ilustrador = input('Ilustrador del libro:\n')
            leido = input('Ya leiste el libro? [S/n]: ').lower().strip()
            libro_original = input('El libro es original? [S/n]:\n')
            tipo_de_libro = input('Tipo de libro (por ejemplo, novela, comic, antologia de cuentos, etc.)')
            traduccion = input('Traducción de:\n')
            Libro.registro = Libro.registro     # Fecha en la que el libro fue registrado en el sistema
            confirmacion = input('Los datos son correctos? [S/n]: ')
            if confirmacion == 'n':
                print('\n\n')
                agregar_libro()
            else:
                save = input('Quieres guardar este libro en el registro? [S/n]: ').lower().strip()
                if save != 's':
                    print()
                    menu_loop()

                elif save == 's':
                    Libro.create(
                        anio_de_edicion = anio_de_edicion,
                        anio_de_publicacion = anio_de_publicacion,
                        autor = autor,
                        coleccion = coleccion,
                        edicion = edicion,
                        editorial = editorial,
                        escritura =  escritura,
                        libro_original = libro_original,  
                        genero = genero,
                        ilustrador = ilustrador,
                        isbn = isbn,
                        leido = leido,
                        es_original = es_original,
                        Tipo_de_libro = tipo_de_libro,
                        titulo_libro = titulo_libro,
                        titulo_original = titulo_original,
                        tradducion = traduccion
                                ) 
                    print('\nTu registro fue guardado exitosamente\n\n')
                    break


# Funcion para ver todos los libros registrados actualmente en el programa.
# libros = Libro.select().order_by(Libro.titulo.desc()). Del mas recientemente agregado al mas antiguamente agregado.

# if search_query:  Si en verdad hay una busqueda, dado que es opcional, entonces:
# libros=libros.where...    libros es igual a todos (select) los libros, donde (where), el titulo del libro contenga (contains)
# la search query, que es lo que el usuario nos paso en la misma search query.

# ciclo for para iterar todos los libros, y va imprimiendo uno por uno el titulo, autor, año, generos, isbn y leido.

# Si el libro.leido == 's', es decir si al registrarlo dijimos que ya lo leimos, entonces imprimimos que si esta leido
# SINO, libro.leido == 'n', entonces imprimimos que no esta leido
# ELSE, imprimimos que no sabemos si esta leido o no.

# sig_accion, un INPUT que detiene el ciclo for en la iteracion actual, asi que si oprimimos s, nos muestra el siguiente libro :D
# Si presionamos q, hace un break, es decir, rompe el ciclo y nos saca de el, dejandonos en el menu principal
# si presionamos e, ejecuta la funcion "eliminar_libro"


def ver_libros(search_query=None):      # Esta función recibe un parámetro, que es la busqueda que el usuario hará (serarch_query). Como cuando buscas un título de un video en YouTube.
    """Ver todos los libros registrados"""    
    libros = Libro.select().order_by(Libro.titulo_libro.desc())   # todos los registros existentes con Libro.select() | ordenados por (ordered_by) . titulo descendente para ver los más recientemente agregados primero.
    
    if search_query:
        libros = libros.where(Libro.titulo_libro.contains(search_query))

    for libro in libros:

        print()
        print('________________________________________')
        print()
        print('Título del libro: ' + libro.titulo_libro)
        print('Autor del libro: ' + libro.autor)
        print('Año de publicación: ' + str(libro.anio_de_publicacion)) 
        print('Géneros(s) del libro: ' + libro.genero)
        print('ISBN del libro: ' + libro.isbn)
        print()
        print('Libro leído? ')
        if libro.leido == 's':
            print('SI!, libro leído :D')
        elif libro.leido == 'n':
            print('NO, libro no leído :(')
        else:
            print('No se sabe si el libro ha sido leído o no')
        print()
        print('________________________________________')
        print('\n')
        print('s) siguiente libro')
        print('e) editar el libro')
        print('x) eliminar libro')
        print('q) regresar al menú')
        print('\n')
        sig_accion = input('Acción: [Seq]: ').lower().strip()
        print('\n')
        if sig_accion == 'q':
            print('\n')
            break
        elif sig_accion == 'e':
            editar_libro(libro)
        elif sig_accion == 'x':
            eliminar_libro(libro)
    
