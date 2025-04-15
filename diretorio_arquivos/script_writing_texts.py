import os

def tranfer_texts(arquivo_origem, arquivo_destino):
    try:
        with open(arquivo_origem, 'r', encoding='utf-8') as file_origem:
            conteudo = file_origem.read();
    except FileNotFoundError:
        print(f'Arquivo {arquivo_origem} não encontrado!')
        return
    except PermissionError:
        print(f'Sem permissão para acessar o arquivo {arquivo_origem}')
        return
    except Exception as e:
        print(f'Erro inesperado ao ler o arquivo {arquivo_origem}', e)
        return
    try:
        with open(arquivo_destino, 'w' , encoding='utf-8') as file_destino: 
            file_destino.write('Cabeçalho: Conteúdo do Arquivo de Destino\n')
            file_destino.write(conteudo)
            print(f'Conteúdo escrito com Sucesso em {arquivo_destino}')
    except PermissionError:
        print(f'Sem permissões para acessar o arquivo {arquivo_destino}.')
        return
    except Exception as e:
        print(f'Erro desconhecido ao acessar o arquivo {arquivo_destino}', e)
        return

def main():
    directory_files = "dir1"
    arquivo_origem = os.path.join(directory_files, 'arquivo_origem1.txt')
    arquivo_destino = os.path.join(directory_files, 'arquivo_destino.txt')
    tranfer_texts(arquivo_origem, arquivo_destino)  

if __name__ == "__main__":
    main()