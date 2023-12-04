import flet as ft

def main(page: ft.Page):
    page.theme_mode = "light"
    page.title="Boarding Page"
    img = ft.Image(
        src=f"/testing.jpg",
        height=150,
        fit=ft.ImageFit.CONTAIN,
    )

    head_text = ft.Text("SELAMAT DATANG",weight=ft.FontWeight.BOLD,size=30)

    body_text = ft.Text("Halo selamat datang di aplikasi presence")

    login_button = ft.ElevatedButton("Login",width=1300)

    page.add(
        ft.Row(controls=[
            ft.Container(
                content=img,
                padding=30,
                margin=ft.margin.only(bottom=50)
            )
        ],alignment="center"),

        ft.Row([
            head_text
        ],alignment="center"),

        ft.Container(margin=ft.margin.only(bottom=5)),#hanya buat spasi anatara head dan body

        ft.Row([
            body_text
        ],alignment="center"),

        ft.Container(
            ft.Stack(
                [
                    ft.Container(
                        content = login_button,
                        border_radius=5,
                        bottom=40,
                        left=20,
                        right=20
                    ),
                ]
            ),
            width=1400,
            expand=True
        )
    )

ft.app(target=main, assets_dir="asset")