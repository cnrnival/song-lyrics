# Animação de Letras - "Apocalypse" do Cigarettes After Sex

Este script Python cria uma animação no terminal da letra da música "Apocalypse" do Cigarettes After Sex, com efeitos visuais especiais.

## Funcionalidades

- **Impressão caractere por caractere** com intervalos variáveis
- **Efeito de gradiente de cores** na palavra "Apocalypse" (tons de vermelho/laranja)
- **Pausas personalizadas** entre linhas para sincronizar com o ritmo da música
- **Loop infinito** que reinicia automaticamente a música

## Como Funciona

O script utiliza:
- Códigos ANSI para o efeito de gradiente
- `time.sleep()` para controle preciso dos tempos
- `sys.stdout.flush()` para impressão imediata dos caracteres

## Requisitos

- Python 3.x
- Terminal com suporte a códigos ANSI de cores

## Como Usar

Execute o script normalmente:
```bash
python apocalypse_lyrics.py
```

Para sair, pressione `Ctrl+C` (isso interromperá o loop infinito).

## Personalização

Você pode modificar facilmente:
- As cores do gradiente editando a lista `colors` na função `apply_gradient()`
- O tempo entre caracteres alterando os valores nas tuplas de `lines`
- Os atrasos entre linhas modificando a lista `delays`

## Exemplo de Saída

O script exibirá a letra com a palavra "Apocalypse" em gradiente colorido, com cada caractere aparecendo em intervalos cuidadosamente cronometrados para combinar com o clima da música.

## Observação

Este script foi criado para fins artísticos/entretenimento e contém um loop infinito por design.