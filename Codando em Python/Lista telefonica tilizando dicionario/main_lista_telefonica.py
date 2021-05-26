from sys import exit
import string

# menu
def menu(lt_dict):
    print(" =========== LISTA TELEFONICA ===========")
    print(" = 1 - Ver lista                        =")
    print(" = 2 - Adicionar contato                =")
    print(" = 3 - Excluir contato                  =")
    print(" = 4 - Excluir lista                    =")
    print(" = 5 - Sair                             =")
    print(f" {40*'='}")

    while True:
        try:
            escolha = int(input(" > "))
            if 0 < escolha < 6:
                break
            else:
                print("\n # Opcao invalida #")
        except ValueError:
            print("\n # Digite um valor valido #")
        
    if escolha == 1:
        ver_lista(lt_dict)
    elif escolha == 2:
        add_contato(lt_dict)
    elif escolha == 3:
        del_contato(lt_dict)
    elif escolha == 4:
        del_lista(lt_dict)
    elif escolha == 5:
        print("\n === Finalizando o programa ===\n")
        exit(0)
        
# inicialização
def inicializar():
    try:
        arquivo = open("Lista telefonica.txt", "a")
        arquivo.close()
    except:
        print(" # Erro ao abrir lista telefonica #")
        
    try:
        arquivo = open("Lista telefonica.txt", "r")
        lt_list = list(arquivo)
        arquivo.close()
    except:
        print(" # Erro ao ler lista telefonica #")
        exit()
    
    lt_dict = {}
    contato = {}
    chaves = list(string.ascii_uppercase)
    for chave in chaves:
       lt_dict[chave] = []
       for linha in lt_list:
           if linha[0].upper() == chave:
               linha = linha.strip('\n').split(',')
               contato['Nome'] = linha[0]
               contato['Numero'] = linha[1]
               lt_dict[chave].append(contato.copy())            
    return lt_dict

# visualizar lista telefonica
def ver_lista(lt_dict):
    print(" =============== CONTATOS ===============")
    for chave in lt_dict:
        print(f"\n - {chave} -\n")
        for contato in lt_dict[chave]:
            print(f" Nome: {contato['Nome']} | Numero: {contato['Numero']}")
    print(f"\n {40*'='}\n")
    menu(lt_dict)

# adicionar contato na lista telefonica
def add_contato(lt_dict):
    print(" =========== ADICIONAR CONTATO ==========")
    while True:
        nome = str(input(" - Digite um nome valido: "))
        if nome != '':
            if nome[0].upper() in lt_dict.keys():
                break
   
    while True:
        try:
            numero = str(input(" - Digite um numero valido (somente numeros): "))
            if len(numero) >= 8:
                if int(numero):
                    break
            else:
                print("\n # O numero deve conter no minimo 8 digitos #")
        except ValueError:
                print("\n # Numero invalido #")
                
    if {'Nome': nome, 'Numero': numero} in lt_dict[nome[0].upper()]:
        print("\n # Contato ja esta salvo na lista! #")
    else:
        try:
            lt_dict[nome[0].upper()].append({'Nome': nome, 'Numero': numero})
            arquivo = open("Lista telefonica.txt", "a")
            arquivo.write(f"{nome},{numero}\n")
            arquivo.close()
            print("\n - Contato salvo com sucesso!\n")
        except:
            print("\n # Erro ao adicionar contato #\n")
    menu(lt_dict)

# deletar contato da lista telefonica
def del_contato(lt_dict):
    nome = str(input(" - Digite o nome do contato para a exclusão: "))
    if nome != '':
        if nome[0].upper() in lt_dict.keys():
            numero = str(input(" - Digite o numero do contato para a exclusão: "))
            if {'Nome': nome, 'Numero': numero} in lt_dict[nome[0].upper()]:
                try:
                    lt_dict[nome[0].upper()].remove({'Nome': nome, 'Numero': numero})
                    arquivo = open("Lista telefonica.txt", "w")
                    for lista in lt_dict.values():
                        for contato in lista:
                            if contato['Nome'] != nome and contato['Numero'] != numero:
                                arquivo.write(contato['Nome'] + "," + contato['Numero'] + "\n")
                                arquivo.close()
                    print("\n - Contato excluido com sucesso!\n")
                except:
                    print("\n # Erro ao excluir contato #\n")
            else:
                print("\n # Este contato nao existe na agenda #\n")
        else:
            print("\n # Nome invalido #\n")
    else:
        print("\n # Erro ao excluir contato #\n")
    menu(lt_dict)
   
# deletar lista telefonica
def del_lista(lt_dict):
    try:
        arquivo = open("Lista telefonica.txt", "w")
        arquivo.close()
        chaves = list(string.ascii_uppercase)
        for chave in chaves:
            lt_dict[chave] = []
        print("\n - Lista excluída com sucesso!\n")
    except:
        print("\n # Falha ao excluir lista telefonica #")
    menu(lt_dict)

# main
lista_telefonica = inicializar()
menu(lista_telefonica)
