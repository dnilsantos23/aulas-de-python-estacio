
from PIL import Image # Importa a biblioteca PIL (Python Imaging Library) para manipulação de imagens
import numpy as np # Importa a biblioteca NumPy para manipulação de arrays
#import sys # Importa o módulo sys para acessar variáveis e funções do sistema
#print(sys.executable) # Imprime o caminho do executável do Python para resolver problemas de importação de bibliotecas


def main():
    #carregar a imagem original
    img = Image.open('imagem.jpg')
    img.show() # Exibe a imagem original

    #converter a imagem em dados binários
    imgdata = np.array(img) # Converte a imagem em um array NumPy
    bynary_data = imgdata.tobytes() # Converte o array em dados binários

    #salvar os dados binários em um arquivo
    with open('original_img.bin', 'wb') as file: # Abre o arquivo 'imagem.bin' para escrita em modo binário
        file.write(bynary_data) # Escreve os dados binários no arquivo

    #copiar o arquivo binário
    with open('original_img.bin', 'rb') as original_file:
        data = original_file.read() # Lê os dados binários do arquivo original
    
    with open('copia_img.bin', 'wb') as copy_file: # Abre o arquivo 'copia_img.bin' para escrita em modo binário
        copy_file.write(data)
    
    #Manipulação dos dados do arquivo binário cópia
    #Exemplo de manipulação: inverter os bytes
    with open('copia_img.bin', 'rb') as file: # Abre o arquivo 'copia_img.bin' para leitura em modo binário
        data = bytearray(file.read()) # Lê os dados binários do arquivo e os armazena em um objeto bytearray

    data = data[::-1] # Inverte os bytes do objeto bytearray
    
    with open('copia_img.bin', 'wb') as file: # Abre o arquivo 'copia_img.bin' para escrita em modo binário
        file.write(data) # Escreve os dados binários manipulados no arquivo
    
    #carregar e mostrar a imagem manipulada
    # Converte os dados binários manipulados de volta para um array NumPy com a mesma forma da imagem original
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(imgdata.shape) 
    modified_img = Image.fromarray(modified_data) # Converte o array NumPy de volta para uma imagem
    modified_img.show() # Exibe a imagem manipulada

if __name__ == "__main__":
    main() # Chama a função principal para executar o código