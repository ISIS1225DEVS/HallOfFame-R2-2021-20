"""
Reto 2 - controller.py

Carlos Arturo Holguín Cárdenas
Daniel Hernández Pineda

 """

import config as cf
import model
import csv


# ==============================================
# Inicialización del catálogo de obras
# ==============================================

def initCatalog():
    """
    Llama la funcion de inicializació del catálogo del modelo
    """
    catalog = model.newCatalog()
    return catalog


# ==============================================
# Funciones para la carga de datos
# ==============================================

def loadData(catalog, file_size):
    """
    Carga los datos de los archivos
    """
    loadArtists(catalog, file_size)
    loadArtworks(catalog, file_size)


def loadArtists(catalog, file_size):
    """
    Carga los artistas del archivo
    """
    artistsfile = cf.data_dir + 'Artists-utf8-' + file_size + '.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.AddIDName(catalog, artist)
        model.AddArtistsDatesREQ1(catalog, artist)
        model.NameIdREQ3(catalog, artist)
        model.AddArtistsNationalitiesREQ4(catalog, artist)  


def loadArtworks(catalog, file_size):
    """
    Carga las obras del archivo
    """
    artworksfile = cf.data_dir + 'Artworks-utf8-' + file_size + '.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.AddArtworksREQ2(catalog,artwork)
        model.AddArtworksWidREQ3(catalog,artwork)
        model.AddTitleAndDataREQ3(catalog,artwork)
        model.AddArtworksREQ4(catalog, artwork)
        model.AddArtworksREQ5(catalog, artwork)
    model.AddDatesREQ1(catalog)
    model.AddDatesREQ2(catalog)



# ==============================================
# Funciones de consulta sobre el catalogo
# ============================================

#Requerimiento 1
def REQ1(catalog, date_initial, date_final):
    return model.REQ1(catalog, date_initial, date_final)

#Requerimiento 2
def REQ2(catalog, date_initial, date_final):
    return model.REQ2(catalog, date_initial, date_final)

#Requerimiento 3
def REQ3GetTechniquees(catalog,Name):
    return model.GetTechniquesReq3(catalog,Name)

#Requerimiento 4
def REQ4(catalog):
    return model.REQ4(catalog)

#Requerimiento 5
def REQ5(catalog, department):
    return model.REQ5(catalog, department)