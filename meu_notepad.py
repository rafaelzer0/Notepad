import flet as ft
import tkinter.filedialog


def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = 'Bloco de notas'
    page.scroll = True
    page.window_width = 500
    page.window_height = 500
    page.window_resizable = True
    page.theme_mode = 'dark'
    page.bgcolor = '#2E2E2E'  # Cor de fundo da página
    page.update()
 
    # Campo de texto multilinha
    text_input = ft.TextField(
        multiline=True,
        border_width=0,
        autofocus=True,
        text_style=ft.TextStyle(color='#FFFFFF')  # Cor do texto digitado
    )

    # Função para salvar o conteúdo em um arquivo de texto
    def save_file(e):
        file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                text_to_save = text_input.value
                file.write(text_to_save)

    # Barra de título do aplicativo
    page.appbar = ft.AppBar(
        title=ft.Text("Rafael Notepad", color='#000000'),
        center_title=True,
        bgcolor='#D5006D'  # Cor de fundo da AppBar
    )
    
    # Menu de navegação
    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor='#D5006D',  # Cor de fundo do menu
            mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT, 
                          ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
        ),
        controls=[  # Item de menu "File"
            ft.SubmenuButton(
                content=ft.Text("File"),
                controls=[  
                    ft.MenuItemButton(
                        content=ft.Text("Save"),
                        leading=ft.Icon(ft.icons.SAVE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=save_file  # Ação ao clicar para salvar
                    )
                ]
            ),
        ]
    )

    # Adicionando o menu e o campo de texto à página
    page.add(ft.Row([menubar]), text_input)

# Inicializando o aplicativo
ft.app(target=main)
