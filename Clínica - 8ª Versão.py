"""
*******************************************************************************************
Autor: Leonardo Oliveira Almeida da Cruz

Componente Curricular: EXA 854-MI- Algoritmos

Concluído em: 18/02/2024

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
********************************************************************************************
"""
"""
Informação importante: Tem 8 pacientes ja cadastrados, os codigos têm 6 digitos, e se inicia em 000001 até 000008
Algumas sessões ja existem também, você pode verificar na função dois do código quais são elas.
"""

import datetime
import json

sua_data = datetime.date.today()
datahj = sua_data.strftime("%d/%m/%Y")
# Aqui ficam as variaveis, dicionarios e listas a serem utilizados ao decorrer do codigo.
pacientes = {}
sessoes = {}
cont = 0 
opcoes = ""
pacientesday = []
sessaoatual = None
paciente_atual = None
validacpf = False

ids_gerados = set()
id_anterior = 0

# A função abaixo faz a recuperação de dados.
def popular(id_anterior):
    print("Fazendo carregamento de dados! Por favor aguarde!\n")

    with open("pacientes.json", "r") as arquivo:
        recriada = json.load(arquivo)

    recriada  = eval(recriada)

    for cada in recriada:
        nome = recriada[cada]["nome"]
        idade = recriada[cada]["idade"]
        cpf = recriada[cada]["cpf"]
        codigo = recriada[cada]["codigo"]
        t = Paciente(nome,idade,cpf,codigo)
        t.primeira_anotacao = recriada[cada]["primeira_anotacao"]
        t.ultima_anotacao = recriada[cada]["ultima_anotacao"]
        t.pront = recriada[cada]["pront"]
        t.datas_sessao = recriada[cada]["datas_sessao"]
        pacientes[codigo] = t
        ids_gerados.add(codigo)
    try:
        id_anterior = int(codigo)
    except:
        pass


    with open("sessoes.json", "r") as arquivo:
        recriado = json.load(arquivo)

    str(recriado)
    recriado = recriado.replace("null","None")

    recriado = eval(recriado)

    poplist = []
    for cada in recriado:
        chave = recriado[cada]["chave"]
        data = cada
        for y in recriado[cada]["lista_diaria"]:
            poplist.append(pacientes[y])
        popsessao = Sessão(1)
        popsessao.data = data
        popsessao.chave = chave
        popsessao.lista_diaria = poplist
        sessoes[data] = popsessao
# A função abaixo serve para guardar os dados em arquivos
def salvar():
    print("Encerrando e salvando, por favor não feche o programa!")

    for x in pacientes:
        seri = pacientes[x].__dict__
        pacientes[x] = seri

    arquive = "pacientes.json"
    paci = json.dumps(pacientes)

    with open(arquive, "w") as arquivo:
        json.dump(paci, arquivo)

    for x in sessoes:
        z = []
        for y in sessoes[x].lista_diaria:
            z.append(y.codigo)
        sessoes[x].lista_diaria = z

        seri = sessoes[x].__dict__
        sessoes[x] = seri

    arquive = "sessoes.json"
    sess = json.dumps(sessoes)

    with open(arquive,"w") as arquivo:
        json.dump(sess,arquivo)
# A função abaixo verifica se o que foi digitado tirando os pontos e "-" têm 11 digitos e retorna false ou true.
def valida_cpf(cpf):
    valid = cpf.replace(".","")
    valida = valid.replace("-","")
    validado = str(valida)
    if len(validado) == 11:
        return True
    else:
        return False
# A função abaixo verifica se a data digitada pelo usuário é uma data real.
def valida_data(data):
    try:
        datetime.datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False
# A função abaixo gera um id para os pacientes que começa em 000001 e vai somando +1 a cada paciente.
def gerar_id(id_anterior,ids_gerados):
    ultimo_id = id_anterior
    while True:
        novo_id = f"{(ultimo_id+1):06d}"
        if novo_id not in ids_gerados:
            ids_gerados.add(novo_id)
            ultimo_id += 1
            return novo_id,ultimo_id

# Definição das classes Medico, Paciente e Sessão e seus atributos e métodos.

class Medico:
    def __init__(self):
        self.chave = 0

class Paciente:
    def __init__(self,nome,idade,cpf,codigo):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.codigo = codigo
        self.datas_sessao = []
        self.primeira_anotacao = ""
        self.ultima_anotacao = ""
        self.pront = {}
        
class Sessão:
    def __init__ (self,chave):
        self.lista_diaria = []
        self.chave = chave
        self.data = ""
        
    def iniciar (self):
        sessaoatual.chave = 0

    def encerrar (self,data):
        sessoes[data].chave = -1

# Gerando um médico que seria utilizado em algumas funções porem não consegui implementar muito bem, logo, a função 12 do código é infuncional.
medico = Medico()

# Popula o código e recupera o ultimo id gerado.
id_anterior = popular(id_anterior)

print("Carregamento de dados concluído com sucesso!\n")

# Loop Principal do Menu
while opcoes != "X" and opcoes != "x":
    menu = None
    opcoes = str(input("""
            Menu

01 - Adicionar nova sessão clinica.
02 - Listar sessões clínicas.
03 - Buscar sessão clínica.
04 - Iniciar sessão clínica pela recepção.
05 - Adicionar novo paciente.
06 - Marcar horário para paciente.
07 - Listar horários marcados do paciente.
08 - Confirmar se o paciente está marcado para a sessão atual.
09 - Colocar paciente na fila de atendimento.
10 - Listar próximo paciente da fila de atendimento.
11 - Localizar sessão clínica para o dentista.
12 - Iniciar sessão clínica do dentista.
13 - Atender próximo paciente.
14 - Ler prontuário completo do paciente atual.
15 - Ler primeira anotação do paciente atual.
16 - Ler ultima anotação do paciente atual.
17 - Anotar prontuário do paciente atual.
18 - Listar consultas realizadas numa sessão clínica.
X - Fechar programa e salvar alterações.

Digite Aqui: """))
    # Verifica se há a condição de parada, se não verifica se o que foi digitado é um número.
    if opcoes != "X" and opcoes != "x":
        try:
            menu = int(opcoes)
        except:
            print("Por favor, digite um número!")
        
        match menu:
            case 1:
                # Pede a data, verifica se é válida, cria a nova sessão e também verifica se a sessão ja existe.
                data = str(input("Qual a data da sessão que deseja adicionar? XX/XX/XXXX: "))
                verificador = valida_data(data)
                if verificador == True and data not in sessoes:
                    sessao = Sessão(1)
                    sessao.data = data
                    sessoes[data] = sessao
                elif verificador == False:
                    print("Você inseriu uma data inválida!")
                elif data in sessoes:
                    print("A sessão ja existe!")

            case 2:
                # Verifica se há sessões, se houver apresenta uma por uma as datas e seu estado. Caso não haja sessões apresenta que não há.
                if sessoes != {}:
                    print("Sessões Documentadas: ")
                    for x in sessoes:
                        estado = ""
                        if sessoes[x].chave == -1:
                            estado = "encerrada"
                        elif sessoes[x].chave == 0:
                            estado = "acontecendo"
                        elif sessoes[x].chave == 1:
                            estado = "não iniciada"
                        print(f"{x}, - {len(sessoes[x].lista_diaria)} paciente(s).  ({estado})")
                else:
                    print("Não há sessões listadas!")
                
            case 3:
                # Recebe uma data, verifica a data, verifica se a sessão existe, caso sim, apresenta os pacientes e seus respectivos IDs. 
                search = str(input("Qual a data da sessão que deseja consultar? XX/XX/XXXX : "))
                verificador = valida_data(search)
                if verificador == True:
                    if search in sessoes:
                        if sessoes[search].lista_diaria != []:
                            print(f"A sessão do dia {search} contém os seguintes pacientes a serem atendidos na ordem em que aparecem:")
                            for y in sessoes[search].lista_diaria:
                                print(y.nome,"-",y.codigo)
                        else:
                            print("Não há pacientes para a data!")
                    else:
                        print(f"Sessão não encontrada na data {search}")
                else:
                    print("Você digitou uma data inválida! ")
            
            case 4:
                # Define a data de hoje (do computador) como sendo a data da sessão atual.
                # Se a sessão existir ele inicia, se não, ele pergunta se quer criar, e se quiser, ele cria e inicia.
                data = datahj
                if data in sessoes:
                    if sessaoatual != None and sessaoatual != sessoes[data]:
                        sessaoatual.encerrar(sessaoatual.data)
                    sessaoatual = sessoes[data]
                    sessaoatual.iniciar
                    pacientesday = sessoes[data].lista_diaria
                    paciente_atual = None
                    cont = 0
                    sessaoatual.chave = 0
                    print(f"Sessão do dia {datahj} iniciada!")

                else:
                    nova = "O"
                    while nova.upper() != "N" and nova.upper() != "Y":
                        nova = str(input("A sessão não está listada, deseja adicionar a sessão? Y/N: "))
                        if nova.upper() == "Y":
                            if sessaoatual != None:
                                sessaoatual.encerrar(sessaoatual.data)
                            sessao = Sessão(0)
                            sessao.data = datahj
                            sessoes[data] = sessao
                            sessaoatual = sessao
                            sessoes[data].iniciar()
                            paciente_atual = None
                            cont = 0
                            print(f"Sessão do dia {datahj} adicionada e iniciada!")
                        elif nova.upper() == "N":
                            print("\n")
                        else:
                            print("Por favor digite um caractere válido!")

            case 5:
                #Recebe o nome do paciente
                #Recebe a idade do paciente verificando se é um numero inteiro
                #Recebe e verifica se o cpf é valido
                #Chama o gerador de ID e cria um novo paciente.
                nome = str(input("Qual o nome do paciente?: "))
                teste = False
                while teste != True:
                    try:
                        idade = int(input("Qual a idade do paciente?: "))
                        teste = True
                    except:
                        print("Por favor, digite um número!")

                while validacpf != True:
                    cpf = str(input("Qual o cpf do paciente?: "))
                    validacpf = valida_cpf(cpf)
                    if validacpf == False:
                        print("o CPF foi digitado de forma incorreta!")
                validacpf = False
                novo_id,id_anterior = gerar_id(id_anterior,ids_gerados)

                paciente = Paciente(nome,idade,cpf,novo_id)
                pacientes[novo_id] = paciente
                print(f"O ID de {nome} é o seguinte: {novo_id}")
            
            case 6:
                #Recebe o codigo(ID) do paciente, verifica se o codigo está no dicionario de pacientes.
                #Recebe a data e valida, se a data que a pessoa deseja for a mesma que a atual, ele coloca o paciente na sessão de hoje.
                #Se a sessão for futura adiciona normalmente e caso não exista apresenta uma mensagem
                #Assim como apresenta se a data for invalida ou o codigo(ID) não exista ainda.
                cod = str(input("Qual o código do paciente que deseja marcar uma data?: "))
                if cod in pacientes.keys():
                    date = str(input("Qual a data que deseja?: "))
                    verificador = valida_data(date)
                    if verificador == True:
                        if date == datahj:
                            pacientesday.append(pacientes[cod])
                            pacientes[cod].datas_sessao.append(date)
                            print("Paciente adicionado na sessão de hoje!")
                        elif date not in sessoes:
                            print("A sessão não existe!")
                        else:
                            (sessoes[date].lista_diaria).append(pacientes[cod])
                            pacientes[cod].datas_sessao.append(date)
                            print("Data marcada com sucesso!")
                    else:
                        print("Data inválida!")
                else:
                    print("Não há pacientes com este código!")

            case 7:
                #Recebe e verifica se o codigo do paciente está na lista.
                #Verifica caso o usuário tenha datas marcadas, e as apresenta. Caso nao tenha apresenta uma mensagem.
                cod = str(input("Qual o código do paciente?: "))
                if cod in pacientes.keys():
                    if pacientes[cod].datas_sessao != []:
                        print(f"As datas marcadas para o paciente {pacientes[cod].nome} de código {cod} são: ")
                        for x in pacientes[cod].datas_sessao:
                            print(x)
                    elif pacientes[cod].datas_sessao == []:
                        print("O paciente não possui datas marcadas")
                else:
                    print("Código de paciente não encontrado no sistema")

            case 8:
                #Recebe o codigo do paciente e verifica se o codigo está na lista.
                #Procura na lista diária se o paciente se encontra e apresenta o resultado.
                cod = str(input("Qual o código do paciente para verificar?: "))
                if cod in pacientes.keys():
                    teste = False
                    while teste == False:
                        for cada in pacientesday:
                            if cada.codigo == cod:
                                print("Sim, o paciente está marcado para hoje!")
                                teste = True
                        if teste == False:
                            print("Não, o paciente não está na lista de atendimento de hoje.")
                            teste = True

            case 9:
                #Recebe e verifica se o codigo do paciente está na lista
                #Adiciona o paciente na sessão atual, e caso ja esteja, apresenta uma mensagem.
                cod = str(input("Digite o código do paciente: "))
                if cod in pacientes.keys():
                    if pacientes[cod] not in pacientesday:
                        pacientesday.append(pacientes[cod])
                        print("Paciente adicionado na sessão atual!")
                    else:
                        print("O paciente já está na fila da sessão atual")

            case 10:
                #Apresenta o proximo paciente da fila com base na variavel cont e apresenta as mensagens.
                if pacientesday != []:
                    if cont < len(pacientesday):
                        print(f"O próximo paciente da fila de atendimento é {pacientesday[cont].nome} de cpf {pacientesday[cont].cpf}")
                    elif cont >= len(pacientesday):
                        print("Não há mais pacientes a serem atendidos")
                if pacientesday == []:
                    print("Não há pacientes para serem atendidos hoje")
            
            case 11:
                # Recebe uma data, verifica.
                # Apresenta o nome e a anotação de cada paciente nesta data
                buscar = str(input("Qual a data da sessão que deseja buscar? XX/XX/XXXX: "))
                p = valida_data(buscar)
                if p == True:
                    if buscar in sessoes:
                        print(f"Pacientes e suas anotações de {buscar}")
                        for cada in sessoes[buscar].lista_diaria:
                            print(cada,"-", cada.pront[buscar])
                    else:
                        print("A sessão não foi encontrada.")
                else:
                    print("Data inválida")
            
            case 12:
                print("")
                #Função 12 infelizmente desisti por alguns erros.
                """
                medico.chave = 1
                print("\nSessão do Médico iniciada com sucesso!")"""
            
            case 13:
                # Verifica se a lista de pacientes do dia tem pacientes.
                # A partir da variável cont, pega o proximo paciente da lista e coloca no atual.
                # Caso a lista acabe, apresenta uma mensagem, e caso a lista já não tenha ninguem de inicio, apresenta também.
                if pacientesday != []:
                    if cont < len(pacientesday):
                        paciente_atual = pacientesday[cont]
                        print(f"Atendendo agora {paciente_atual.nome}!")
                        cont += 1
                    elif cont >= len(pacientesday):
                        print("Não há mais pacientes para serem atendidos hoje!\n")
                        cont = 0
                
                elif pacientesday == []:
                    paciente_atual = None
                    print("Não há mais pacientes listados para hoje!")
            
            case 14:
                #Verifica se tem paciente sendo atendido, e printa todas as anotações juntamente com as suas respectivas datas.
                #Printa uma mensagem se ele não tiver anotações.
                #Se não houver paciente sendo atendido, pede para utilizar a opção 13
                if paciente_atual != None:
                    if paciente_atual.pront != {}:
                        print(f"O prontuário do(a) paciente {paciente_atual.nome} de cpf {paciente_atual.cpf} se encontra abaixo: ")
                        for x in paciente_atual.pront:
                            print(x," - ",paciente_atual.pront[x])
                    else:
                        print("O paciente atual não possui anotações registradas no prontuário!")
                elif paciente_atual == None:
                    print("Não há paciente sendo atendido no momento \nCaso queira atender o próximo paciente da fila utilize a opção n° 13")
            
            case 15:
                #Apresenta a primeira anotação do paciente atual
                if paciente_atual != None:
                    print(paciente_atual.primeira_anotacao)
                else:
                    print("Não há paciente em atendimento!")

            case 16:
                #Apresenta a ultima anotação do paciente atual.
                if paciente_atual != None:
                    print(paciente_atual.ultima_anotacao)
                else:
                    print("Não há paciente em atendimento!")
            
            case 17:
                #Permite que o médico escreva uma anotação do paciente atual.
                if paciente_atual != None:
                    paciente_atual.pront[datahj] = str(input("Escreva o prontuário do paciente: "))
                    if paciente_atual.primeira_anotacao == "":
                        paciente_atual.primeira_anotacao = paciente_atual.pront[datahj]
                    paciente_atual.ultima_anotacao = paciente_atual.pront[datahj]
                else:
                    print("Não há paciente sendo atendido no momento")
            
            case 18:
                #Recebe uma data, verifica se a data é valida e apresenta o nome das pessoas que foram atendidas na data.
                data = str(input("Qual a data que deseja consultar? XX/XX/XXXX: "))
                veri = valida_data(data)
                if veri == True:
                    print(f"As consultas feitas em {data} foram:")
                    for cada in sessoes[data].lista_diaria:
                        print(cada.nome)
                else:
                    print("Data inválida")
            case _:
                print("Número inválido")

medico.chave = 0
#Encerra a sessão atual antes de encerrar o programa
if sessaoatual != None:
    sessaoatual.chave = -1

salvar()