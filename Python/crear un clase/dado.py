from random import randint

class Dado:
    """Clase que simula un dado"""

    def __init__(self, num_lados=8):
        '''De manera predeterminada el dado tiene 6 caras'''
        self.num_caras = num_lados

    def tira_dados(self):
        '''Regresa el valor después de lanzar el dado'''
        return randint(1, self.num_caras)

miDado = Dado()
resultados = []
for i in range(0, 1000, 1):
    resultados.append(miDado.tira_dados())
print(resultados)

#cuántas veces se obtuvo como resultado 1, 2, 3.... 8
frecuencias = []
for valor in range(1, miDado.num_caras+1):
    frecuencia = resultados.count(valor)
    frecuencias.append(frecuencia)
print(frecuencias)


miDado = Dado()
resultados = []
for i in range(0, 1000, 1):
    resultados.append(miDado.tira_dados())

frecuencias = []
for valor in range(1, miDado.num_caras+1):
    frecuencia = resultados.count(valor)
    frecuencias.append(frecuencia)




