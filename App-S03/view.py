﻿"""
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

from typing import List
import config as cf
import sys
import controller
import model
from DISClib.ADT import list as lt
assert cf
import time

defaul_time = 1000
sys.setrecursionlimit(defaul_time*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lista cronológica de los artistas")
    print("3- Lista cronológica de adquisiciones")
    print("4- Calsificación de obras de un artista por técnica")
    print("5- Clasificar obras por la nacionalidad de sus creadores")
    print("6- Transporte de obras de un departamento")

catalog = None

#funciones de print


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        start_time = time.process_time()
        controller.loadData(catalog)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("El tiempo utilizado es de: "+str(elapsed_time_mseg)+ " milisegundos")
        model.getArtworkNationality(catalog)


    elif int(inputs[0]) == 2:

        #Req 1
        anoInicial = int(input('Ingresa el año inicial del rango: '))
        anoFinal = int(input('Ingrese el año final del rango: '))
        DatesA = controller.getArtistByDate(catalog, anoInicial, anoFinal)
        print("Tiempo utilizado en el ordenamiento: " + str(DatesA[1]) + " Milisegundos" )
        print('There are ' + str(lt.size(DatesA[0])) + ' artists born between ' + str(anoInicial) + ' and ' + str(anoFinal))
        print("First three artists:")
        print(DatesA[0]['elements'][0:3])
        print("Last three artists: ")
        print(DatesA[0]['elements'][-3:])


    elif int(inputs[0]) == 3:
        #Req 2: 
        Inicial = input('Ingresa la fecha inicial del rango, en el formato AAAA-MM-DD: ')
        Final = input('Ingrese la fecha final del rango, en el formato AAAA-MM-DD: ')
        datesArtworks = controller.getArtworksByDateAcquired(catalog, Inicial, Final)
        print('The MoMA acquired ' + str(lt.size(datesArtworks[0])) + ' unique pieces between ' + Inicial + ' and ' + Final)
        print('And purchased ' + str(controller.getartworkPurchased(datesArtworks[0])) + ' of them.')
        print("First three elements: ")
        print(datesArtworks[0]['elements'][0:3])
        print("Last three elements: ")
        print(datesArtworks[0]['elements'][-3:])
        print("Tiempo utilizado en el ordenamiento: " + str(datesArtworks[1]) + " Milisegundos")


    
    elif int(inputs[0]) == 4:
        #Req 3:
        #Louise Bourgeois
        Artistname = input('Ingrese el nombre del artista: ') 
        ArtworkTecnique = controller.getArtworksMediumOneArtist(catalog, Artistname)
        countM = lt.size(ArtworkTecnique[0]) #Número de Medios utilizados por el artista
        countA = 0
        for tec in lt.iterator(ArtworkTecnique[0]):
            countA += int(tec['NumbArtworks']) #El número de obras que tiene el artista 
        sort_list = ArtworkTecnique[0]
        Medium = lt.getElement(sort_list, 1)
        medium = Medium['Medium'] #Nombre del medio más utilizado
        
        mayorM = Medium['NumbArtworks'] #Número de obras del medio más utlizado 

        obras = controller.getArtworkOneMedium(catalog, medium) #obras del medio más utlizado

        #str(artist_id) + 
        print("Tiempo utilizado en el ordenamiento: " + str(ArtworkTecnique[1]) + " Milisegundos")  
        print(Artistname + ' has ' + str(countA) + ' pieces in his/her name at the museum.')
        print('There are ' + str(countM) + ' different mediums/tecniques in his/her work.')
        print('His/Her most used Medium/Tecnique is ' + str(medium) + ' with ' + str(mayorM) + ' pieces')
        print('List of the artworks of the most used tecnique/medium:')
        print('Fisrt three artworks: ')
        print(obras['elements'][0:3])
        print('Last three artworks: ')
        print(obras['elements'][-3:])


    elif int(inputs[0]) == 5:
        #Req 4:
        DatesA = controller.getArtworksNationality(catalog)
        i = 1
        top10 = lt.subList(DatesA[0],1,10)
        print("--------------------------------------------------------------------------")
        print("TOP 10 Nationalities")
        print("--------------------------------------------------------------------------")
        for item in lt.iterator(top10):           
            
            print(str(i) +'. '+ str(item["Nationality"]) +' with '+ str(item["NumbArtworks"]) + " Artworks")
            i+=1
        firtsplace= lt.getElement(top10,1)
        print("--------------------------------------------------------------------------")
        print("ARTWORKS FROM " + str(firtsplace["Nationality"]).upper())
        list_needed = controller.getArtworksOneNat(catalog, firtsplace["Nationality"])
        first_three = lt.subList(list_needed,1,3)
        size_needed = lt.size(list_needed)
        last_three = lt.subList(list_needed,size_needed-3,3)
        print("--------------------------------------------------------------------------")
        print("First three")
        for artwork in lt.iterator(first_three):
            artists = controller.getArtists(catalog,artwork)
            print(str(artwork["Title"]) +', '+ str(artwork["DateAcquired"]) +', '+ str(artwork["Medium"])+', '+str(artwork["Dimensions"]) + ','+ str(artists))
        print("--------------------------------------------------------------------------")
        print("Last three")
        for artwork in lt.iterator(last_three):
            artists = controller.getArtists(catalog,artwork)
            print(str(artwork["Title"]) +', '+ str(artwork["DateAcquired"]) +', '+ str(artwork["Medium"])+', '+str(artwork["Dimensions"]) + ','+ str(artists))
        print("--------------------------------------------------------------------------")
        print("Tiempo utilizado en el ordenamiento: " + str(DatesA[1]) + " Milisegundos")

    elif int(inputs[0]) == 6:
        #Req 5:
        dep = input('Ingrese el departamento del museo: ').lower()
        DatesA = controller.getArtworksByDepartment(catalog,dep.lower())
        print('The MoMA is going to transport ' +str(lt.size(DatesA[0]))+ ' artifacts from Drawings and Prints')
        print("REMEMBER! NOT all MoMA's data is complete!!!... These are estimates.")
        print("Estimated cargo weight (kg): " + str(DatesA[2]))
        print("Estimated cargo cost (USD): "+ str(DatesA[3]))
        print("--------------------------------------------------------------------------")
        print("Top 5 oldest artworks to transport: ")
        top5a = lt.subList(DatesA[1],1,5)
        top5p = lt.subList(DatesA[0],1,5)
        i = 1
        for item in lt.iterator(top5a): 
            lisArtist = controller.getArtists(catalog,item)
            print(str(i) +'. Title: '+ str(item["Title"]) +', Artists: ' +str(lisArtist)+ ', Date: ' + str(item["Date"]) + ', Medium: ' + str(item["Medium"]) +', Cost of transportation: ' 
            + str(item["Price"]) + ',Dimensions: ' + str(item["Dimensions"]))
            i+=1
        print("--------------------------------------------------------------------------")
        print("Top 5 most expensive artworks to transport: ")
        i = 1
        for item in lt.iterator(top5p):  
            lisArtist = controller.getArtists(catalog,item)
            print(str(i) +'. Title: '+ str(item["Title"]) +', Artists: ' +str(lisArtist)+ ', Date: ' + str(item["Date"]) + ', Medium: ' + str(item["Medium"]) +', Cost of transportation: ' 
            + str(item["Price"]) + ',Dimensions: ' + str(item["Dimensions"]))
            i += 1
        print("--------------------------------------------------------------------------")
        print("Tiempo utilizado en el ordenamiento: " + str(DatesA[4]) + " Milisegundos")
    else:
        sys.exit(0)
sys.exit(0)

