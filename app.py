#Gerenciador de tarefas

tarefas_pendentes = []
tarefas_andamento = []
tarefas_concluidas = []

print('\n Olá, seja bem vindo ao gerenciador de tarefas! \n')

def negative_number(task):
    if task <= 0:
        print('\nAdicione apenas números positivos!\n')
        

def addTask():
    task = input('Digite o título da tarefa que deseja adicionar:').lower()
    tarefas_pendentes.append(task)

    print('')
    print(f'Perfeito! A tarefa {task} foi adicionada com êxito!')

def removeTask():
    try:
        task = int(input('Digite o número da posição da tarefa que deseja remover: '))
        negative_number(task)
        del tarefas_pendentes[task -1]

        print('')
        print(f'Perfeito! A tarefa número {task} foi deletada com êxito!')


    except IndexError:
        print('\nEita! Parece que você digitou o valor errado, tente novamente!\n')

def concludeTask():
    try: 
        task = int(input('Digite o número da posição da tarefa que foi concluída (na lista "tarefas em andamento": '))
        negative_number(task)
        moved = tarefas_andamento.pop(task-1)
        tarefas_concluidas.append(moved)

        print('')
        print(f'Perfeito! A tarefa número {task} foi concluída com êxito!')

    except IndexError:
        print('\nEita! Parece que você digitou o valor errado, tente novamente!\n')

def startTask():
    try:
        task = int(input('Digite o número da posição da tarefa que deseja iniciar: '))
        negative_number(task)
        moved = tarefas_pendentes.pop(task-1)
        tarefas_andamento.append(moved)

        print('')
        print(f'Perfeito! A tarefa número {task} foi iniciada com êxito!')

    except IndexError: 
        print('\nEita! Parece que você digitou o valor errado, tente novamente!\n')

def taskInScreen(task_module1, task_module2):
        
        print('Tarefas em andamento: \n')
        for i in range(len(task_module1)):
            print(f'{i + 1}: {task_module1[i]}\n')

        print('Tarefas pendentes: \n')
        for i in range(len(task_module2)):
            print(f'{i + 1}: {task_module2[i]}\n')
            

while True:
    taskInScreen(tarefas_andamento, tarefas_pendentes)

    try: 
        option = int(input('Selecione a opção desejada:\n' \
        '1: Adicionar tarefa;\n' \
        '2: Remover tarefa;\n' \
        '3: Concluir tarefa;\n' \
        '4: Iniciar tarefa;\n'
        '5: Fechar.\n'))
        negative_number(option)
    except ValueError:
        print('\nEspera ai! Aqui só podem ser digitados números, tente novamente!\n')
        continue

    if option == 1:
        addTask()

    elif option == 2: 
        removeTask()

    elif option == 3:
        concludeTask()

    elif option == 4:
        startTask()

    elif option == 5:
        break
