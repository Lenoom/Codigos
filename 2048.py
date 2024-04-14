"""
*******************************************************************************************
Autor: Leonardo Oliveira Almeida da Cruz

Componente Curricular: EXA 854-MI- Algoritmos

Concluído em: 09/10/2023

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
********************************************************************************************
"""

from random import *

# Função que soma na Vertical;
def soma_ws(a,b,c,p,s,jogo,pontuacao,sumtrue):
    pontuacao = pontuacao
    sumtrue
    b1 = b
    if c == 1:
        b1 += -1

    for x in range(a,b,c):
            z = p
            for y in range(a,b1,c):
                teste = 0
                z = y + s
                while teste == 0 and -1< z <4:
                    if jogo[y][x] == 0:
                        teste = 1

                    elif jogo[y][x] == jogo[z][x]:
                        jogo[y][x] = jogo[y][x] + jogo[z][x]
                        pontuacao += int(jogo[y][x])
                        jogo[z][x] = 0
                        teste = 1
                        sumtrue = True

                    elif jogo[z][x] == 0:
                        z += s

                    elif jogo[y][x] != jogo[z][x]:
                        teste = 1

    return pontuacao,sumtrue
# Função que soma na Horizontal;
def soma_ad(a,b,c,p,s,jogo,pontuacao,sumtrue):
    sumtrue
    b1 = b
    if c == 1:
        b1 += -1

    for y in range(a,b,c):
            z = p
            for x in range(a,b1,c):
                teste = 0
                z = x+s
                while teste == 0 and -1< z <4:

                    if jogo[y][x] == 0:
                        teste = 1

                    elif jogo[y][x] == jogo[y][z]:
                        jogo[y][x] = jogo[y][x] + jogo[y][z]
                        pontuacao += int(jogo[y][x])
                        jogo[y][z] = 0
                        teste = 1
                        sumtrue = True

                    elif jogo[y][z] == 0:
                        z += s

                    elif jogo[y][x] != jogo[y][z]:
                        teste = 1

    return pontuacao,sumtrue
# Função que movimenta na Horizontal;
def mov_ad(a,b,c,p,w,jogo,movetrue):
    movetrue
    w = w
    z = p
    b1 = b
    if c == 1:
        b1 += -1
        
    for y in range(a,b,c):
         for w in range(3):
            for x in range(a,b1,c):
                z = x + c
                if jogo[y][x] == 0 and jogo[y][z] != 0 and -1<z<4:
                    jogo[y][x] = jogo[y][z]
                    jogo[y][z] = 0
                    movetrue = True
    return movetrue
# Função que movimenta na Vertical;
def mov_ws(a,b,c,p,w,jogo,movetrue):
    movetrue
    w = w
    z = p
    b1 = b
    if c == 1:
        b1 += -1

    for x in range(a,b,c):
        for w in range(3):
            for y in range(a,b1,c):
                z = y + c
                if jogo[y][x] == 0 and jogo[z][x] != 0 and -1<z<4:
                    jogo[y][x] = jogo[z][x]
                    jogo[z][x] = 0
                    movetrue = True
    return movetrue
# Função que cria a lista com zeros do tabuleiro e sorteia uma posição aleatória e adiciona 2 ou 4;
def addrandom(jogo,zeros,ok,movetrue,sumtrue,k):
    k
    for k in range(0,ok):
        zeros = []
        for i in range(4):
            for j in range(4):
               if jogo[i][j] == 0:
                   zeros.append((i,j))
        if movetrue == True or sumtrue == True:
            y, x = choice(zeros)
            jogo[y][x] = choice([2,4])
    zeros = []
    for i in range(4):
        for j in range(4):
            if jogo[i][j] == 0:
                zeros.append((i,j))
    ok = 1 
    return ok,zeros
# Função que verifica se há somas possiveis no tabuleiro;
def possiblesum(jogo):
    y = 0
    x = 0
    z = 0
    w = 0
    confirm = False
    confirm1 = False
    confirm2 = False
    p = ""

    while p != "ok":
        for y in range(4):
            if confirm1 == True:
                break
            for x in range(3):
                z = x+1
                if jogo[y][x] == jogo[y][z]:
                    confirm1 = True
                    p = "ok"
                    break
                else:
                    confirm1 = False
        p = "ok"
    p = ""
        
    while p != "ok":
        for x in range(4):
            if confirm2 == True:
                break
            for y in range(3):
                w = y+1
                if jogo[y][x] == jogo[w][x]:
                    confirm2 = True
                    p = "ok"
                    break
                else:
                    confirm2 = False
        p = "ok"
    
    if confirm1 == True or confirm2 == True:
        confirm = True
    else:
        confirm = False

    return confirm
# Função que reseta todas as variáveis utilizadas no jogo;
def zerar():
    fechar = ""
    y = 0 
    x = 0
    k = 0
    ok = 2
    zeros = []
    movetrue = True
    sumtrue = True
    confirm = True
    jogo = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
    pontuacao = 0
    jogadas = 0
    lado = ""
    saida = ""

    return fechar,y,x,k,ok,zeros,movetrue,sumtrue,confirm,jogo,pontuacao,jogadas,lado,saida
# -------------------------------------------------------------------------------------------------------------
# Variáveis Iniciais;
lado = ""
replay = ""
historico = [[],[],[]]

# Looping principal do jogo;
while lado.upper() != "X" and replay.upper() != "N":
    # Apresenta uma mensagem caso a ultima partida tenha sido vencida ou perdida.
    if lado != "" and lado != "X" and lado != "R":
        if saida == "V":
            print(f"Você {pontuacao} pontos em {jogadas} jogadas e venceu!!")
        elif saida == "D":
            print(f"Você obteve {pontuacao} pontos em {jogadas} jogadas mas infelizmente perdeu!")
    replay = ""
    # Em caso de derrota ou vitória pergunta ao usuário se ele deseja jogar novamente.
    if lado != "" and lado.upper() != "R":
        while replay.upper() != "N" and replay.upper() != "Y":
            replay = str(input("Deseja jogar novamente? Y/N: "))

    fechar,y,x,k,ok,zeros,movetrue,sumtrue,confirm,jogo,pontuacao,jogadas,lado,saida = zerar()

    # Looping que roda enquanto o usuário desejar jogar
    while lado.upper() != "R" and lado.upper() != "X" and replay.upper() != "N" and saida != "D" and saida != "V":   
        # Verifica se é a primeira vez que o looping roda, para adicionar 2 números e da proxima adicionar apenas um por vez.
        if ok == 2:
            ok,zeros = addrandom(jogo,zeros,ok,movetrue,sumtrue,k)
            movetrue = False
            sumtrue = False

        # Caso não haja blocos numerados de "0" o jogo verifica se há somas possiveis.
        if zeros == []:   
            confirm = possiblesum(jogo)

        # Faz o print do tabuleiro, da pontuação e das jogadas na tela.
        for y in range(4):
            print(f"|{jogo[y][x]:^4}|{jogo[y][x+1]:^4}|{jogo[y][x+2]:^4}|{jogo[y][x+3]:^4}|")
        print("Pontuação:",pontuacao)
        print("Jogadas:",jogadas)

        # Caso não haja zeros e após verificar, não houver somas possiveis, apresenta derrota.
        if confirm == False:
            print("DERROTA!")
            saida = "D"
            historico[0].append(pontuacao)
            historico[1].append(jogadas)
            historico[2].append("Derrota!")

        if lado.upper() != "R" and saida != "D" and saida != "V":
            # Pergunta ao usuário para qual direção ele deseja movimentar, ou se deseja fechar ou reiniciar.
            lado = str(input("""
Para onde deseja mover?
W = Cima | S = Baixo | D = Direita | A = Esquerda | X = Sair | R = Reiniciar
Insira: """).lower())
            

            # Verifica se a posição que o usuário deseja é na vertical, passa valores para as funções de soma e movimentação.
            if lado == "w" or lado == "a":
                a = 0
                b = 4
                c = 1
                p = 1
                s = 1
                w = 0

                if lado == "w":
                    pontuacao, sumtrue = soma_ws(a,b,c,p,s,jogo,pontuacao,sumtrue)
                    movetrue = mov_ws(a,b,c,s,w,jogo,movetrue)
                elif lado == "a":
                    pontuacao, sumtrue = soma_ad(a,b,c,p,s,jogo,pontuacao,sumtrue)
                    movetrue = mov_ad(a,b,c,s,w,jogo,movetrue)


            # Verifica se a posição que o usuário deseja é na horizontal, passa valores para as funções de soma e movimentação.
            elif lado == "s" or lado == "d":
                a = 3
                b = -1
                c = -1
                p = 2
                s = -1
                w = 0

                if lado == "s":
                    pontuacao, sumtrue = soma_ws(a,b,c,p,s,jogo,pontuacao,sumtrue)
                    movetrue = mov_ws(a,b,c,s,w,jogo,movetrue)
                elif lado == "d":
                    pontuacao, sumtrue = soma_ad(a,b,c,p,s,jogo,pontuacao,sumtrue)
                    movetrue = mov_ad(a,b,c,p,w,jogo,movetrue)
            
            # Abaixo, caso o usuário queira sair, reiniciar ou tenha digitado algo inválido, apresenta informativos.
            elif lado.upper() == "X":
                print("Fechando!")

            elif lado.upper() == "R":
                print("Reiniciando!")

            else:
                print("Por favor, digite um caractere válido!")

            # Caso tenha tido movimento ou soma, adiciona uma jogada.
            if movetrue == True or sumtrue == True:
                jogadas += 1
            
            ok,zeros = addrandom(jogo,zeros,ok,movetrue,sumtrue,k)
            movetrue = False
            sumtrue = False

            # Verifica se tem o número 2048 no tabuleiro e declara vitoria caso tenha.
            for linha in jogo:
                for vitoria in linha:
                    if vitoria == 2048:
                        print("Você Venceu!")
                        saida = "V"
                        historico[0].append(pontuacao)
                        historico[1].append(jogadas)
                        historico[2].append("Vitória!")

# Verifica se houve jogos e caso sim, apresenta o histórico de todos os jogos: Sua pontuação, quantidade de jogadas e se venceu ou perdeu.
# Caso contrario imprime que nao houve jogos
if historico == [[],[],[]]:
    print("Não tiveram jogos finalizados!")
else:
    print("""
             HISTÓRICO:""")
    print("Jogo | Pontuação | Jogadas | Win/Lost")
    for i in range(len(historico[0])):
        print(f"{i+1}º   - {historico[0][i]:^9} - {historico[1][i]:^7} - {historico[2][i]}")

# Pelos meus testes está tudo correndo bem! Boa correção professora!
