def main():
    maiores_de_18 = 0
    for i in range(5):
        try:
            idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
            if idade > 18:
                maiores_de_18 += 1
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    print(f"Quantidade de pessoas com mais de 18 anos: {maiores_de_18}")

if __name__ == "__main__":
    main()
