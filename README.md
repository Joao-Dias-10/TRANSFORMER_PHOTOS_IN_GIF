# GIF Creator

Este projeto permite criar um GIF a partir de uma série de imagens, com um intervalo configurável entre elas. O código foi feito em Python usando a biblioteca [Pillow](https://pillow.readthedocs.io/), que é uma das bibliotecas mais populares para processamento de imagens.

## Descrição

Esse código simples me ajudou a juntar várias imagens em um único GIF animado. Ele recebe uma lista de caminhos de imagens e cria um GIF, exibindo uma imagem por vez com um intervalo de tempo especificado (por padrão, 2 segundos).

É útil quando você tem várias imagens e deseja criar uma animação sem perder qualidade.

## Funcionalidade

- O código carrega imagens de arquivos locais.
- Cria um GIF a partir dessas imagens com a capacidade de definir o intervalo entre elas.
- Utiliza o Pillow para manipulação de imagens e criação do GIF.

## Como Usar

1. **Instale as dependências**:
   Para usar esse código, você precisa da biblioteca Pillow. Você pode instalá-la com o pip:

   ```bash
   pip install pillow
