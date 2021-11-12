"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from time import process_time
assert cf
import sys as sis
from datetime import datetime
from DISClib.ADT import map as mp

default_limit = 1000
sys.setrecursionlimit(default_limit*10)
catalog = None

#Imprimir el Menú
def printMenu():
    print ("Bienvenido")
    print ("1. Cargar archivos.")
    print ("2. Requerimiento 1: Listar cronológicamente los artistas.")
    print ("3. Requerimiento 2: Listar cronológicamente las adquisiciones.")
    print ("4. Requerimiento 3: Clasificar las obras de un artista por técnica.")
    print ("5. Requerimiento 4: Clasificar las obras por la nacionalidad de sus artistas.")
    print ("6. Requerimiento 5: Transportar obras de un departamento.")
    print ("7. Requerimiento 6: Artistas más prolíficos de un periodo.")
    print ("0. Salir")

#Iniciador de catalogos y carga de datos
def initCatalog():
    return controller.initCatalog()
def loadData(catalog):
    controller.loadData(catalog)


#Funciones de imprimir: listas y cmpfunction de estas

#Menú Principal
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        t1 = process_time()
        catalog = initCatalog()
        loadData(catalog)
        t2 = process_time()
        time = t2-t1
        print("El tiempo para cargar los archivos fue de:", str(time) , "s") 

    elif int(inputs[0]) == 2: 
        
        begin1 = int(input("Digite el año de nacimiento inicial: "))
        begin2 = int(input("Digite el año de nacimiento final: "))
        t1 = process_time()
        respuestas = controller.requerimiento1(catalog, begin1, begin2)
        t2 = process_time()
        time = t2-t1
        print("El tiempo para cargar los archivos fue de:", str(time) , "s") 
        print("El número total de artistas que nacieron en ese rango de fechas fue de " + str(respuestas[0]))
        print("Los primeros 3 artistas y los últimos 3 artistas fueron: ")
        print("+"+("-"*217)+"+")
        print("|"+"ConstituentID".center(18)+" | "+ "DisplayName".center(61)+" | "+"BeginDate".center(15)+" | "+"Nationality".center(20)+" | "+"Gender".center(15)+" | "+"ArtistBio".center(30) + " | " + "Wiki QID".center(16) + " | " + "ULAN".center(20) + " | ")
        print("+"+("-"*217)+"+")

        for i in lt.iterator(respuestas[1]):
            print("|"+ i["ConstituentID"].center(18)+" | "+ i["DisplayName"].center(61)+" | "+ i["BeginDate"].center(15)+" | "+i["Nationality"].center(20)+" | "+i["Gender"].center(15)+" | "+ i["ArtistBio"].center(30) + " | " + i["Wiki QID"].center(16) + " | " + i["ULAN"].center(20) + " | ")
            print("+"+("-"*217)+"+")
        
    elif int(inputs[0]) == 3:
        begin = input("Digite la fecha en formato YYYY-MM-DD: ")
        end = input("Digite la fecha en formato YYYY-MM-DD: ")
        t1 = process_time()
        respuestas = controller.requerimiento2(catalog,begin,end)
        t2 = process_time()
        time = t2-t1
        print("El tiempo para cargar los archivos fue de:", str(time) , "s") 
        print("El número total de obras en el rango deseado es de: " + str(respuestas[0]))
        print("Las obras adquiridas por Purchase es de: " + str(respuestas[1]))
        print("Las primeras 3 y últimas 3 obras de ese rango de tiempo fueron: ")
        print("=" * 200)
        for i in lt.iterator(respuestas[2]):
            print("ObjectID: " + i["ObjectID"])
            print("Title: " + i["Title"])
            print("ArtistNames: ")
            CI = i["ConstituentID"].split(",")
            for artista in CI: 
                artista = artista.strip("[] ")
                print(mp.get(catalog["ConstituentName"], artista)["value"])
            print("Medium: " + i["Medium"])
            print("Dimensions: " + i["Dimensions"])
            print("Date: " + i["Date"])
            print("DateAcquired: " + i["DateAcquired"])
            print("URL: " + i["URL"])       
            print("=" * 200)
        
        
    elif int(inputs[0]) == 4: 
        artist =  input("Ingrese el nombre del artista de las obras a clasificar: ")
        t1 = process_time()
        
        info = controller.artworksClasification(catalog, artist)
        s = mp.size(info[1])
        print(str(artist) + " identificado con el ID " + str(info[0]) + " tiene un total de " + str(s) + " obras")      
        t1 = process_time()
        topMeds = controller.topMeds(info[1])
        orden = controller.orden(topMeds)
        respuestas = controller.requerimiento2(catalog,begin,end)
        t2 = process_time()
        time = t2-t1
        print("El tiempo para cargar los archivos fue de:", str(time) , "s") 
        print("Tiene un total de " + str(orden[0]) + " medios diferentes")
        print("Medio".center(50)+"|"+"Obras".center(9))
        print("-"*60)
        t = 0
        while t < 10:
            a = str(orden[1]["elements"][t])
            b = str(orden[1]["elements"][t+1])
            print(a.center(50)+"|"+b.center(9))
            print("-"*60)
            t+=2      
        
        a = str(orden[1]["elements"][0])
        med = controller.printArtMed(catalog, info[0],a) 

    elif int(inputs[0]) == 5:        
        t1 = process_time()
        respuestas = controller.requerimiento4(catalog)
        t2 = process_time()
        time = t2-t1
        print("El tiempo para cargar los archivos fue de:", str(time) , "s") 
        print("Nationality".center(30)+"|"+"Artworks".center(7))
        print("-"*39)
        t = 0
        while t < 20:
            a = str(respuestas["elements"][t])
            b = str(respuestas["elements"][t+1])
            print(a.center(30)+"|"+ b.center(7))
            print("-"*39)
            t+=2
        c = controller.printNats(catalog, respuestas["elements"][0])
    
    elif int(inputs[0]) == 6:
        department = input("Digite el departamento a evaluar: ")
        t1 = process_time()
        respuesta = controller.requerimiento5(catalog,department)
        t2 = process_time()
        time = t2-t1
        print("El tiempo para cargar los archivos fue de:", str(time) , "s") 
        print ("El tamaño del departamento es de " + str(respuesta[0]) + " obras.")
        print ("El costo total de transporte es de " + str(respuesta[1]) + "USD")
        print("Las 5 obras más caras a transportar son:")
        print ("=" * 200)
        for x in lt.iterator(respuesta[2]):
            print("ObjectID: " + x["ObjectID"])
            print("Title: " + x["Title"])
            print("ArtistsNames: ")
            CI = x["ConstituentID"].split(",")
            for artista in CI: 
                artista = artista.strip("[] ")
                print(mp.get(catalog["ConstituentName"], artista)["value"])
            print("Medium: " + x["Medium"])
            print("Date: " + x["Date"])
            print("Dimensions: " + x["Dimensions"])
            print("Classification: " + x["Classification"] )
            print("Costo de transporte" + str(x["Costo"]))
            print("URL: " + x["URL"])
            print ("=" * 200)
        print ("Las obras mas antiguas a transportar son: ")
        print ("=" * 200)
        for x in lt.iterator(respuesta[3]):
            print("ObjectID: " + x["ObjectID"])
            print("Title: " + x["Title"])
            print("ArtistsNames: ")
            CI = x["ConstituentID"].split(",")
            for artista in CI: 
                artista = artista.strip("[] ")
                print(mp.get(catalog["ConstituentName"], artista)["value"])
            print("Medium: " + x["Medium"])
            print("Date: " + x["Date"])
            print("Dimensions: " + x["Dimensions"])
            print("Classification: " + x["Classification"] )
            print("Costo de transporte" + str(x["Costo"]))
            print("URL: " + x["URL"])
            print ("=" * 200)
    
    elif int(inputs[0])== 7:
        begin = int(input("Digite el año de nacimiento inicial: "))
        end = int(input("Digite el año de nacimiento final: "))
        cant = int(input("Ingrese la cantidad de artistas que desea ver: "))
        t1 = process_time()
        respuestas = controller.requerimiento6(catalog, begin, end)
        top = controller.top(catalog, respuestas,cant)
        t2 = process_time()
        time = t2-t1
        print("El tiempo para cargar los archivos fue de:", str(time) , "s") 
    else:
        sys.exit(0)
sys.exit(0)