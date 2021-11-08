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

from App.model import calcularCostoTransporteObra
import config as cf
import model
import csv
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo 

def initCatalogo1():
    return model.crearCatalogo1()


def cargarDatos1(catalogo):
       
    #cargarDatosArtistas(catalogo)
    #cargarDatosObras(catalogo)
    cargarObras1(catalogo)
    cargarArtistas1(catalogo)
    agregarNacimientoYNacionalidad(catalogo)
    agregarFechaAdquisicionMedioYDepartamento(catalogo)
    
    
def cargarDatosArtistas(catalogo):
    
    archivoArtistas = cf.data_dir + 'Artists-utf8-large.csv'

    input_file=csv.DictReader(open(archivoArtistas, encoding='utf8'))
    
    for artista in input_file:
        model.agregarDatoArtista(catalogo, artista)
        
def cargarDatosObras(catalogo):
    
    archivoObras=cf.data_dir + 'Artworks-utf8-large.csv'
    input_file=csv.DictReader(open(archivoObras, encoding='utf8'))
    
    for obra in input_file:
        model.agregarDatoObra(catalogo, obra)
    
    
def cargarArtistas1(catalogo):
    
    archivoArtistas = cf.data_dir + 'Artists-utf8-large.csv'

    input_file=csv.DictReader(open(archivoArtistas, encoding='utf8'))
    
    for artista in input_file:
        model.agregarArtista1(catalogo, artista)
        model.agregarIDArtista(catalogo, artista)
  

def cargarObras1(catalogo):
    
    archivoObras=cf.data_dir + 'Artworks-utf8-large.csv'
    input_file=csv.DictReader(open(archivoObras, encoding='utf8'))
        
    for obra in input_file:
        model.agregarObra1(catalogo, obra)
        model.agregarIdObra(catalogo, obra)
           
        
def agregarNacimientoYNacionalidad(catalogo):
    
    lista_artistas = mp.valueSet(catalogo['artistas'])
    
    for artista in lt.iterator(lista_artistas):
        model.agregarNacimiento(catalogo, artista)
        model.agregarNacionalidad(catalogo, artista)
        
        
def agregarFechaAdquisicionMedioYDepartamento(catalogo):
    
    obras = mp.valueSet(catalogo['obras'])
    
    for obra in lt.iterator(obras):
        model.agregarFechaAdquisicion(catalogo, obra)
        model.agregarMedio(catalogo, obra)
        model.agregarDepartamento(catalogo, obra)
        

def rangoArtistasPorAnho(catalogo, anho_inicial, anho_final):
    return model.rangoArtistasPorAnho(catalogo, anho_inicial, anho_final)
        

        
        











def initCatalogo(tipo_lista):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalogo = model.crearCatalogo(tipo_lista)
    return catalogo

# Funciones para la carga de datos

def cargarDatos(catalogo):
    cargarArtistas(catalogo)
    cargarObras(catalogo)

def cargarArtistas(catalogo):
    archivoArtistas = cf.data_dir + 'Artists-utf8-large.csv'
    #archivoArtistas='D:\Descargas\Repositorio GitHub\Reto1-G07\Data\Artists-utf8-small.csv'
    input_file=csv.DictReader(open(archivoArtistas, encoding='utf8'))
    for artista in input_file:
        model.agregarArtista(catalogo, artista)   

def cargarObras(catalogo):
    archivoObras=cf.data_dir + 'Artworks-utf8-large.csv'
    input_file=csv.DictReader(open(archivoObras, encoding='utf8'))
    for obra in input_file:
        model.agregarObra(catalogo, obra)
        model.agregarMedio(catalogo, obra)
        model.agregarNacionalidad(catalogo, obra)

# Funciones de ordenamiento

def llamarInsertion(datos, identificador):
    resultado = model.insertion(datos, identificador)
    return resultado

def llamarShell(datos, identificador):
    resultado = model.shell(datos, identificador)
    return resultado

def llamarMerge(datos, identificador):
    resultado = model.merge(datos, identificador)
    return resultado

def llamarQuicksort(datos, identificador):
    resultado = model.quicksort(datos, identificador)
    return resultado

#def llamarOrdenarArtistasPorNacimiento(info, cmpFunction):
 #   return model.insertion(info, cmpFunction)

# Funciones de consulta sobre el catálogo

def llamarArtistas(datos, anho_inicial, anho_final, tipo_lista):
    return model.compararFechasArtistas(datos, anho_inicial, anho_final, tipo_lista)
    
def obrasAdquiridasPorCompra(datos):
    resultado = model.obrasAdquiridasPorCompra(datos)
    return resultado

def llamarConsultarId(datos, nombreArtista):
    return model.consultarId(datos, nombreArtista)

def llamarFiltrarObrasPorId(datos, idArtista, tipo_lista):
    return model.filtrarObrasPorId(datos, idArtista, tipo_lista)

#def llamarOrdenarObras(lista, identificador):
 
#   return model.shell(lista, identificador)
def llamarOrdenarObras(lista, identidficador):
    return model.shell(lista, identidficador)

def llamarListaNacionalidades(datos):
    return model.listaNacionalidades(datos)

def llamarBuscarObrasPorNacionalidad(datos, nacionalidad):
    return model.buscarObrasPorNacionalidad(datos, nacionalidad)

def llamarObtenerRangoObras(datos, anhoInicial, anhoFinal, tipo_lista):
    return model.obtenerRangoObras(datos, anhoInicial, anhoFinal, tipo_lista)

def llamarCrearExposicion(rangoObrasRequerido, areaDisponible, tipo_lista):
    return model.crearExposicion(rangoObrasRequerido, areaDisponible, tipo_lista)

def llamarAgregarArtistaPorId(datos, datosArtistas):
    return model.agregarArtistaPorId(datos, datosArtistas)
    

def llamarDarListaObrasDepartamento(datos, departamento):
    return model.darListaObrasDepartamento(datos, departamento)

def llamarCalcularCostoTransporteObra(obra):
    return calcularCostoTransporteObra(obra)

def llamarDarPrecioTransporteDepartamento(lista):
    return model.darPrecioTransporteDepartamento(lista)

def llamarDarPesoTotalDepartamento(lista_obras):
    return model.darPesoTotalDepartamento(lista_obras)

def llamarfiltrarFechasObras(datos):
    return model.filtrarFechasObras(datos)