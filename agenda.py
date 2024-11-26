import pywhatkit as kit
import datetime

def menu():
    opcao = input('''
.......................................................
                 Agenda de Contatos 
Menu
[1] Cadastrar Contato.
[2] Listar Contato.
[3] Deletar Contato.                                 
[4] Buscar Contato.
[5] Sair.
.......................................................                   
Escolha uma opção acima: ''')
    while opcao != "5":
        if opcao == "1":
            cadastrarContato()
        elif opcao == "2":
            listarContato()
        elif opcao == "3":
            deletarContato() 
        elif opcao == '4':
            buscarContato()  
        elif opcao =='5':
            sair()
        else:
            print ("Erro!") 

def cadastrarContato(): 
    cadastrado=False
    identificacao = input("Escolha a identificação do contato: ")
    nome = input ("Informe o nome do contato: ")
    telefone = input ("Informe o número de telefone do contato: ")
    email = input ("Informe o e-mail do contato: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{identificacao.upper()}; {nome.upper()}; {telefone}; {email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso!!')
        cadastrado=True     
    except:
        print('ERRO!! Contato NÃO gravado.')    
    if cadastrado:
        f = datetime.datetime.now() + datetime.timedelta(seconds=61)
        kit.sendwhatmsg(f"+55{telefone.replace("-","").replace(" ","")}", f"Olá {nome}, seja bem-vindo na minha lista de contato. =D", f.hour, f.minute,15,True,3)

def listarContato():
    agenda = open ("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()

def organizarLista(): 
    with open('agenda.txt', 'r') as agenda:
        antes_de_organizar = agenda.readlines()
        contato_organizados = sorted(antes_de_organizar, key=lambda x: x.split(";"[0]))
        print(contato_organizados)

def deletarContato():
    nomeDeletado = input("Informe o nome para deletar o contato: ")
    agenda = open ("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range (0, len(aux)):
        if nomeDeletado.upper() not in aux [i].upper():
            aux2.append(aux[i])   
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!!')
    listarContato

def buscarContato():
    nome = input(f"Infome o nome a ser procurado: ")
    agenda = open ("agenda.txt", "r")
    for contato in agenda:
        if nome in contato.split(";")[1]:
            print(contato)
    agenda.close()  

def sair():
    print(f'Até a próxima!')
    exit()      

def main():
    menu()

main()