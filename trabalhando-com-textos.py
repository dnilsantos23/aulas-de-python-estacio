arquivoTeste = open('teste.txt', 'w')
arquivoTeste.write('Esse é um teste de escrita em arquivo.\n')
arquivoTeste.write('Essa é a segunda linha do arquivo.\n')
with open('teste.txt', 'r') as arquivoTeste:
    conteudo = arquivoTeste.read()
    print(conteudo)
