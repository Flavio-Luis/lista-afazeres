import os

backup_directory = "C:\\Users\\lista\\backup.txt" # diretório do arquivo

def create_file(): # function que cria o arquivo backup_.txt
    if not os.path.exists(backup_directory):
        os.makedirs(os.path.dirname(backup_directory),exist_ok=True)
        with open(backup_directory, "w") as create_file_backup:
           ...

def undo(lista): # function que retira da lista o atribui esse valor a function que escreve no backup.txt
    try:
        backup_activities = lista.pop()
        backup_activity(backup_activities)
    except IndexError:
        print("\nNão há Tarefas a serem desfeitas!⚠️")
        return lista

def backup_activity(backup_activities): # function que recebe um valor e escreve no meu arquivo backup.txt
    with open(backup_directory, "a") as backup_files: 
        backup_files.write(f"{backup_activities}\n")

def backup_read(): # function que lê o arquivo
    with open(backup_directory, "r") as file_read:
        rows = file_read.readlines()
    return rows

def atribuir_arquivo(): # function que atribui o arquivo lido a uma variavel
    last_data = backup_read()
    if last_data != []:
        given_treaty = last_data[-1].strip()
        return given_treaty
    else:
        given_treaty = None
        return given_treaty

def add_data(lista,remake): # function que acrescenta dados na lista real
    lista.append(remake)
    return lista

def modify_backup(): # function que retorna a variavel com todos os dados que devem ficar no backup após desfazer algum movimento
    del_last_data = backup_read()
    del_last_data.pop()
    
    return del_last_data
    
def resetar_backup(modify_backup): # function que reseta meu arquivo backup.txt e deixa somente os arquivos que não foram refeitos
    with open(backup_directory, "w") as resetar:
        resetar.writelines(modify_backup)
    
def lista(command,lista=[]): # function que realiza os comandos na lista
    match command:
        case "listar":
           exibition(lista)
        case "desfazer":
            undo(lista)
        case "refazer":
            remake = atribuir_arquivo()
            if remake is not None:
                lista = add_data(lista,remake)
                resetar_backup(modify_backup())
            else:
                print("\nNão há tarefas a serem refeitas!⚠️")
        case _:
            lista.append(command)
    return lista

def exibition(lista): # function que exibe minha lista com as atividades separas em cada linha e enumeradas
    cont = 0
    print("\nTAREFAS:")
    for i in lista:
        cont += 1
        print(f"{cont}° {i}")
    print()

create_file() # chamada da fucntion que cria o arquivo backup.txt

while True: # loop do programa
    
    print("Comandos: listar, desfazer, desfazer") 
    my_list = lista(input("Digite uma tarefa ou comando: "))
    
    exibition(my_list) # exibição da minha lista separando as atividades em cada linha