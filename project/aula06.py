# Definição de Dados:

# Defina estruturas de dados para representar tarefas. Cada tarefa pode incluir

# informações como nome, descrição, prioridade e categoria. Você pode usar
# dicionários para representar as tarefas.

# Funções:
# Crie funções para adicionar tarefas, listar tarefas, marcar tarefas
# como concluídas, exibir tarefas por prioridade ou categoria, e outras
# funcionalidades que desejar.

# Menu de Comandos:
# Crie um menu de comandos de linha de comando que permita ao
# usuário interagir com o programa.

taskList = []

def addTask(taskList, taskName, taskDescrption, taskPriority, taskCategory):
  task = {
    'name': taskName,
    'description': taskDescrption,
    'priority': taskPriority,
    'category': taskCategory,
    'completed': False
  }
  taskList.append(task)
  print(f"✅Tarefa adicionada com sucesso!")

def list(taskList):
    
  if not taskList:
    print('☹️ Você ainda não criou uma tarefa!')
    
  else:
    num = 1
    for task in taskList:
      status = '✅' if task['completed'] else '❌'
      print(f'''
            {num}. {task['name']}
            Descrição: {task['description']}
            Prioridade: {task['priority']}
            Categoria: {task['category']}
            Concluída: {status}\n
      ''')
      num += 1


def priorityList (taskList): 
    orderedPriority = {
        'alta': 1,
        'média': 2,
        'baixa': 3
    }
    
    if not taskList:
        print('☹️ Você ainda não criou uma tarefa!')
    
    else:
        positionTasks = taskList.copy()
        positionTasks.sort(key=lambda x: orderedPriority[x['priority']])
        
        num = 1
        for task in positionTasks:
            status = '✅' if task['completed'] else '❌'
            print(f'''
                    {num}. {task['name']}
                    Descrição: {task['description']}
                    Prioridade: {task['priority']}
                    Categoria: {task['category']}
                    Concluída: {status}\n
            ''')
            num += 1

def checkList(taskList, cheking):
    value = cheking - 1
    if 0 <= value < len(taskList):
        taskList[value]['completed'] = True
        print(f"Tarefa '{taskList[value]['name']}' marcada como concluída.")
    



while True:
    print('''
        ::::::::::: MY TODO LIST :::::::::::::
        
        Olá, sou seu assistente de tarefas!☺️
        Escolha o número da opção que deseja:
        
        1. Adicionar tarefas
        2. Listar tarefas
        3. Listar tarefas por prioridade
        4. Checklist
        5. Sair
        
        ''')
    inputUser = int(input('Digite a opção desejada: '))
    
    if inputUser == 1:
        taskName = str(input('Qual o nome da tarefa? '))
        taskDescription = str(input('Descreva sua tarefa: '))
        taskPriority = str(input('Descreva qual a prioridade dela entre: Alta, Média e Baixa:  ')).lower()
        taskCategory = str(input('Qual a categoria da tarefa? '))
        
        addTask(taskList, taskName, taskDescription, taskPriority, taskCategory)
           
    elif inputUser == 2:
        list(taskList)
        
    elif inputUser == 3:
        priorityList(taskList)
        
    elif inputUser == 4:
        if not taskList:
            print('☹️ Você ainda não criou uma tarefa!')
        else:
            print('Escolha o número da tarefa que deseja marcar como concluída: ')
            list(taskList)
            cheking = int(input('Digite o número da tarefa: '))
            checkList(taskList, cheking)
        
    elif inputUser == 5:
        print('🙂Até a próxima!')
        break
    else:
        print('😅Ops, escolha uma das minhas opções!')
  
  
  
