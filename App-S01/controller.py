"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
import model
import csv
import time

###########################################################################################
# Inicialización del Catálogo de libros
###########################################################################################

def initCatalog(data_structure):
    return model.newCatalog(data_structure)

###########################################################################################
# Funciones para la carga de datos
###########################################################################################

def loadData(initiation_data, data_structure, artists_sample_size, artworks_sample_size):
    loadArtistsRelatedData(initiation_data, data_structure, artists_sample_size)
    loadArtworksRelatedData(initiation_data, data_structure, artworks_sample_size)

###########################################################################################

def loadArtistsRelatedData(catalog, data_structure, sample_size):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    artists_info = list(input_file)[:sample_size]
    for artist in artists_info:
        model.addArtist(catalog, artist, data_structure)
        model.addBirthYearArtist(catalog, artist, data_structure)
    
###########################################################################################

def loadArtworksRelatedData(catalog, data_structure, sample_size):
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    artworks_info = list(input_file)[:sample_size]
    for artwork in artworks_info:
        model.addArtwork(catalog, artwork)
        model.addAdquisitionYear(catalog, artwork, data_structure)
        model.addMedium(catalog, artwork, data_structure)
        model.addNationality(catalog, artwork, data_structure)
        model.addDepartment(catalog, artwork, data_structure)

###########################################################################################
# Funciones de ordenamiento
###########################################################################################

def requirement1Info(requirement_list):
    return model.requirement1Info(requirement_list)

###########################################################################################

def requirement2Info(requirement_list):
    return model.requirement2Info(requirement_list)

###########################################################################################

def requirement3Info(requirement_list):
    return model.requirement3Info(requirement_list)

###########################################################################################

def requirement4Info(requirement_list_artworks, requirement_list_nationalities):
    return model.requirement4Info(requirement_list_artworks, requirement_list_nationalities)

###########################################################################################

def requirement5Info(requirement_list_by_date, requirement_list_by_price):
    return model.requirement5Info(requirement_list_by_date, requirement_list_by_price)

###########################################################################################
# Funciones de consulta sobre el catálogo
###########################################################################################

def getDataStructure(data_structure):
    return model.getDataStructure(data_structure)

###########################################################################################

def getArtistsListInStr(catalog, artwork):
    return model.getArtistsListInStr(catalog, artwork)

###########################################################################################

def getArtistsByBirthYear(catalog, data_structure, initial_birth_year, end_birth_year):
    start_time = time.process_time()

    requirement_list = model.getArtistsByBirthYear(catalog, data_structure,
                                                     initial_birth_year, end_birth_year)

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000 
    return elapsed_time, requirement_list

###########################################################################################

def getArtworksByAdquisitonDate(catalog, data_structure, sorting_method,
                                                    initial_adquisiton_date, end_adquisition_date):
    start_time = time.process_time()

    requirement_list = model.getArtworksByAdquisitonDate(catalog, data_structure, sorting_method,
                                                    initial_adquisiton_date, end_adquisition_date)
    num_purchased_artworks = model.getNumPurchasedArtworks(requirement_list, sorting_method)

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000  
    return elapsed_time, requirement_list, num_purchased_artworks

###########################################################################################

def getArtworksByMediumAndArtist(catalog, artist_name):
    start_time = time.process_time()

    requirement_info = model.getArtworksByMediumAndArtist(catalog, artist_name)
    requirement_list = requirement_info[0]
    num_total_artworks = requirement_info[1]
    num_total_mediums = requirement_info[2]
    name_most_used_medium = requirement_info[3]

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000  
    return elapsed_time, requirement_list, num_total_artworks, num_total_mediums, name_most_used_medium

###########################################################################################

def getNationalitiesByNumArtworks(catalog, data_structure, sorting_method):
    start_time = time.process_time()

    requirement_info = model.getNationalitiesByNumArtworks(catalog, data_structure, sorting_method)
    requirement_list_artworks = requirement_info[0]
    requirement_list_nationalities = requirement_info[1]

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000  
    return elapsed_time, requirement_list_artworks, requirement_list_nationalities

###########################################################################################

def getTransportationCostByDepartment(catalog, data_structure, sorting_method, department):
    start_time = time.process_time()

    requirement_info = model.getTransportationCostByDepartment(catalog, data_structure,
                                                                sorting_method, department)
    requirement_list_by_date = requirement_info[0]
    requirement_list_by_price = requirement_info[1]
    total_cost = requirement_info[2]
    total_weight = requirement_info[3]

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000 
    return elapsed_time, requirement_list_by_date, requirement_list_by_price, total_cost, total_weight

###########################################################################################

def getMostProlificArtists(catalog, data_structure, sorting_method,
                                                    initial_birth_year, end_birth_year, num_artists):
    start_time = time.process_time()

    requirement_info = model.getMostProlificArtists(catalog, data_structure, sorting_method,
                                                    initial_birth_year, end_birth_year, num_artists)
                                                    
    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000  
    return elapsed_time, requirement_info