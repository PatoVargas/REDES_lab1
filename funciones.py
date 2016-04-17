from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
import numpy as np

"""
Entrada: info del audio y la frecuencia
Salida: gráfico de la transformada de fourier
Funcion: realizar la transformada de fourier, guardar en Z y posteriormente graficar
"""
def transformadaFourier(signal,frecuencia):
	largo_n = signal.size 
	k = arange(largo_n) #crear un arreglo del tamaño de la señal
	T = largo_n/frecuencia #Periodo es igual al largo partido la frecuencia
	x = int(largo_n/2) #para graficar solo la mitad de la transformada
	frq = k/T #Se asigna una frecuencia a cada elemento de k
	frq = frq[0:x] # se limita el rango del arrreglo frq

	Y = fft(signal) #Transformada de fourier de la señal
	Z =Y #Se guarda para retornar
	Y = Y[0:x]    #Se acota solo al conjunto de interes
	 
	plot(frq,abs(Y),'g') #Grafico de la transformada dejando solo la parte positiva
	title('Transformada de fourier vs Frecuencia')
	xlabel('Freq (Hz)') #nombre de los ejes
	ylabel('F (w)')
	return Z

"""
Entrada: info del audio y la frecuencia
Salida: gráfico de la transformada inversa de fourier
Funcion: realizar la transformada inversa de fourier, guardar en W y posteriormente graficar
"""
def transformadaInversaFourier(signal,frecuencia):
	W = np.fft.ifft(signal) #Transformada inversa del vector
	Tiempo=np.linspace(0, signal.size/frecuencia, num=signal.size) #arreglo para cambiar el eje x a tiempo
	plot(Tiempo,W,'r') 
	title('Transformada inversa de fourier a la transformada de fourier')
	xlabel('Tiempo (s)')
	ylabel('f(t)')
	return W

"""
Entrada: info del audio
Salida: valor de la amplitud maxima
Funcion: buscar el maximo dentro de un arreglo
"""
def buscarMaximo(signal):
	maximo = signal.max()
	return maximo

"""
Entrada: info del audio y su valor maximo
Salida: posicion del valor maximo
Funcion: buscar el indice del maximo dentro de un arreglo
"""
def buscarIndice(signal,maximo):
	contador = 0
	for i in signal:
		if i == maximo:
			return contador
		else:
			contador =contador+1

"""
Entrada: info del audio
Salida: grafico del espectro truncado
Funcion: graficar el escpectro después del truncamiento
"""
def graficarNuevoEspectro(signal):
	plot(abs(signal),'r')
	title('Nueva grafica de la transformada truncada')
	xlabel('Freq(Hz)')
	ylabel('F(w)')


"""
Entrada: info del audio e indice del valor maximo
Salida: un subconjunto del espectro original
Funcion: reducir el espectro incluyendo en un arreglo auxiliar los valores entre un 15 porciento
menos del maximo y 15%  mas respecto al mismo valor
"""
def reducirEspectro(signal,indice):
	contador = 0
	quinceporciento= int(indice*0.15)
	listaAuxiliar = []
	for i in signal:
		contador =contador+1
		if contador >= indice-quinceporciento:
			if contador <= indice+quinceporciento:
				listaAuxiliar.append(i)
		else:
			contador = contador
	return listaAuxiliar
