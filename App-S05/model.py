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


from DISClib.DataStructures.arraylist import newList
from DISClib.DataStructures.chaininghashtable import keySet
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
from datetime import date, datetime
import time

# Construccion de modelos
def newCatalog():
    catalog = {'artists': None,
               'artworks': None,
               }
    catalog["artists"] = mp.newMap(numelements = 30449, maptype="PROBING", loadfactor= 0.5 ) #ID-InfoArtists ####
    catalog["artworks"] = mp.newMap(numelements = 276302, maptype="PROBING", loadfactor= 0.5 ) #ID-InfoArtworks ####
    catalog["Medios"] = mp.newMap(numelements = 769, maptype="PROBING", loadfactor= 0.5 ) #Medio-TitleObras
    catalog["Obras"] = mp.newMap(numelements = 276302, maptype="PROBING", loadfactor= 0.5 ) #TitleObra-Fecha ####
    catalog["NacimientoArtistas"] = mp.newMap(numelements=1667, maptype="PROBING", loadfactor= 0.5) #BeginDate-InfoArtistas
    catalog["DateAcquired"] = mp.newMap(numelements= 389, maptype="PROBING", loadfactor= 0.5) #DateAquired-InfoArtistas ####
    catalog["Medartist"]= mp.newMap(numelements=30449, maptype="PROBING", loadfactor= 0.5) #ID-Medios ####
    catalog["ids"] = mp.newMap(numelements=30449, maptype="PROBING", loadfactor= 0.5) #Name-ID ####
    catalog["Nat"] = mp.newMap(numelements=30449, maptype="PROBING", loadfactor= 0.5) #ID-Nat ####
    catalog["ID"] = lt.newList(datastructure="ARRAY_LIST") #Todos los ids de artworks ####
    catalog["ArtNat"] = mp.newMap(numelements=401, maptype="PROBING", loadfactor= 0.5) #Nat-IDs ####
    catalog["Department"] = mp.newMap(numelements=23, maptype= "PROBING", loadfactor= 0.5) #Catalogo con los medios de las artworks Dept-Obras
    catalog["ConstituentName"] = mp.newMap(numelements=30449, maptype="PROBING", loadfactor= 0.5) #Llave: Constituent ID - Valor: Nombre del artista ####
    return catalog 

# Funciones para agregar informacion a los catalogos
def addArtists(catalog,artist):
    mp.put(catalog["artists"], int(artist["ConstituentID"]), artist)
    addBeginDate(catalog,artist)
    
def fechas(catalog, artwork):
    mp.put(catalog["Obras"], artwork["Title"], artwork["Date"])

def addArtworks(catalog, artwork):   
    listaartistas = artwork["ConstituentID"].strip("[]")  
    listaartistas = listaartistas.replace(" ","")
    listaartistas = listaartistas.split(",")   
    for artista in listaartistas:     
        presente = mp.contains(catalog["artworks"], int(artista))
        if presente:
            l = mp.get(catalog["artworks"],int(artista))["value"]
            lt.addLast(l, artwork)
            mp.put(catalog["artworks"],int(artista),l)
        else:
            l = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(l, artwork)
            mp.put(catalog["artworks"], int(artista),l)    
  
def addMedium(catalog, artwork):  
    presente = mp.contains(catalog["Medios"], artwork["Medium"])
    if not presente:
        if artwork["Medium"] != "" and artwork["Medium"] != None:
            lista = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lista, artwork["Title"])
            mp.put(catalog["Medios"], artwork["Medium"], lista)
        else:
            None
    else:
        lista = mp.get(catalog["Medios"], artwork["Medium"])["value"]
        lt.addLast(lista, artwork["Title"])
        mp.put(catalog["Medios"], artwork["Medium"], lista)

def addDepartment(catalog, artwork):  
    presente = mp.contains(catalog["Department"], artwork["Department"])
    if not presente:
        if artwork["Department"] != "" and artwork["Department"] != None:
            lista = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lista, artwork)
            mp.put(catalog["Department"], artwork["Department"], lista)
    else:
        lista = mp.get(catalog["Department"], artwork["Department"])["value"]
        lt.addLast(lista, artwork)
        mp.put(catalog["Department"], artwork["Department"], lista)


def addBeginDate(catalog,artist):
    presente = mp.contains(catalog["NacimientoArtistas"], int(artist["BeginDate"]))
    if not presente:
        lista = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lista,artist)
        mp.put(catalog["NacimientoArtistas"], int(artist["BeginDate"]),lista)
    else: 
        lista = mp.get(catalog["NacimientoArtistas"], int(artist["BeginDate"]))["value"]
        lt.addLast(lista,artist)
        mp.put(catalog["NacimientoArtistas"],int(artist["BeginDate"]),lista)

def AddConstituentName (catalog, artist):
    mp.put(catalog["ConstituentName"],artist["ConstituentID"], artist["DisplayName"])

def addDateAcquired(catalog, artwork):  
    if artwork["DateAcquired"] == "":
        artwork["DateAcquired"] = "0000"
    presente = mp.contains(catalog["DateAcquired"], artwork["DateAcquired"][0:4])
    if not presente:
            lista = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lista, artwork)
            mp.put(catalog["DateAcquired"], artwork["DateAcquired"][0:4], lista)
    else:
            lista = mp.get(catalog["DateAcquired"], artwork["DateAcquired"][0:4])["value"]
            lt.addLast(lista, artwork)
            mp.put(catalog["DateAcquired"], artwork["DateAcquired"][0:4],lista)

def ids(catalog, artist):
    mp.put(catalog["ids"], artist["DisplayName"], int(artist["ConstituentID"]))

def mediumartists(catalog, artworks):
    ids = artworks["ConstituentID"].strip("[]")
    ids = ids.split(",")
    for i in ids:
        i = i.strip()
        presente = mp.contains(catalog["Medartist"], int(i))
        if not presente:
            lista = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lista, artworks["Medium"])
            mp.put(catalog["Medartist"], int(i),lista)
        else:
            lista = mp.get(catalog["Medartist"], int(i))["value"]
            lt.addLast(lista,artworks["Medium"])
            mp.put(catalog["Medartist"], int(i), lista)

def Nat(catalog, artist):
    n = artist["Nationality"]
    if n == "" or n == None:
        n = "Nationality unknown"
        mp.put(catalog["Nat"], int(artist["ConstituentID"]), n)
    else:
        mp.put(catalog["Nat"], int(artist["ConstituentID"]), n)

def NatArt(catalog, artworks):
    lista = catalog["ID"]
    ids = artworks["ConstituentID"].strip("[]")
    ids = ids.split(",")   
    for i in ids:
        id = i.strip()
        lt.addLast(lista, int(i))

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpfunctionrequerimiento1(date1,date2):
    date1 = int(date1["BeginDate"])
    date2 = int(date2["BeginDate"])
    return date1 < date2

def cmpfunctionrequerimiento2(date1,date2):
    date1 = datetime.strptime(date1["DateAcquired"], "%Y-%m-%d")
    date2 = datetime.strptime(date2["DateAcquired"], "%Y-%m-%d")
    return date1 < date2

def cmpfunctionrequerimiento3(med1,med2):
    return med1 > med2

def cmpfun6(val1,val2):
    return val1 > val2

def cmpfun(date1,date2):
    if date1 == "" or date1 == None:
        date1 = 0
    if date2 == "" or date2 == None:
        date2 = 0
        
def cmpfunctionmascaros(element1, element2):
    return element1["Costo"] > element2["Costo"]

def cmpfunctionantiguedad(element1,element2):
    if element1["Date"] == "" or element1["Date"] == None:
        element1["Date"]= "9999"
    if element2["Date"] == "" or element2["Date"] == None:
        element2["Date"] = "9999" 
    return element1["Date"] < element2["Date"]

#Funciones de los requerimientos

def obrasantiguas(catalog, medio):
    medios = catalog["Medios"]
    m = mp.get(medios, medio)
    obras = m["value"]["elements"]
    llaves = lt.newList(datastructure="ARRAY_LIST")
    aorden = lt.newList(datastructure="ARRAY_LIST")

    for i in obras:     
        cat = catalog["Obras"]
        pareja = mp.get(cat, i)        
        fecha = pareja["value"]
        lt.addLast(llaves,i)
        lt.addLast(llaves,fecha)
        lt.addLast(aorden,fecha)

    ordenada = ms.sort(aorden, cmpfun)
    
    l = lt.newList(datastructure="ARRAY_LIST")
    for f in lt.iterator(ordenada):
        pos = lt.isPresent(llaves,f)
        pos2 = pos-1
        obras = lt.getElement(llaves, pos2)
        fecha = lt.getElement(llaves, pos)
        lt.addLast(l,obras)      
        lt.addLast(l,fecha)    
        lt.deleteElement(llaves,pos2)        
        lt.deleteElement(llaves,pos2)
        
    print(l)

    return int(date1) < int(date2)

def requerimiento1(catalog, begin1, begin2):
    listaartistas= lt.newList(datastructure="ARRAY_LIST")
    for año in range(begin1,(begin2+1)):
        listaartistasmp=mp.get(catalog["NacimientoArtistas"], año)["value"]
        for agregar in lt.iterator(listaartistasmp):
            lt.addLast(listaartistas,agregar)
    numerototaldeartistas = lt.size(listaartistas)
    listaartistas = ms.sort(listaartistas,cmpfunctionrequerimiento1)
    sublista1 = lt.subList(listaartistas,1,3)
    sublista2 = lt.subList(listaartistas,(numerototaldeartistas-2),3)
    listarespuesta3y3 = lt.newList(datastructure="ARRAY_LIST")
    for artista in lt.iterator(sublista1):
        lt.addLast(listarespuesta3y3,artista)
    for artista in lt.iterator(sublista2):
        lt.addLast(listarespuesta3y3,artista)
    return (numerototaldeartistas,listarespuesta3y3)

def requerimiento2(catalog,begin,end):
    beginyear = int(begin[0:4])
    endyear= int(end[0:4])
    begin = datetime.strptime(begin,"%Y-%m-%d")
    end = datetime.strptime(end,"%Y-%m-%d")
    listaobras = lt.newList(datastructure="ARRAY_LIST")
    purchase = 0
    for year in range(beginyear,endyear+1):
        year = str(year)
        presente = mp.contains(catalog["DateAcquired"],year)
        if presente:
            year= mp.get(catalog["DateAcquired"], year)["value"]
            for obra in lt.iterator(year):
                if datetime.strptime(obra["DateAcquired"], "%Y-%m-%d") >= begin and datetime.strptime(obra["DateAcquired"], "%Y-%m-%d") <= end:
                    lt.addLast(listaobras,obra)
                    acomparar = obra["CreditLine"].lower()
                    acomparar = acomparar.find("purchase")
                    if acomparar != -1:
                        purchase += 1
    totalobras = lt.size(listaobras)
    listaobras = ms.sort(listaobras,cmpfunctionrequerimiento2)
    sublista1 = lt.subList(listaobras,1,3)
    sublista2 = lt.subList(listaobras,(totalobras-2),3)
    listarespuesta3y3 = lt.newList(datastructure="ARRAY_LIST")
    for artista in lt.iterator(sublista1):
        lt.addLast(listarespuesta3y3,artista)
    for artista in lt.iterator(sublista2):
        lt.addLast(listarespuesta3y3,artista)
    return (totalobras,purchase,listarespuesta3y3)



def requerimiento3(catalog,artist):
    
    id = mp.get(catalog["ids"], artist)["value"]   
    meds = mp.get(catalog["Medartist"], id)["value"]
    return(id,meds)
   
def topMeds(medios):
    map = mp.newMap(numelements=50, maptype="PROBING", loadfactor= 0.5)
    for i in lt.iterator(medios):
        presente = mp.contains(map, i)
        if not presente:
            count = 1
            mp.put(map, i,count)
        else:
            count = mp.get(map, i)["value"]
            count += 1
            mp.put(map, i,count)
    return map

def orden(map):
    llaves = mp.keySet(map)
    valores = mp.valueSet(map)
    lista = lt.newList(datastructure="ARRAY_LIST")
    size = mp.size(llaves)
    sub = lt.subList(valores, 0, size)
    orden = ms.sort(sub,cmpfunctionrequerimiento3)
    for i in lt.iterator(orden):
        
        pos = lt.isPresent(valores, i)
        key = lt.getElement(llaves,pos)
        lt.addLast(lista, key)
        lt.addLast(lista, i)

        lt.deleteElement(valores, pos)
        lt.deleteElement(llaves, pos)
    return (size, lista) 

def printArtMed(catalog, id, med):
    obras = mp.get(catalog["artworks"],id)["value"]
    print(" ")
    print("+"+("-"*217)+"+")
    print("|" + "Title".center(105)+" | "+ "Date".center(13)+" | "+"Medium".center(15)+" | "+"Dimensions".center(74)+" | ")
    print("+"+("-"*217)+"+")
    for i in lt.iterator(obras):
        if i["Medium"] == med:
           
            print("|"+i["Title"].center(105)+" | "+ i["Date"].center(13)+" | "+i["Medium"].center(15)+" | "+i["Dimensions"].center(74)+" | ")
            print("+"+("-"*217)+"+")

def printNats(catalog, Nat):
    ids = mp.get(catalog["ArtNat"],Nat)["value"]
    
    for i in range(0,2):
        obras = mp.get(catalog["artworks"],ids["elements"][i])["value"]
        for i in lt.iterator(obras):
            
            print("|"+i["Title"].center(60)+" | "+ i["Date"].center(13)+" | "+i["Medium"].center(15)+" | ")
            print("+"+("-"*217)+"+")
            
def requerimiento4(catalog):
    lista = catalog["ID"]
    nat = catalog["Nat"]
    for i in lt.iterator(lista):
        n = mp.get(nat, i)["value"]
        presente = mp.contains(catalog["ArtNat"], n)
        if not presente:
            lista = lt.newList(datastructure="ARRAY_LIST")          
            lt.addLast(lista, i)
            mp.put(catalog["ArtNat"], n,lista)
        else:
            lista = mp.get(catalog["ArtNat"], n)["value"]
            lt.addLast(lista,i)
            mp.put(catalog["ArtNat"], n, lista)    
    valores = mp.valueSet(catalog["ArtNat"])
    sizes = lt.newList("ARRAY_LIST")

    for i in lt.iterator(valores):
        size = i["size"]       
        lt.addLast(sizes,size)
    
    orden = ms.sort(sizes, cmpfunctionrequerimiento3)
    llaves = mp.keySet(catalog["ArtNat"])
    s = lt.size(orden)  
    
    ret = lt.newList(datastructure="ARRAY_LIST")
    num = 0  
    while num < s:
        for i in lt.iterator(llaves):
            
            g = orden["elements"][num]                     
            f = mp.get(catalog["ArtNat"],i)["value"]            
            f = lt.size(f)
            k = mp.get(catalog["ArtNat"],i)["key"]
            
            if f == g:               
                lt.addLast(ret, k)
                lt.addLast(ret, f)
        num += 1                      
    return ret

def requerimiento5(catalog, department):
    departamentolista = mp.get(catalog["Department"], department)["value"]
    #El tamañodepartamento es para sacarlo por respuesta, se da con el size de la lista creada que contiene los departamentos.
    tamañodepartamento = lt.size(departamentolista)
    #Se cre la variable que va a contener el costo.
    costototal = float(0)
    #Se hace un recorrido en la lista departamentolista que tiene todas las obras pertenecientes a un departamento.
    for obra in lt.iterator(departamentolista):
        if obra["Circumference (cm)"] == None or obra["Circumference (cm)"] == "":
            obra["Circumference (cm)"] = 0
        if obra["Depth (cm)"] == None or obra["Depth (cm)"] == "":
            obra["Depth (cm)"] = 0
        if obra["Diameter (cm)"] == None or obra["Diameter (cm)"] == "":
            obra["Diameter (cm)"] = 0
        if obra["Height (cm)"] == None or obra["Height (cm)"] == "":
            obra["Height (cm)"] = 0
        if obra["Length (cm)"] == None or obra["Length (cm)"] == "":
            obra["Length (cm)"] = 0
        if obra["Weight (kg)"] == None or obra["Weight (kg)"] == "":
            obra["Weight (kg)"] = 0
        if obra["Width (cm)"] == None or obra["Width (cm)"] == "":
            obra["Width (cm)"] = 0
        #Se crean las variables par acada valor, el costo por defecto y el costo mayor que es el que retornará, aparte se crea el costo multiplicar que es el valor dado en el requerimiento.
        #Es de aclarar que como se piden los costos por metro, y todos los datos entran en cm, se hace el factor de conversión de cm a metros en cada operación.
        costokilo = float(0)
        costoarea = float(0)
        costovolumen = float(0)
        costodefecto = 48.00
        costomayor = float(0)
        costomultiplicar = 72.00
        # Costo por kilo. Primero se calcula el costo por kilo.
        if obra["Weight (kg)"] != 0:
            costokilo = costomultiplicar * float(obra["Weight (kg)"])
        #Circulo o esféra. Si tiene diametro, debe ser un circulo o esféra, para eso son formulas diferentes.
        if obra["Diameter (cm)"] != 0:
            #área. Si no tiene alto es decir que no tiene grosor, así que es plano y se saca área.
            if obra["Height (cm)"] == 0: 
                radio = ((float(obra["Diameter (cm)"]) * (1/100))/2)
                aream = (radio*radio)*3.1416
                costoarea = costomultiplicar * aream
            #volumen. Si tiene alto es decir que tiene volúmen, se saca el volúmen.
            else: 
                radio = ((float(obra["Diameter (cm)"]) * (1/100))/2)
                volumen = (radio*radio)*float(obra["Height (cm)"])*3.1416
                costovolumen = volumen * costomultiplicar
        #Cuadro o bloque. Si no tiene diametro se entiende que es un cubo o cuadrado.

        if obra["Height (cm)"] != 0  or obra["Length (cm)"] != 0:
            #Con length
            if obra["Length (cm)"] != 0:
                largo = float(obra["Length (cm)"]) * (1/100)
                if obra["Width (cm)"] != 0 :
                    ancho = float(obra["Width (cm)"]) * (1/100)
                    area= largo*ancho
                    if obra["Depth (cm)"] != 0:
                        profundidad = float(obra["Depth (cm)"]) * (1/100)
                        volumen = area*profundidad
                        costovolumen = volumen * costomultiplicar
                    if costovolumen == 0:
                        costoarea = area*costomultiplicar
            #Con height
            if obra["Height (cm)"] != 0:
                largo = float(obra["Height (cm)"]) * (1/100)
                if obra["Width (cm)"] != 0 :
                    ancho = float(obra["Width (cm)"]) * (1/100)
                    area= largo*ancho
                    if obra["Depth (cm)"] != 0:
                        profundidad = float(obra["Depth (cm)"]) * (1/100)
                        volumen = area*profundidad
                        costovolumen = volumen * costomultiplicar
                    if costovolumen == 0:
                        costoarea = area*costomultiplicar
        #Se evalua el costo mayor de los 3 posibles.
        costomayor = max(costovolumen,costoarea,costokilo)
        #Costo mayor cuando no hay datos suficientes.
        if costoarea == 0 and costovolumen == 0 and costokilo ==0:
            costomayor = costodefecto
        #Se agrega una nueva información a la obra, su costo. 
        obra["Costo"] = costomayor
        #Se suma al costo total el costo de la obra.
        costototal += costomayor
    #Se hace un ordenamiento con merge sort para obtener los mas caros, y mas antiguos.
    mascaros = ms.sort(departamentolista, cmpfunctionmascaros)
    mascaros = lt.subList(mascaros,1,5)
    masviejos = ms.sort(departamentolista, cmpfunctionantiguedad)
    masviejos = lt.subList(masviejos,1,5)
    respuesta = (tamañodepartamento,costototal,mascaros,masviejos)
    return respuesta

def requerimiento6(catalog, begin, end):
    listaartistas = lt.newList(datastructure="ARRAY_LIST")
    for año in range(begin,(end+1)):
        listaartistasmp = mp.get(catalog["NacimientoArtistas"], año)["value"]
        for agregar in lt.iterator(listaartistasmp):
            lt.addLast(listaartistas,agregar)
    
    listaartistas = ms.sort(listaartistas,cmpfunctionrequerimiento1)
    obras = catalog["artworks"]
   
    obrascount = lt.newList(datastructure="ARRAY_LIST")
    ids = lt.newList(datastructure="ARRAY_LIST")
    for i in lt.iterator(listaartistas):    
        id = i["ConstituentID"]
        
        l = mp.get(obras, int(id))
       
        if l == None:
            None
        else:
            s = lt.size(l["value"])
            lt.addLast(ids, int(id))
            lt.addLast(obrascount,s)

    size = lt.size(obrascount)
    sub = lt.subList(obrascount,0,size)
    sub = sub.copy()
    
    orden = ms.sort(sub, cmpfunction=cmpfun6)
    lista = lt.newList(datastructure="ARRAY_LIST")
    n = 0
   
    while n < size:      
        pos = lt.isPresent(obrascount, orden["elements"][n])
        key = lt.getElement(ids,pos)      
        
        lt.addLast(lista, key)
        lt.addLast(lista, orden["elements"][n])
        lt.deleteElement(obrascount, pos)
        lt.deleteElement(ids, pos)
        n +=1
    return lista

def topArtist(catalog, lista, cant):
    info = catalog["artists"]
    info2 = catalog["artworks"]
    meds = catalog["Medartist"]
    print("+"+("-"*80)+"+")
    for i in range(0,(cant*2),2):       
        artist = lista["elements"][i]            
        list = mp.get(info, int(artist))["value"]       
        print("|"+list["ConstituentID"].center(10)+" | "+ list["DisplayName"].center(30)+" | "+list["BeginDate"].center(15)+" | "+list["Gender"].center(15)+" | ")
        print("+"+("-"*80)+"+")

    list = mp.get(info2, lista["elements"][0])["value"]       
    obras = lt.size(mp.get(meds,lista["elements"][0])["value"])

    print("El artista "+ str(mp.get(info, int(lista["elements"][0]))["value"]["DisplayName"])+" tiene un total de "+ str(obras)+" obras en el museo.") 
    artist = lista["elements"][0]   
    list = mp.get(info2, int(artist))["value"]
    print("+"+("-"*147)+"+")
    for i in range(0,5):
   
        print("|"+list["elements"][i]["Title"].center(62)+" | "+ list["elements"][i]["Medium"].center(30)+" | "+list["elements"][i]["Date"].center(15)+" | "+list["elements"][i]["DateAcquired"].center(15)+ "|" + list["elements"][i]["Department"].center(15)+"| ")
        print("+"+("-"*147)+"+")


