

resultados = []
dados = open("dadosvibracoes.txt", "r")

linhas = dados.readlines()[1:]
dados.close()

for linha in linhas:
    fields = linha.split()

    frequencia = float(fields[0])
    vv = float(fields[1])
    hh = float(fields[2])

    todos = [frequencia, vv, hh]
    resultados.append(todos)

dados = open('dadosvibracoes.txt', 'r')

