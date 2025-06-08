import flet as ft 

# [PYIA-A09] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a uma lista de tarefas. 
# A interface da aplicação deve incluir um campo de entrada de texto para o usuário digitar o nome da tarefa e um botão para adicionar a tarefa à lista. 
# Quando o usuário clicar no botão, o item deve ser adicionado a uma lista exibida na tela, 
# mostrando todas as tarefas que foram incluídas até o momento. A lista de tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado.

def main(page: ft.Page):
    page.title = 'Gerenciador de Tarefas'
    
    def add_task(e):
        page.add(ft.Text(new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(label="😄 Me conta qual a sua tarefa do dia?", width=500)
    page.add(ft.Row([new_task, ft.ElevatedButton("+", on_click=add_task)]))

ft.app(main)

