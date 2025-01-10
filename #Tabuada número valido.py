def main():
    while True:
        try:
            numero = int(input("Digite um número entre 1 e 10: "))
            if 1 <= numero <= 10:
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro entre 1 e 10.")

    print(f"Tabuada do {numero}:")
    i = 1
    while i <= 10:
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
        i += 1

if __name__ == "__main__":
    main()
