import flet as ft

def main(page: ft.Page):

    page.window_title_bar_hidden = True
    page.window_frameless = True
    page.window_left = 400
    page.window_top = 200
    page.add(ft.ElevatedButton("I'm a floating button!"))

ft.app(target=main)