from dado import Dado

Dado1 = Dado()
Dado2 = Dado()
resultados = []
for i in range(0,1000,1):
    resultados.append(Dado1.tira_dados() + Dado2.tira_dados())

frecuencias = []
for valor in range(2,Dado1.num_caras+Dado2.num_caras+1):
    frecuencia = resultados.count(valor)
    frecuencias.append(frecuencia)

#Visualización de los resultados
# Genera una lista con valores del 1 al número de caras
valores_x = list(range(2,Dado1.num_caras+Dado2.num_caras+1))
print(valores_x)
data = [Bar(x=valores_x,y = frecuencias)]

configuracion_eje_x = {'title':'Resultados','dtick':1}
configuracion_eje_y = {'title':'frecuencia'}

my_layout = Layout(title='Resultados de tirar un dado de 6 caras 1000 veces',xaxis = configuracion_eje_x,
                  yaxis = configuracion_eje_y)

offline.plot({'data':data,'layout':my_layout},filename = 'd6_d6.html')