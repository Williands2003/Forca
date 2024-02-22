#faça uma forca(a que eu fiz na aula)
#--------------------------------

# Palavra que o jogador precisa adivinhar
palavra = "vasco"

# Número de tentativas permitidas
tentativas = 6

# Letras já digitadas pelo jogador
letras_digitadas = []

# Função para exibir a forca com base nas tentativas
def exibir_forca(tentativas):
    if tentativas == 6:
        print("  _________     ")
        print(" |/        |    ")
        print(" |              ")
        print(" |              ")
        print(" |              ")
        print("_|_             ")
    elif tentativas == 5:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |              ")
        print(" |              ")
        print("_|_             ")
    elif tentativas == 4:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |    ")
        print(" |              ")
        print("_|_             ")
    elif tentativas == 3:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |    ")
        print(" |        /     ")
        print("_|_             ")
    elif tentativas == 2:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |    ")
        print(" |        / \\  ")
        print("_|_             ")
    elif tentativas == 1:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        ( )   ")
        print(" |         |\\   ")
        print(" |        / \\  ")
        print("_|_             ")
    elif tentativas == 0:
        print("  _________     ")
        print(" |/        |    ")
        print(" |        (x)   ")
        print(" |         |\\   ")
        print(" |        / \\  ")
        print("_|_             ")

# Função para exibir a palavra oculta com base nas letras digitadas
def exibir_palavra_oculta(palavra, letras):
    resultado = ""
    for letra in palavra:
        if letra in letras:
            resultado += letra + " " #+= é como uma atalho para somar um valor a uma variável.
        else:
            resultado += "_ "
    return resultado.strip()#remove os espaços 

# Mensagem inicial
print("________________________________________")
print("Bem-vindo ao Jogo da Forca!")
print("________________________________________")

# Loop principal do jogo
maxtentativas = tentativas
while tentativas > 0:
    # Exibe a forca atual
    exibir_forca(tentativas)

    # Exibe a palavra oculta
    print("Palavra:", exibir_palavra_oculta(palavra, letras_digitadas))

    # Pede ao jogador para digitar uma letra
    letra = input("Digite uma letra: ").lower()# .lower vai converter as letras para o mesmo tamanho

    # Verifica se a letra já foi digitada
    if letra in letras_digitadas:
        print("Você já digitou essa letra. Tente novamente.")
        continue

    # Adiciona a letra às letras digitadas
    letras_digitadas.append(letra)

    # Verifica se a letra está na palavra
    if letra not in palavra:
        tentativas -= 1
        print(f"A letra '{letra}' não está na palavra. Tentativas restantes: {tentativas}")
    else:
        print(f"A letra '{letra}' está na palavra!")

    # Verifica se o jogador venceu
    if set(palavra) <= set(letras_digitadas):
        print("Parabéns! Você venceu!")
        break

# Se as tentativas acabaram, exibe a mensagem de derrota
if tentativas == 0:
    exibir_forca(tentativas)
    print(f"Você perdeu! A palavra era '{palavra}'.")




