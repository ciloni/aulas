# lacos de repeticao while e for
# o laco de repeticao for executa por uma quantidade (limite) de vezes

# imprima numeros de 1 até 10
# for variavel_de_incremento in range(1,11,1):
#     print(variavel_de_incremento)

# imprima numeros pares de 0 até 10
# for variavel_de_incremento in range(0,11,2):
#     print(variavel_de_incremento)


# imprima os numeros pares e multiplique os impares por 5 de 0 até 10
# for i in range(0,101,1):
#     if(i%2 == 0):
#         print(i)
#     else:
#         #concatenacao é juntar 2 informacoes gerando uma string unica
#         texto_retorno = str(i)+" * 5 ="+ str((i*5))
#         print(texto_retorno)

# senha = ""
# numero_tentativas = 0
# # enquanto senha for diferente 87654321 faça
# while(senha != "87654321"):
#     # pergunte a senha
#     senha = input("Qual a senha: ")
#     numero_tentativas = numero_tentativas +1
#     print("Voce já tentou "+str(numero_tentativas)+" vezes.")
#     if(numero_tentativas >= 3):
#         # bloco de comandos caso exceda o numero de tentativas
#         print("Fim do programa, você excedeu o número máximo de tentativas.")
#         break
opcao = "vazio"
while(opcao != "0"):
    print("Selecione uma opção")
    print("1 - programa soma.")
    print("2 - programa multiplicacao.")
    print("0 - sair")
    opcao = input()
    if(opcao == "1" ):
        primeiro_valor = input("Digite o primeiro valor: ")
        segundo_valor = input("Digite o segundo valor: ")
        print(int(primeiro_valor)+int(segundo_valor))
    elif(opcao == "2"):
        primeiro_valor = input("Digite o primeiro valor: ")
        segundo_valor = input("Digite o segundo valor: ")
        print(float(primeiro_valor)*float(segundo_valor))
    elif(opcao == "0"):
        print("Encerrando o programa.")
    else:
        print("Opcao inválida.")

# Exercicio: Faça um programa com laço de repetição que descrubra uma senha numérica de 8 digitos.
# A senha do sistema é 87654333