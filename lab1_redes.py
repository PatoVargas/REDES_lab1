"""
Codigo elaborado por Patricio Vargas Pino, rut : 18455204-3 y que
utiliza como base el ejemplo presentado por Maximiliano Perez en la ayudantia.
"""
#Importaciones
import numpy as np
from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt
from funciones import *

"""
Entrada: audio: beacon.wav.
Salida: ǵrafico de datos versus amplitud y rate del audio.
Funcion: las siguientes lineas de codigo imprimen el grafico que representan
los datos del audio y sus respectivas amplitudes.
"""
rate,info=read("beacon.wav") 
plt.rcParams['agg.path.chunksize'] = 100000 #se ajusta para visualizar los datos

"""
Primer gráfico Tiempo vs amplitu
"""
plt.title('Amplitud vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('f(t)')
Tiempo=np.linspace(0, len(info)/rate, num=len(info))
plt.plot(Tiempo,info)
plt.show() 

"""
Grafico de la transformada de fourier de la señal de entrada
"""
signal =info[:,1]
transformada = transformadaFourier(signal,rate)
show()
"""
Grafico de la transformada inversa de fourier de la transfomada antes graficada
"""
transformadainversa = transformadaInversaFourier(transformada,rate)
show()

"""
Truncar la inversa en torno a la maxima con un margen del 15%
"""
maximo = buscarMaximo(transformadainversa)
indice = buscarIndice(transformadainversa,maximo)
listaAuxiliar = np.array(reducirEspectro(transformadainversa,indice))
graficarNuevoEspectro(listaAuxiliar)
show()
transformadainversa_15 = transformadaInversaFourier(listaAuxiliar,rate)
show()

print("La amplitud maxima es:")
print(maximo)

