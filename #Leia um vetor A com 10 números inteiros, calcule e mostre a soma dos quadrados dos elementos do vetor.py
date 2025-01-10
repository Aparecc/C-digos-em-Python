def main():
    vetor = []  # Crie um vetor vazio para armazenar os números inteiros
    for i in range(10):
        try:
            numero = int(input(f"Digite o {i+1}º número inteiro: "))
            vetor.append(numero)  # Adicione o número ao vetor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    # Calcula a soma dos quadrados dos elementos do vetor
    soma_quadrados = sum(num ** 2 for num in vetor)

    print(f"Soma dos quadrados dos elementos do vetor: {soma_quadrados}")

if __name__ == "__main__":
    main()
