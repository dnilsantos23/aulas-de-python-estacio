def main(): 
    print('Digite suas frases. Para sair, digite "sair".') # Solicita ao usuário que digite frases
    frases = []
    while True:
        entrada = input(">") # Lê a entrada do usuário
        if entrada.lower() == "sair": # Verifica se o usuário digitou "sair" em minusculo através do método lower()
             break # Encerra o loop se o usuário digitar "sair"
        frases.append(entrada) # Adiciona a frase à lista de frases
    with open("meu_arquivo.txt", "w", encoding='utf-8' ) as arquivo: # Abre o arquivo 'meu_arquivo.txt' para escrita
        for frase in frases: # Para cada frase na lista de frases
            arquivo.write(frase + "\n") # Escreve a frase no arquivo, adicionando uma nova linha após cada frase

    print("Frases escritas no arquivo meu_arquivo.txt com sucesso! Agora vamos manipular os dados!")    
    dados_modificados = [] # Lista para armazenar os dados modificados
    with open("meu_arquivo.txt", "r" , encoding='utf-8') as arquivo: # Abre o arquivo 'meu_arquivo.txt' para leitura
        # Lê o conteúdo do arquivo e armazena em uma lista
        for linha in arquivo: # Para cada linha no arquivo
            dados_modificados.append(linha.strip().upper()) # Adiciona a linha à lista de dados modificados, removendo espaços em branco e convertendo para maiúsculas
    with open("meu_arquivo.txt", "w", encoding='utf-8') as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")
    print("Dados modificados e reescritos no arquivo meu_arquivo.txt com sucesso!\n")
    arquivo = open("meu_arquivo.txt", "r", encoding='utf-8') # Abre o arquivo 'meu_arquivo.txt' para leitura
    print('\n\nSegue abaixo texto do arquivo "meu_arquivo.txt":\n', arquivo.readlines()) # Lê o conteúdo do arquivo e imprime na tela
    arquivo.close() # Fecha o arquivo após a leitura

if __name__ == "__main__":
    main()