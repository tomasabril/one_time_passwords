# Tomás Abril
#
# Servidor
#######
# http://dainf.ct.utfpr.edu.br/~maurofonseca/doku.php?id=cursos:if68e:geradorsenhas

import hashlib
import datetime

#######

arquivo = open("server_file", 'r+', encoding='utf8')

texto = arquivo.readline().strip()
usuario = texto.split(":")[1]
texto = arquivo.readline().strip()
semente = texto.split(":")[1]


if not usuario:
    print("criando novo usuario")
    usuario = input("usuario: ")
    semente = hashlib.sha512(input("semente: ").encode()).hexdigest()
    semente = semente[:2] + semente[-2:]

    arquivo.seek(0)
    arquivo.write("usuario:" + usuario + "\n")
    arquivo.write("semente:" + semente)

else:
    minuto_senha = -1
    tokens = [0, 0]
    while True:
        login = input("usuario: ")
        if usuario == login:
            # gerando tokens
            now = datetime.datetime.now()
            minuto_atual = now.minute
            # if minuto diferente gerar novos tokens
            if len(tokens) <= 1:
                print("acabaram os tokens, espere um minuto")
            # else:
            if minuto_atual != minuto_senha:
                tokens.clear()
                minuto_senha = now.minute
                tokens.append(semente + str(now.year) + str(now.month) +
                              str(now.day) + str(now.hour) + str(now.minute))
                print("gerando novos tokens...")
                for i in range(1, 6):
                    tk = hashlib.sha512(tokens[i - 1].encode()).hexdigest()
                    tk = tk[:2] + tk[-2:]
                    tokens.append(tk)

            # else usar proximo token
            token_lido = input("token para o usuario " + usuario + " : ")
            if token_lido in tokens:
                # retirando token utilizado e os acima
                pos = tokens.index(token_lido)
                tam = len(tokens)
                for i in range(pos, tam):
                    tokens.pop()
                print("login bem sucedido")
            else:
                print("erro!")
            # print(tokens)

        else:
            print("usuario não encontrado")

