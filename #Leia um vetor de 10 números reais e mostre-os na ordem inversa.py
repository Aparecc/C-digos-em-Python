def main():
    vetor = []  # Crie um vetor vazio para armazenar os números
    for i in range(10):
        try:
            numero = float(input(f"Digite o {i+1}º número real: "))
            vetor.append(numero)  # Adicione o número ao vetor
        except ValueError:
            print("Entrada inválida. Digite um número real.")

    print("Números digitados na ordem inversa:")
    for num in reversed(vetor):
        print(num)

if __name__ == "__main__":
    main()
