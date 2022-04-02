import numpy as np

diodo = '1N4007'

# --------------------- Valores

Vd = 0.79
n = 1.45 #1.45
Vt = 0.025852
Id = 0.0971
Is = 76.9e-12

valor_Rs = ((Vd - (n*Vt*np.log(Id/Is)))/Id)
print(f'Resistencia Serie do diodo {diodo}: {valor_Rs} ou {np.format_float_scientific(valor_Rs, precision = 4)}')
print(f'Resistencia Serie do diodo {diodo} + 0.5 Ohm: {valor_Rs+0.5}')
print(f'Resistencia Serie do diodo {diodo} - 0.5 Ohm: {valor_Rs-0.5}')