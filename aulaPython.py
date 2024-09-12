

f= open("leituraArquivo.txt", "r")

dados_arquivos = f.read()

f.close()
print("Informações da leitura do arquivo")
print(dados_arquivos)

#dados = [1.6, 3.4, 5.5, 9.4]
#
#f= open("dadosExemplo2Criar.txt", "a")

#for valor in dados:
#    grava = str(valor * 2)
#    f.write(grava)
#    f.write("\n")

#f.close()