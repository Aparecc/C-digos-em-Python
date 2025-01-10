def main():
    senha_correta = "1234"  # Defina a senha correta
    while True:
        senha_digitada = input("Digite a senha: ")
        if senha_digitada == senha_correta:
            print("Senha Correta")
            break
        else:
            print("Senha Incorreta. Tente novamente.")

if __name__ == "__main__":
    main()
