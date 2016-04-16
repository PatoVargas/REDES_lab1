from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
import numpy as np

"""
Entrada: info del audio y la frecuencia
Salida: gráfico de la transformada de fourier
Funcion: realizar la transformada de fourier en 2 dimensiones, guardar en z y posteriormente graficar
"""
def transformadaFourier(signal,frecuencia):
	largo_n = signal.size 
	k = arange(largo_n) #crear un arreglo del tamaño de la señal
	T = largo_n/frecuencia #Periodo es igual al largo partido la frecuencia
	x = int(largo_n/2) #para graficar solo la mitad de la transformada
	frq = k/T #Se asigna una frecuencia a cada elemento de k
	frq = frq[0:x] # se limita el rango del arrreglo frq

	Y = fft(signal)/largo_n #Transformada de fourier de la señal
	Z =Y #Se guarda para retornar
	Y = Y[0:x]    #Se acota solo al conjunto de interes
	 
	plot(frq,abs(Y),'g') #Grafico de la transformada dejando solo la parte positiva
	title('Transformada de fourier vs Frecuencia')
	xlabel('Freq (Hz)') #nombre de los ejes
	ylabel('F (w)')
	return Z

def transformadaInversaFouerier(signal,frecuencia):
	W = np.fft.ifft(signal)
	Tiempo=np.linspace(0, len(signal)/frecuencia, num=len(signal))
	plot(Tiempo,W,'g')
	title('Transformada inversa de fourier a la transformada de fourier')
	xlabel('Tiempo')
	ylabel('Amplitud')
