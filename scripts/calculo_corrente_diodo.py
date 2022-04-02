import numpy as np
import math

# --------------------- Valores
Vd = None
n = 1.45 #1.45
Vt = 0.025852
Id = None
Is = 76.9e-12

if Vd is None:
    if Id is None:
        print("Preciso da Corrente no Diodo!")
    else:
        Vd = n*Vt*np.log(Id/Is)
        print(f'A tensão no diodo é de {Vd} V')
elif Id is None:
    if Vd is None:
        print("Preciso da Tensão no Diodo!")
    else:
        Id = Is*pow(math.e,(Vd/(n*Vt)))
        print(f'A corrente no diodo é de {Id} V')