import numpy as np

anos = [
    1872, 1890, 1900, 1920, 1940,
    1950, 1960, 1970, 1980, 1991,
    2000, 2010, 2022
]

populacoes = [
    9930478, 14333915, 17438434, 30635605, 41236315,
    51944397, 70992343, 94508583, 121150573, 146917459,
    169872856, 190755799, 203080756
]

#Mediana da populações

n = len(populacoes)
meio = n // 2
if meio % 2 == 0:
    mediana = populacoes[meio]
else:
    mediana = (populacoes[meio - 1] + populacoes[meio]) / 2

print("A mediana da lista de populações é {}".format(mediana))


#Desvio padrão

desvio_padrao = np.std(populacoes)

print("O desvio padrão é {:.2f}".format(desvio_padrao))

