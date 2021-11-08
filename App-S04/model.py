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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
import re
import operator
import math
from decimal import Decimal, Rounded
from DISClib.Algorithms.Sorting import insertionsort as ist
from DISClib.Algorithms.Sorting import mergesort as mst
from DISClib.Algorithms.Sorting import quicksort as qst
from DISClib.Algorithms.Sorting import shellsort as sst
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
    
def crearCatalogo1():
    
    catalogo = {
                'id_obras': None,
                'artistas': None,
                'obras': None,
                'nacimientos': None,
                'fechas_obras': None,
                'medios': None,
                'nacionalidades': None,
                'departamentos': None,
                'id_artistas': None,
                }
    
    catalogo['id_obras'] = mp.newMap()
    catalogo['artistas'] = mp.newMap()
    catalogo['obras'] = mp.newMap()
    catalogo['nacimientos'] = mp.newMap()
    catalogo['medios'] = mp.newMap()
    catalogo['fechas_obras'] = mp.newMap()
    catalogo['nacionalidades'] = mp.newMap()
    catalogo['departamentos'] = mp.newMap()
    catalogo['id_artistas'] = mp.newMap()
    
    return catalogo


# Funciones para agregar informacion al catalogo

def agregarIdObra(catalogo, obra):
    
    obra['ConstituentID'] = obra['ConstituentID'][1:-1]
    obra['ConstituentID'] = obra['ConstituentID'].replace(" ", "")
    
    if ',' in obra['ConstituentID']:
        lista_id = obra['ConstituentID'].split(',')
        
        for id in lista_id:
            existe = mp.contains(catalogo['id_obras'], id)
            
            if existe:
                entry = mp.get(catalogo['id_obras'], id)
                lista_obras = me.getValue(entry)
                lt.addLast(lista_obras, obra['Title'])
            else:
                lista_obras = lt.newList(datastructure='ARRAY_LIST')
                lt.addLast(lista_obras, obra['Title'])
                mp.put(catalogo['id_obras'], id, lista_obras)
                
    else:
        existe = mp.contains(catalogo['id_obras'], obra['ConstituentID'])
        
        if existe:
            entry = mp.get(catalogo['id_obras'], obra['ConstituentID'])
            lista_obras = me.getValue(entry)
            lt.addLast(lista_obras, obra['Title'])
        else:
            lista_obras = lt.newList(datastructure='ARRAY_LIST')
            lt.addLast(lista_obras, obra['Title'])
            mp.put(catalogo['id_obras'], obra['ConstituentID'], lista_obras)

def agregarIDArtista(catalogo, artista):
    
    existe = mp.contains(catalogo['id_artistas'], artista['ConstituentID'])
    
    if existe:
        return
    else:
        nuevoArtista = crearArtista1(catalogo, artista)
        mp.put(catalogo['id_artistas'], artista['ConstituentID'], nuevoArtista)
        

def agregarArtista1(catalogo, artista):
    
    existe = mp.contains(catalogo['artistas'], artista['DisplayName'])
    
    if existe:
        return
    else:
        nuevoArtista = crearArtista1(catalogo, artista)
        mp.put(catalogo['artistas'], artista['DisplayName'], nuevoArtista)
        

def agregarDatoArtista(catalogo, artista):
    artista = nuevoDatoArtista(artista['ConstituentID'],artista['DisplayName'],artista['BeginDate'],artista['EndDate'],artista['Nationality'], artista['Gender'])
    lt.addLast(catalogo['datos_artistas'], artista)
    
    
#def agregarNacionalidad(catalogo, obra):
 #   lista_id_artistas = lt.newList('ARRAY_LIST')
   # x = obra['ConstituentID']
    #characters = "[] "
    #for s in range(len(characters)):
     #   x = x.replace(characters[s],"")       
    
    #lista = x.split(',')
    #for a in lista:
     #       lt.addLast(lista_id_artistas, a)
            
    
#def nuevoDatoArtista(id, nombre, fecha_nacimiento, fecha_muerte, nacionalidad, genero):
    
    #for i in lt.iterator(lista_id_artistas):
        #nacionalidad = consultarNacionalidad(catalogo, int(i))
        #existeNacionalidad = mp.contains(catalogo['nacionalidades'], nacionalidad)
        #if existeNacionalidad:
            #entri = mp.get(catalogo['nacionalidades'], nacionalidad)
            #entry = me.getValue(entri)
        #else:
            #entry = lt.newList('ARRAY_LIST')
            #mp.put(catalogo['nacionalidades'], nacionalidad, entry)
        #lt.addLast(entry, obra)
    
        
# Funciones para creacion de datos

def nuevoDatoArtista(id, nombre, fecha_nacimiento, fecha_muerte, nacionalidad, genero):
    artista={'id':"", 'nombre':"", 'fecha_nacimiento':"", 'fecha_muerte':"", 'nacionalidad':"", 'genero':""}
    artista['id'] = id
    artista['nombre'] = nombre
    artista['fecha_nacimiento'] = fecha_nacimiento
    artista['fecha_muerte'] = fecha_muerte
    artista['nacionalidad'] = nacionalidad
    artista['genero'] = genero

    return artista
    

def agregarDatoObra(catalogo, obra):
    
    obra=nuevoDatoObra(obra['ConstituentID'], obra['ObjectID'], obra['Title'], obra['Date'], obra['Medium'], obra['Department'], obra['DateAcquired'], obra['Height (cm)'], obra['Width (cm)'], obra['Weight (kg)'], obra['CreditLine'], obra['Dimensions'], obra['Diameter (cm)'], obra['Length (cm)'], obra['Classification'])
    lt.addLast(catalogo['datos_obras'], obra)
    
    
def nuevoDatoObra(id, objectId, titulo, fecha, tecnica, departamento, fecha_adquisicion, altura, ancho, peso, linea, dimensiones, diametro, largo, clasificacion):
    
    obra={'id':"", 'objectId':"", 'titulo':"", 'fecha':"", 'tecnica':"", 'departamento':"", 'fecha_adquisicion':"", 'altura':"", 'ancho':"", 'peso':"", 'linea_adquisicion':"", 'dimensiones':"", 'diametro':"", 'largo':"", 'clasifiacion':""}
    obra['id']=id
    obra['objectId'] = objectId
    obra['titulo']=titulo
    obra['fecha']=fecha
    obra['tecnica']=tecnica
    obra['departamento']=departamento
    obra['fecha_adquisicion']=fecha_adquisicion
    obra['altura']=altura
    obra['ancho']=ancho
    obra['peso']=peso
    obra['linea_adquisicion']=linea
    obra['dimensiones'] = dimensiones
    obra['diametro']=diametro
    obra['largo']=largo
    obra['clasificacion'] = clasificacion
    
    return obra
    
    
def crearArtista1(catalogo, artista):
    
    temp = artista['BeginDate']
    lista_nacimiento_final = []
    
    if not temp.isnumeric():
        lista_nacimiento_parcial = temp.split(' ')
        
        for i in lista_nacimiento_parcial:
            if i.isnumeric():
                lista_nacimiento_final.append(i)
                
    if len(lista_nacimiento_final) == 0:
        nacimiento_final = temp
    else:
        nacimiento_final = lista_nacimiento_final[0] 
    
    nuevoArtista = {'id': artista['ConstituentID'],
                    'num_prolifico': None,
                    'nombre': artista['DisplayName'],
                    'fecha_nacimiento': nacimiento_final,
                    'fecha_muerte': artista['EndDate'],
                    'nacionalidad': artista['Nationality'],
                    'genero': artista['Gender'],
                    'obras': None,
                    }
    
    nuevoArtista['obras'] = asignarArtistasAObra(catalogo, artista)
    temp = nuevoArtista['obras']
    
    if lt.size(temp) == 0:
        nuevoArtista['num_prolifico'] = 0
    else:
        nuevoArtista['num_prolifico'] = lt.size(temp)
    
    return nuevoArtista


def asignarArtistasAObra(catalogo, artista):
    
    entry = mp.get(catalogo['id_obras'], artista['ConstituentID'])
    
    if entry == None:
        lista = lt.newList(datastructure='ARRAY_LIST')
    else:
        lista = me.getValue(entry)
                
    return lista


def agregarObra1(catalogo, obra):
    
    existe = mp.contains(catalogo['obras'], obra['Title'])
    
    if existe:
        return
    else:
        nuevaObra = crearObra1(catalogo, obra)
        mp.put(catalogo['obras'], obra['Title'], nuevaObra)
        
        
def crearObra1(catalogo, obra):
        
    nuevaObra = {'id': obra['ConstituentID'],
                 'titulo': obra['Title'],
                 'fecha': obra['Date'],
                 'medio': obra['Medium'],
                 'departamento': obra['Department'], 
                 'fecha_adquisicion': obra['DateAcquired'],
                 'linea_adquisicion': obra['CreditLine'],
                 'dimensiones': obra['Dimensions'],
                 'diametro': obra['Diameter (cm)'],
                 'altura': obra['Height (cm)'], 
                 'largo': obra['Length (cm)'],
                 'ancho': obra['Width (cm)'], 
                 'peso': obra['Weight (kg)'],
                 'clasificacion': obra['Classification'],
                 }
    
    return nuevaObra
        

def agregarNacimiento(catalogo, artista):
    
    existe = mp.contains(catalogo['nacimientos'], artista['fecha_nacimiento'])
    entry_artistas = mp.get(catalogo['artistas'], artista['nombre'])
    info_artistas = me.getValue(entry_artistas)
    
    if existe:
        entry = mp.get(catalogo['nacimientos'], artista['fecha_nacimiento'])
        lista_nacimientos = me.getValue(entry)
        lt.addLast(lista_nacimientos, info_artistas)

    else:
        lista = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista, info_artistas)
        mp.put(catalogo['nacimientos'], artista['fecha_nacimiento'], lista)
        
        
def agregarNacionalidad(catalogo, artista):
    
    existe = mp.contains(catalogo['nacionalidades'], artista['nacionalidad'])
    entry_artistas = mp.get(catalogo['artistas'], artista['nombre'])
    info_artistas = me.getValue(entry_artistas)
    
    if existe:
        entry = mp.get(catalogo['nacionalidades'], artista['nacionalidad'])
        lista_nacionalidades = me.getValue(entry)
        lt.addLast(lista_nacionalidades, info_artistas)

    else:
        lista = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista, info_artistas)
        mp.put(catalogo['nacionalidades'], artista['nacionalidad'], lista)
        

def agregarFechaAdquisicion(catalogo, obra):
    
    existe = mp.contains(catalogo['fechas_obras'], obra['fecha_adquisicion'])
    entry_obras = mp.get(catalogo['obras'], obra['titulo'])
    info_obras = me.getValue(entry_obras)
    
    if existe:
        entry = mp.get(catalogo['fechas_obras'], obra['fecha_adquisicion'])
        lista_fechas = me.getValue(entry)
        lt.addLast(lista_fechas, info_obras)

    else:
        lista = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista, info_obras)
        mp.put(catalogo['fechas_obras'], obra['fecha_adquisicion'], lista)
        

def agregarMedio(catalogo, obra):
    
    existe = mp.contains(catalogo['medios'], obra['medio'])
    entry_obras = mp.get(catalogo['obras'], obra['titulo'])
    info_obras = me.getValue(entry_obras)
    
    if existe:
        entry = mp.get(catalogo['medios'], obra['medio'])
        lista_medios = me.getValue(entry)
        lt.addLast(lista_medios, info_obras)

    else:
        lista = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista, info_obras)
        mp.put(catalogo['medios'], obra['medio'], lista)
        
        
def agregarDepartamento(catalogo, obra):
    
    existe = mp.contains(catalogo['departamentos'], obra['departamento'])
    entry_obras = mp.get(catalogo['obras'], obra['titulo'])
    info_obras = me.getValue(entry_obras)
    
    if existe:
        entry = mp.get(catalogo['departamentos'], obra['departamento'])
        lista_departamentos = me.getValue(entry)
        lt.addLast(lista_departamentos, info_obras)

    else:
        lista = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista, info_obras)
        mp.put(catalogo['departamentos'], obra['departamento'], lista)
             
             
             
        
# Funciones para creacion de datos
    
def rangoArtistasPorAnho(catalogo, anho_inicial, anho_final):
    
    lista_info = lt.newList(datastructure='ARRAY_LIST')
    
    for anho in range(anho_inicial, anho_final+1):
        
        llave_anho = str(anho)
        entry = mp.get(catalogo['nacimientos'], llave_anho)
        
        if entry == None:
            valores_anho = lt.newList(datastructure='ARRAY_LIST')
            
        else:
            valores_anho = me.getValue(entry)
        lt.addLast(lista_info, valores_anho)
        
    return lista_info




# Funciones de consulta

def darListaObrasDepartamento(datos, departamento):

    lista_obras = lt.newList('ARRAY_LIST')
    info = datos['obras']

    for i in lt.iterator(info):
        if i['departamento'] == departamento:
            lt.addLast(lista_obras, i)

    return lista_obras

def darPrecioTransporteDepartamento(lista_obras):
    costo_total=0
    for i in lt.iterator(lista_obras):
        costo_total = costo_total + calcularCostoTransporteObra(i)
    
    return costo_total

def darPesoTotalDepartamento(lista_obras):
    pesoTotal = 0
    for i in lt.iterator(lista_obras):
        if not i['peso']:
            pass
        else:
            pesoTotal = Decimal(i['peso']) + pesoTotal

    return pesoTotal  


def compararFechasArtistas(datos, anho_inicial, anho_final, tipo_lista):
    
    listaInfo = lt.newList(tipo_lista)
    
    for i in lt.iterator(datos['artistas']):
        
        if (int(i['fecha_nacimiento']) >= anho_inicial and int(i['fecha_nacimiento']) <= anho_final):
            lt.addLast(listaInfo, i)
    
    return listaInfo
            
        
def obrasAdquiridasPorCompra(datos):
    
    contador=0

    for dato in lt.iterator(datos):
        frase=dato['linea_adquisicion']
        if re.search('purchase',frase.lower()):
            contador=contador + 1

    return contador


def consultarId(datos, nombreArtista):
    
    info = datos['artistas']
    idArtista = '0'
    
    for i in lt.iterator(info):
        i['nombre']
        if i['nombre'] == nombreArtista:
            idArtista = i['id']
            
    return idArtista 
        
         

def buscarObrasPorNacionalidad(datos, nacionalidad):
    info_obras = datos['obras']
    keys_obras = mp.keySet(info_obras)
    lista_obras = lt.newList('ARRAY_LIST')    

    for j in lt.iterator(keys_obras):

        entry = mp.get(info_obras, j)
        i = me.getValue(entry)

        x=i['id']
    
        characters = "[] "

        for s in range(len(characters)):
            x = x.replace(characters[s],"")

        lista = x.split(',')
        for j in lista:
            if consultarNacionalidad(datos, int(j)) == nacionalidad:
                lt.addLast(lista_obras, i)

    return lista_obras


    

def consultarNacionalidad(datos, id):
    entry = mp.get(datos['id_artistas'], str(id))
    artista = me.getValue(entry)
    nacionalidad = artista['nacionalidad']
        
    return nacionalidad 

def listaNacionalidades(datos):

    info_obras = datos['obras']
    #info_obras = datos['obras']['elements']

    lista_id_artistas = lt.newList('ARRAY_LIST')
    dic_nacionalidades = {}

    for i in lt.iterator(info_obras):

        x = i['id']
        characters = "[] "

        for s in range(len(characters)):
            x = x.replace(characters[s],"")

        lista = x.split(',')
        #print(lista)
        for a in lista:
            if lt.isPresent(lista_id_artistas, a) == -1 or a == ' ' or a == '':
               pass
            else:
                lt.addLast(lista_id_artistas, a)
    
    for i in lt.iterator(lista_id_artistas):
        
        nacionalidad = consultarNacionalidad(datos, int(i))

        if nacionalidad in dic_nacionalidades:
            dic_nacionalidades[nacionalidad]=dic_nacionalidades[nacionalidad]+1
        else:
            dic_nacionalidades[nacionalidad]=1

    del dic_nacionalidades['']

    nacionalidades_sort = sorted(dic_nacionalidades.items(), key=operator.itemgetter(1), reverse=True)
    
    return nacionalidades_sort


def filtrarObrasPorId(datos, idArtista, tipo_lista):
    
    obrasDelArtista = lt.newList(tipo_lista)
    lista_temp_1 = []
    lista_temp_2 = lt.newList(tipo_lista)
    
    for i in lt.iterator(datos['obras']):
        
        tamanho_id = len(i['id'])
        if (str(i['id'][1:(tamanho_id-1)]) == idArtista):
            lt.addLast(obrasDelArtista, i)
            lista_temp_1.append(i['tecnica'])

            if (lt.isPresent(lista_temp_2, i['tecnica']) == 0):
                lt.addLast(lista_temp_2, i['tecnica'])
    
    return obrasDelArtista, lista_temp_1, lista_temp_2


def filtrarFechasObras1(datos):
    
    for i in lt.iterator(datos):
        pass

def filtrarFechasObras(datos):
    for i in lt.iterator(datos):
        
        fecha = i['fecha']
        
        if not(fecha.isnumeric()):
            if fecha.count('(') != 0: 
                if fecha.index("(") == 0 and fecha.index(")") == len(fecha)-1:
                    fecha = fecha[1:-1] 
                elif fecha.index("(") == 0: 
                    fecha = fecha[1:] 
            if fecha.count('.') != 0:
                fecha = fecha.replace('.', '')
            if fecha == 'Unknown':
                i['fecha'] = 0
            elif fecha == 'n.d.':
                i['fecha'] = 0
            elif fecha.count(" ") == 0:  
                if '–' in fecha:
                    fechaLista = fecha.split("–") 
                elif '-' in fecha:
                    fechaLista = fecha.split("-") 
                fechaLista = fecha.split() 
                fechaAnho = encontrarAnho(fechaLista)
                i['fecha'] = fechaAnho[0]
            else:
                fechaLista = fecha.split() 
                fechaAnho = encontrarAnho(fechaLista)
                i['fecha'] = fechaAnho[0] 
        
    return datos
          
    
def obtenerRangoObras(datos, anhoInicial, anhoFinal, tipo_lista):

    rangoObras = lt.newList(tipo_lista)
    
    for i in lt.iterator(datos['obras']):
              
        if i['fecha'] == '':
            i['fecha'] = 0
                     
        if ((int(i['fecha']) <= anhoFinal) and (int(i['fecha']) >= anhoInicial)):
            alturaObra = i['altura']
            anchoObra = i['ancho']
            
            if alturaObra == "":
                alturaObra = 0
            if anchoObra == "":
                anchoObra = 0
                
            i['areaObra'] = (((float(alturaObra))*(float(anchoObra))))*0.0001
            lt.addLast(rangoObras, i)    
            
    return rangoObras


def agregarArtistaPorId(datos, datosArtistas):
    
    for i in lt.iterator(datos):   
        if len(i['id']) > 8:
            i['artista'] = 'Varios'
            
        else:
            for j in lt.iterator(datosArtistas): 
                if (j['nombre'] != ""):
                    if i['id'][1:-1] == j['id']:
                        i['artista'] = j['nombre']
                else:
                    i['artista'] = 'Unknown'
                
    return datos
            
    
# Funciones utilizadas para comparar elementos dentro de una lista

def encontrarAnho(lista):
    
    listaNueva = []
    for i in lista:
        if i.isnumeric() and len(i)>3:
            listaNueva.append(i)
            
    return listaNueva
            

def cmpArtworkByDateAcquired(artwork1, artwork2):
    
    if artwork1['fecha_adquisicion'] < artwork2['fecha_adquisicion']:
        return True
    else:
        return False
    
def cmpArtistaPorNacimiento(artista1, artista2):
    
    if int(artista1['fecha_nacimiento']) < int(artista2['fecha_nacimiento']):
        return True
    else:
        return False
    
def cmpNumProlifico(artista1, artista2):
    
    if int(artista1['num_prolifico']) == int(artista2['num_prolifico']):
        return cmpNumMedios(artista1, artista2)
    
    elif int(artista1['num_prolifico']) > int(artista2['num_prolifico']):
        return True
    else:
        return False
    
def cmpNumMedios(artista1, artista2):
    
    if int(artista1['num_prolifico']) > int(artista2['num_prolifico']):
        return True
    else:
        return False
    
    
def cmpObrasPorFecha(obra1, obra2):
    
    if obra1['fecha'] == '':
        obra1['fecha'] = 0
    if obra2['fecha'] == '':
        obra2['fecha'] = 0
        
    if (int(obra1['fecha']) < int(obra2['fecha'])):
        return True
    else:
        return False

def cmpObrasPorCostoTransporte(obra1, obra2):
    
    if (int(obra1['costo_transporte']) < int(obra2['costo_transporte'])):
        return True
    else:
        return False

# Funciones de ordenamiento

def insertion(datos, identificador): 
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = ist.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = ist.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada = ist.sort(datos, cmpArtworkByDateAcquired)
    elif identificador == 4:
        lista_ordenada = ist.sort(datos, cmpObrasPorCostoTransporte)
    elif identificador == 5:
        lista_ordenada = ist.sort(datos, cmpNumProlifico)
        
    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def shell(datos, identificador):   
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = sst.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = sst.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada = sst.sort(datos, cmpArtworkByDateAcquired)
    elif identificador == 4:
        lista_ordenada = sst.sort(datos, cmpObrasPorCostoTransporte)
    elif identificador == 5:
        lista_ordenada = sst.sort(datos, cmpNumProlifico)
        
    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def merge(datos, identificador):
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = mst.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = mst.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada = mst.sort(datos, cmpArtworkByDateAcquired)
    elif identificador == 4:
        lista_ordenada = mst.sort(datos, cmpObrasPorCostoTransporte)
    elif identificador == 5:
        lista_ordenada = mst.sort(datos, cmpNumProlifico)

    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def quicksort(datos, identificador):
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = qst.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = qst.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada = qst.sort(datos, cmpArtworkByDateAcquired)
    elif identificador == 4:
        lista_ordenada = qst.sort(datos, cmpObrasPorCostoTransporte)
    elif identificador == 5:
        lista_ordenada = qst.sort(datos, cmpNumProlifico)

    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

#Otras
  
def crearExposicion(rangoObrasRequerido, areaDisponible, tipo_lista):
    
    areaUsada = 0
    i = 0
    info = rangoObrasRequerido['elements']
    nuevaExposicion = lt.newList(tipo_lista)
    
    for i in lt.iterator(rangoObrasRequerido):
        
        if areaUsada <= areaDisponible:
            areaUsada += i['areaObra']
            lt.addLast(nuevaExposicion, i)
        else:
            break
        
    return nuevaExposicion, areaUsada
        

def calcularCostoTransporteObra(obra):

    costo_peso = 0
    costo_area = 0
    costo_volumen = 0

    costo_mayor=0

    costo = 72

    if not obra['altura']:
        altura = 0
    else:
        altura = float(Decimal(obra['altura'])/100)
    if not obra['largo']:
        largo = 0
    else:
        largo = float(Decimal(obra['largo'])/100)
    if not obra['ancho']:
        ancho = 0
    else:
        ancho = float(Decimal(obra['ancho'])/100)
    if not obra['peso']:
        peso = 0
    else:
        peso = float((Decimal(obra['peso'])))
    if not obra['diametro']:
        diametro = 0
    else:
        diametro = float(Decimal(obra['diametro'])/100)
    
    #Calculo del peso
    if peso != 0:
        costo_peso=peso*costo

    #Calculo del area
    if diametro != 0:
        costo_area=(math.pi*((diametro)/2.0)*(diametro/2.0))*float(costo)
    elif largo != 0 and ancho != 0:
        costo_area=(largo*ancho)*costo
    elif altura != 0 and ancho != 0:
        costo_area=(altura*ancho)*costo

    #Calculo del volumen
    if diametro != 0 and altura != 0:
        costo_volumen=(math.pi*((diametro)/2.0)*(diametro/2.0)*float(altura))*float(costo)
    elif largo != 0 and ancho != 0 and altura != 0:
        costo_volumen=(largo*ancho*altura)*costo

    if costo_area > costo_peso and costo_area > costo_volumen:
        costo_mayor=costo_area
    elif costo_peso > costo_area and costo_peso > costo_volumen:
        costo_mayor=costo_peso
    else:
        costo_mayor=costo_volumen

    if costo_mayor == 0:
        obra['costo_transporte']=48
        return 48
    else:
        obra['costo_transporte']=costo_mayor
        return costo_mayor


def compararFechasNacimiento(anho_nacimiento, entry):
    
    anentry = me.getKey(entry)
    if (int(anho_nacimiento) == int(anentry)):
        return 0
    elif (int(anho_nacimiento) > int(anentry)):
        return 1
    else:
        return -1
    