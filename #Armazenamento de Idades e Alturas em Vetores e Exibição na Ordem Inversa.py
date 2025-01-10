def main():
    idades = [int(input(f"Digite a idade da {i+1}ª pessoa: ")) for i in range(5)]
    alturas = [float(input(f"Digite a altura da {i+1}ª pessoa (em metros): ")) for i in range(5)]

    print("Idades na ordem inversa:")
    for idade in reversed(idades):
        print(idade)

    print("Alturas na ordem inversa:")
    for altura in reversed(alturas):
        print(f"{altura:.2f} metros")

if __name__ == "__main__":
    main()
