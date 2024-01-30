# o mesmo codigo anterior mas quero usar um input para que o jogador escolha a palavra
#-------------------

# Palavra que o jogador precisa adivinhar
palavra = ("batman")

# Letras já digitadas pelo jogador
letras_digitadas = []

# Função para exibir a forca com base nas tentativas
def exibir_forca():
    if len(letras_digitadas) == 6:
        print("  _________     ")
        print(" |/        |    ")
        print(" |              ")
        print(" |              ")
        print(" |              ")
        print("_|_             ")
    elif len(letras_digitadas) == 5:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |              ")
        print(" |              ")
        print("_|_             ")
    elif len(letras_digitadas) == 4:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |    ")
        print(" |              ")
        print("_|_             ")
    elif len(letras_digitadas) == 3:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |    ")
        print(" |        /     ")
        print("_|_             ")
    elif len(letras_digitadas) == 2:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |    ")
        print(" |        / \  ")
        print("_|_             ")
    elif len(letras_digitadas) == 1:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |\   ")
        print(" |        / \  ")
        print("_|_             ")
    elif len(letras_digitadas) == 0:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        (x)   ")
        print(" |        /|\   ")
        print(" |        / \  ")
        print("_|_             ")

# Função para exibir a palavra oculta com base nas letras digitadas
def exibir_palavra_oculta():
    resultado = ""
    for letra in palavra:
        if letra in letras_digitadas:
            resultado += letra + " "# += é como uma atalho para somar um valor a uma variável.
        else:
            resultado += "_ "
    return resultado.strip()

# Mensagem inicial
print("________________________________________")
print("Bem-vindo ao Jogo da Forca!")
print("________________________________________")

# Loop principal do jogo
while len(letras_digitadas) < 6:
    # Exibe a forca atual
    exibir_forca()

    # Exibe a palavra oculta
    print("Palavra:", exibir_palavra_oculta())

    # Pede ao jogador para digitar uma letra
    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra já foi digitada
    if letra in letras_digitadas:
        print("Você já digitou essa letra. Tente novamente.")
        continue

    # Adiciona a letra às letras digitadas
    letras_digitadas.append(letra)

    # Verifica se a letra está na palavra
    if letra not in palavra:
        print(f"A letra '{letra}' não está na palavra.")
    else:
        print(f"A letra '{letra}' está na palavra!")

# Se chegou aqui, o jogo acabou
exibir_forca()
print(f"Fim do jogo! A palavra era '{palavra}'.")
