import sys
from time import sleep
import time
from colorama import init

# 1. Inicializa o colorama. Tenta forçar a compatibilidade ANSI (necessário no Windows).
# Se as cores de 256 bits não aparecerem, é devido à limitação do seu terminal (mude para o Windows Terminal).
init() 

def apply_gradient(text):
    """
    Aplica um gradiente de cores ao texto fornecido (tons de Vermelho/Laranja de 256 bits).
    
    Args:
        text (str): Texto que receberá o efeito de gradiente
    
    Returns:
        str: Texto com códigos ANSI para as cores do gradiente
    """
    # Define a paleta de cores do gradiente (tons de vermelho e laranja, códigos 256 bits)
    colors = [
        "\033[38;5;88m",    # vermelho escuro (88)
        "\033[38;5;130m",   # laranja avermelhado (130)
        "\033[38;5;94m",    # laranja (94)
        "\033[38;5;136m",   # laranja médio (136)
        "\033[38;5;166m",   # laranja escuro (166)
        "\033[38;5;202m",   # vermelho alaranjado (202)
        "\033[38;5;124m",   # vermelho (124)
        "\033[38;5;196m",   # vermelho vivo (196)
    ]
    
    gradient_text = ""
    for i, char in enumerate(text):
        # Seleciona a cor baseado na posição do caractere (looping pela paleta)
        color = colors[i % len(colors)]
        gradient_text += color + char
        gradient_text += "\033[0m"  # Reseta a cor após cada caractere
    
    return gradient_text

def print_lyrics():
    """
    Imprime a letra da música com efeitos especiais (typing effect e gradiente).
    - Exibe caractere por caractere com intervalos variáveis.
    - Aplica gradiente na palavra "----".
    - Pausas personalizadas após cada linha para simular o ritmo.
    """
    # linha da letra, intervalo entre caracteres
    lines = [
        ("Got the music in you, baby", 0.08), 
        ("tell me why", 0.08), 
        ("Got the music in you, baby", 0.08),
        ("tell me why", 0.08),
        ("You've been locked in here forever", 0.05), 
        ("And you just can't say goodbye", 0.09), 
        ("Your lips, my lips", 0.09),
        ("Apocalypse", 0.009),  # Intervalo rápido para efeito especial
        ("Your lips, my lips", 0.09),
        ("Apocalypse", 0.009)
    ]

    # Intervalos após cada linha (em segundos)
    delays = [0.1, 2, 0.3, 2, 0.2, 6.6, 1.2, 6.4, 1.2, 5]

    for i, (line, char_delay) in enumerate(lines):
        # Aplica gradiente apenas na palavra-chave
        if "Apocalypse" in line:
            line = line.replace("Apocalypse", apply_gradient("Apocalypse"))
        
        # Imprime cada caractere com um pequeno atraso
        for char in line:
            print(char, end='')
            sys.stdout.flush()  # Garante que o caractere seja exibido imediatamente
            sleep(char_delay)   # Pausa entre caracteres
        
        time.sleep(delays[i])   # Pausa mais longa após a linha completa
        print() # Quebra de linha


# Inicia a animação das letras
if __name__ == "__main__":
    try:
        print_lyrics()
    except KeyboardInterrupt:
        # Permite que o usuário saia pressionando Ctrl+C
        print("\nAnimação interrompida.")