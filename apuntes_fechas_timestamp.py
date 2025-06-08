#--------------Trabajando con fechas:
#importar libreria "datetime", cada libreria tiene subpaquetes
import datetime as dt

#importar paquetes:
from datetime import date as dt_date
from datetime import datetime as dt_dt

#hoy = dt_dt.now()
hora = hoy.hour
año = hoy.year
minutos = hoy.minute
print(f'hora {hora}') #"clave agregar la f para que sepa que tiene que buscar arriba"
print(f'año {año}')
print(f'minutos {minutos}')

#otra forma de usar el now es el metodo today()
hoy = dt_dt.today()
print(hoy)
#para usar solo la fecha (sin importar hora)
dia = dt_date.today()
#print(dia,type(dia))

#fecha con formato string:
hoy = dt.datetime.today()
hoy_str = hoy.ctime()
print(hoy_str, type(hoy_str))
#Casteo de string a DateTime

#"Segunda parte de fechas"
hoy = dt_dt.today()
vencimiento_str= "2030,01,09" # se pasa un string
expiracion = dt.datetime.strptime(vencimiento_str, "%Y,%m,%d")
#print(expiracion)
diasrestantes =(expiracion - hoy).days
#print(diasrestantes)

#para pasar a str
hoy_txt = dt_dt.strftime(hoy, "%d/%m/%Y")
hoy_txt

#-----------Ejercicios Timestamp:
#Timestamp son los segundos que pasaron desde 1/1/1970 es decir fecha epoch
from datetime import datetime as dt_dt
hoy = dt_dt.now()
hoy
timestamp = hoy.timestamp() #asi se obtiene el timestamp
#timestamp
#obtener el fecha de un timestamp
timestamp = 1456629347
fecha = dt_dt.fromtimestamp(timestamp)
fecha