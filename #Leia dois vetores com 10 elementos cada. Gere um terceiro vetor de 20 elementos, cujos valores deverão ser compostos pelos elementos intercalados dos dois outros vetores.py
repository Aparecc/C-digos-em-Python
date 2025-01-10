def intercalar_vetores(vetor1, vetor2):
    # Verifica se os vetores têm o mesmo tamanho
    if len(vetor1) != len(vetor2):
        print("Os vetores devem ter o mesmo tamanho.")
        return None

    # Cria o terceiro vetor com o dobro do tamanho
    vetor3 = [0] * (len(vetor1) + len(vetor2))

    # Intercala os elementos dos vetores
    for i in range(len(vetor1)):
        vetor3[2*i] = vetor1[i]
        vetor3[2*i + 1] = vetor2[i]

    return vetor3

def main():
    vetor1 = list(map(int, input("Digite os valores do primeiro vetor separados por espaço: ").split()))
    vetor2 = list(map(int, input("Digite os valores do segundo vetor separados por espaço: ").split()))

    vetor_resultante = intercalar_vetores(vetor1, vetor2)
    if vetor_resultante:
        print("Vetor resultante (elementos intercalados):")
        print(vetor_resultante)

if __name__ == "__main__":
    main()
