'''
    Faça uma lista de tarefas com as seguintes opções:
        - adicionar tarefas
        - listar tarefas
        - desfazer tarefas (desfazer a ultima)
        - refazer tarefa (a cada chamada retorna a ultima
'''

def add_task(tarefa, lista):
    lista.append(tarefa)
    return lista

def undo_task(lista, safe_list):
    safe_list.append(lista.pop())
    return lista, safe_list

def redo_task(lista, safe_list):
    return undo_task(safe_list, lista)

lista = []
safeList = []

while True :
    option = 0
    while(True):
        try:
            option = int(input("1: Inserir Task || 2: Remove Task || 3: Desfazer || 4:Exit || : "))
        except ValueError:
            option = 0
        if option != 0:
            break

    if option == 1:
        insert_task = input("Insert Task: ")
        add_task(insert_task, lista)
    elif option == 2:
        if len(lista) > 0:
            undo_task(lista, safeList)
        else:
            print('Not possible...')
    elif option == 3:
        if len(safeList) > 0:
            redo_task(lista, safeList)
        else:
            print('Not possible...')
    elif option == 4:
        break

    print(lista)