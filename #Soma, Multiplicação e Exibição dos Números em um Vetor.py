def main():
    numeros = [int(input(f"Digite o {i+1}º número inteiro: ")) for i in range(5)]

    soma = sum(numeros)
    multiplicacao = 1
    for num in numeros:
        multiplicacao *= num

    print(f"Soma dos números: {soma}")
    print(f"Multiplicação dos números: {multiplicacao}")
    print("Números digitados:")
    print(numeros)

if __name__ == "__main__":
    main()
