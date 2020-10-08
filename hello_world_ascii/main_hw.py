# pip install pyfiglet

# Bibliotecas utilizadas
import os
import pyfiglet as pyf
from time import sleep

# Números que serão utilizados na formatação das cores;
# Estrutura: \x1b[style;bg;fgm' | Exemplo → \x1b[0;0;31m' → Vermelho.
style = bg = 0  # Estilo, Background (zerados como padrão)
colors = [30, 90, 31, 91, 32, 92, 33, 93, 34, 94, 35, 95, 36, 96, 37, 97] # Foreground

# Alterando uma String comum para um ASCII Art.
banner = 'Hello World'
custom_fig = pyf.Figlet(font='big')
banner_format = custom_fig.renderText(banner)

# Execução
while True:
    for fg in colors:
        os.system('cls')    # Limpa o console
        color = '\x1b[' + (';'.join([str(style), str(bg), str(fg)])) + 'm'
        reset = '\x1b[0m'
        print(color, end='')    # Seta uma cor
        print(banner_format, end='')    # Printa a mensagem
        print(reset)    # Reseta cor
        sleep(1)    # Espera 1 seg
