# Tomás Abril
#
# aplicativo do Token
#######

import hashlib
import os.path

#######

m = hashlib.sha256()
m.update(b"Nobody inspects the spammish repetition")
hashum = m.hexdigest()

arquivo = open("token_file", 'r+', encoding='utf8')

texto = arquivo.readline().strip()
usuario = texto.split(":")[1]
texto = arquivo.readline().strip()
hashdasenha = texto.split(":")[1]
texto = arquivo.readline().strip()
semente = texto.split(":")[1]

if not usuario:
    usuario = input("usuario: ")
    hashdasenha = hashlib.sha512(input("senha: ").encode()).hexdigest()
    semente = hashlib.sha512(input("semente: ").encode()).hexdigest()
    hashdasenha = hashdasenha[:2] + hashdasenha[-2:]
    semente = semente[:2] + semente[-2:]

    arquivo.seek(0)
    arquivo.write("usuario:" + usuario + "\n")
    arquivo.write("hash_da_senha:" + hashdasenha + "\n")
    arquivo.write("semente:" + semente)

else:
    if usuario == input("usuario: ") and hashdasenha == hashlib.sha512(input("senha: ").encode()).hexdigest():
        print ("deu certo")
    else:
        print("nao deu certo")
