#lanchonete

import os


def exibir_nome_do_programa():
    print('''
██╗░░░░░░█████╗░███╗░░██╗░█████╗░██╗░░██╗░█████╗░███╗░░██╗███████╗████████╗███████╗
██║░░░░░██╔══██╗████╗░██║██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝╚══██╔══╝██╔════╝
██║░░░░░███████║██╔██╗██║██║░░╚═╝███████║██║░░██║██╔██╗██║█████╗░░░░░██║░░░█████╗░░
██║░░░░░██╔══██║██║╚████║██║░░██╗██╔══██║██║░░██║██║╚████║██╔══╝░░░░░██║░░░██╔══╝░░
███████╗██║░░██║██║░╚███║╚█████╔╝██║░░██║╚█████╔╝██║░╚███║███████╗░░░██║░░░███████╗
╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚══════╝''')
    
    
def exibir_opcoes():
    print(" 100 - Cachorro-quente : 1.20")
    print(" 101 - Bauru Simples : 1.30")
    print(" 102 - Bauru com Ovo : 1.50")
    print(" 103 - Hamburger : 1.20")
    print(" 104 - ChesseBurger : 1.70")
    print(" 105 - Suco : 2.20")
    print(" 106 - Refrigerante: 1.00")

def escolher_opcoes():
    try:
        opcao_escolhida = (int(input('Escolha o código do lanche que deseja: ')))
        quantidade = (int(input('\nEscolha a quantidade desejada:')))
        if opcao_escolhida == 100:
            valor_a_pagar = 1.20
        elif opcao_escolhida == 101:
            valor_a_pagar = 1.30
        elif opcao_escolhida == 102:
            valor_a_pagar = 1.50
        elif opcao_escolhida == 103:
            valor_a_pagar = 1.20
        elif opcao_escolhida == 104:
            valor_a_pagar = 1.70
        elif opcao_escolhida == 105:
            valor_a_pagar = 2.20
        elif opcao_escolhida == 106:
            valor_a_pagar = 1.00
            
            
            
        print(f'O valor de {quantidade} Lanche(s) é igual a {valor_a_pagar*quantidade:.2f}')
        
        voltar_ao_menu_principal()
        
        
        
    except:
        opcao_invalida()
    




































def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()




def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
    

if __name__ == '__main__':
    main()