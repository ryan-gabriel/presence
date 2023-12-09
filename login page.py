import flet as ft
import math

def main(page:ft.Page):
    page.padding = 0
    page.horizontal_alignment = "center"
    logo_img=ft.Image(
        src=f"/testing.jpg",
        width=1000,
        height=140,
        fit = ft.ImageFit.COVER
    )
    page.add(
        ft.Container(
        content=ft.Stack([
            ft.Container(
                content =logo_img,
                right = 40,
                left = 40,
                top = 40
            ),
            ft.Container(
                content=ft.Row([
                    ft.Text("Log In",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,size=30),
                ],alignment="center"),
                top = 250,
                width=1000,
                right=50,
                left=50,
            ),
            ft.Container(
                content=ft.Row([
                    ft.Text("Absen Kehadiranmu dengan presence",color=ft.colors.BLACK,weight=ft.FontWeight.W_200,size=15),
                ],alignment="center"),
                top = 305,
                width=1000,
                right=50,
                left=50,
            ),
            ft.Container(
                content=ft.Column([
                    ft.TextField(label="NIM",hint_text="Masukkan NIM...",color=ft.colors.BLACK,border_color=ft.colors.BLUE,border=ft.InputBorder.UNDERLINE,suffix_icon=ft.icons.TAG_FACES,cursor_color=ft.colors.BLUE,keyboard_type=ft.KeyboardType.NUMBER),
                    ft.TextField(label="PASSWORD",password=True,can_reveal_password=True,hint_text="Masukkan Password...",color=ft.colors.BLACK,border_color=ft.colors.BLUE,border=ft.InputBorder.UNDERLINE),
                ],alignment=ft.MainAxisAlignment.CENTER,spacing=20),
                top = 340,
                width=1000,
                right=50,
                left=50,
            ),
            ft.Container(
                content=ft.Row([
                    ft.ElevatedButton("Log In",color=ft.colors.WHITE,bgcolor="#94D3E4",width=250,height=50),
                ],alignment="center"),
                width=1000,
                top = 600,
                right=50,
                left=50,
            ),
            ft.Container(
                content=ft.Row([
                        ft.Text("Belum punya akun?",color=ft.colors.BLACK,weight=ft.FontWeight.W_600),
                        ft.TextButton("Register")
                ],alignment="center"),
                width=1000,
                top = 655,
                right=50,
                left=50,
            )
        ],
        expand=True,
        width=14000
        ),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=['#00A7D2', ft.colors.WHITE],
            stops=[0.2, 0.55]
        ),
        width=14000,
        expand=True,
        )
    )


ft.app(target=main,assets_dir="asset")