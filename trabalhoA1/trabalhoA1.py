import numpy as np
import scipy.stats as stats
from scipy.stats import norm

from aulaPython01.leituraExcel import desvio_padrao


def intervalo_confianca(media_amostral, desvio_padrao_amostral, n, confianca=0.95):
    """
    Calcula o intervalo de confiança para a média de uma população normal com variância desconhecida.
    """
    alfa = 1 -confianca
    t_critico = stats.t.ppf(1 - alfa/ 2, df=n -1)
    erro_padrao = desvio_padrao_amostral / np.sqrt(n)
    margem_erro = t_critico * erro_padrao

    limite_inferior = media_amostral - margem_erro
    limite_superior = media_amostral + margem_erro

    return limite_inferior, limite_superior


def teste_hipotese(media_amostral, media_hipotetica, desvio_padrao_amostral, n, alfa=0.05, tipo='bilateral'):
    """
    Realiza o teste de hipótese para a média de uma população normal com variância desconhecida.
    """
    t_calculado = (media_amostral - media_hipotetica) / (desvio_padrao_amostral / np.sqrt(n))
    df = n - 1

    if tipo == 'bilateral':
        t_critico = stats.t.ppf(1 - alfa / 2, df=df)
        p_valor = (1 - stats.t.cdf(abs(t_calculado), df=df)) * 2
        rejeitar_h0 = abs(t_calculado) > t_critico
    elif tipo == 'cauda_esquerda':
        t_critico = stats.t.ppf(alfa, df=df)
        p_valor = stats.t.cdf(t_calculado, df=df)
        rejeitar_h0 = t_calculado < t_critico
    elif tipo == 'cauda_direita':
        t_critico = stats.t.ppf(1 - alfa, df=df)
        p_valor = 1 - stats.t.cdf(t_calculado, df=df)
        rejeitar_h0 = t_calculado > t_critico
    else:
        raise ValueError("Tipo de teste deve ser 'bilateral', 'cauda_esquerda' ou 'cauda_direita'.")

    return t_calculado, t_critico, p_valor, rejeitar_h0


def teste_diferenca_medias(x1, x2, alfa=0.05):
    """
    Testa a diferença entre duas médias de amostras independentes.
    """

    n1, n2 =len(x1), len(x2)
    media1, media2 = np.mean(x1), np.mean(x2)
    var1, var2 =np.var(x1, ddof=1), np.var(x2, ddof=1)

    erro_padrao = np.sqrt(var1/n1 + var2/n2)

    t_calculado = (media1 - media2) / erro_padrao

    df = ((var1/n1 + var2/n2)**2) / (((var1/n1)**2 /(n1-1)) + ((var2/n2)**2 / (n2-1)))

    t_critico = stats.t.ppf(1 - alfa/2, df)
    p_valor = (1 - stats.t.cdf(abs(t_calculado), df)) * 2

    rejeitar_h0 = abs(t_calculado) > t_critico

    return t_calculado, t_critico, p_valor, rejeitar_h0

def intervalo_confianca_variancia(x, alfa=0.05):
    """
    Calcula o intervalo de confiança para a variância de uma população normal.
    """
    n = len(x)
    s2 = np.var(x, ddof=1)
    chi2_inf = stats.chi2.ppf(1- alfa/ 2, df=n - 1)
    chi2_sup = stats.chi2.ppf(alfa/2, df=n - 1)

    limite_inferior = (n - 1) * s2/ chi2_inf
    limiere_superior = (n - 1) * s2/ chi2_sup

    return limite_inferior, limiere_superior

def teste_hipotese_variancia(x, sigma0_2, alfa=0.05, tipo='bilateral'):
    """
    Realiza o teste de hipótese para a variância de uma população normal.
    """

    n = len(x)
    s2 = np.var(x, ddof=1)
    chi2_calculado = (n - 1) * s2 / sigma0_2
    df = n- 1

    if tipo == 'bilateral':
        chi2_critico_inf = stats.chi2.ppf(alfa / 2, df)
        chi2_critico_sup = stats.chi2.ppf(1 - alfa / 2, df)
        rejeitar_h0 = chi2_calculado < chi2_critico_inf or chi2_calculado > chi2_critico_sup
        return chi2_calculado, (chi2_critico_inf, chi2_critico_sup), rejeitar_h0
    elif tipo == 'cauda_esquerda':
        chi2_critico = stats.chi2.ppf(alfa, df)
        rejeitar_h0 = chi2_calculado < chi2_critico
        return chi2_calculado, chi2_critico, rejeitar_h0
    elif tipo == 'cauda_direita':
        chi2_critico = stats.chi2.ppf(1 - alfa, df)
        rejeitar_h0 = chi2_calculado > chi2_critico
        return chi2_calculado, chi2_critico, rejeitar_h0
    else:
        raise ValueError("Tipo de teste deve ser 'bilateral', 'cauda_esquerda' ou 'cauda_direita'.")

    return chi2_calculado, chi2_critico, rejeitar_h0


def probabilidade_media_acima(media_populacional, desvio_padrao_populacional, n, media_amostra):
    """
    Calcula a probabilidade de a média de uma amostra ser superior a um valor específico
    usando o Teorema Central do Limite.

    Parâmetros:
    - media_populacional: Média da população (float)
    - desvio_padrao_populacional: Desvio padrão da população (float)
    - n: Tamanho da amostra (int)
    - media_amostra: Média da amostra para a qual queremos calcular a probabilidade (float)

    Retorna:
    - Valor de Z
    - Probabilidade de a média amostral ser superior a 'media_amostra'
    """
    # Calcular o erro padrão da média
    erro_padrao = desvio_padrao_populacional / np.sqrt(n)

    # Calcular o valor de Z
    z = (media_amostra - media_populacional) / erro_padrao

    # Calcular a probabilidade de Z ser maior que o valor calculado
    probabilidade = 1 - norm.cdf(z)

    return z, probabilidade

media_populacional = 10  # Média da população em minutos
desvio_padrao_populacional = 2  # Desvio padrão da população em minutos
n = 36  # Tamanho da amostra
media_amostra = 11  # Média para a qual queremos calcular a probabilidade

# Chamando a função
z, probabilidade = probabilidade_media_acima(media_populacional, desvio_padrao_populacional, n, media_amostra)

print(f"Valor de Z: {z}")
print(f"Probabilidade de que a média da amostra seja maior que 11 minutos: {probabilidade:.4f}")
