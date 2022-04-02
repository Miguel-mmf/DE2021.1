import numpy as np
import math

print("Diodo 1N4007")


# --------------------- Tensão de Alimentação
Vfonte1 = 1.1
Vfonte2 = 2.1

# --------------------- Resistencia Serie com o Diodo
R = 1000

# --------------------- Tensão nos Diodos
Vd1 = 0.589
Vd2 = 0.629

# --------------------- Tensão Térmica
Vt = 0.025852

def calc_coeficiente_emissao(Vd1,Vd2,R,Vfonte1,Vfonte2):
  Id1 = (Vfonte1 - Vd1)/R
  Id2 = (Vfonte2 - Vd2)/R
#   print(Id1," --- ",Id2)
  if Vd1 > Vd2:
    return ((Vd1-Vd2)/(Vt*(np.log(Id1/Id2))))
  else:
    return ((Vd2-Vd1)/(Vt*(np.log(Id2/Id1))))

n = calc_coeficiente_emissao(Vd1,Vd2,R,Vfonte1,Vfonte2)
print(f'Coeficiente de Emissao: {n}')
print(f'Coeficiente de Emissao - 20%: {n*0.8}')
print(f'Coeficiente de Emissao + 20%: {n*1.2}')

def calc_corrente_saturacao(Vd1,Vd2,R,Vfonte1,Vfonte2,ValorN):
  Id1 = ((Vfonte1 - Vd1)/R)
  Id2 = (Vfonte2 - Vd2)/R

  Is1 = (Id1/(pow(math.e,(Vd1/(ValorN*Vt)))))
  Is2 = (Id2/(pow(math.e,(Vd2/(ValorN*Vt)))))

#   print(f'Is1: {Is1} ou {np.format_float_scientific(Is1, precision = 4)}')
#   print(f'Is2: {Is2} ou {np.format_float_scientific(Is2, precision = 4)}')
#   print(f'Diferenca: {Is1-Is2}\n')

  return Is1

Is = calc_corrente_saturacao(Vd1,Vd2,R,Vfonte1,Vfonte2,n)
print(f'Corrente de Satuação: {Is}')
print(f'Corrente de Satuação * 0.1: {Is*0.1}')
print(f'Corrente de Satuação * 10: {Is*10}')