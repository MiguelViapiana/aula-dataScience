import numpy as np
import scipy.stats as stats

class Estatistica:
    def __init__(self, amostra):
        self.amostra = np.array(amostra)
        self.n = len(self.amostra)
        self.media =np.mean(self.amostra)
        self.desvio_padrao = np.std(self.amostra, ddof=1)

    #Calcular o valor de Z utilizando o Teorema Central do Limite
    def calcular_z(self, valor):

        erro_padrao = self.desvio_padrao / np.sqrt(self.n)
        z = (valor - self.media) / erro_padrao
        return z

    #Calcula a probabilidade acumulada para um valor Z usando a distribuição normal padrão.
    def probabilidade_z(self, z):
        return stats.norm.cdf(z)

