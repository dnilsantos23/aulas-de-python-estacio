import os

def listar_arquivos(diretorio): 
    arquivos_encontrados = [] # Lista para armazenar os caminhos completos dos arquivos encontrados

    for raiz, diretorios, arquivos in os.walk(diretorio): # Percorre o diretório e subdiretórios
        for arquivo in arquivos: # Para cada arquivo encontrado
            caminho_completo = os.path.join(raiz, arquivo) # Cria o caminho completo do arquivo
            arquivos_encontrados.append(caminho_completo) # Adiciona o caminho completo à lista

    return arquivos_encontrados # Retorna a lista de arquivos encontrados


arquivoTexto = open('praticando-em-python.txt', 'w+') # Abre o arquivo 'arquivos.txt' para escrita
arquivoTexto.write('Arquivos encontrados novo:\n') # Escreve o cabeçalho no arquivo
arquivoTexto.seek(0) # Move o cursor para o início do arquivo
arquivoTexto.write(str(listar_arquivos('C:/PYTHON-PROJECTS'))) # Escreve os arquivos encontrados no arquivo de texto
print(arquivoTexto.readlines()) # Lê o conteúdo do arquivo e imprime na tela
arquivoTexto.close() # Fecha o arquivo