'''
1- Armar un script que me defina en una sola condición la variable hold para un activo es verdadera o
falsa, en función de las siguientes premisas:
• Que esté en tendencia bull, asumiendo para ello que la media rápida sea un 2% mayor a una
media lenta
• Que no rompa un stopLoss del 5% abajo del precio de compra
• Que la ganancia acumulada no sea superior al 20% ya que en ese caso se tomaría ganancias

Y verificar que nos devuelve lo siguiente para los siguientes precios:
• price = 97 => False
• price = 100 => False
• price = 101 => True
• price = 121 => True
• price = 128 => False
'''
precio_compra=106
media_rapida=100
media_lenta=98
precio_actual=121

stopLoss=precio_actual < precio_compra*0.95
ganancia_acumulada= precio_actual > 1.2 *precio_compra
#print(ganancia_acumulada) #funciona
#print(stopLoss) #funciona
tendencia_bull = media_rapida >media_lenta * 1.02

hold = tendencia_bull and not stopLoss and not ganancia_acumulada
print(hold)
print("--------")
'''
2. Con las mismas premisas del ejercicio anterior, modificarlo para que me devuelva en una variable
state un string que me indique si sigo invertido en ese activo, pero además en caso de ser falso me
indique si se salió por stopLoss o por toma de ganancias
Verificar que nos devuelve lo siguiente para los siguientes precios:
• price = 97 => Salida por stopLoss
• price = 100 => Salida por stopLoss
• price = 101 => Invertidos
• price = 121 => Invertidos
• price = 128 => Salida por takeProfit
'''
precio_compra=106
media_rapida=100
media_lenta=98
precio_actual=128

stopLoss=precio_actual < precio_compra*0.95
ganancia_acumulada= precio_actual > 1.2 *precio_compra
#print(ganancia_acumulada) #funciona
#print(stopLoss) #funciona
tendencia_bull = media_rapida >media_lenta * 1.02

hold = tendencia_bull and not stopLoss and not ganancia_acumulada

if hold:
  state="se sigue invertido"
else:
  if stopLoss:
    state="sale por stoploss"
  else:
    state="sale por take profit"
print("ejercicio 2 "+state)
print("--------")

'''
3. Reforzar la lógica del ejercicio anterior agregando a la condición del stopLoss que el precio tiene
que cortar a la media móvil lento para abajo para disparar el stopLoss. Verificar que nos devuelve lo
siguiente para los siguientes precios:
• price = 97 => Salida por stopLoss
• price = 100 => Invertidos
• price = 101 => Invertidos
• price = 121 => Invertidos
• price = 128 => Salida por takeProfit
'''
precio_compra=106
media_rapida=100
media_lenta=98
precio_actual=128

stopLoss=precio_actual < precio_compra*0.95 and precio_actual<media_lenta
ganancia_acumulada= precio_actual > 1.2 *precio_compra
#print(ganancia_acumulada) #funciona
#print(stopLoss) #funciona
tendencia_bull = media_rapida >media_lenta * 1.02

hold = tendencia_bull and not stopLoss and not ganancia_acumulada

if hold:
  state="se sigue invertido"
else:
  if stopLoss:
    state="sale por stoploss"
  else:
    state="sale por take profit"
print("ejercicio 3 "+state)
print("--------")
#'''4 - Reforzar la lógica del ejercicio anterior, haciendo que para gatillar el take profit puede o bien
#darse el 20% de ganancia o bien un 10% de ganancia y el precio superar en más del 20% a la media
#móvil rápido Verificar que nos devuelve lo siguiente para los siguientes precios:
#• price = 97 => Salida por stopLoss
#• price = 100 => Invertidos
#• price = 101 => Invertidos
#• price = 121 => Salida por takeProfit
#• price = 128 => Salida por takeProfit '''

precio_compra=106
media_rapida=100
media_lenta=98
precio_actual=100

takeprofit=precio_actual>=precio_compra*1.2 or (precio_actual>=precio_compra*1.1 and precio_actual > media_rapida *1.2)
stopLoss=precio_actual < precio_compra*0.95 and precio_actual<media_lenta
ganancia_acumulada= precio_actual > 1.2 *precio_compra
#print(ganancia_acumulada) #funciona
#print(stopLoss) #funciona
tendencia_bull = media_rapida >media_lenta * 1.02

hold = tendencia_bull and not stopLoss and not takeprofit

if hold:
  state="se sigue invertido"
else:
  if stopLoss:
    state="sale por stoploss"
  else:
    state="sale por take profit"
print("ejercicio 4 "+state)
print("-------")


#5 - Hacer un script que arranque definiendo el diccionario:
#Que representa los activos de la cartera y sus porcentajes de peso

#que me pida el ticker por un input y me devuelva el % de cada uno y si ingreso en el input un activo inexistente que me devuelva un
#mensaje aclarando que ese activo no está en la cartera
#Tener en cuenta que el script debe funcionar si el usuario ingresa el ticker con alguna o todas sus
#letras en minúscula

cartera = {"AAPL":30,"AMZN":25,"NFLX":20,"FB":10,"KO":5,"USD":10} #ya esta en porcentaje

ticker = input("ingrese ticker ").upper()#se castea a mayuscula
try:
  print(f"porcentaje de {ticker} es {cartera[ticker]}%")
except:
  print(f"{ticker} no se encuentra en cartera")

from itertools import count
activos1 = ["ALUA","BMA","BYMA","CEPU","COME","CRES","CVH","EDN","GGAL","MIRG"]
activos2 = ["PAM","SUPV","TECO2","TGNNO4","TGSU2","TRAN","TXAR","VALO","YPF"]
print("-------")

#6- Armar un script que genere una lista llamada activos con todos los elementos de ambas listas y
#devolver la cantidad total
activos = activos1#se copia 1 lista
activos.extend(activos2)#se agrega a la primera lista, la segunda
total_activos= len(activos)#se cuenta los elementos
print(f"total activos en cartera: {total_activos} y son: {activos}")
print("-------")


#7- Pedir un ticker al usuario vía input () y devolver si está o no en la variable activos y que funcione
#independientemente si se ingresa el ticker en minúscula o mayúscula

ticker_ej6=input("ingrese ticker nuevo").upper()#casteo Mayus
try:
  ticker_ej6 in activos
  print(f"{ticker_ej6} esta en cartera")
except:
  print(f"{ticker} no se encuentra en cartera")

#8- Dado el siguiente diccionario
precios = {"GGAL":80,"YPF":500}
activos1 = ["ALUA","BMA","BYMA","CEPU","COME","CRES","CVH","EDN","GGAL","MIRG"]
activos2 = ["PAM","SUPV","TECO2","TGNNO4","TGSU2","TRAN","TXAR","VALO","YPF"]
activos = activos1

#Hacer un script que le pida por un input () un ticker al usuario y
#• Si el ticker está en el listado de precios le devuelva el precio
#• Si no está el precio, pero sí se encuentra en el listado de activos, que le devuelva el mensaje
#que no tiene el precio de ese ticker (y nombrarlo en el mensaje)
#• Si ni siquiera encuentra el ticker en el listado de activos que le avise que el ticker no está ni en
#el listado de tickers
ticker_precios=precios.keys()#se trae las keys de precios
ticker8=input("ingrese ticker a buscar").upper()
if ticker8 in ticker_precios:
  print(f"{ticker8} esta en cartera y vale {precios[ticker8]}")#trae precio de DICCIONARIO Y se pasa la clave y trae el valor
else:
  if ticker8 in activos:
    print(f"{ticker8} no tengo precio")
  else:
    print(f"no se encontro {ticker8} en el listado de activos")