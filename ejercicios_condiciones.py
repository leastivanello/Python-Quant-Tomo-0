#1
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
print("--------------")