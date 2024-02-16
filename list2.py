import time

start_time = time.time()

def generar_numero():
    #print("estoy en generar_numero")
    numero_actual = 37
    diferencias = [21, 9, 81, 15, 69, 36, 195, 24, 105, 60, 45, 231, 54, 90, 15, 51, 180, 84, 21, 195, 15, 114, 105,
                   96, 30, 39, 45, 75, 6, 99, 51, 54, 21, 9, 165, 66, 180, 9, 165, 231, 24, 165, 120, 195, 15, 21,
                   30, 165, 234, 96, 30, 39, 21, 105, 99, 6, 120, 9, 180, 231, 9, 75, 90, 66, 39, 36, 114, 81, 84, 21,
                   129, 81, 120, 30, 165, 99, 90, 45, 21, 39, 66, 39, 21, 45, 159, 126, 90, 15, 315, 9, 105, 231, 39,
                   45, 21, 54, 90, 21, 45, 75, 105, 105, 30, 165, 24, 75, 30, 105, 21, 39, 126, 99, 90, 15, 51, 54,
                   111, 84, 36, 195, 15, 219, 210, 21, 159, 6, 99, 126, 69, 15, 51, 180, 84, 30, 126, 39, 36, 90, 24,
                   75, 6, 150, 84, 81, 99, 51, 354, 141, 90, 45, 60, 105, 99, 30, 96, 69, 330, 30, 60, 66, 39, 66,
                   39, 120, 111, 45, 75, 90, 99, 240, 75, 156, 39, 36, 30, 39, 66, 60, 84, 120]
    indice_diferencia = 0
    i = 1
    lista_infinita = []
    while i == 1:
        lista_infinita.append(numero_actual)
        numero_actual += diferencias[indice_diferencia]
        indice_diferencia = (indice_diferencia + 1) % len(diferencias)
        tratar_numero(numero_actual)
    
    #return lista_infinita


def tratar_numero(lista_rx):
    #print(" Funcion tratar_numero")
    #print("lista rx = ", lista_rx," -----> +1 ", lista_rx+1)
    comprobar(lista_rx )



def comprobar(numero_ingresado):
        #print(" Estoy en comprobar")
        
        #no_es_multiplo_de_3 = [1]
        #resto3 = numero_ingresado % 3
    
        #no_es_multiplo_de_5 = [2,3]
        #resto5 = numero_ingresado % 5
    
        #no_es_multiplo_de_7 = [1,2,4]
        #resto7 = numero_ingresado % 7
    
        #no_es_multiplo_de_11 = [1,3,4,5,9]
        #resto11 = numero_ingresado % 11
    
        #no_es_multiplo_de_13 = [2,5,6,7,8,11]
        #resto13 = numero_ingresado % 13

        no_es_multiplo_de_17 = [3,5,6,7,10,11,12,14]
        resto17 = numero_ingresado % 17

        no_es_multiplo_de_19 = [1,4,5,6,7,9,11,16,17]
        resto19 = numero_ingresado % 19

        no_es_multiplo_de_23 = [1,2,3,4,6,8,9,12,13,16,18]
        resto23 = numero_ingresado % 23

        no_es_multiplo_de_29 = [2,3,8,10,11,12,14,15,17,18,19,21,26,27]
        resto29 = numero_ingresado % 29

        no_es_multiplo_de_31 = [1,2,4,5,7,8,9,10,14,16,18,19,20,25,28]
        resto31 = numero_ingresado % 31

        no_es_multiplo_de_37 = [2,5,6,8,13,14,15,17,18,19,20,22,23,24,29,31,32,35]
        resto37 = numero_ingresado % 37

        no_es_multiplo_de_41 = [3,6,7,11,12,13,14,15,17,19,22,24,26,27,28,29,30,34,35,38]
        resto41 = numero_ingresado % 41

        no_es_multiplo_de_43 = [1,4,6,9,10,11,13,14,15,16,17,21,23,24,25,31,35,36,38,40,41]
        resto43 = numero_ingresado % 43

        no_es_multiplo_de_47 = [1,2,3,4,6,7,8,9,12,14,16,17,18,21,24,25,27,28,32,34,36,37,42]
        resto47 = numero_ingresado % 47

        no_es_multiplo_de_53 = [2,3,5,8,12,14,18,19,20,21,22,23,26,27,30,31,32,33,34,35,39,41,45,48,50,51]
        resto53 = numero_ingresado % 53

        no_es_multiplo_de_59 = [1,3,4,5,7,9,12,15,16,17,19,20,21,22,25,26,27,28,29,35,36,41,45,46,48,49,51,53,57]
        resto59 = numero_ingresado % 59

        no_es_multiplo_de_61 = [2,6,7,8,10,11,17,18,21,23,24,26,28,29,30,31,32,33,35,37,38,40,43,44,50,51,53,54,55,59]
        resto61 = numero_ingresado % 61

        no_es_multiplo_de_67 = [1,4,6,9,10,14,15,16,17,19,21,22,23,24,25,26,29,33,35,36,37,39,40,47,49,54,55,56,59,60,62,64,65]
        resto67 = numero_ingresado % 67

        no_es_multiplo_de_71 = [1,2,3,4,5,6,8,9,10,12,15,16,18,19,20,24,25,27,29,30,32,36,37,38,40,43,45,48,49,50,54,57,58,60,64]
        resto71 = numero_ingresado % 71

        no_es_multiplo_de_73 = [5,7,10,11,13,14,15,17,20,21,22,26,28,29,30,31,33,34,39,40,42,43,44,45,47,51,52,53,56,58,59,60,62,63,66,68]
        resto73 = numero_ingresado % 73

        no_es_multiplo_de_79 = [1,2,4,5,8,9,10,11,13,16,18,19,20,21,22,23,25,26,31,32,36,38,40,42,44,45,46,49,50,51,52,55,62,64,65,67,72,73,76]
        resto79 = numero_ingresado % 79

        no_es_multiplo_de_83 = [1,3,4,7,9,10,11,12,16,17,21,23,25,26,27,28,29,30,31,33,36,37,38,40,41,44,48,49,51,59,61,63,64,65,68,69,70,75,77,78,81]
        resto83 = numero_ingresado % 83

        no_es_multiplo_de_89 = [3,6,7,12,13,14,15,19,23,24,26,27,28,29,30,31,33,35,37,38,41,43,46,48,51,52,54,56,58,59,60,61,62,63,65,66,70,74,75,76,77,82,83,86]
        resto89 = numero_ingresado % 89

        no_es_multiplo_de_97 = [5,7,10,13,14,15,17,19,20,21,23,26,28,29,30,34,37,38,39,40,41,42,45,46,51,52,55,56,57,58,59,60,63,67,68,69,71,74,76,77,78,80,82,83,84,87,90,92]
        resto97 = numero_ingresado % 97

        no_es_multiplo_de_101 = [2,3,7,8,10,11,12,15,18,26,27,28,29,32,34,35,38,39,40,41,42,44,46,48,50,51,53,55,57,59,60,61,62,63,66,67,69,72,73,74,75,83,86,89,90,91,93,94,98,99]
        resto101 = numero_ingresado % 101

        no_es_multiplo_de_103 = [1,2,4,7,8,9,13,14,15,16,17,18,19,23,25,26,28,29,30,32,33,34,36,38,41,46,49,50,52,55,56,58,59,60,61,63,64,66,68,72,76,79,81,82,83,91,92,93,97,98,100]
        resto103 = numero_ingresado % 103

        no_es_multiplo_de_107 = [1,3,4,9,10,11,12,13,14,16,19,23,25,27,29,30,33,34,35,36,37,39,40,41,42,44,47,48,49,52,53,56,57,61,62,64,69,75,76,79,81,83,85,86,87,89,90,92,99,100,101,102,105]
        resto107 = numero_ingresado % 107

        no_es_multiplo_de_109 = [2,6,8,10,11,13,14,17,18,19,23,24,30,32,33,37,39,40,41,42,44,47,50,51,52,53,54,55,56,57,58,59,62,65,67,68,69,70,72,76,77,79,85,86,90,91,92,95,96,98,99,101,103,107]
        resto109 = numero_ingresado % 109

        no_es_multiplo_de_113 = [3,5,6,10,12,17,19,20,21,23,24,27,29,33,34,35,37,38,39,40,42,43,45,46,47,48,54,55,58,59,65,66,67,68,70,71,73,74,75,76,78,79,80,84,86,89,90,92,93,94,96,101,103,107,108,110]
        resto113 = numero_ingresado % 113

        no_es_multiplo_de_127 = [1,2,4,8,9,11,13,15,16,17,18,19,21,22,25,26,30,31,32,34,35,36,37,38,41,42,44,47,49,50,52,60,61,62,64,68,69,70,71,72,73,74,76,79,81,82,84,87,88,94,98,99,100,103,104,107,113,115,117,120,121,122,124]
        resto127 = numero_ingresado % 127



           #resto3 in no_es_multiplo_de_3 and resto5 in no_es_multiplo_de_5 and resto7 in no_es_multiplo_de_7 and resto11 in no_es_multiplo_de_11 and resto13 in no_es_multiplo_de_13 and 
        if resto17 in no_es_multiplo_de_17 and resto19 in no_es_multiplo_de_19 and resto23 in no_es_multiplo_de_23 and resto29 in no_es_multiplo_de_29 and resto31 in no_es_multiplo_de_31 and resto37 in no_es_multiplo_de_37 and resto41 in no_es_multiplo_de_41 and resto43 in no_es_multiplo_de_43 and resto47 in no_es_multiplo_de_47 and resto53 in no_es_multiplo_de_53 and resto59 in no_es_multiplo_de_59 and resto61 in no_es_multiplo_de_61 and resto67 in no_es_multiplo_de_67 and resto71 in no_es_multiplo_de_71 and resto73 in no_es_multiplo_de_73 and resto79 in no_es_multiplo_de_79 and resto83 in no_es_multiplo_de_83 and resto89 in no_es_multiplo_de_89 and resto97 in no_es_multiplo_de_97 and resto101 in no_es_multiplo_de_101 and resto103 in no_es_multiplo_de_103 and resto107 in no_es_multiplo_de_107 and resto109 in no_es_multiplo_de_109 and resto113 in no_es_multiplo_de_113: #and resto127 in no_es_multiplo_de_127:
            print("-------------------->  ¡El ", numero_ingresado, " funciona!")
            #pause()
            current_time = time.time()
            execution_time = current_time - start_time
            print(f"Tiempo de ejecución: {execution_time} segundos")
            print(f"Ahora: {current_time} segundos")
            #time.sleep(0.3)
            #start_time = time.time()



# PROGRAMA PRINCIPAL
# Llamar a la función y almacenar la lista resultante
start_time = time.time()

print("Llamar a generar_numero")
num_obtenido = generar_numero()

# Imprimir los primeros 10 elementos de la lista
#print(num_obtenido[:10])

tratar_numero(num_obtenido)

# Imprimir los múltiplos de 7 de la lista resultante
multiplos_de_7 = [num for num in num_obtenido if num % 7 == 0]
print(multiplos_de_7)
