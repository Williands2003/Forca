# Palavra que o jogador precisa adivinhar
palavra = input("Qual a palavra secreta? ").lower()

# Letras já digitadas pelo jogador
letras_digitadas = []

# Membros do boneco
membros_boneco = 6

# Função para exibir a forca com base nos membros do boneco
def exibir_forca():
    if len(letras_digitadas) < 6:
        print("  _________     ")
        print(" |/        |    ")
        print(" |              ")
        print(" |              ")
        print(" |              ")
        print("_|_             ")
    if len(letras_digitadas) < 5:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |              ")
        print(" |              ")
        print("_|_             ")
    elif len(letras_digitadas) < 4:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |    ")
        print(" |              ")
        print("_|_             ")
    elif len(letras_digitadas) <4:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |    ")
        print(" |        /     ")
        print("_|_             ")
    elif len(letras_digitadas) < 3:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |    ")
        print(" |        / \  ")
        print("_|_             ")
    elif len(letras_digitadas) < 2:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |\   ")
        print(" |        / \  ")
        print("_|_             ")
    elif len(letras_digitadas) < 1:
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
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

# Mensagem inicial
print("________________________________________")
print("Bem-vindo ao Jogo da Forca!")
print("________________________________________")

# Loop principal do jogo
while membros_boneco > 0:
    # Exibe a forca atual
    exibir_forca()

    # Exibe a palavra oculta
    print("Palavra:", exibir_palavra_oculta())

    # Pede ao jogador para digitar uma palavra
    tentativa = input("Digite uma palavra: ").lower()

    # Verifica se a palavra já foi digitada
    if tentativa == palavra:
        print(f"Parabéns! Você acertou a palavra '{palavra}'.")
        break
    else:
        membros_boneco -= 1
        print("Você errou. Tente novamente.")

# Se chegou aqui, o jogo acabou
exibir_forca()

if membros_boneco == 0:
    print(f"Fim do jogo! Você não acertou a palavra. A palavra era '{palavra}'.")
