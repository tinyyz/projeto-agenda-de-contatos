import pywhatkit as kit
import datetime

def menu():
    opcao = input('''
.......................................................
                 Agenda de Contatos 
Menu
[1] Cadastrar Contato
[2] Listar Contato
[3] Deletar Contato                                 
[4] Buscar Contato
[5] Sair
.......................................................                   
Escolha uma opção acima: ''')
    if opcao == "1":
       cadastrarContato()
    elif opcao == "2":
       listarContato()
    elif opcao == "3":
       deletarContato() 
    elif opcao == '4':
       buscarContato()  
    else:
        sair()  

def cadastrarContato(): 
    f = datetime.datetime.now() + datetime.timedelta(seconds=15)
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
        #kit.sendwhatmsg("+55{telefone.replace("-","").replace(" ","")}", "Olá {nome}, seja bem-vindo na minha lista de contato. =D", f.hour, f.minute,15,True,3)
        #kit.sendwhatmsg("+5515997863013", "oiiiii",  f.hour, f.minute,15,True,31) 
    except:
        print('ERRO!! Contato NÃO gravado.')    

def listarContato():
    agenda = open ("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()
    
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