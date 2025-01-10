def main():
    vetor = []  # Crie um vetor vazio para armazenar os números
    for i in range(5):
        try:
            numero = int(input(f"Digite o {i+1}º número inteiro: "))
            vetor.append(numero)  # Adicione o número ao vetor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    print("Números digitados:")
    for num in vetor:
        print(num)

if __name__ == "__main__":
    main()
