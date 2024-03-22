# -*- coding: utf-8 -*-

import random as rd
"""
* Clase para usar los métodos de ordenamiento.
* @author Jesús García Abreu.
* @since Programación para la Ciencia de Datos.
* @date 18/03/2024
"""
class algoritmosOrdenamiento:
    
    """
    * Método burbuja.
    * @param lista, la lista a ordenar.
    * @return la lista ordenada.
    """
    def bubble_sort(self, lista) -> list:
        
        # Este contador nos sirve para ir moviendonos con el indice j para ir haciendo los intercambios en caso que sucedan.
        contador = 0
        
        # Este limitador nos sirve porque al hacer el primer recorrido, el último elemento de la lista ya esta ordenado,
        # por lo que no hace falta volver a hacer la comparación.
        limitador = 0
        
        # Cada que terminemos una iteración, aumentamos en uno al limitador logrando hacer una comparación menos.
        for i in range(0, len(lista) - 1 - limitador):
            for j in range(1, len(lista)):
                if(lista[j] < lista[contador]):
                    
                    # Intercambio de los elementos en al lista.
                    lista[j] , lista[contador] = lista[contador], lista[j]
                contador += 1
            contador = 0
            limitador += 1       
        return lista
    
    """
    * Método auxiliar para el merge sort.
    * @param lista1, la lista 1 a combinar y ordenar con la lista 2.
    * @param lista2, la lista 2 a combinar y ordenar con la lista 1.
    * @return lista_aux, la lista combinada y ordenada de la lista 1 y 2.
    """
    def ordenamiento(self, lista1, lista2) -> list:
        
        # La lista auxiliar en donde iremos juntando los elementos de ambas listas.
        lista_aux = list()
        i = 0
        j = 0
        
        # Vamos a ir metiendo los elementos de forma ordenada de manera que una lista la terminaremos de recorrer, y la otra lista
        # le faltaran elementos a recorrer.
        while(i < len(lista1) and j < len(lista2)):
            
            # Si el elemento de la primer lista es menor que el de la segunda lista, entonces agregamos ese elemento a la lista y
            # sumamos uno al contador en la primer lista.
            if(lista1[i] < lista2[j]):
                lista_aux.append(lista1[i])
                i += 1
                
            # En caso contrario, agregamos el elemento de la segunda lista y sumamos uno al contador de la lista 2.
            else:
                lista_aux.append(lista2[j])
                j += 1
                
        # De la lista a la que falten recorrer elementos, se los agregamos a la lista_aux.        
        while(j < len(lista2)):
            lista_aux.append(lista2[j])
            j += 1
                
        while(i < len(lista1)):
            lista_aux.append(lista1[i])
            i += 1
            
        # Regresamos la lista ya combinada y ordenada.
        return lista_aux
    
    
    """
    * Método merge_sort.
    * @param lista, la lista a ordenar.
    * @return la lista ordenada.
    """
    def merge_sort(self, lista) -> list:
        
        # Si la lista tiene un solo elemento, entonces la regresamos tal cual.
        if len(lista) <= 1:
            return lista
        
        # Calculamos el punto medio de la lista.
        medio = len(lista) // 2
        
        # Dividimos la lista en dos partes.
        lista1 = lista[:medio]
        lista2 = lista[medio:]
        
        # Vamos a ir dividiendo la lista hasta que solo quede un elemento en cada sublista.
        lista1 = self.merge_sort(lista1)
        lista2 = self.merge_sort(lista2)
        
        # Regresamos la lista ordenada y combinada.
        return self.ordenamiento(lista1, lista2)

    """
    * Método auxiliar para dejar los elementos menores de lado izquierdo de la lista, y los mayores de lado derecho.
    * @param lista, la lista a separar sus elementos.
    * @return el indice separador.
    """
    def particion(self, lista, inicio, fin):  
        # Pivote el de la derecha
        pivote = lista[fin]
            
        # Apuntador del último elemento más pequeño
        i = inicio - 1
            
        for j in range(inicio, fin):
            if (lista[j] <= pivote):
                # Avanzar apuntador
                i = i + 1
                # Intercambiar elementos
                lista[i], lista[j] = lista[j], lista[i]
            
        # Al final intercambiar el pivote
        lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
            
        # Regresa la posición final del pivote
        return i + 1    
    
    
    """
    * Método quick_sort.
    * @param lista, la lista a ordenar.
    * @param inicio, el inicio de donde vamos a partir la lista.
    * @param final, hasta que indice vamos a partir la lista.
    * @return la lista ordenada
    """
    def quick_sort(self, lista, inicio, fin) -> list:
        
        if inicio < fin:
            # Dividir y acomodar pivote
            pivote = self.particion(lista, inicio, fin)
            self.quick_sort(lista, inicio, pivote - 1)
            self.quick_sort(lista, pivote + 1, fin)
            
        return lista
            
    """
    * Función auxiliar para generar una lista aleatoria de n números.
    * @return una lista con numeros aleatorios del 0 al 1000. 
    """
    def generar_lista_aleatoria(self):
        longitud_lista = rd.randint(0,1001)
        lista_aux = list()
        for i in range(longitud_lista):
            lista_aux.append(rd.randint(0,1001))
        conjunto_aux = set(lista_aux)
        lista_res = list(conjunto_aux)
        return lista_res
        
    """
    * Función para mostrar el menú de opciones.
    """
    def menu(self) -> None:
        while(True):
            try:
                print("\n\tMenu")
                print("\n1.- Bubble Sort.\n2.- Merge Sort.\n3.- Quick Sort.\n4.- Salida")
                opcion = int(input("Escoge una opción: "))
                if(opcion == 1):
                    print('\n\nLa lista desordenada: ')
                    lista = self.generar_lista_aleatoria()
                    print(lista)
                    print('\nLa lista ordenada: ')
                    print(self.bubble_sort(lista))
                elif(opcion == 2):
                    print('\n\nLa lista desordenada: ')
                    lista = self.generar_lista_aleatoria()
                    print(lista)
                    print('\nLa lista ordenada: ')
                    print(self.merge_sort(lista))     
                elif(opcion == 3):
                    print('\n\nLa lista desordenada: ')
                    lista = self.generar_lista_aleatoria()
                    print(lista)
                    print('\nLa lista ordenada: ')
                    print(self.quick_sort(lista, 0, len(lista) - 1))
                elif(opcion == 4):
                    return
                else:
                    print('\nEscoge una opción entre 1 y 4.')
                    
                catch = input("Presiona enter para continuar...")
            except ValueError:
                print('\nIngresa un número entero.')
                catch = input("Presiona enter para continuar...")
            except Exception as e:
                print(f'\nOcurrió un error: {e}')
                catch = input("Presiona enter para continuar...")
            except KeyboardInterrupt:
                print('\n\nSaliendo...')
                return
                
if __name__ == '__main__':
    
    prueba = algoritmosOrdenamiento()
    prueba.menu()
    
    
    
    