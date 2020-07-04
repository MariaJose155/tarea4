#María José Arce Marín
#B60561
#TAREA 4 Modelos probabilisticos 
import csv
import pandas as pd
import numpy as np
from scipy import stats
from scipy import signal
from scipy import integrate
import matplotlib.pyplot as plt

# Importamos el archivo de datos brindado
#lo cargamos en la siguiente lista
bits = []


with open('bits10k.csv', newline='') as archivo:
	lectura = csv.reader(archivo)
	next(lectura, None) 	# no guardar el encabezado
	for fila in lectura:
		bits.append(fila)	# adjuntar cada fila a lote
# Número de bits
N = len(bits)
#Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.
# Frecuencia 
f = 5000 # Hz

# Duración del período para cada onda
T = 1/f # en milisegundos

#cantidad de puntos
puntos = 50

# Puntos de muestreo para cada período
tp = np.linspace(0, T, puntos)

#fase = representa cada uno de los valores posibles de la fase, tantos como estados tenga la señal codificada en banda base multinivel.
fase = np.pi;
#tomamos una amplitud de 1
A = 1;
# Creamos la onda portadora

ondaPortadora = A*np.sin(2*np.pi * f * tp+fase)

# graficamos
plt.plot(tp, ondaPortadora)
plt.title('Onda Portadora')
plt.xlabel('Tiempo')
plt.savefig("graf 1")
plt.cla()
# Frecuencia del muestreo
fs = puntos/T # 1000000Hz

# Creamos la linea temporal para toda la señal
t = np.linspace(0, N*T, N*puntos)

# Inicializamos la señal modulada en cero
senal = np.zeros(t.shape)

# Creaciamos la  señal modulada
for k, b in enumerate(bits):
  bb = ''.join(map(str,b)) #convertimos a string
  bbb = int(bb) #convertimos a entero
  if bbb == 0:
    senal[k*puntos:(k+1)*puntos] = -1*(ondaPortadora)
  else:
    senal[k*puntos:(k+1)*puntos] = (bbb*ondaPortadora)


#graficamos
pb = 5
plt.title('Señal modulada')
plt.xlabel('tiempo')
plt.ylabel('amplitud')
plt.plot(senal[0:pb*puntos])
plt.savefig("graf 2")
plt.cla()
#Calcular la potencia promedio de la señal modulada generada.

Pinstantanea = senal**2 #potencia instantanea (así calculamos la seudo energía)

# Potencia promedio usando trapz(hace aprox numerica trapezoidal de una función en el tiempo)
Ppromedio = integrate.trapz(Pinstantanea, t) / (N * T)


print('La potencia promedio es: ',Ppromedio, 'W')

#Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.
# Relación señal-a-ruido deseada
#(SNR) desde -2 hasta 3 dB.
SNR = 3 #relación señal-ruido deseada
Pruido = Ppromedio/(10**(SNR/10)) #Potencia del ruido
#sigma = 0.01 #para que tenga poco ruido
sigma = np.sqrt(Pruido)#desviación estandar del ruido
ruido = np.random.normal(0,sigma,senal.shape)

#señal recibida
Rx = senal + ruido

# graficamos
pb = 5
plt.title('Señal recibida con SNR = 3')
plt.xlabel('tiempo')
plt.plot(Rx[0:pb*puntos])
plt.savefig("graf 3")
plt.cla()


#Demodulación y decodificación de la señal

# Pseudo-energía (sirve como umbral) 
Eseudo = np.sum(ondaPortadora**2) #la suma de la potencia instantanea al cuadrado
# Importamos otra vez el archivo pero esta vex por medio de pandas
bitss = pd.read_csv('bits10k.csv')

# Inicializamos el vector de bits recibidos
bitsRx = np.zeros(bitss.shape) #rx de recepción
umbral = Eseudo/2 #para que este bien parejo umbral al 50%
# Hacemos la demodulación de la señal por detección de energía
for k, b in enumerate(bitss):
    Demodulacion = np.sum(Rx[k*puntos:(k+1)*puntos] * ondaPortadora[k*puntos:(k+1)*puntos])  #producto interno de 2 funciones
    
    if Demodulacion > umbral:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0


error = np.sum(np.abs(bitss - bitsRx)) #errores
BER = error/N #tasa de error de bits, osea cuantos bits malos entre la cantidad total de bits

print('El error total es: ', error)
print('La tasa de error es: ',BER) #error menor a 10 a la menos 4 debe ser
#obtenemos vectores de las respuestas impresas en consola
vBER = [0,0,0,0,0,0]
vSNR = [-2,-1,0,1,2,3]
#graficamos
plt.title('BER vs SNR')
plt.ylabel('BER')
plt.xlabel('SNR')
plt.plot(vSNR,vBER)
plt.savefig("graf 6")
plt.cla()

#Densidad espectral de potencia

# Después del canal ruidoso
fw, PSD = signal.welch(Rx, fs, nperseg=1024)
plt.title('Densidad espectral de potencia después del canal ruidoso')
plt.semilogy(fw, PSD)
plt.xlabel('Hz')
plt.ylabel('')
plt.savefig("graf 5")
plt.cla()

# Antes del canal ruidoso
fw, PSD = signal.welch(senal, fs, nperseg=1024)
plt.title('Densidad espectral de potencia antes del canal ruidoso')
plt.semilogy(fw, PSD)
plt.xlabel('Hz')
plt.ylabel('Densidad espectral de potencia ')
plt.savefig("graf 4")
plt.cla()
