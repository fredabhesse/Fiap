# DESCRIÇÃO: Projeto de nivelamento em linguagens de computação, o objetivo é criar uma agenda que possua menu com as
# opções de cadastro, edição, pesquisa, listagem e exclusão de contatos.

# definindo funções necessárias

# Descrição: cria uma sublista de usuários para busca de contatos através do índice
# Nome: get_user
# Tipo: Procedimento
def get_user():
    lista = []
    for elem in listaUsuario:
        lista.append(elem[0])
    try:
        index = lista.index(input("Digite o nome do usuário procurado:"))
    except ValueError:
        print("Usuário não existe.")
        return get_user()
    return index


# Descrição: Exibe os dados de um usuário através do número de índice
# Nome: show_user
# Tipo: Procedimento
def show_user():
    index = get_user()
    i = listaUsuario[index]
    print(f"Nome.....:{i[0]}\nCelular..:{i[1]}\nE-mail...:{i[2]}\n--------------------------")
    return index


# Descrição: Aguarda o input de qualquer dado para exibir o menu principal
# Nome: wait_prompt()
# Tipo: Procedimento
def wait_prompt():
    input("Pressione qualquer tecla para continuar")
    print("\n" * 30)
    menu()


# Descrição: Exibe o menu de opções
# Nome: menu()
# Tipo: Procedimento
def menu():
    select = int(input("\n ********** M E N U **********\n1 - Adicionar novo contato\n2 - Editar contato\n3 - "
                       "Pesquisar contato\n4 - Lista de contatos\n5 - Apagar um contato\n6 - Sair\n\n"
                       "Escolha um opção: "))
    if select == 1:  # Adicionar
        print("\n" * 30)
        add_user()
    elif select == 2:  # Editar
        print("\n" * 30)
        edit_user()
    elif select == 3:  # Pesquisar
        print("\n" * 30)
        print("---------MODO DE PESQUISA")
        show_user()
        wait_prompt()
        menu()
    elif select == 4:  # Listar
        print("\n" * 30)
        list_users()
    elif select == 5:  # Deletar
        print("\n" * 30)
        print("---------MODO DE EXCLUSÃO")
        delete_user()
    elif select == 6:  # Sair
        print("\n" * 30)
        print("OBRIGADO POR UTILIZAR NOSSA AGENDA")
    else:
        print("Opção não existe")
        wait_prompt()


# Descrição: Adiciona usuários
# Nome: add_user()
# Tipo: Procedimento
def add_user():
    print("---------CADASTRO DE NOVO USUÁRIO:")
    nome = str(input("Nome.....:"))
    celular = str(input("Celular..:"))
    email = str(input("E-mail...:"))
    listaUsuario.append([nome, celular, email])
    print("\n" * 3)
    print(f"Usuário {nome} adicionado com sucesso!")
    wait_prompt()


# Descrição: Edita usuários existentes
# Nome: edit_user()
# Tipo: Procedimento
def edit_user():
    print("---------MODO DE EDIÇÃO")
    index = show_user()
    updatefield = int(input("\nSelecione o dado que gostaria de editar\n1 - Nome\n2 - Celular\n3 - E-mail\nOpção "
                            "desejada_"))
    if updatefield == 1:
        print(f"\nNome.....:{listaUsuario[index][0]}")
        listaUsuario[index][0] = str(input("Altere o nome do usuário: "))
    elif updatefield == 2:
        print(f"\nCelular..:{listaUsuario[index][1]}")
        listaUsuario[index][1] = str(input("Altere o celular do usuário: "))
    elif updatefield == 3:
        print(f"\nE-mail...:{listaUsuario[index][2]}")
        listaUsuario[index][2] = str(input("Altere o e-mail do usuário: "))
    else:
        print("Opção inválida")
        edit_user()
    print("\n\nDado alterado com sucesso, dados atualizados do usuário:")
    i = listaUsuario[index]
    print(f"Nome.....:{i[0]}\nCelular..:{i[1]}\nE-mail...:{i[2]}\n--------------------------")
    wait_prompt()
    return listaUsuario


# Descrição: Deleta usuários
# Nome: delete_user()
# Tipo: Procedimento
def delete_user():
    index = show_user()
    option = (str(input("Deletar o usuário selecionado? Digite S para SIM, N para não")))
    while option not in ['S', 's', 'N', 'n']:
        print("Opção digitada inválida")
        option = (str(input("Deletar o usuário selecionado? Digite S para SIM, N para não")))
    if option in ['S', 's']:
        del listaUsuario[index]
        print("USUÁRIO DELETADO")
        wait_prompt()
    else:
        print("\n" * 30)
        print("Exclusão cancelada.")
        wait_prompt()


# Descrição: Lista todas as informações de contatos da agenda
# Nome: list_users()
# Tipo: Procedimento
def list_users():
    print("---------CONTATOS DA AGENDA:")
    for elem in listaUsuario:
        i = elem
        print(f"Nome.....:{i[0]}\nCelular..:{i[1]}\nE-mail...:{i[2]}\n--------------------------")
    wait_prompt()


listaUsuario = [["Edson", "119543-5567", "eds@hotmail.com"],
                ["Maria", "1193322-3456", "maria@gmail.com"],
                ["Adriano", "1198786-8584", "adriano@ig.com.br"]]

while True:
    menu()
