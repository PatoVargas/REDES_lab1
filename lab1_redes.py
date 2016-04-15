import numpy as np
from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt
from funciones import *

"""
Codigo elaborado por Patricio Vargas Pino, rut : 18455204-3 y que
utiliza como base el ejemplo presentado por Maximiliano Perez en la ayudantia.
"""

"""
Entrada: audio: beacon.wav.
Salida: ǵrafico de datos versus amplitud y rate del audio.
Funcion: las siguientes lineas de codigo imprimen el grafico que representan
los datos del audio y sus respectivas amplitudes.
"""
rate,info=read("beacon.wav") 
plt.rcParams['agg.path.chunksize'] = 100000
plt.title('Grafico datos versus amplitud')
plt.xlabel('tiempo')
plt.ylabel('amplitud')

Tiempo=np.linspace(0, len(info)/rate, num=len(info))

plt.plot(Tiempo,info)
plt.show() #primer grafico

z = np.fft.fft2(info)
plt.plot(z)
plt.show()

plt.plot(np.fft.ifft2(z))
plt.show()

print("El rate es:")
print(rate)
print("Tiempo total:")
print(info.size/rate)

