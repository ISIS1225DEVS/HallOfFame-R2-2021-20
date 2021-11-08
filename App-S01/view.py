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
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

###########################################################################################
#Funciones de exposición de resultados
###########################################################################################

def printRequirement1(requirement_list):
    requirement_info = controller.requirement1Info(requirement_list)
    num_artists = requirement_info[0]
    first_artists = requirement_info[1]
    last_artists = requirement_info[2]
    print('Existen', num_artists, 'artistas nacidos en el rango de fechas indicado')
    print('')
    print('Los primeros 3 artistas del rango de años son:')
    for artist in lt.iterator(first_artists):
        print('Nombre: ' + artist['DisplayName'] + ', Año de nacimiento: ' +  artist['BeginDate'] + 
                    ', Año de fallecimiento: ' + artist['EndDate'] + ', Nacionalidad: '+ artist['Nationality'] + 
                    ', Genero: ' + artist['Gender'])
    print('')
    print('Los últimos 3 artistas del rango de años son:')
    for artist in lt.iterator(last_artists):
        print('Nombre: ' + artist['DisplayName'] + ', Año de nacimiento: ' +  artist['BeginDate'] + 
                    ', Año de fallecimiento: ' + artist['EndDate'] + ', Nacionalidad: '+ artist['Nationality'] + 
                    ', Genero: ' + artist['Gender'])

###########################################################################################

def printRequirement2(catalog, requirement_list, num_purchased_artworks):
    requirement_info = controller.requirement2Info(requirement_list)
    num_artworks = requirement_info[0]
    first_artworks = requirement_info[1]
    last_artworks = requirement_info[2]
    print('Existen', num_artworks, 'obras de arte adquiridas en el rango de fechas indicado')
    print('Existen', num_purchased_artworks, 'obras de arte adquiridas por compra en el rango de fechas indicado')
    print('')
    print('Las primeras 3 obras de arte del rango de fechas son:')
    for artwork in lt.iterator(first_artworks):
        artists = controller.getArtistsListInStr(catalog, artwork)
        print('Título: ' + artwork['Title'] + ', Artista(s): ' +  artists + 
                    ', Fecha de adquisición: ' + artwork['DateAcquired'] + ', Medio '+ artwork['Medium'] + 
                    ', Dimensiones: ' + artwork['Dimensions'])
    print('')
    print('Las últimas 3 obras de arte del rango de fechas son:')
    for artwork in lt.iterator(last_artworks):
        artists = controller.getArtistsListInStr(catalog, artwork)
        print('Título: ' + artwork['Title'] + ', Artista(s): ' +  artists + 
                    ', Fecha de adquisición: ' + artwork['DateAcquired'] + ', Medio '+ artwork['Medium'] + 
                    ', Dimensiones: ' + artwork['Dimensions'])

###########################################################################################

def printRequirement3(requirement_list, num_total_artworks, num_total_mediums, name_most_used_medium):
    requirement_info = controller.requirement3Info(requirement_list)
    num_artworks_medium = requirement_info[0]
    first_artworks = requirement_info[1]
    last_artworks = requirement_info[2]
    print('Existen', num_total_artworks, 'obras de arte del artista.')
    print('El artista empleó', num_total_mediums, 'técnicas en sus obras')
    print('Existen', num_artworks_medium, 'obras de arte del artista hechos con su técnica más utilizada,', name_most_used_medium)
    #+ name_most_used_medium + ' .'
    print('')
    print('Las primeras 3 obras de arte de la técnica más utilizada por el artista son:')
    for artwork in lt.iterator(first_artworks):
        print('Título: ' + artwork['Title'] + ', Fecha de creación: ' + artwork['Date'] +
                 ', Medio '+ artwork['Medium'] + ', Dimensiones: ' + artwork['Dimensions'])
    print('')
    print('Las últimas 3 obras de arte de la técnica más utilizada por el artista son:')
    for artwork in lt.iterator(last_artworks):
        print('Título: ' + artwork['Title'] + ', Fecha de creación: ' + artwork['Date'] +
                 ', Medio '+ artwork['Medium'] + ', Dimensiones: ' + artwork['Dimensions'])

###########################################################################################

def printRequirement4(catalog, requirement_list_artworks, requirement_list_nationalities):
    requirement_info = controller.requirement4Info(requirement_list_artworks, requirement_list_nationalities)
    first_artworks = requirement_info[0]
    last_artworks = requirement_info[1]
    first_nationalities = requirement_info[2]
    print('Las primeras 10 nacionalidades por número de obras son: ')
    print('{:<20}{:<20}'.format('Nacionalidad', 'Número de obras'))
    for nationality in lt.iterator(first_nationalities):
        num_artworks_nationality = nationality[1]
        nationality_name = nationality[0]
        if nationality_name == '':
                nationality_name = 'Desconocida'
        print('{:<20}{:<20}'.format(nationality_name, num_artworks_nationality))
    print('')
    print('Las primeras 3 obras de la nacionalidad con más obras son:')
    for artwork in lt.iterator(first_artworks):
        artists = controller.getArtistsListInStr(catalog, artwork)
        print('Título: ' + artwork['Title'] + ', Artista(s): ' +  artists + 
                    ', Fecha de creación: ' + artwork['Date'] + ', Medio '+ artwork['Medium'] + 
                    ', Dimensiones: ' + artwork['Dimensions'])
    print('')
    print('Las últimas 3 obras de la nacionalidad con más obras son:')
    for artwork in lt.iterator(last_artworks):
        artists = controller.getArtistsListInStr(catalog, artwork)
        print('Título: ' + artwork['Title'] + ', Artista(s): ' +  artists + 
                    ', Fecha de creación: ' + artwork['Date'] + ', Medio '+ artwork['Medium'] + 
                    ', Dimensiones: ' + artwork['Dimensions'])

###########################################################################################

def printRequirement5(catalog, requirement_list_by_date, requirement_list_by_price, total_cost, total_weight):
    requirement_info = controller.requirement5Info(requirement_list_by_date, requirement_list_by_price)
    num_artworks = requirement_info[0]
    oldest_artworks = requirement_info[1]
    most_expensive_artworks = requirement_info[2]
    print('Existen', num_artworks, 'obras de arte en el departamento')
    print('El costo total de transporte de las obras de arte del departamento es', round(total_cost, 2), 'USD.')
    print('El peso total de las obras del departamento es', round(total_weight, 2), 'Kg.')
    print('')
    print('Las 5 obras de arte más costosas de transportar eson:')
    for artwork in lt.iterator(most_expensive_artworks):
        artwork_info = artwork[0]
        artwork_cost = artwork[1]
        artists = controller.getArtistsListInStr(catalog, artwork_info)
        print('Título: ' + artwork_info['Title'] + ', Artista(s): ' +  artists + 
                    ', Fecha de creación: ' + artwork_info['Date'] + ', Medio '+ artwork_info['Medium'] + 
                    ', Dimensiones: ' + artwork_info['Dimensions'] + ', Costo de transporte: ' +
                    str(round(artwork_cost, 2)) + ' USD')
    print('')
    print('Las 5 obras más antiguas del departamento son:')
    for artwork in lt.iterator(oldest_artworks):
        artwork_info = artwork[0]
        artwork_cost = artwork[1]
        artists = controller.getArtistsListInStr(catalog, artwork_info)
        print('Título: ' + artwork_info['Title'] + ', Artista(s): ' +  artists + 
                    ', Fecha de creación: ' + artwork_info['Date'] + ', Medio '+ artwork_info['Medium'] + 
                    ', Dimensiones: ' + artwork_info['Dimensions'] + ', Costo de transporte: ' + 
                    str(round(artwork_cost, 2)) + ' USD')

###########################################################################################

def printRequirement6(requirement_list, num_artists):
    print('Los', num_artists, 'artistas más prolíficos del periodo son:')
    print('')
    for artist in lt.iterator(requirement_list):
        artist_name = artist[0]
        artworks_most_used_medium = artist[1]
        num_total_artworks = artist[2]
        num_total_mediums = artist[3]
        num_most_used_medium = artist[4]
        name_most_used_medium = artist[5]
        print(artist_name + ' con:')
        print('-', num_total_artworks, 'obras de arte creadas')
        print('El artista empleó', num_total_mediums, 'técnicas en sus obras')
        print('-', 'Existen', num_most_used_medium, 'obras de arte hechas con su técnica más utilizada,', name_most_used_medium)
        print('')
        print('Las primeras 5 obras de arte hechas en la técnica más utilizada por el artista son: ')
        for artwork in lt.iterator(artworks_most_used_medium):
            print('Título: ' + artwork['Title'] + ', Fecha de creación: ' + artwork['Date'] +
                     ', Medio '+ artwork['Medium'] + ', Dimensiones: ' + artwork['Dimensions'])

###########################################################################################
#Menu principal
###########################################################################################

def printMenu():
    print('')
    print('Bienvenido')
    print('1- Cargar información en el catálogo')
    print('2- REQ. 1: listar cronológicamente los artistas')
    print('3- REQ. 2: listar cronológicamente las adquisiciones')
    print('4- REQ. 3: clasificar las obras de un artista por técnica')
    print('5- REQ. 4: clasificar las obras por la nacionalidad de sus creadores')
    print('6- REQ. 5: transportar obras de un departamento')
    print('7- REQ. 6: Encontrar los artistas más prolíficos del museo')
    print('0- Salir')
    option = int(input('Seleccione una opción para continuar: '))
    return option

###########################################################################################

def SortingAlgorithmOptions():
    print('Algoritmos de ordenamiento disponibles: ')
    print('1) Insertion Sort')
    print('2) Shell Sort')
    print('3) Merge Sort')
    print('4) Quick Sort')
    sorting_method = input('Ingrese el algoritmo elegido: ')
    return sorting_method

###########################################################################################

catalog = None

while True:
    option = printMenu()
    if option == 1:
        print('Existen 15223 artistas y 138150 obras de arte en los archivos')
        artists_sample_size = int(input('Elija la cantidad de artistas que desea cargar: '))
        artworks_sample_size = int(input('Elija la cantidad de obras de arte que desea cargar: '))
        print('')
        print('Las estructuras de datos disponibles para cargar los datos son: ')
        print('1- Lista encadenada')
        print('2- Lista ordenada')
        data_structure = controller.getDataStructure(int(input('Elija la estructura de datos: ')))
        print("Cargando información de los archivos ...")
        catalog = controller.initCatalog(data_structure)
        controller.loadData(catalog, data_structure, artists_sample_size, artworks_sample_size)

    elif option == 2:
        initial_birth_year = int(input('Ingrese el primer año del intervalo: '))
        end_birth_year = int(input('Ingrese el último año del intervalo: '))
        print('Procesando...')
        requirement_info = controller.getArtistsByBirthYear(catalog, data_structure,
                                                                initial_birth_year, end_birth_year)
        elapsed_time = requirement_info[0]
        print('')
        print('Tiempo empleado:', elapsed_time, 'mseg')
        print('')
        requirement_list = requirement_info[1]
        printRequirement1(requirement_list)

    elif option == 3:
        initial_adquisiton_date = input('Ingrese la primera fecha del intervalo: ')
        end_adquisition_date = input('Ingrese la última fecha del intervalo: ')
        print('')
        sorting_method = SortingAlgorithmOptions()
        print('Procesando...')
        requirement_info = controller.getArtworksByAdquisitonDate(catalog, data_structure, sorting_method,
                                                        initial_adquisiton_date, end_adquisition_date)
        elapsed_time = requirement_info[0]
        print('')
        print('Tiempo empleado:', elapsed_time, 'mseg')
        print('')
        requirement_list = requirement_info[1]    
        num_purchased_artworks = requirement_info[2]                         
        printRequirement2(catalog, requirement_list, num_purchased_artworks)

    elif option == 4:
        artist_name = input('Ingrese el nombre del artista: ')
        print('')
        print('Procesando...')
        requirement_info = controller.getArtworksByMediumAndArtist(catalog, artist_name)
        elapsed_time = requirement_info[0]
        print('')
        print('Tiempo empleado:', elapsed_time, 'mseg')
        print('')
        requirement_list = requirement_info[1]
        num_total_artworks = requirement_info[2]
        num_total_mediums = requirement_info[3]
        name_most_used_medium = requirement_info[4]
        printRequirement3(requirement_list, num_total_artworks, num_total_mediums, name_most_used_medium)

    elif option == 5:
        print('')
        sorting_method = SortingAlgorithmOptions()
        print('Procesando...')
        requirement_info = controller.getNationalitiesByNumArtworks(catalog, data_structure, sorting_method)
        elapsed_time = requirement_info[0]
        print('')
        print('Tiempo empleado:', elapsed_time, 'mseg')
        print('')
        requirement_list_artworks = requirement_info[1]
        requirement_list_nationalities = requirement_info[2]
        printRequirement4(catalog, requirement_list_artworks, requirement_list_nationalities) 

    elif option == 6:  
        department = input('Ingrese el nombre del departamento: ')
        print('')
        sorting_method = SortingAlgorithmOptions()
        print('Procesando...')
        requirement_info = controller.getTransportationCostByDepartment(catalog, data_structure, 
                                                                                sorting_method, department)
        elapsed_time = requirement_info[0]
        print('')
        print('Tiempo empleado:', elapsed_time, 'mseg')
        print('')
        requirement_list_by_date = requirement_info[1]
        requirement_list_by_price = requirement_info[2]
        total_cost = requirement_info[3]
        total_weight = requirement_info[4]
        printRequirement5(catalog, requirement_list_by_date, requirement_list_by_price, total_cost, total_weight) 

    elif option == 7: 
        num_artists = int(input('Ingrese el número de artistas que desea en la clasificación: '))
        initial_birth_year = int(input('Ingrese el primer año del intervalo: '))
        end_birth_year = int(input('Ingrese el último año del intervalo: '))
        print('')
        sorting_method = SortingAlgorithmOptions()
        print('Procesando...')
        requirement_info = controller.getMostProlificArtists(catalog, data_structure, sorting_method,
                                                                    initial_birth_year, end_birth_year, num_artists)
        elapsed_time = requirement_info[0]
        print('')
        print('Tiempo empleado:', elapsed_time, 'mseg')
        print('')
        requirement_list = requirement_info[1]
        printRequirement6(requirement_list, num_artists)
    else:
        sys.exit(0)
sys.exit(0)