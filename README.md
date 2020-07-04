# tarea4



# punto 1
Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.


Entonces se tiene lo siguiente:


<img src="https://render.githubusercontent.com/render/math?math=-Acos[2\pi ft] ">

El enunciado nos pide que usemos seno entonces:


<img src="https://render.githubusercontent.com/render/math?math=-Asen[2\pi ft] ">


Lo anterior es lo mismo a <img src="https://render.githubusercontent.com/render/math?math=2\pi ft "> sumarle <img src="https://render.githubusercontent.com/render/math?math=\phi"> y multiplicar la amplitud no por un -1 si no que por un 1.



Donde A = 1 y <img src="https://render.githubusercontent.com/render/math?math=\phi = \pi">




<img src=".../master/graf1" width ="450">

<img src=".../master/graf2" width ="450">

# punto 2
Calcular la potencia promedio de la señal modulada generada.


La potencia promedio es : 0.4900009800999702 W

# punto 3

Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.


Para este punto es importante tomar en cuenta que el ruido fue generado de manera aleatoria y con una distrinución normal. Las maginitudes que se obtuvieron se le agregaron a la señal modulada.



Para este punto podemos ver en  las imagenes los diferentes señales de ruido con los cambios de SNR.

<img src=".../master/graf3-2" width ="450">

<img src=".../master/graf3-1" width ="450">

<img src=".../master/graf30" width ="450">

<img src=".../master/graf31" width ="450">

<img src=".../master/graf32" width ="450">

<img src=".../master/graf33" width ="450">

# punto 4
Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.



<img src=".../master/graf4" width ="450">

<img src=".../master/graf5" width ="450">

Donde la densidad espectral antes del ruido es la señal limpia y la señal espectral despues es la señal pues efectivamente con ruido.

# punto 5
Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.


Se obtuvieron buenos resultados ya que se demoduladoron todos los bits con todos los SNR.  


Entonces para este punto podemos ver que para cualquier SNR en el rango solicitado que, el error es: 0 y el BER es 0. 

# punto 6
La gráfica de la relación entre BER y SNR es


<img src=".../master/graf6" width ="450">
