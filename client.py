# Tomás Abril
#
# aplicativo do Token
#######
# http://dainf.ct.utfpr.edu.br/~maurofonseca/doku.php?id=cursos:if68e:geradorsenhas

import hashlib
import os.path
import datetime

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
    print("criando novo usuario")
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
    login = input("usuario: ")
    senha_login = hashlib.sha512(input("senha: ").encode()).hexdigest()
    senha_login = senha_login[:2] + senha_login[-2:]
    if usuario == login and hashdasenha == senha_login:
        print("deu certo")
        minuto_senha = -1
        token = [0, 0]
        while True:
            now = datetime.datetime.now()
            minuto_atual = now.minute
            if int(input("aperte 1 para um novo token: ")):
                # if minuto diferente gerar novos tokens
                if len(token) <= 1:
                    print("acabaram os tokens, espere um minuto")
                # else:
                if minuto_atual != minuto_senha:
                    token.clear()
                    minuto_senha = now.minute
                    token.append(semente + str(now.year) + str(now.month) +
                                 str(now.day) + str(now.hour) + str(now.minute))
                    print("gerando novos tokens...")
                    for i in range(1, 6):
                        tk = hashlib.sha512(token[i-1].encode()).hexdigest()
                        tk = tk[:2] + tk[-2:]
                        token.append(tk)
                # else mostrar proximo token
                elif len(token) > 1:
                    print(token.pop())
                # print(token)

    else:
        print("erro no login")

