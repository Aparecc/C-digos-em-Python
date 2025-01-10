def main():
    notas = []  # Crie uma lista vazia para armazenar as notas
    for i in range(4):
        try:
            nota = float(input(f"Digite a {i+1}ª nota: "))
            notas.append(nota)  # Adicione a nota à lista
        except ValueError:
            print("Entrada inválida. Digite um número real.")

    print("Notas digitadas:")
    for i, nota in enumerate(notas, start=1):
        print(f"Nota {i}: {nota:.2f}")

    media = sum(notas) / len(notas)
    print(f"Média: {media:.2f}")

if __name__ == "__main__":
    main()
