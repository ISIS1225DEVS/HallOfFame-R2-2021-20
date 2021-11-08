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
from os import system
from datetime import date, time, datetime
import time
import operator
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from App import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la operación solicitada
"""

def printMenu():
    system("cls")
    
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lista cronólógica de los artistas")
    print("3- Lista cronológica de las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento ")
    print("7- Crear nueva exposición")

catalogo = None

def initCatalogo():
    """
    Inicializa el catalogo del modelo
    """
    return controller.initCatalogo1()

def cargarDatos1(catalogo):
    """
    Carga las obras y los artistas en la estructura de datos
    """
    controller.cargarDatos1(catalogo)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
        tiempo_inicial = time.process_time()    
        print("Cargando información de los archivos ....")

        catalogo = controller.initCatalogo1()
        cargarDatos1(catalogo)
        tiempo_final = time.process_time()
        duracion = (tiempo_final - tiempo_inicial)*1000
        
        print(f"El tiempo de carga de datos es: {duracion} milisegundos")
        
        system("cls")    

    elif int(inputs[0]) == 2:
        
        anho_inicial = int(input("Digite el año inicial: "))
        anho_final = int(input("Digite el año final: "))
        
        tiempo_inicial = time.process_time()
        
        rango_artistas = controller.rangoArtistasPorAnho(catalogo, anho_inicial, anho_final)
        info_artistas = lt.newList(datastructure='ARRAY_LIST')
        
        for i in lt.iterator(rango_artistas):
            for j in lt.iterator(i):
                lt.addLast(info_artistas, j)
                
        primeros_3 = lt.subList(info_artistas, 1, 3)  
        ultimos_3 = lt.subList(info_artistas, (lt.size(info_artistas)-2), 3)  
        resultado_1 = 'Hay {} artistas nacidos entre {} y {}'.format(lt.size(info_artistas), str(anho_inicial), str(anho_final))
        
        print(resultado_1)
        print('========================================================')
        
        print('Los primeros 3 artistas en el rango son: ')
        print('        Nombre         | Fecha de Nacimiento | Fecha de muerte |   Nacionalidad   |    Género   ')
        print('==================================================================================================')
        for i in lt.iterator(primeros_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['nombre'], i['fecha_nacimiento'], i['fecha_muerte'], i['nacionalidad'], i['genero']))
        print(' ')  
        print('Los últimos 3 artistas en el rango son: ')
        print('        Nombre         | Fecha de Nacimiento | Fecha de muerte |   Nacionalidad   |    Género   ')
        print('==================================================================================================')
        for i in lt.iterator(ultimos_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['nombre'], i['fecha_nacimiento'], i['fecha_muerte'], i['nacionalidad'], i['genero']))
        print('==================================================================================================')    
        
        tiempo_final = time.process_time()
        duracion = (tiempo_final - tiempo_inicial)*1000
        
        print('El tiempo de ejecución fue de: ', duracion, ' ms.')

        input()
        system("cls")
             
    elif int(inputs[0]) == 3:

        tiempo_inicial = time.process_time()

        fecha_inicial_texto = input('Escriba la fecha inicial: ')
        fecha_inicial = datetime.strptime(fecha_inicial_texto, '%Y-%m-%d')
        fecha_final_texto = input('Escriba la fecha final: ')
        fecha_final = datetime.strptime(fecha_final_texto, '%Y-%m-%d')
        datosArtistas = catalogo['artistas']
        datos = catalogo['obras']
        identificador = 3
        key_obras = mp.keySet(catalogo['obras'])
        print('============================================')
        lista_rango=lt.newList('ARRAY_LIST')
        
        for key in lt.iterator(key_obras):
            entry = mp.get(catalogo['obras'], key)
            elemento = me.getValue(entry)
            if elemento['fecha_adquisicion']=='':
                pass
            else:
                fecha_elemento=datetime.strptime(elemento['fecha_adquisicion'], '%Y-%m-%d')
                if fecha_elemento > fecha_inicial and fecha_elemento < fecha_final:
                  lt.addLast(lista_rango, elemento)

        numero_elementos = lt.size(lista_rango)

        lista = controller.llamarMerge(lista_rango, identificador)[1]

        primeros_3 = lt.subList(lista, 1, 3)
        ultimos_3 = lt.subList(lista, lt.size(lista)-4, 3)
        print("El número total de obras adquiridas por compra es de : " + str(controller.obrasAdquiridasPorCompra(lista)))
        print('El número de elementos en el rango es: ' + str(numero_elementos))
        print(' ')
        print('Los tres primeros elementos son:')
        print('        Título         |    Fecha    |     Medio     |       Dimensiones       ')
        print('==================================================================================================')
        for i in lt.iterator(primeros_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}'.format(i['titulo'], i['fecha_adquisicion'], i['medio'], i['dimensiones']))
        print('')
        print('Los tres últimos elementos son:')
        print('        Título         |    Fecha    |     Medio     |       Dimensiones       ')
        print('==================================================================================================')
        for i in lt.iterator(ultimos_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}'.format(i['titulo'], i['fecha_adquisicion'], i['medio'], i['dimensiones']))
        print(' ')
        tiempo_final = time.process_time()
        duracion = (tiempo_final - tiempo_inicial)*1000
        print('El tiempo de ejecución fue de: ',duracion, ' ms.')

        input()
        system("cls") 
    
    elif int(inputs[0]) == 4:
        
        nombre_artista = input("Digite el nombre del artista: ")
        
        tiempo_inicial = time.process_time()
        
        entry_artista = mp.get(catalogo['artistas'], nombre_artista)
        info_artista = me.getValue(entry_artista)
        obras_artista = info_artista['obras']   
        info_obras = lt.newList(datastructure='ARRAY_LIST')
        idArtista = info_artista['id']
        lista_medios = lt.newList(datastructure='ARRAY_LIST')
        #lista_todos_medios = lt.newList(datastructure='ARRAY_LIST')
        lista_todos_medios = []
        
        for i in lt.iterator(obras_artista):
            entry_medio = mp.get(catalogo['obras'], i)
            info_medio = me.getValue(entry_medio)
            medio = info_medio['medio']
            
            if lt.isPresent(lista_medios, medio) == 0:
                lt.addLast(lista_medios, medio)
                
            lista_todos_medios.append(medio)
            lt.addLast(info_obras, info_medio)
            
        obras_artista_ordenada = controller.llamarMerge(info_obras, identificador=2)
        mayor = 0
        medio_mayor = None
            
        for i in lista_todos_medios:
            cont = lista_todos_medios.count(i)
            
            if cont > mayor:
                mayor = cont
                medio_mayor = i
            
        print("Clasificando ...")       
        print(('{} con MOMA Id {} tiene {} obras a su nombre en el museo.').format(nombre_artista, idArtista, lt.size(obras_artista)))
        print(('Existen {} medios/técnicas diferentes en su trabajo.').format(lt.size(lista_medios)))
        print('Su técnica más utilizada es {} con {} obras.'.format(medio_mayor, mayor))    
        print('')   
        print('\tTítulo \t |Fecha de la obra|    Técnica    |    \t\t Dimensiones    ')  
        print('==================================================================================================')      
        for i in lt.iterator(obras_artista_ordenada[1]):
            entry_cada_obra = mp.get(catalogo['obras'], i['titulo'])
            info_cada_obra = me.getValue(entry_cada_obra)
            
            if info_cada_obra['medio'] == medio_mayor:
                print('{}\t   {} \t\t {} \t\t {}'.format(info_cada_obra['titulo'], info_cada_obra['fecha'], info_cada_obra['medio'], info_cada_obra['dimensiones']))
        print('')
        
        tiempo_final = time.process_time()
        duracion = (tiempo_final - tiempo_inicial)*1000
        
        print('El tiempo de ejecución fue de: ', duracion, ' ms.')
        
        input()
        system("cls")  

    elif int(inputs[0]) == 5:

        tiempo_inicial = time.process_time()

        lista_nacionalidades = catalogo['nacionalidades']
        lista_llaves = mp.keySet(lista_nacionalidades)

        dic = {}

        for i in lt.iterator(lista_llaves):
            entry = mp.get(catalogo['nacionalidades'], i)
            info = me.getValue(entry)
            dic[i]=lt.size(info)
        
        dic_sort = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
        
        print('Las 10 nacionalidades con más obras son:')

        for i in range(10):
            print(dic_sort[i])

        lista_obras = lt.newList('ARRAY_LIST')

        if dic_sort[0].__contains__(''):
            nacionalidad_dic = dic_sort[1]
        else:
            nacionalidad_dic = dic_sort[0]
        
        nacionalidad = str(nacionalidad_dic[0])

        entry_nacionalidad = mp.get(catalogo['nacionalidades'], nacionalidad)
        artistas_nacionalidad = me.getValue(entry_nacionalidad)
        lista1 = controller.llamarBuscarObrasPorNacionalidad(catalogo, nacionalidad)
        lista = controller.llamarMerge(lista1,3)[1]
        print('Los tres primeros elementos son:')
        primeros_3=lt.subList(lista,1,3)
        print('        Título         |    Fecha    |     Medio     |       Dimensiones       ')
        print('==================================================================================================')
        for i in lt.iterator(primeros_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}'.format(i['titulo'], i['fecha_adquisicion'], i['medio'], i['dimensiones']))
        print('')
        ultimos_3=lt.subList(lista,lt.size(lista)-4,3)
        print('Los tres últimos elementos son:')
        print('        Título         |    Fecha    |     Medio     |       Dimensiones       ')
        print('==================================================================================================')
        for i in lt.iterator(ultimos_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}'.format(i['titulo'], i['fecha_adquisicion'], i['medio'], i['dimensiones']))
        print('')      
        tiempo_final = time.process_time()
        duracion = (tiempo_final - tiempo_inicial)*1000
        print('El tiempo de ejecución fue de: ',duracion, ' ms.')
        input()
        system("cls")

    elif int(inputs[0]) == 6:

        departamento = input("Escriba el departamento del museo a analizar: ")
        entry = mp.get(catalogo['departamentos'], departamento)
        lista_obras_departamento = me.getValue(entry)

        print('El número de obras en el departamento es: ' + str(lt.size(lista_obras_departamento)))
        costo = controller.llamarDarPrecioTransporteDepartamento(lista_obras_departamento)
        print('El costo de transportar todo el departamento de obras es de: ' + str(round(costo, 2)) + ' USD')
        peso_total = controller.llamarDarPesoTotalDepartamento(lista_obras_departamento)
        print('El peso total de las obras del departamento es de: ' + str(peso_total) + 'Kg')
        lista_ordenada = controller.llamarMerge(lista_obras_departamento, 3)
        tiempo1 = lista_ordenada[0]
        antiguas5 = lt.subList(lista_ordenada[1], 1, 5)
        
        print('Las 5 obras mas antiguas son:')
        print('\tTítulo \t |   Clasificación   |    Fecha de la obra   |    Técnica    |  \t\t Dimensiones   | Costo Asociado ')  
        print('===============================================================================================================')
        for i in lt.iterator(antiguas5):
            print('{}\t   {} \t\t {} \t\t {} \t\t {} \t\t {}'.format(i['titulo'], i['clasificacion'], i['fecha_adquisicion'], i['medio'], i['dimensiones'], i['costo_transporte']))
        print(' ')
        lista_obras_ordenadas_costo = controller.llamarMerge(lista_ordenada[1], 4)
        costosas5 = lt.subList(lista_obras_ordenadas_costo[1], (lt.size(lista_obras_ordenadas_costo[1])- 4), 5)
        tiempo2 = lista_obras_ordenadas_costo[0]
        print('Las 5 obras mas costosas para transportar son:')
        print('\tTítulo \t |   Clasificación   |    Fecha de la obra   |    Técnica    |  \t\t Dimensiones   | Costo Asociado ')  
        print('===============================================================================================================')
        for i in lt.iterator(costosas5):
            print('{}\t   {} \t\t {} \t\t {} \t\t {} \t\t {}'.format(i['titulo'], i['clasificacion'], i['fecha_adquisicion'], i['medio'], i['dimensiones'], i['costo_transporte']))
        print('')
        tiempo_total = tiempo1 + tiempo2
        print('El tiempo de ejecución fue de: ',tiempo_total, ' ms.')

        input()
        system("cls")
        
    elif int(inputs[0]) == 7:
        
        numero_artistas = int(input("Digite el número de artistas que desea en la clasificación: "))
        anho_inicial = int(input("Digite el año inicial: "))
        anho_final = int(input("Digite el año final: "))
        
        tiempo_inicial = time.process_time()
        rango_artistas = controller.rangoArtistasPorAnho(catalogo, anho_inicial, anho_final)
        lista_final = lt.newList(datastructure='ARRAY_LIST')
        
        for i in lt.iterator(rango_artistas):
            for j in lt.iterator(i):
                lt.addLast(lista_final, j)
            
        info_artista_ordenada = controller.llamarShell(lista_final, identificador=5)
        
        lista_prolificos = lt.subList(info_artista_ordenada[1], 1, numero_artistas)
        temp1 = lt.getElement(lista_prolificos, 1)
        id_mas_prolifico = temp1['id']
        lista_id = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista_id, id_mas_prolifico)
        
        print('\t Nombre \t |Fecha de nacimiento|    Género    |    \t\t Total obras  |  Total técnicas   |  Técnica mayor')  
        print('=================================================================================================')     
        
        for i in lt.iterator(lista_prolificos):
            
            listax = i['obras']
            lista_medio = lt.newList(datastructure='ARRAY_LIST')
            lista_todos_medios = []
            
            for j in lt.iterator(listax):
                entry = mp.get(catalogo['obras'], j)
                info_obra = me.getValue(entry)
                medio = info_obra['medio']
                
                if lt.isPresent(lista_medio, medio) == 0:      
                    lt.addLast(lista_medio, medio)
                    
                lista_todos_medios.append(medio)
                
            mayor = 0
            medio_mayor = None
            
            for n in lt.iterator(lista_medio):
                cont = lista_todos_medios.count(n)
                if cont > mayor:
                    mayor = cont
                    medio_mayor = n
                    
            temp = lt.isPresent(lista_id, i['id'])
            if  temp == 1:
                medio_mas_prolifico = medio_mayor
                
            i['numMedio'] = mayor
                    
            print('{}\t   {} \t\t {} \t\t {} \t\t {} \t\t {}'.format(i['nombre'], i['fecha_nacimiento'], i['genero'], lt.size(i['obras']), mayor, medio_mayor))


        lista_prolificos_ordenada = controller.llamarMerge(lista_prolificos, identificador=5)
        artista_mas_prolifico = lt.getElement(lista_prolificos_ordenada[1], 1)
        obras_prolifico = artista_mas_prolifico['obras']
        lista_mas_prolifico = lt.newList(datastructure='ARRAY_LIST')
        
        for i in lt.iterator(obras_prolifico):
            entry1 = mp.get(catalogo['obras'], i)
            info_obra_1 = me.getValue(entry1)
            medio = info_obra_1['medio']
            
            if medio == medio_mas_prolifico:
                lt.addLast(lista_mas_prolifico, info_obra_1)
                
        print('{} con MoMA ID {} tiene {} obras a su nombre en el museo'.format(artista_mas_prolifico['nombre'], artista_mas_prolifico['id'], artista_mas_prolifico['num_prolifico']))  
        print('A continuación se muestran las 5 primeras obras ordenadas por fecha de adquisición: \n') 
        print('\Título \t |Fecha de la obra|    Fecha de adquisicion    |    \t\t Departamento  |   Dimensiones   |')  
        print('===========================================================================================================')  
        
        if lt.size(lista_mas_prolifico) <= 5:
            for i in lt.iterator(lista_mas_prolifico):
                print('{}\t   {} \t\t {} \t\t {} \t\t {}'.format(i['titulo'], i['fecha_obra'], i['fecha_adquisicion'], i['departamento'], i['dimensiones']))
        else:
            sublista_prolificos = lt.subList(lista_mas_prolifico, 1, 5)
            #sublista_prolificos_ordenada = controller.llamarQuicksort(sublista_prolificos, identificador=3)
            sublista_prolificos_ordenada = controller.llamarMerge(sublista_prolificos, identificador=3)
            
            for i in lt.iterator(sublista_prolificos_ordenada[1]):
                print('{}\t   {} \t\t {} \t\t {} \t\t {} \t\t {}'.format(i['titulo'], i['fecha'], i['fecha_adquisicion'], i['medio'], i['departamento'], i['dimensiones']))
                
        tiempo_final = time.process_time()
        duracion = (tiempo_final - tiempo_inicial)*1000
        print('El tiempo de ejecución fue de: ',duracion, ' ms.')
                
        input()
        system("cls")
            
        

sys.exit(0)
