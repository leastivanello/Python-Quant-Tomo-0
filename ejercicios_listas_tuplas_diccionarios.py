listado = [1,2,3,4,5,6,7,8,9,10,11,12]
#filtrar solo los números pares

numeros_pares = listado[1::2]#desde el primero, hasta el ultimo, saltando de a 2
print(numeros_pares)

#Filtrar solo los valores del 4 hasta el final de la lista
desde_4 = listado[4:]
print(desde_4)

# Filtrar solo los valores del 5 hasta el 10
desde_4_hasta10 = listado[4:10]
print(desde_4_hasta10)

#4 – Filtrar solo los valores menores a 10 que sean pares
menor10par = listado[1:9:2]
print(menor10par)

#5 – Filtrar solo los múltiplos de 3 ordenados al revés
multiplo_3_alreves = listado[2::3]
multiplo_3_alreves.reverse()
print(multiplo_3_alreves)

#6 - Calcular el promedio de todos los números (usando las funciones sum y len)
print(sum(listado)/len(listado))

#DADAS LAS SIGUIENTES LISTAS
lideres = ["GGAL","PAMP","YPFD","TECO2","EDN","LOMA","BBAR"]
galpones = ["AGRO","FIPL","MIRG","GARO","LONG"]
#7- Elegir un galpón al azar y agregarlo a la lista lideres al final
import random
galpon = random.choice(galpones)
lideres2=lideres.copy() #para laburar con copia
lideres2.append(galpon)
print(lideres2)

#8 - Elegir un galpón al azar y remplazar a EDN por ese galpón
lideres3=lideres.copy()
print(lideres3)#original
lideres3[4]=galpon
print(lideres3)#reemplazado
print("--------------4/6")

#9 - Elegir 3 galpones al azar y remplazar una líder
#cualquiera por esos dos galpones
lideres4=lideres.copy()
agregado = random.sample(galpones,3)#agarramos 3 galpones al azar
numero_aleatorio = random.randint(1, 6)#se genera indicice aleatorio
lideres4[numero_aleatorio]=[agregado[0:2]]#se insertan 2 de 3 a lista
print(lideres4)#sale ok
'''
Solucion libro:
galpon_x3 = random.sample(galpones,3)
indice = random.randrange(0,5)
lideres[indice] = galpon_x3#la consigna pide 2 de 3 pero bueno
lideres
'''
#Diccionarios:
panel = {'ALUA': 29.35, 'BBAR': 120.85, 'BMA': 265.2, 'BYMA': 290, 'CEPU': 29, 'COME': 3, 'CRES': 40.7}
print(panel)
#10 - Remplazar el precio de BBAR por un precio al azar que elija python
#que varíe +/- $1 del precio que tiene (con precisión de 0,01)
panel1 = panel.copy()
numero_aleatorio = random.uniform(-1, 1)#traemos la dif +- 1$
panel1['BBAR']=round(panel1.get('BBAR')+numero_aleatorio,2)
print(panel1.get('BBAR'))#chequea valor modificado

#11 - Remplazar el precio de BBAR por un precio al azar que elija python
#ue varíe +/- 3% del precio que tiene (con precisión de 0,01)
panel2 = panel.copy()
print(panel2)
numero_aleatorio2= random.uniform(0.97,1.03)#le doy aleatoriamente una variación
panel2['BBAR']=round((panel2.get('BBAR') * numero_aleatorio2),2)
print(panel2)

#12 - Elegir un ticker al azar y mostrarlo
print(panel)
tickers = panel.keys()#trae las keys
random.choice(list(tickers))#castea los tickers y elige al azar

#13 - Re-ordenar el diccionario al azar
lista_panel=(list(panel))
print(lista_panel)
random.shuffle(lista_panel)
print(lista_panel)

#14 - Re-ordenar el diccionario alfabéticamente en forma inversa (de la Z a la A
lista_panel=(list(panel))
print(lista_panel)
lista_panel[::-1]
