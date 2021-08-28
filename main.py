#SISTEMA DE CADASTRO DE CLIENTE - SCC 1.0
import os
import time
import getpass

class Cliente(): #Classe vai receber os dados do cliente
  def __init__(self,cpf, nome, telefone, email):
    self.cpf = cpf
    self.nome = nome
    self.telefone = telefone
    self.email = email
    
  def printCliente(self): #imprime as informações coletadas na tela.
    print(f'{"Nome: ":<11}{self.nome:<10}')
    print(f'{"CPF: ":<11}{self.cpf:<10}')
    print(f'{"Telefone: ":<11}{self.telefone:<10}')
    print(f'{"Email: ":<11}{self.email:<10}')
#-----------------------------------------------*

listaClientes = [] #Vai armazenar as informações dos clientes
cad = 1 #Contador de cadastros, incrementa a cada cadastro realizado
def cabecalho(): #Informações e boas vindas
  os.system('clear')
  print("\n\t\t-=-=-=-=-= SCC v1.0 -=-=-=-=-= ")
  print("\n\t** MARCCOS DISTRIBUIDORA DE ALIMENTOS E CIA LTDA **")
  print("\t\t\t\tAv. 2 de Julho, Centro")
  print("\t\t- Onde tudo que você precisa custa barato -")
  print("")
  print("-=*"*18)
  print("")
  print("\n\t\t\t -=-= Seja bem vindo -=-=")
  print("")

def menu(): #Menu de acesso à opções do sistema.
  while(True):
    cabecalho()
    print("\n\t[1] - Inserir Cliente\n\t[2] - Listar Clientes\n\t[3] - Pesquisar Cliente\n\t[4] - Excluir Cliente\n\t[5] - Sobre o programa\n\t[6] - Manual do Usuário\n\t[7] - FAQ\n\t[8] - Sair")
  
    opcao = int(input("\nEscolha uma opção: ")) # usuário escolhe a opção
    if opcao == 1:
      inserirCliente()
    if opcao == 2:
      listarClientes() 
    if opcao == 3:
      pesquisarCliente()
    if opcao == 4:
      excluirCliente()
    if opcao == 5:
      sobrePrograma()
    if opcao == 6:
      manualUsuario()
    if opcao == 7:
      faq()
    elif opcao == 8:
      sair()
      os.system('clear') #limpa a tela
      break
  else:
    print("[!] Opção inválida!") # caso digite uma opção que não esteja disponível
  os.system('clear') 

def inserirCliente(): #solicita e amazena as informações  dos clientes até que a tecla 'N' seja precionada
  global cad #interação de cadastros
  while(True):
    os.system('clear')
    print("\t\t *** CADASTRO DE CLIENTE ***")
    print("\nCadastro Nº",cad)
    cpf = leiaInt("CPF: ") #função que verifica se foi digitado realmente um inteiro
    for i in listaClientes: #varre os itens da lista
      if cpf == i.cpf: #compara os itens da lista com o digitado
        print("\n[!]Cliente já cadastrado!")
        time.sleep(3)
        return     
    nome = input("Nome: ")
    telefone = int(input("Telefone: "))
    email = input("Email: ")
  
    cli = Cliente(cpf, nome, telefone, email)
    listaClientes.append(cli) #os dados coletados são armazenados numa lista
    cad += 1 #incremeto dos cadastros

    print("\nCadastrar outro cliente?")
    opc = input("* Aperte qualquer tecla para continue ou [N] para voltar: ")#encerra o loop de cadastro
    if opc == 'N' or opc == 'n':
      break

def listarClientes(): # verifica e lista os clientes cadastrados
  os.system('clear')
  print("\n\t\t *** LISTA DE CLIENTES ***")
  if len(listaClientes) == 0: #conta os itens da lista
    print("\n\t[!] Nenhum cliente Cadastrado")
    time.sleep(3)
  else:
    print("")
    print("-=*"*15)
    for i in listaClientes: #imprime a lista
      print("")
      i.printCliente()
      print("")
      print("-=*"*15)

    input("\n\n[*_*] Precione qualquer tecla para voltar ")

def pesquisarCliente(): #Busca um cliente na lista e retorno seus dados
  os.system('clear')
  print("\n\t\t *** PESQUISA DE CLIENTE ***")
  if len(listaClientes) == 0:
    print("\n\t[!] Nenhum cliente Cadastrado")
    time.sleep(3)
  else:
    esc = int(input("\nFiltro da pesquisa\n\n\t[1]-Nome\n\t[2]-CPF\n\nOpção:  "))
    if esc == 1:
      nPesq = input("\n\nDigite o nome do cliente: ")
      os.system('clear')
      print("\n\t\t*** RESULTADO PESQUISA ***")
      for i in listaClientes:
        if nPesq == i.nome:
          print("*****"*10)
          print("")
          i.printCliente()
          print("")
          print("*/*/*"*10)

          input("\n[*_*] Precione qualquer tecla para voltar ")# se precionada, realizará outro cadastro
          return
        
      print("\n[!]Cliente com este nome não encontrado! ")
      time.sleep(3)
        #return cabecalho()

    if esc == 2:
      cPesq = int(input("Digite o CPF do cliente: "))
      os.system('clear')
      print("\n\t\t*** RESULTADO PESQUISA ***")

      for i in listaClientes:
        if cPesq == i.cpf:      
          print("*****"*10)
          i.printCliente()
          print("*/*/*"*10)

          input("\n[*_*] Precione qualquer tecla para voltar ")# se precionada, realizará outro cadastro
          return

      print("\n[!] Cliente com este CPF não encontrado!")
      time.sleep(5)
    else:
      print("[!]Opção Inválida!")

def excluirCliente():#excluir algum cliente da lista, caso necessário
  os.system('clear')
  print("\n\t\t*** EXCLUIR CLIENTE ***")
  if len(listaClientes) == 0:
    print("\n\t[!] Nenhum cliente Cadastrado")
    time.sleep(3)
  else:
    cpfCli = int(input("\nDigite o CPF do cliente: "))
    for item in listaClientes:
      if cpfCli == item.cpf:
        listaClientes.remove(item) #remove item encontrado
        print("\n[*_*] Cliente removido com sucesso!")

def manualUsuario(): #as principais funcionalidades do programa 
  os.system('clear')
  print("\n\t *** MANUAL DO USUÁRIO ***")
  print("\n! Aqui você encontra o manual do nosso programa")
  print("\n- Para iniciar o programa, digite o login e a senha.")
  print("- OBS: Se o usuário ou a senha for digitado incorretamente por 5 vezes o usuário será bloqueado. Pare restabelecer o acesso entre em contato com o administrador.")
  print("\n- Ao abrir o sistem aparece um menu. Digite a opção desejada.")
  print("\n-Insira todas as informações pedidas.")
  print("\n- Após o cadastro, na tela aparecerá uma mensagem para, caso desejar, cadastrar outro cliente. Se for o seu desejo faça o que ela pede. ")
  print("\n- Caso não queira realizar outro cadastro, clique na opção para voltar ao menu inicial")
  print("\n- Na opção Listar Clientes, será mostrado todos os clientes armazenados até agora. ")
  print("\n- Na opção Pesquisar Clientes, você escolherá algum cliente que deseje visualizar as informações. Pode fazer a pesquisa pelo nome ou CPF do cliente.")
  print("\n- Caso deseje excluir algum cliente, selecione a opção Excluir Cliente no menu e coloque o cliente que queira tirar da lista. ")
  print("\n- Na opção Sobre o Programa, poderá encontrar informações sobre o nosso programa. ")
  print("\n- Se precisar do manual, selecione a opção 6.")
  print("\n- Dúvidas? Selecione a opção 7, e lá você encontra as perguntas que são frequentes. Quem sabe alguma poderá te ajudar! ")
  print("\n- Para fechar o programa, selecione a opção Sair no menu. ")
  
  input("\n\n[*_*] Digite qualquer tecla para retornar")

def faq(): #repostas às perguntas mais conus sobre o programa
  os.system('clear')
  print("\t****** PERGUNTAS FREQUENTES ******")  
  print("\n1- Onde eu acho o login e a senha?")
  print("- Eles serão enviados pelo email ou telefone que forem informados.")
  print("\n2-  Por que a senha não aparece na tela de login?")
  print("-  Ela não aparece por motivo de segurança.")
  print("\n3- Quero fazer outro cadastro, como faço? ")
  print("-  É só selecionar no menu a opção Inserir Clientes. ")
  print("\n4- Como saber os clientes que estão na lista?")
  print("- Basta seleciona a opção Listar Clientes e os que estiverem na lista vão aparecer. ")
  print("\n5- Como excluir algum cliente da lista? ")
  print("- Selecione a opção Excluir Cliente.")
  
  input("\n\n[*_*] Digite qualquer tecla para retornar")
  
def sobrePrograma(): # informações sobre o programa
  os.system('clear')
  print("\n\t * SCC - Sistema de Cadastramento de Clientes * ")
  print("\nVersão 1.0 - Agosto 2021")
  print("Licença: Teste - Atividade do Curso de Programador de Sistemas - SENAC/Bahia")
  print("Idealizadores: Willa Almeida e Adaias dos Reis")
  print("Docência: Rafeael Santos")
  print("\nObrigado por usar nosso sistema")
  print("\n\t\t ***** DONATE ***** ")
  input("\n\nPrecione qualquer tecla para voltar ")
  os.system('clear') 

def credUser(): #credenciais de acessoa ao sistema
  user = "marccos"
  senha = '123456'
  pWord = 0
  tLogin = 1

  while(tLogin < 6): #loop de tentativas de login incorreto
    print("\n\t\t-=-=-=-=-= SCC v1.0 -=-=-=-=-= ")
    print("")
    print("Tentativa: ",tLogin)
    login = input("Digite seu usuário: ")
    if (login != user):
      print("\n\t[!] Usuário incorreto, tente novamente.\n")
      time.sleep(3)
      os.system('clear')
      tLogin += 1 #incremento das tentativas de login
    else:
      pWord = getpass.getpass('Digite sua senha: ')#impede a exibição do que é digitado
      if (pWord != senha):
        print("\n\t[!] Senha incorreta, tente novamente.")
        time.sleep(3)
        os.system('clear')
        tLogin += 1
      else:
        print("")
        print("\n\t[*_*] Login realizado com sucesso!")
        time.sleep(3)
        os.system('clear')
        menu() #inicia o progrma depois do login
        break       
  else:  
    print("\n\t\t\t\t[!!!]\n\nDesculpe pelo inconveniente!\n\nVocê atingiu o número máximo de tentativas. \n\nEntre em contato com o administrador do sistema")
    time.sleep(5)
    os.system('clear')

def sair(): # encerrará o programa
  os.system('clear')
  print("\n\tObrigado pela preferência!\n\t\t\tVolte sempre!")
  print("")
  print("")
  print("\t *** Sistema Desligando... ***")
  time.sleep(5)

def leiaInt(msn): #função para verificar se foi digitado um numero inteiro
  numInt = False
  num = 0
  while True:
    x = str(input(msn))
    if x.isnumeric():
      num = int(x)
      numInt = True
    else:
      print("\n[!] Por favor, digite só os números.")
      time.sleep(2)
    if numInt:
      break
  return num
  
credUser()