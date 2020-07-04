# tarea4



# punto 1
Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.


Entonces se tiene lo siguiente:


<img src="https://render.githubusercontent.com/render/math?math=A*cos[2\pi ft + \phi] ">

El enunciado nos pide que usemos seno entonces:


<img src="https://render.githubusercontent.com/render/math?math=A*sen[2\pi ft + \phi] ">

ver graf2 para la modulación


ver graf1 para la onda portadora

# punto 2
Calcular la potencia promedio de la señal modulada generada.


La potencia promedio es : 0.4900009800999702 W

# punto 3

Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.
Para este punto es importante tomar en cuenta que el ruido fue generado de manera aleatoria y con una distrinución normal. Las maginitudes que se obtuvieron se le agregaron a la señal modulada.



Para este punto podemos ver las imagenes graf -2,graf -1,graf 0,graf 1,graf 2,graf 3

# punto 4
Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.


Para este punto ver las imagenes graf 4 y graf 5

# punto 5
Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.


Se obtuvieron buenos resultados ya que se demoduladoron todos los bits con todos los SNR.  


Entonces para este punto podemos ver que para cualquier SNR en el rango solicitado que, el error es: 0 y el BER es 0. 

# punto 6
La gráfica de la relación entre BER y SNR es graf6
