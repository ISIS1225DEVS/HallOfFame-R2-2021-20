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
import model
import csv

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.newCatalog()
    return catalog
    
# Funciones para la carga de datos
def loadData(catalog):
    loadArtists(catalog)
    loadArtworks(catalog)


    
def loadArtists(catalog):
    artistfile = cf.data_dir + "Artists-utf8-large.csv"
    input_file = csv.DictReader(open(artistfile, encoding ="utf-8"))
    for artist in input_file:
        model.addArtists(catalog, artist)
        model.ids(catalog, artist)
        model.Nat(catalog, artist)
        model.AddConstituentName(catalog,artist)
        

def loadArtworks(catalog):
    awfile = cf.data_dir + "Artworks-utf8-large.csv"
    input_file = csv.DictReader(open(awfile, encoding ="utf-8"))
    for aw in input_file:
        model.addArtworks(catalog, aw)
        model.addMedium(catalog, aw)
        model.fechas(catalog,aw)
        model.addDateAcquired(catalog,aw)
        model.mediumartists(catalog, aw)
        model.NatArt(catalog, aw)
        model.addDepartment(catalog, aw)
        

#Funciones de requerimientos y ordenamientos

def requerimiento4(catalog):
    return model.requerimiento4(catalog)

def obrasantiguas(cat, medio):
    model.obrasantiguas(cat, medio)

def requerimiento1(catalog, begin1, begin2):
    return model.requerimiento1(catalog, begin1, begin2)

def requerimiento2(catalog,begin,end):
    return model.requerimiento2(catalog,begin,end)
    
def artworksClasification(catalog, artist):
    return model.requerimiento3(catalog,artist)

def topMeds(medios):
    return model.topMeds(medios)

def orden(top):
    return model.orden(top)
    
def printArtMed(catalog, id, med):
    model.printArtMed(catalog, id, med)  

def printNats(catalog, Nat):
    model.printNats(catalog, Nat)  

def requerimiento5(catalog,department):
    return model.requerimiento5(catalog,department)

def requerimiento6(catalog, begin, end):
    return model.requerimiento6(catalog, begin, end)

def top(catalog,lista, cant):
    return model.topArtist(catalog, lista, cant)