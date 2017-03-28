# one_time_passwords
OTP - One-Time Passwords - Gerador de senhas descartáveis


http://dainf.ct.utfpr.edu.br/~maurofonseca/doku.php?id=cursos:if68e:geradorsenhas

Gerador de senhas descartáveis

Este trabalho tem como objetivo que todos os alunos conheçam e implementem uma técnica de autenticação que use senhas descartáveis (OTP - One-Time Passwords).

    Uma senha descartável só pode ser usada uma única vez.
    Perde sua validade após esse uso.

Atenção - O sistema deverá:

    ser dividido em duas partes(que devem ser executadas em terminais diferentes, sem comunicação).

    Gerador de senha (Token)
        Primeira vez criar
            uma senha semente e
            uma senha local.
            Armazenar o Hash das duas senhas localmente.
        Próximas vezes
            Digitar nome e a senha local, se correto continua.
            Quando requisitado gera uma senha(Token).
                A senha (Token) deve ser gerada a partir da hash da senha semente do usuário (diferente da senha do usuário).
                O aluno deve propor uma variante do algoritmo OTP de Lamport, visto em aula.
                Este algoritmo deve levar em consideração o tempo (data hora minuto).
                As senhas devem ter validade de no máximo um minuto e só podem ser usadas uma única vez.(Fazer uma lista de senhas para ser usada no minuto. Ex.lista com 5 senhas para o minuto solicitado)
                somente gerar lista de senhas para o minuto solicitado.
    Aplicativo
        Quando acessado usa o mesmo algoritmo gerador de senhas anterior. Mas em instância separada.
            A lista de senha gerada será a mesma nas duas partes, apesar de estarem em aplicativos separados e sem comunicação.
            Verifica se senha digitada esta na lista gerada e não foi usada e nem invalidada.
                nesta caso apresenta “Chave válida”.
                Atenção:
                    As senhas devem ter validade de no máximo um minuto e só podem ser usadas uma única vez.
                    Senhas são geradas a partir de outras senhas, e se for usada uma chave todas as chaves geradas pela mesma devem ser invalidadas.
        Se o cliente digitar uma senha válida o servidor aceita, caso contrario retorna mensagem de erro.

    devem ser usados como função hash MD5 ou SHA.
        Os hash são muito grandes, logo podem ser truncados para facilitar o manuseio.
        Normalmente usa-se tamanho igual a 6 ou 8 casas para a senha (token).

    As informações que são conhecidas pelos dois aplicativos são:
        Usuários.
        Hash da senha sementes de cada usuário.

Obs.: Será avaliado com ZERO trabalhos que armazenarem senhas em texto sem hash.

Para aumentar a segurança além da senha semente do usuário é possível concatenar mais uma cadeia de caracteres recebida no dispositivo (via SMS) que foi instalado o gerador de senha. Assim se precisar instalar em outro local, basta trocar a cadeia de caracteres e não precisa alterar a senha semente do usuário. 
