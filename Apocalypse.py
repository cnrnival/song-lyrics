import sys
from time import sleep
import time

def apply_gradient(text):
    """
    Aplica um gradiente de cores ao texto fornecido
    
    Args:
        text (str): Texto que receberá o efeito de gradiente
    
    Returns:
        str: Texto com códigos ANSI para as cores do gradiente
    """
    # Define a paleta de cores do gradiente (tons de vermelho e laranja)
    colors = [
        "\033[38;5;88m",   # vermelho escuro
        "\033[38;5;130m",  # laranja avermelhado
        "\033[38;5;94m",   # laranja
        "\033[38;5;136m",  # laranja médio
        "\033[38;5;166m", # laranja escuro
        "\033[38;5;202m", # vermelho alaranjado
        "\033[38;5;124m", # vermelho
        "\033[38;5;196m", # vermelho vivo
    ]
    
    gradient_text = ""
    for i, char in enumerate(text):
        # Seleciona a cor baseado na posição do caractere
        color = colors[i % len(colors)]
        gradient_text += color + char
        gradient_text += "\033[0m"  # Reseta a cor após cada caractere
    
    return gradient_text

def print_lyrics():
    """
    Imprime a letra da música com efeitos especiais:
    - Exibe caractere por caractere com intervalos variáveis
    - Aplica gradiente na palavra "Apocalypse"
    - Tempos personalizados após cada linha
    """
    # Lista de tuplas: (linha da letra, intervalo entre caracteres)
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
        # Aplica gradiente apenas em "Apocalypse"
        if "Apocalypse" in line:
            line = line.replace("Apocalypse", apply_gradient("Apocalypse"))
        
        # Imprime cada caractere com intervalo
        for char in line:
            print(char, end='')
            sys.stdout.flush()  # Força a impressão imediata
            sleep(char_delay)   # Pausa entre caracteres
        
        time.sleep(delays[i])   # Pausa após a linha completa
        print()  # Quebra de linha

    # ATENÇÃO: Isso cria um loop infinito
    print_lyrics()  # Reinicia a música automaticamente

# Inicia a animação das letras
print_lyrics()