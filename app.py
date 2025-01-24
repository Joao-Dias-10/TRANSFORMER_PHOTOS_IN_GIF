from PIL import Image
import os

def create_gif(image_paths, output_path, duration=2000):
    try:
        # Validar se todos os caminhos são válidos
        if not all(os.path.isfile(path) for path in image_paths):
            raise ValueError("Um ou mais caminhos de imagem são inválidos.")
        
        # Abrir as imagens
        images = [Image.open(img_path) for img_path in image_paths]
        
        # Criar o GIF
        images[0].save(
            output_path, 
            save_all=True, 
            append_images=images[1:], 
            duration=duration, 
            loop=0  # O GIF vai se repetir indefinidamente
        )
        print(f"GIF criado com sucesso: {output_path}")
    
    except Exception as e:
        print(f"Erro ao criar GIF: {e}")

# Exemplo de uso:
image_paths = [
    rf"C:\TRANSFORMER_PHOTOS_IN_GIF\assets\png\img_1.png", 
    rf"C:\TRANSFORMER_PHOTOS_IN_GIF\assets\png\img_2.png", 
    rf"C:\TRANSFORMER_PHOTOS_IN_GIF\assets\png\img_3.png"
]
output_gif_path = "output.gif"  


if __name__ == "__main__":
    create_gif(image_paths, output_gif_path)
