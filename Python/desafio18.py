"""import math
a = float(input('Digite um angulo: '))
s = math.sin(math.radians(a))
c = math.cos((math.radians(a)))
t = math.tan(math.radians(a))
print(f'O angulo de {a} tem o SENO de: {s:.2f}')
print(f'O angulo de {a} tem o COSSENO de: {c:.2f}')
print(f'O angulo de {a} tem a TANGENTE de: {t:.2f}')'"""

from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
print(f'O angulo de {angulo} tem o SENO de: {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O angulo de {angulo} tem o COSSENO de: {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} tem a TANGENTE de: {tangente:.2f}')

