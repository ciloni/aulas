# senha de 8 digitos 00000000 até 99999999
# a senha criptografada é 1d79c5c9f6a7bf07d9b9efd47d45672e
# foi utilizada a criptografia md5 nessa senha
# descubra qual a senha

import hashlib

senha_criptografada = "1d79c5c9f6a7bf07d9b9efd47d45672e"

# executar 99 milhoes de vezes a condicao de comparacao
for i in range(0,99999999,1):
    senha_md5 = hashlib.md5()
    senha= str(i)
    # print(senha)
    senha =senha.zfill(8)
    if(i%1000 == 0):
        print(i)
    senha_md5.update(senha.encode('utf-8'))
    # print(senha_md5.hexdigest())
    if(senha_md5.hexdigest() == senha_criptografada):
        print("Descobri a senha!!!")
        print(senha)
        break
    # print(senha_criptografada)

# v=1
# v=str(v)
# v=v.zfill(8)
# print(v)
# md5_hash = hashlib.md5()
# md5_hash.update(senha.encode('utf-8'))
# print(md5_hash.hexdigest())

