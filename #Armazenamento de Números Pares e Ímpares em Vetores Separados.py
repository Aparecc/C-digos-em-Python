def main():
    numeros = [int(input(f"Digite o {i+1}º número inteiro: ")) for i in range(20)]

    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    print("Números pares:")
    print(pares)
    print("Números ímpares:")
    print(impares)

if __name__ == "__main__":
    main()
