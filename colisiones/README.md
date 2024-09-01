# Conteo de Colisiones de Robots

Este proyecto implementa una función para contar las colisiones de robots en una secuencia dada.

## Descripción del Problema

- Secuencia de Robots: Cada robot está representado por 'R' (derecha) o 'L' (izquierda).
- Distancia Inicial: La distancia inicial entre cada par de robots adyacentes es de 2 metros.
- Colisiones: Cuando dos robots se encuentran (uno moviéndose hacia la derecha y otro hacia la izquierda), ambos cambian de dirección instantáneamente.
- Espacio Infinito: Los robots pueden moverse indefinidamente en cualquier dirección.
- Objetivo: Contar cuántas veces colisiona cada robot en la secuencia.

## Implementación

La función `contar_colisiones(movimientos)` simula el movimiento de los robots y cuenta las colisiones. El algoritmo sigue estos pasos:

1. Inicializa las posiciones y direcciones de los robots.
2. Simula el movimiento de los robots en pasos discretos.
3. Detecta y maneja las colisiones, actualizando las direcciones y el conteo de colisiones.
4. Continúa la simulación hasta que no haya más colisiones posibles.

## Los casos de prueba incluyen:

Ejemplos básicos ('LR', 'RL', 'RRR', 'RRL')
Casos sin colisiones ('LLL', 'RRRR')
Casos con múltiples colisiones ('RLRLRL', 'RLRL', 'RLLR')

## Ejecución de las Pruebas

```python
python -m unittest test_colisiones.py
```

#### Analsis de movimientos de ejemplo

### Revisión del Caso 'RRL'
El caso 'RRL' debería procesarse de la siguiente manera:

Estado inicial: 'RRL'

R1 (primer robot) se mueve hacia la derecha.
R2 (segundo robot) también se mueve hacia la derecha.
L1 (tercer robot) se mueve hacia la izquierda.
R1 y R2 no colisionan porque ambos se mueven en la misma dirección.
R2 y L1 colisionan, lo que da como resultado el estado 'RLR' y las colisiones [0, 1, 1].
Segundo estado: 'RLR'

R1 ahora colisiona con L1.
Ambos cambian de dirección, resultando en 'LRR'.
Se actualizan las colisiones: [1, 2, 1].
Estado final: 'LRR'

En este estado, no ocurren más colisiones, ya que L1 se mueve a la izquierda y R1 y R2 se mueven a la derecha.
El conteo final de colisiones es [1, 2, 1].


### Revisión del Caso 'RLRL' (Nota: R=Right y L=Left)
El caso 'RLRL' debería procesarse de la siguiente manera:

Estado inicial: 'RLRL'

R1 (primer robot) se mueve hacia la derecha.
L1 (segundo robot) se mueve hacia la izquierda.
R2 (tercer robot) se mueve hacia la derecha.
L2 (tercer robot) se mueve hacia la izquierda.

R1 y L1 colisionan, ambos cambian de dirección, lo que da como resultado el estado 'LRRL' conteo: [1,1,0,0]

Segundo estado: 'LRRL'
R2 y L2 colisionan, ambos cambian de dirección, lo que da como resultado el estado 'LRLR' conteo: [1,1,1,1].

Tercer estado: 'LRLR'
R1 ahora colisiona con L2, ambos cambian de dirección, lo que da como resultado el estado 'LLRR' conteo: [1,2,2,1].

Estado final: 'LLRR'. En este estado, no ocurren más colisiones, ya que L1 y L2 se mueve a la izquierda y R1 y R2 se mueven a la derecha.
El conteo final de colisiones es [1, 2, 2, 1].

### Revisión del Caso 'RLLR'
 RLLR [1,1,0,0]
 LRLR [1,2,1,0]
 LLRR

### Revision del caso 'RLRLRL'
'RLRLRL' [0,0,0,0,0,0]
'RLRLRL' [1,1,0,0,0,0]
'LRRLRL' [1,1,1,1,0,0]
'LRLRRL' [1,2,2,1,0,0]
'LLRRRL' [1,2,2,1,1,1]
'LLRRLR' [1,2,2,2,2,1]
'LLRLRR' [1,2,3,3,2,1]
'LLLRRR' [1,2,3,3,2,1]
 
## Función contar_colisiones(movimientos)

La función `contar_colisiones(movimientos)` toma una cadena de caracteres que representa la dirección de movimiento de los robots (`R` para derecha y `L` para izquierda) y devuelve una lista con el conteo de colisiones para cada robot.



