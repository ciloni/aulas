# def func_soma(parametro_1, parametro_2):
#     soma = parametro_1+parametro_2
#     return soma

# print("inicio do programa")
# primeiro_parametro = float(input("Insira o primeiro número: "))
# segundo_parametro = float(input("Insira o segundo número: "))

# print(func_soma(primeiro_parametro,segundo_parametro))

# estrutura de repetição
# fatorial
# o fatorial de 5 é 5 * 4 * 3 * 2 * 1
# dado determinado numero , calcule o fatorial

# sem funcoes utilizando o for
# numero = 5

# for variavel_incremento in range(numero-1,0,-1):
#     print (str(numero)+"*"+str(variavel_incremento))
#     numero = numero * variavel_incremento
#     print (str(numero))

# funcoes recursivas
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n*fatorial(n-1)


print(fatorial(10))




