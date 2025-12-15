# 🎵 Animação de Letras - "Apocalypse" (Cigarettes After Sex)

Este script Python cria uma animação no terminal da letra da música "Apocalypse" do Cigarettes After Sex, com efeitos visuais especiais.

## Funcionalidades

- **Impressão caractere por caractere** com intervalos variáveis (efeito 'typing').
- **Efeito de gradiente de cores** na palavra "Apocalypse" (tons de vermelho/laranja).
- **Pausas personalizadas** entre linhas para sincronizar com o ritmo da música.
- **Execução única** da música (o loop infinito original foi removido para fins práticos).

## Como Funciona

O script utiliza:
- **`colorama.init()`** para melhor compatibilidade com códigos ANSI no terminal (especialmente no Windows).
- Códigos ANSI de 256 cores (`\033[38;5;...m`) para o efeito de gradiente.
- `time.sleep()` para controle preciso dos tempos.
- `sys.stdout.flush()` para impressão imediata dos caracteres.

## Requisitos

- Python 3.x
- **Biblioteca `colorama`**: `pip install colorama`
- **Terminal Moderno**: Recomenda-se o **Windows Terminal** ou terminais Linux/macOS, pois terminais antigos podem não suportar o gradiente de 256 cores.

## Como Usar

1.  **Instale a biblioteca:**
    ```bash
    pip install colorama
    ```
2.  **Execute o script:**
    ```bash
    python apocalypse_lyrics.py
    ```

Para parar a execução (caso o script esteja no meio da música), pressione `Ctrl+C`.

## Personalização

Você pode modificar facilmente:
- As cores do gradiente editando a lista `colors` na função `apply_gradient()`
- O tempo entre caracteres alterando os valores nas tuplas de `lines`
- Os atrasos entre linhas modificando a lista `delays`

## Exemplo de Saída

O script exibirá a letra com a palavra "Apocalypse" em gradiente colorido, com cada caractere aparecendo em intervalos cuidadosamente cronometrados.

## Observação

Este script foi modificado para execução única (sem loop) para melhor usabilidade no terminal.