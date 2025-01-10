def main():
    num_alunos = 10
    notas_alunos = []

    for _ in range(num_alunos):
        notas = [float(input(f"Digite a {i+1}ª nota: ")) for i in range(4)]
        media = sum(notas) / 4
        notas_alunos.append(media)

    alunos_aprovados = sum(1 for nota in notas_alunos if nota >= 7.0)

    print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")

if __name__ == "__main__":
    main()
