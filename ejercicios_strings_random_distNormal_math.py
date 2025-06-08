
#---------------"Ejercicios con String:"
#1
cadena = "La ponderacion de AAPL en nuestro fondo paso del 4.35% a 4.23%"
string = cadena.rfind("AAPL")
string2 = cadena.count("%")
#print(string2)

#2
opcion = "GFCG155.AG"
print(opcion[:3]) #para sacar ticker del subyacente
#para encontrar todo despues del punto
ultimoPunto = opcion.find(".") #se busca el argumento
ultimos = opcion[ultimoPunto+1:] # se recorre opcion desde el ultimoPunto hasta finalizar
print(ultimos)


#----------"Ejercicios con Num. al azar:"

# Para generar numero aleatorio:
import random
#random.random()

#para darle un rango(min y max):
random.uniform(10,24)

# darle rangos e intervalos
min = 100
max = 1000
paso = 15

random.randrange(min,max,paso)

#Numero aleatorio en distribución normal:
import random

mu=0
sigma=1
random.normalvariate(mu,sigma)

#La seed es para generar los mismos numeros aleatorios siempre
random.seed(8)
random.random()
a = random.random()
print(a)

random.seed(0)
random.random()
b = random.random()
print(b)

#--------------Ejercicios con Math:


import math
#dos constantes que se usan pi y e

#truncado, piso y techo:
a = 5.44
b = -14.44

#entero inmediato inferior
#a = math.floor(a)
b = math.floor(b)

#entero inmediato superior
math.ceil(a)

c = 32742.392423
#redondea a entero
c = math.trunc(c)
c

d = 3.423423
round(d,2) # parametro y decimales

#---------Ejercicios con  random y dias:
import random
import matplotlib.pyplot as plt  # Asegúrate de tener matplotlib instalado

ggal4 = 135.51
random.seed(123)  # fija aleatoriedad
mu, sigma = 0.00012, 0.035

# Día lunes
variacion = random.normalvariate(mu, sigma)
lunes = round(ggal4 * (1 + variacion), 2)

# Día martes
variacion = random.normalvariate(mu, sigma)
martes = round(lunes * (1 + variacion), 2)

# Día miércoles
variacion = random.normalvariate(mu, sigma)
miercoles = round(martes * (1 + variacion), 2)

# Día jueves
variacion = random.normalvariate(mu, sigma)
jueves = round(miercoles * (1 + variacion), 2)

# Día viernes
variacion = random.normalvariate(mu, sigma)
viernes = round(jueves * (1 + variacion), 2)

# Mostrar precios
print(f"precios: {ggal4}, lunes: {lunes}, martes: {martes}, miercoles: {miercoles}, jueves: {jueves}, viernes: {viernes}")



print("Agregado para jugar con IA")
# Preparar datos para graficar
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
valores = [lunes, martes, miercoles, jueves, viernes]

# Graficar (esto fue agregado para verificar si funcionaba codigo con IA)
plt.figure(figsize=(8, 5))
plt.plot(dias, valores, marker='o', linestyle='-', color='blue')
plt.title("Evolución de precio durante la semana")
plt.xlabel("Día de la semana")
plt.ylabel("Precio")
plt.grid(True)
plt.tight_layout()
plt.show()