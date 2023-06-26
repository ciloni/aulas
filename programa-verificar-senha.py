# a variavel senha sistema é de um numero inteiro
senha_sistema = "87654321"
# print(type(senha_sistema))
# tipos de dados exemplo
# string (texto)
# integer (inteiro)
# float (decimais)

# A linha baixo escreve no terminal o nome do programa
print("Programa que verica se a senha está correta")
# A linha abaixo guarda em uma variavel o que o usuario do programa digitar
senha_inf_usuario = input("Qual a senha? ")

# senha_sistema = 87654321
# print("O tipo de dados da senha do sistema é:")
# print(type(senha_sistema))
# print(type(senha_inf_usuario))
# cast (conversão de tipo)
# print("Transformando a senha do sistema para string.")
# senha_sistema = str(senha_sistema)
# print(type(senha_sistema))
# print("Concluido o cast.")

# Estrutura de condicao comando IF
# verificar se as senhas são iguais
if(senha_sistema == senha_inf_usuario ):
    # bloco de comandos caso a condicao seja verdadeira
    print("Senha correta")
else:
    # bloco de comandos se a condicao for falsa
    print("Senha incorreta")
    print("Numero de tentativas excedidas")
# mensagem de ultima linha de código
print("Fim do programa.")