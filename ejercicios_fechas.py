"""
2b- Hacer el mismo ejercicio pero en lugar de usar calendar, usar solo la librería datetime
3- Hacer un script que le informe al usuario cuantos días faltan para terminar el año
4- Hacer un script que le informe al usuario que fracción de año queda para la expiración de una
opción que vence el 18 de diciembre del corriente año desde la fecha en que se ejecuta el script
- Que funcione sea cual sea el año que se ejecute el código
- Usar el sub-paquete date de la librería datetime
5- Hacer un script que el usuario ingrese en las variables mes y año los valores del mes y año para el
cual se quiere saber el nombre del primer dia de ese mes
"""
#1 Hacer un script que devuelva en la variable año, el año actual
from datetime import datetime as dt_dt
hoy = dt_dt.now()
año2 = hoy.year
print(año2)

"""
2 Escribir el código al que el usuario le asigne:
- día
- mes
- año
Y devuelva el nombre en español del día de la semana cae esa fecha
Usar para ello la librería calendar
"""
import calendar
dia = int(input("ingrese dia "))
mes = int(input ("ingrese mes "))
año = int(input("ingrese año "))
fecha_string = año+"-"+mes+"-"+dia
print(fecha_string)#funciona ok
fecha = dt_dt.strptime(fecha_string, '%Y-%m-%d')
print(fecha)
es_dia= calendar.weekday(año,mes,dia)
print(f"es día {es_dia}")