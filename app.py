from PIL import Image
import os
import cv2
from PIL import Image

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

def video_to_gif(input_path, output_path, start_time=0, end_time=None, resize_height=None, optimize_palette=True):
    """
    Converte um vídeo em GIF com qualidade aprimorada.
    
    :param input_path: Caminho do vídeo de entrada
    :param output_path: Caminho do arquivo de saída GIF
    :param start_time: Tempo de início em segundos
    :param end_time: Tempo de término em segundos
    :param resize_height: Altura desejada do GIF (mantendo proporção)
    :param optimize_palette: Se True, otimiza a paleta de cores para melhor qualidade
    """
    try:
        # Abrir o vídeo com OpenCV
        video = cv2.VideoCapture(input_path)
        fps = int(video.get(cv2.CAP_PROP_FPS))
        frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        # Calcular os frames de início e fim
        start_frame = int(start_time * fps)
        end_frame = int(end_time * fps) if end_time else total_frames

        # Ajustar altura se resize_height foi fornecido
        if resize_height:
            scale = resize_height / frame_height
            frame_width = int(frame_width * scale)
            frame_height = resize_height

        # Iterar pelos frames e coletar imagens
        frames = []
        current_frame = 0
        while video.isOpened():
            ret, frame = video.read()
            if not ret or current_frame > end_frame:
                break

            if current_frame >= start_frame:
                # Redimensionar frame se necessário
                if resize_height:
                    frame = cv2.resize(frame, (frame_width, frame_height))

                # Converter BGR para RGB (necessário para Pillow)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frames.append(Image.fromarray(frame))

            current_frame += 1

        video.release()

        # Salvar as imagens como GIF
        if frames:
            frames[0].save(
                output_path,
                save_all=True,
                append_images=frames[1:],
                duration=int(1000 / fps),
                loop=0,
                optimize=optimize_palette  # Corrigido: parâmetro corretamente utilizado
            )
            print(f"GIF criado com sucesso: {output_path}")
        else:
            print("Nenhum frame encontrado no intervalo especificado.")

    except Exception as e:
        print(f"Erro ao converter vídeo para GIF: {e}")
# Exemplo de uso da função
input_video = rf"C:\TRANSFORMER_PHOTOS_IN_GIF\assets\webm\Macbook-Air-10.71.201.251-wcsa99nr-gugf6.webm"
output_gif = rf"C:\TRANSFORMER_PHOTOS_IN_GIF\assets\gif\output_vidio.gif"

# Exemplo de uso:
image_paths = [
    rf"C:\TRANSFORMER_PHOTOS_IN_GIF\assets\png\img_1.png", 
    rf"C:\TRANSFORMER_PHOTOS_IN_GIF\assets\png\img_2.png", 
    rf"C:\TRANSFORMER_PHOTOS_IN_GIF\assets\png\img_3.png"
]
output_gif_path = rf"C:\TRANSFORMER_PHOTOS_IN_GIF\assets\gif\output.gif"  


if __name__ == "__main__":
    # create_gif(image_paths, output_gif_path)
    video_to_gif(input_video, output_gif, start_time=0, end_time=10, resize_height=720, optimize_palette=True)
