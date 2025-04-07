from datetime import datetime

arquivoTeste = open('teste.txt', 'w')
arquivoTeste.write('Esse é um teste de escrita em arquivo.\n')
arquivoTeste.write('Essa é a segunda linha do arquivo.\n')
with open('teste.txt', 'r') as arquivoTeste:
    conteudo = arquivoTeste.read()
    print(conteudo)

nome = 'Ellen Mikaella do Prado Severo'
idade = 32
mensagem = f'Meu nome é {nome} e minha idade é {idade} anos'
pi = 3.1416
print(mensagem)
print(f'O valor da variável PI é {pi:.2f}')
hoje = datetime.now() 
data_formatada = hoje.strftime('Data: %d/%m/%y') 
print(hoje)
print(data_formatada)
