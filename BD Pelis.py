import os
import sqlite3
import sqlite3

dbName = "filmsDB.db"

def mostrarMenu():
    print("")
    print("----------------------------------")
    print("1. Mostrar todas las películas")
    print("2. Mostrar todos los directores")
    print("3. Ver peliculas de un director")
    print("0. Salir")

def devolverRegistros(sql):
    cn = sqlite3.connect(dbName)

    cur = cn.cursor()

    registros = cur.execute(sql).fetchall()

    cn.close()

    return registros

def listarPeliculas():
    os.system("cls")
    print("-----PELICULAS------")
    
    pelis = devolverRegistros("SELECT * FROM Films")
    for r in pelis:
        print(r)

def listarDirectores():
    os.system("cls")
    print("\n-----DIRECTORES------")
    dires = devolverRegistros("SELECT * FROM Directors")
    for r in dires:
        print(r)

def obtenerDatosDirector(idDirec):
    regs = devolverRegistros("SELECT Directors.name, surname FROM Directors WHERE id=" + idDirec)
    if (len(regs)>0):
        return regs[0][0], regs[0][1]
    else:
        return "No encontrado", ""

def mostrarPeliculasDirector(idDirector):
    os.system("cls")
    nombre, apellidos = obtenerDatosDirector(idDirector)
    print(f"\n----- PELICULAS DE {nombre} {apellidos} ------")
    pelis = devolverRegistros("SELECT title FROM Films, Directors WHERE Films.director=Directors.id AND Directors.id=" + idDirector)
    for r in pelis:
        print(r[0])

opcion = 1
os.system("cls")
while(opcion!=0):
    mostrarMenu()

    opcion = int(input("Teclee opción deseada:"))
    
    if (opcion==1):
        listarPeliculas()
    elif (opcion==2):
        listarDirectores()
    elif (opcion==3):
        idDirector = input("ID del director: (use antes la opción mostrar directores) \n")
        mostrarPeliculasDirector(idDirector)

