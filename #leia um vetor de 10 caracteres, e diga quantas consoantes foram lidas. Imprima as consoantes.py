def main():
    vogais = {'A', 'E', 'I', 'O', 'U'}
    caracteres = [input(f"Digite o {i+1}º caractere: ") for i in range(10)]

    consoantes = [c for c in caracteres if c.upper() not in vogais]
    print(f"Quantidade de consoantes lidas: {len(consoantes)}")
    print("Consoantes digitadas:")
    for consoante in consoantes:
        print(consoante)

if __name__ == "__main__":
    main()
