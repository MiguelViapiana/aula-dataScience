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
    def probabilidade_z(z):
        return stats.norm.cdf(z)

    #Calcula a covariância entre a amostra atual e outra amostra.
    def covariancia(self, outra_amostra):

        outra_amostra = np.array(outra_amostra)
        if len(outra_amostra) != self.n:
            raise ValueError("As duas amostras devem ter o mesmo tamanho.")

        cov = np.cov(self.amostra, outra_amostra)[0, 1]
        return cov
