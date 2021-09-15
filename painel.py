from Fila import Fila

fila = Fila()

senhasChamadas = []

contadorSenhas = 0


def verificaOpcao():
    global contadorSenhas

    if opcaoDesejada == 1:
        print(f"Sua senha é {contadorSenhas}")
        fila.enqueue(contadorSenhas)
        contadorSenhas += 1
        menu()

    elif opcaoDesejada == 2:
        senhasChamadas.append(fila._vet[0])
        print(F"A senha chamada é {fila._vet[0]}")
        fila.dequeue()
        menu()

    elif opcaoDesejada == 3:
        print(f"As senhas já chamadas: {senhasChamadas}")
        menu()

    else:
        print("Essa opção não existe. Por favor, tente novamente.")
        menu()


def menu():
    global opcaoDesejada
    opcaoDesejada = int(input(
        "Digite 1 se você quer obter uma nova senha, 2 se você quer chamar a próxima senha e 3 se você quer mostras as senhas chamadas: "))
    verificaOpcao()


menu()
