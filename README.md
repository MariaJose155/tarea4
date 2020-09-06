# Tarea ILP
María José Arce Marín
B60561

Heillen Sosa

Darieth Fonseca

# Introducción
Para estudiar las decisiones de diseño necesarias para implementar la concurrencia ocasionada por el efecto superescalar y las consecuencias de pipelines más profundos. Entonces es de importancia generar una distinción entre front-end y back-end del pipeline.
Entonces el front-end tiene las etapas IF e ID que buscan y decodifican varias instrucciones al mismo tiempo. Ahora el back-end que tiene las estapas EX,Mem y WB que ejecutan y escriben varias instrucciones de manera simultanea.


# Conceptos importantes

** IPL (programación dinamica) propone: 

-El hardware reorganiza la ejecución de instrucciones.

-Es más poderoso que la programación estática (SW).

-Elimina el requerimiento de que las instrucciones se ejecuten en el orden del programa.

-Aprovechar el pipeline al máximo.

Se basa en dos enfoques:

A) Estático: basado en SW

Entonces tenemos lo siguiente

LOOP:

1.LD FO,0(R1)

2.ADD F4, F0, F2

3.SD F4,0(R1)

4.ADDIU R1,R1,#-8

5.BNE R1,R2,LOOP

Entonces notemos que en la linea 1 y 2 con la dependencia F0 se da un stall (se inserta una burbuja), en la linea 3 con la dependencia  F4 se da un stall y en la linea 4 y 5 con la dependencia R1 se da un stall.

Entonces podes se puede hacer el siguiente cambio:

1.LD FO,0(R1)

2.ADDIU R1,R1,#-8

3.ADD F4, F0, F2

4.SD F4,8(R1)

5.BNE R1,R2,LOOP

Donde el único stall se da en la linea 4 con F4.
Entonces se detentan dependencias simples en el codigo y se reordena para evitar burbujas.

B) Loop unralling: Aumentar el número de instrucciones relativas al branch para aumantar el número de instrucciones sobre las cuales se detecta paralelismo.

Entonces en general ILP:Entonces se detentan dependencias simples en el codigo y se reordena para evitar burbujas.

OOO (Ejecución fuera de orden):

-La ejecución de las operaciones inicia tan pronto sus operandos esten listos.
-El problema de la ejecución fuera de orden es que existe la posibilidad de introducir Hazards WAR y WAW que no existen en el pipeline con ejecución en orden.
-La solución a este problema es renombrar el registro, separar el concepto de registros de arquitectura y registros físicos.

Registros de Arquitectura:

Son los disponibles para el compilador. EL compilador no usa registros físicos porque hay N registros físicos y hay un límite de registros que la arquitectura nos permite exponer.

Registros físicos:

Son los registros en hardware donde se puede almacenar un valor.

Tabla RAT (register alias table):

Es una tabla donde se lleva el mapeo entre registros de arquitectura y registros físicos.

Tomasulo:

Es un algoritmo que permite ejecutar instrucciones fuera de orden.

-Emite las instrucciones en orden del procesador.

-Determina de donde vienen las operaciones (RF,RS).

-Obtiene una estacion de reserva.

-Etiqueta el registro destino.

Tomasulo(ciclos y restricciones):

-Capture y Dispath (típicamente no se realizan en el mismo ciclo)

-Issue y Dispath (típicamente no se realizan en el mismo ciclo)

-RAT-Write y Issue (observar el issue)

-Load y store(esto se realiza en orden)


# insertar ejemplo Tomasulo simple y luego uno más compicado ambos de un ciclo


<img src="https://render.githubusercontent.com/render/math?math=-Acos[2\pi ft] ">








