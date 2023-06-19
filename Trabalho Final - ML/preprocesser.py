from PIL import Image
import os

class PreProcesser:
    """
    Classe que encapsula a lógica de redimensionamento das imagens. O construtor da classe recebe os caminhos das 
    pastas de entrada e saída, bem como a dimensão desejada para redimensionamento. O método `resize_images()` é responsável por 
    iterar sobre os arquivos da pasta de entrada, redimensionar as imagens e salvá-las na pasta de saída.
    
    """
    def __init__(self, 
                input_folder : str , 
                output_folder : str , 
                dim : int):
        
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.dim = dim
        self.__resize_images()

    def __resize_images(self) -> None:
        """
        Itera sobre os arquivos da pasta de entrada, redimensiona as imagens e salva na pasta de saída.
        """

        # Lista todos os arquivos da pasta de entrada
        files = os.listdir(self.input_folder)

        for filename in files:
            if filename.endswith(".jpg"):
                # Abre a imagem original
                img_path = os.path.join(self.input_folder, filename)
                img = Image.open(img_path)

                # Redimensiona a imagem
                img = img.resize((self.dim, self.dim), Image.ANTIALIAS)

                # Salva a imagem redimensionada na pasta de saída
                output_path = os.path.join(self.output_folder, filename)
                img.save(output_path)

# Caminhos das pastas de entrada e saída
input_folder = "/content/drive/MyDrive/caminho/para/pasta_de_imagens/"
output_folder = "/content/drive/MyDrive/caminho/para/pasta_de_saida/"

# Dimensão desejada para redimensionamento
dim = 128

# Instanciar e usar a classe ImageResizer
resizer = PreProcesser(input_folder, output_folder, dim)
resizer.resize_images()
