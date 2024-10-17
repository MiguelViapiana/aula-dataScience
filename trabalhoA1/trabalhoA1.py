import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


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

    #Plota a distribuição das médias amostrais para visualizar o Teorema Central do Limite.
    def plotar_tcl(self, n_amostras, tamanho_amostra):

        media = []

        for _ in range(n_amostras):
            amostra =np.random.choice(self.amostra, tamanho_amostra, replace=True)
            media.append(np.mean(amostra))

        media_das_medias = np.mean(media)
        desvio_padrao_das_medias = np.std(media, ddof=1)

        x = np.linspace(media_das_medias - 4 * desvio_padrao_das_medias,
                        media_das_medias + 4 * desvio_padrao_das_medias, 100)
        y = stats.norm.pdf(x, media_das_medias, desvio_padrao_das_medias)

        #Plotar
        plt.figure(figsize=(10, 6))
        plt.hist(media, bins=30, density=True, alpha=0.6, color='g', label='Distribuição das Médias Amostrais')
        plt.plot(x, y, 'k', linewidth=2, label='Distribuição Normal Ajustada')
        plt.title('Teorema Central do Limite')
        plt.xlabel('Média Amostral')
        plt.ylabel('Densidade')
        plt.legend()
        plt.grid()
        plt.show()


    #Calcula a covariância entre a amostra atual e outra amostra.
    def covariancia(self, outra_amostra):

        outra_amostra = np.array(outra_amostra)
        if len(outra_amostra) != self.n:
            raise ValueError("As duas amostras devem ter o mesmo tamanho.")

        cov = np.cov(self.amostra, outra_amostra)[0, 1]
        return cov

# Exemplo de uso
if __name__ == "__main__":
    amostra = [10, 12, 23, 23, 16, 23, 21]
    estatistica = Estatistica(amostra)
    estatistica.plotar_tcl(n_amostras=1000, tamanho_amostra=30)
