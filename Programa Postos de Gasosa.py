"""
*******************************************************************************************
Autor: Leonardo Oliveira Almeida da Cruz

Componente Curricular: EXA 854-MI- Algoritmos

Concluído em: 28/08/2023

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
********************************************************************************************
"""

teste = ""
gas_valid1 = ""
gas_valid2 = ""
gas_valid3 = ""
eta_valid1 = ""
eta_valid2 = ""
eta_valid3 = ""
die_valid1 = ""
die_valid2 = ""
die_valid3 = ""

gasolina_posto_um = ""
gasolina_posto_dois = ""
gasolina_posto_tres = ""
etanol_posto_um = ""
etanol_posto_dois = ""
etanol_posto_tres = ""
diesel_posto_um = ""
diesel_posto_dois = ""
diesel_posto_tres = ""
# Declarações de Variáveis do Menu
opcao = ""
escolha = ""
validacao = ""
break_ = 0

combustivel = ""
litros = ""
seu_combustivel = ""

combposto1 = 0
combposto2 = 0
combposto3 = 0
   
combbarato = 0
combmedio = 0
combcaro = 0

posto_barato = ""
posto_medio = ""
posto_caro = ""

#_______________________________
#Declarações de variáveis usadas ao sair do Menu
consultas = 0

vzsbarato1 = 0
vzsbarato2 = 0
vzsbarato3 = 0

litrospost1 = 0
litrospost2 = 0
litrospost3 = 0

mediaposto1 = ""
mediaposto2 = ""
mediaposto3 = ""

gasbarato = 0
gascaro = 0
etabarato = 0
etacaro = 0
diebarato = 0
diecaro = 0

postogasbarata = ""
postoetabarato = ""
postodiebarato = ""

postogascara = ""
postoetacaro = ""
postodiecaro = ""
#_____________
#Fazer os inputs dos postos de gasolina e seus respectivos preços:
while teste.upper() != "S":
  posto_um = str(input("Insira o nome do primeiro posto: "))
  while gas_valid1 != True:
    gaspost1 = str(input(f"Qual o preço da Gasolina no {str(posto_um)}?: "))
    gaspost1_sem_virgula = gaspost1.replace(",",".")
    gaspost1_sem_ponto = gaspost1_sem_virgula.replace(".","")

    if gaspost1_sem_virgula == "0" or gaspost1_sem_virgula == "0.0":
        gas_valid1 = False

    elif gaspost1_sem_virgula != "0" or gaspost1_sem_virgula != "0.0":
        gas_valid1 = gaspost1_sem_ponto.isnumeric()

      
    if gas_valid1 == False:
        print("""   --- Por favor, digite um número válido! ---
               """)
  gasolina_posto_um = float(gaspost1_sem_virgula)
  gas_valid1 = ""

  while eta_valid1 != True:
    etapost1 = str(input(f"Qual o preço do Etanol no {str(posto_um)}?: "))
    etapost1_sem_virgula = etapost1.replace(",",".")
    etapost1_sem_ponto = etapost1_sem_virgula.replace(".","")

    if etapost1_sem_virgula == "0" or etapost1_sem_virgula == "0.0":
        eta_valid1 = False

    elif etapost1_sem_virgula != "0" or etapost1_sem_virgula != "0.0":
        eta_valid1 = etapost1_sem_ponto.isnumeric()

      
    if eta_valid1 == False:
        print("""   --- Por favor, digite um número válido! ---
               """)
  etanol_posto_um = float(etapost1_sem_virgula)
  eta_valid1 = ""

  while die_valid1 != True:
    diepost1 = str(input(f"Qual o preço do Diesel no {str(posto_um)}?: "))
    diepost1_sem_virgula = diepost1.replace(",",".")
    diepost1_sem_ponto = diepost1_sem_virgula.replace(".","")

    if diepost1_sem_virgula == "0" or diepost1_sem_virgula == "0.0":
        die_valid1 = False

    elif diepost1_sem_virgula != "0" or diepost1_sem_virgula != "0.0":
        die_valid1 = diepost1_sem_ponto.isnumeric()

      
    if die_valid1 == False:
        print("""   --- Por favor, digite um número válido! ---
               """)
  diesel_posto_um = float(diepost1_sem_virgula)
  die_valid1 = ""

  print(f"""O nome do posto e os preços foram digitados corretamente?
  Nome do posto: {posto_um}
  Gasolina: R${gasolina_posto_um}
  Etanol: R${etanol_posto_um}
  Diesel: R${diesel_posto_um}""")
  teste = input("Digite (S) caso esteja tudo correto ou digite (N) caso algum valor esteja incorreto: ")
teste = ""

while teste.upper() != "S":
  posto_dois = str(input("Insira o nome do segundo posto: "))
  while gas_valid2 != True:
    gaspost2 = str(input(f"Qual o preço da Gasolina no {str(posto_dois)}?: "))
    gaspost2_sem_virgula = gaspost2.replace(",",".")
    gaspost2_sem_ponto = gaspost2_sem_virgula.replace(".","")

    if gaspost2_sem_virgula == "0" or gaspost2_sem_virgula == "0.0":
        gas_valid2 = False

    elif gaspost2_sem_virgula != "0" or gaspost2_sem_virgula != "0.0":
        gas_valid2 = gaspost2_sem_ponto.isnumeric()

      
    if gas_valid2 == False:
        print("""   --- Por favor, digite um número válido! ---
               """)
  gasolina_posto_dois = float(gaspost2_sem_virgula)
  gas_valid2 = ""

  while eta_valid2 != True:
    etapost2 = str(input(f"Qual o preço do Etanol no {str(posto_dois)}?: "))
    etapost2_sem_virgula = etapost2.replace(",",".")
    etapost2_sem_ponto = etapost2_sem_virgula.replace(".","")

    if etapost2_sem_virgula == "0" or etapost2_sem_virgula == "0.0":
        eta_valid2 = False

    elif etapost2_sem_virgula != "0" or etapost2_sem_virgula != "0.0":
        eta_valid2 = etapost2_sem_ponto.isnumeric()

      
    if eta_valid2 == False:
        print("""   --- Por favor, digite um número válido! ---
               """)
  etanol_posto_dois = float(etapost2_sem_virgula)
  eta_valid2 = ""

  while die_valid2 != True:
    diepost2 = str(input(f"Qual o preço do Diesel no {str(posto_dois)}?: "))
    diepost2_sem_virgula = diepost2.replace(",",".")
    diepost2_sem_ponto = diepost2_sem_virgula.replace(".","")

    if diepost2_sem_virgula == "0" or diepost2_sem_virgula == "0.0":
        die_valid2 = False

    elif diepost2_sem_virgula != "0" or diepost2_sem_virgula != "0.0":
        die_valid2 = diepost2_sem_ponto.isnumeric()

      
    if die_valid2 == False:
        print("""   --- Por favor, digite um número válido! ---
               """)
  diesel_posto_dois = float(diepost2_sem_virgula)
  die_valid2 = ""

  print(f"""O nome do posto e os preços foram digitados corretamente?
  Nome do posto: {posto_dois}
  Gasolina: R${gasolina_posto_dois}
  Etanol: R${etanol_posto_dois}
  Diesel: R${diesel_posto_dois}""")
  teste = input("Digite (S) caso esteja tudo correto ou digite (N) caso algum valor esteja incorreto: ")
teste = ""

while teste.upper() != "S":
  posto_tres = str(input("Insira o nome do terceiro posto: "))
  while gas_valid3 != True:
    gaspost3 = str(input(f"Qual o preço da Gasolina no {str(posto_tres)}?: "))
    gaspost3_sem_virgula = gaspost3.replace(",",".")
    gaspost3_sem_ponto = gaspost3_sem_virgula.replace(".","")

    if gaspost3_sem_virgula == "0" or gaspost3_sem_virgula == "0.0":
        gas_valid2 = False

    elif gaspost3_sem_virgula != "0" or gaspost3_sem_virgula != "0.0":
        gas_valid3 = gaspost3_sem_ponto.isnumeric()

      
    if gas_valid3 == False:
        print("""   --- Por favor, digite um número válido! ---
               """)
  gasolina_posto_tres = float(gaspost3_sem_virgula)
  gas_valid3 = ""

  while eta_valid3 != True:
    etapost3 = str(input(f"Qual o preço do Etanol no {str(posto_tres)}?: "))
    etapost3_sem_virgula = etapost3.replace(",",".")
    etapost3_sem_ponto = etapost3_sem_virgula.replace(".","")

    if etapost3_sem_virgula == "0" or etapost3_sem_virgula == "0.0":
        eta_valid3 = False

    elif etapost3_sem_virgula != "0" or etapost3_sem_virgula != "0.0":
        eta_valid3 = etapost3_sem_ponto.isnumeric()

      
    if eta_valid3 == False:
        print("""   --- Por favor, digite um número válido! ---
               """)
  etanol_posto_tres = float(etapost3_sem_virgula)
  eta_valid3 = ""

  while die_valid3 != True:
    diepost3 = str(input(f"Qual o preço do Diesel no {str(posto_tres)}?: "))
    diepost3_sem_virgula = diepost3.replace(",",".")
    diepost3_sem_ponto = diepost3_sem_virgula.replace(".","")

    if diepost3_sem_virgula == "0" or diepost3_sem_virgula == "0.0":
        die_valid3 = False

    elif diepost3_sem_virgula != "0" or diepost3_sem_virgula != "0.0":
        die_valid3 = diepost2_sem_ponto.isnumeric()

      
    if die_valid3 == False:
        print("""   --- Por favor, digite um número válido! ---
               """)
  diesel_posto_tres = float(diepost3_sem_virgula)
  die_valid3 = ""

  print(f"""O nome do posto e os preços foram digitados corretamente?
  Nome do posto: {posto_tres}
  Gasolina: R${gasolina_posto_tres}
  Etanol: R${etanol_posto_tres}
  Diesel: R${diesel_posto_tres}""")
  teste = input("Digite (S) caso esteja tudo correto ou digite (N) caso algum valor esteja incorreto: ")
teste = ""

#_____________
while opcao != "4":
# Input da escolha do usuário no menu.
   opcao = str(input("""
- Escolha uma das opções abaixo - 
                  
   1 - Para fazer a consulta do posto mais em conta digite 1 e insira 
   o combustivel que deseja e quantos litros deseja abastecer.

   2 - Digite 2 para exibir a consulta e o posto com menor preço do seu combustível.

   3 - Digite 3 para exibir os postos e o valor de cada combustível. 

   4 - Ou digite 4 para sair da consulta.
                     
   Insira: """))

# Caso escolha a opção "1"
   if opcao == str(1):
    seu_combustivel = ""
    while seu_combustivel == "":
      combustivel = str(input("""
Qual o tipo de combustivel que deseja comprar?: 
1 - Gasolina
2 - Etanol
3 - Diesel 
Insira: """)).upper()

      if combustivel != "1" and combustivel != "2" and combustivel != "3" and str(combustivel).upper() != "GASOLINA" and str(combustivel).upper() != "ETANOL" and str(combustivel).upper() != "DIESEL":
        print("""
              Por favor insira um número válido ou o nome do combustível desejado!
              """)
        
      elif combustivel == "1" or str(combustivel).upper() == "GASOLINA":
         seu_combustivel = "Gasolina"
        
      elif combustivel == "2" or str(combustivel).upper() == "ETANOL":
         seu_combustivel = "Etanol"
    
      elif combustivel == "3" or str(combustivel).upper() == "DIESEL":
         seu_combustivel = "Diesel"        

# Atribuir o valor de um combustível especifico escolhido pelo usuario, para ser usado na comparação de preços.
    if seu_combustivel == "Gasolina":
      combposto1 = gasolina_posto_um
      combposto2 = gasolina_posto_dois
      combposto3 = gasolina_posto_tres
        
    elif seu_combustivel == "Etanol":
      combposto1 = etanol_posto_um
      combposto2 = etanol_posto_dois
      combposto3 = etanol_posto_tres
        
    elif seu_combustivel == "Diesel":
      combposto1 = diesel_posto_um
      combposto2 = diesel_posto_dois
      combposto3 = diesel_posto_tres

# Descobrir qual o combustível mais barato, o mais caro e o médio e atribuir a variáveis.
    while combbarato == 0 and combcaro == 0:
      if combposto1 == combposto2 and combposto1 == combposto3 and combposto2 == combposto3 and combposto2 == combposto1:
        posto_barato = str(posto_um)
        combbarato = combposto1

        posto_medio = str(posto_dois)
        combmedio = combposto2

        posto_caro = str(posto_tres)
        combcaro = combposto3

# Caso sejam diferentes o codigo define qual ocupa qual posição em relação a seu preço.
      elif combposto1 <= combposto2 and combposto1 <= combposto3:
        posto_barato = str(posto_um)
        combbarato = combposto1

      elif combposto2 <= combposto1 and combposto2 <= combposto3:
        posto_barato = str(posto_dois)
        combbarato = combposto2

      else:
        posto_barato = str(posto_tres)
        combbarato = combposto3

      if combcaro == "":
        if combposto1 >= combposto2 and combposto1 >= combposto3:
          posto_caro = str(posto_um)
          combcaro = combposto1

        elif combposto2 >= combposto1 and combposto2 >= combposto3:
          posto_caro = str(posto_dois)
          combcaro = combposto2

        else:
          posto_caro = str(posto_tres)
          combcaro = combposto3

# Aqui encontro o combustível médio fazendo uma conta básica.
    combmedio = round(combposto1 + combposto2 + combposto3 - combbarato - combcaro,2)

# A parte abaixo define o nome do posto médio. Pois não consigo fazer a mesma conta usando uma string.
    posto_medio = posto_um
    while str(posto_medio) == str(posto_caro) or posto_medio == str(posto_barato):
      if str(posto_medio) == str(posto_caro) or posto_medio == str(posto_barato):
         posto_medio = posto_um
      
      if str(posto_medio) == str(posto_caro) or posto_medio == str(posto_barato):
         posto_medio = posto_dois
    
      if str(posto_medio) == str(posto_caro) or posto_medio == str(posto_barato):
         posto_medio = posto_tres

# Pedir o input dos litros desejados e verificar se o usuário colocou realmente um número,
# Substituir virgula por ponto para cálculo futuro.

    while validacao != True: 
        litros = str(input(f"E quantos litros de {seu_combustivel} deseja abastecer?: "))
        litros_sem_virgula = litros.replace(",",".")
        litros_sem_pontos = litros_sem_virgula.replace(".","")
        litros = litros_sem_virgula

        if litros_sem_virgula != "0" or litros_sem_virgula != "0.0":
            validacao = litros_sem_pontos.isnumeric()

        if litros_sem_virgula == "0" or litros_sem_virgula == "0.0":
            validacao = False
          
        if validacao == False:
            print("""   --- Por favor, digite um número válido! ---
                  """)
    validacao = False
         
# Caso selecione "2" no Menu.
   elif opcao == "2":
    # Verificar se a opção "1" ja está preenchida e apresentar a pesquisa.
    if seu_combustivel != "":
      print(f"""De acordo com a pesquisa realizada, os preços de 1L de {seu_combustivel} em cada posto:
{posto_barato}: R${round(combbarato,2)}
{posto_medio}: R${round(combmedio,2)}
{posto_caro}: R${round(combcaro,2)}
           
O preço de {litros_sem_virgula} litros de {seu_combustivel} em cada posto do mais barato para o mais caro é respectivamente:
{posto_barato}: R${round(combbarato * float(litros_sem_virgula),2)}
{posto_medio}: R${round(combmedio * float(litros_sem_virgula),2)}
{posto_caro}: R${round(combcaro * float(litros_sem_virgula),2)}
      
      """)
# Verificar se há postos com preços iguais para que o usuário escolha onde abastecerá.
# Apresentar quanto seria economizado em relação aos outros.
      while break_ == 0:
        if combbarato == combcaro:
          print(f"""Os postos têm o mesmo valor entre si. Infelizmente não há como economizar. ,_,""")
          while escolha == "":
             escolha = str(input(f"Qual dos 3 postos você deseja? O {posto_barato}-(1), o {posto_medio}-(2) ou o {posto_caro}-(3)?: "))
             if escolha != "1" and escolha != "2" and escolha != "3" and str(escolha.lower()) != str(posto_barato.lower()) and str(escolha.lower()) != str(posto_medio.lower()) and str(escolha.lower()) != str(posto_caro.lower()):
              print("Por favor, digite 1,2 ou 3, ou o nome do posto desejado!")
              escolha = ""


        elif combbarato == combmedio and combbarato != combcaro:
          print(f"""
O {posto_barato} e o {posto_medio} têm o mesmo valor de {seu_combustivel}.
Em relação ao {posto_caro} você economizaria: R${round((combcaro*float(litros_sem_virgula)) - (combbarato*float(litros_sem_virgula)),2)}""")
                
          while escolha == "":
            escolha = str(input(f"Qual dos dois postos você deseja? O {posto_barato}(1) ou o {posto_medio}(2)?: "))
            if escolha != "1" and escolha != "2" and str(escolha.lower()) != str(posto_barato.lower()) and str(escolha.lower()) != str(posto_medio.lower()):
              print("Por favor, digite 1 ou 2, ou o nome do posto desejado!")
              escolha = ""
        
        elif combbarato != combmedio and combbarato != combcaro:
          print(f"""Comprando {seu_combustivel} no {posto_barato}:
Você economizaria R${round((combmedio*float(litros_sem_virgula)) - (combbarato*float(litros_sem_virgula)),2)} em relação ao {posto_medio}.
E economizaria R${round((combcaro*float(litros_sem_virgula)) - (combbarato*float(litros_sem_virgula)),2)} em relação ao {posto_caro}""")
          
          
# Atribuir o valor de vezes que cada posto foi mais barato e a litragem que seria comprada.
      # Caso o usuário tenha escolhido algum que tinha preço igual a outro.
        if escolha == "1" or str(escolha.lower()) == str(posto_barato.lower()):
          vzsbarato1 += 1
          litrospost1 += float(litros_sem_virgula)
          escolha = ""
          break_ = 1
          
        elif escolha == "2" or str(escolha.lower()) == str(posto_medio.lower()):
          vzsbarato2 += 1
          litrospost2 += float(litros_sem_virgula)
          escolha = ""
          break_ = 1

        elif escolha == "3" or str(escolha.lower()) == posto_caro.lower():
          vzsbarato3 += 1
          litrospost3 += float(litros_sem_virgula)
          escolha = ""
          break_ = 1

        else:
          print("""Por favor digite o nome do posto!
          """)
        # Em caso de preços diferentes.
          if posto_barato == posto_um:
            vzsbarato1 += 1
            litrospost1 += float(litros_sem_virgula)
          elif posto_barato == posto_dois:
            vzsbarato2 += 1
            litrospost2 += float(litros_sem_virgula)
          elif posto_barato == posto_tres:
            vzsbarato3 += 1
            litrospost3 += float(litros_sem_virgula)
            
          break_ = 1
      break_ = 0

    # Atribuir +1 à contagem de consultas.
      consultas += 1

  # Retornar o usuário ao Menu
    elif seu_combustivel == "":
      print("Insira um combustível e a quantidade que deseja primeiro! (Utilize a opção 1)")
    
# Apresentar  as informações coletadas dos postos, e adicionar +1 ao numero de consultas.
   elif opcao == "3":
     print(f"""A lista dos postos e seus respectivos preços é: 
     {posto_um}: 
     Gasolina - R${round(gasolina_posto_um,2)}
     Etanol - R${round(etanol_posto_um,2)}
     Diesel - R${round(diesel_posto_um,2)}
         
     {posto_dois}:
     Gasolina - R${round(gasolina_posto_dois,2)} 
     Etanol - R${round(etanol_posto_dois,2)}
     Diesel - R${round(diesel_posto_dois,2)}

     {posto_tres}:
     Gasolina - R${round(gasolina_posto_tres,2)}
     Etanol - R${round(etanol_posto_tres,2)}
     Diesel - R${round(diesel_posto_tres,2)}""")

     consultas += 1

#_____________________________________________________________________________________________
# Definir o posto com gasolina mais barata.
if gasolina_posto_um == gasolina_posto_dois == gasolina_posto_tres:
   postogasbarata = "Todos"
   postogascara = "Todos"
else:
  if gasolina_posto_um <= gasolina_posto_dois and gasolina_posto_um <= gasolina_posto_tres:
    gasbarato = gasolina_posto_um
    postogasbarata = posto_um
        
  elif gasolina_posto_dois <= gasolina_posto_um and gasolina_posto_dois <= gasolina_posto_tres:
    gasbarato = gasolina_posto_dois
    postogasbarata = posto_dois

  else:
    gasbarato = gasolina_posto_tres
    postogasbarata = posto_tres

  # Definir o posto com gasolina mais cara.
  if gasolina_posto_um >= gasolina_posto_dois and gasolina_posto_um >= gasolina_posto_tres:
    gascaro = gasolina_posto_um
    postogascara = posto_um

  elif gasolina_posto_dois >= gasolina_posto_um and gasolina_posto_dois >= gasolina_posto_tres:
    gascaro = gasolina_posto_dois
    postogascara = posto_dois

  else:
    gascaro = gasolina_posto_tres
    postogascara = posto_tres

#_____________________________________________________________________________________________
# Definir o posto com etanol mais barato.
if etanol_posto_tres == etanol_posto_dois == etanol_posto_um:
   postoetabarato = "Todos"
   postoetacaro = "Todos"

else:
  if etanol_posto_um <= etanol_posto_dois and etanol_posto_um <= etanol_posto_tres:
    etabarato = etanol_posto_um
    postoetabarato = posto_um
        
  elif etanol_posto_dois <= etanol_posto_um and etanol_posto_dois <= etanol_posto_tres:
    etabarato = etanol_posto_dois
    postoetabarato = posto_dois

  else:
    etabarato = etanol_posto_tres
    postoetabarato = posto_tres

  # Definir o posto com etanol mais caro.
  if etanol_posto_um >= etanol_posto_dois and etanol_posto_um >= etanol_posto_tres:
    etacaro = etanol_posto_um
    postoetacaro = posto_um

  elif etanol_posto_dois >= etanol_posto_um and etanol_posto_dois >= etanol_posto_tres:
    etacaro = etanol_posto_dois
    postoetacaro = posto_dois

  else:
    etacaro = etanol_posto_tres
    postoetacaro = posto_tres

#_____________________________________________________________________________________________
# Definir o posto com diesel mais barato.
if diesel_posto_um == diesel_posto_dois == diesel_posto_tres:
   postodiebarato = "Todos"
   postodiecaro = "Todos"
else:
  if diesel_posto_um <= diesel_posto_dois and diesel_posto_um <= diesel_posto_tres:
    diebarato = diesel_posto_um
    postodiebarato = posto_um
        
  elif diesel_posto_dois <= diesel_posto_um and diesel_posto_dois <= diesel_posto_tres:
    diebarato = diesel_posto_dois
    postodiebarato = posto_dois

  else:
    diebarato = diesel_posto_tres
    postodiebarato = posto_tres

  # Definir o posto com diesel mais caro.
  if diesel_posto_um >= diesel_posto_dois and diesel_posto_um >= diesel_posto_tres:
    diecaro = diesel_posto_um
    postodiecaro = posto_um

  elif diesel_posto_dois >= diesel_posto_um and diesel_posto_dois >= diesel_posto_tres:
    diecaro = diesel_posto_dois
    postodiecaro = posto_dois

  else:
    diecaro = diesel_posto_tres
    postodiecaro = posto_tres
#_____________________________________________________________________________________________

# Verificar se algum posto não foi mais barato para não dividir por zero.
# Calcular a média de litros. Ou definir a média como zero.
if vzsbarato1 != 0:
   mediaposto1 = litrospost1 / vzsbarato1
elif vzsbarato1 == 0:
  mediaposto1 = "0"
if vzsbarato2 != 0:
  mediaposto2 = litrospost2 / vzsbarato2
elif vzsbarato2 == 0:
  mediaposto2 = "0"
if vzsbarato3 != 0:
  mediaposto3 = litrospost3 / vzsbarato3
elif vzsbarato3 == 0:
  mediaposto3 = "0"

# Agradecer ao Usuário
print("""
------ Obrigado por utilizar nosso programa! ------ """)
# Apresentar as quatro informações finais ao fechar o programa.
print(f"""
Relatório:
* Número de consultas realizadas: {consultas}.

* Quantidade de vezes com menor valor de combustível:
{posto_um}: {vzsbarato1}.
{posto_dois}: {vzsbarato2}.
{posto_tres}: {vzsbarato3}.

* Média de litros consultado por posto:
{posto_um}: {round(float(mediaposto1),2)}L;
{posto_dois}: {round(float(mediaposto2),2)}L;
{posto_tres}: {round(float(mediaposto3),2)}L;

* Relação por combustivel, do posto que possui o menor valor e o maior valor:
*GASOLINA*
O posto com menor valor de gasolina é:
{postogasbarata}
O posto com maior valor de gasolina é:
{postogascara}

*ETANOL*
O posto com menor valor de etanol é:
{postoetabarato}
O posto com maior valor de etanol é:
{postoetacaro}

*DIESEL*
O posto com menor valor de diesel é:
{postodiebarato}
O posto com maior valor de diesel é:
{postodiecaro}.
""")
# Cabô professora <3 
# 1° Código grandinho e todo corrigido.