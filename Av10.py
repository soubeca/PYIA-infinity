import flet as ft 

def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Por favor, preencha o seu nome!"
            page.update()
        elif not txt_email.value:
            txt_email.error_text = "Por favor, preencha o seu email!"
            page.update()
        else:
            name = txt_name.value
            email = txt_email.value
            message = txt_message.value
            page.clean()
            page.add(ft.Text(f"Seus dados foram salvos com sucesso! ✅ \nNome: {name}\nEmai: {email}\nDescrição: {message}"))

    txt_name = ft.TextField(label="Me informe o seu nome:")
    txt_email = ft.TextField(label="Me informe o seu email:")
    txt_message = ft.TextField(label="Descreva algo:")

    page.add(txt_name,txt_email,txt_message, ft.ElevatedButton("Enviar", on_click=btn_click))

ft.app(main)
