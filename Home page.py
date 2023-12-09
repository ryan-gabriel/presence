from datetime import datetime
import flet as ft

sekarang = datetime.now()
hari = sekarang.strftime("%A")
tanggal = sekarang.day
bulan = sekarang.strftime("%B")
tahun = sekarang.year
jam = sekarang.strftime("%H")
menit = sekarang.strftime("%M")

def main(page:ft.Page):
    page.padding = 0
    page.horizontal_alignment = "center"
    page.theme_mode=ft.ThemeMode.LIGHT

    opt = ft.Ref[ft.Dropdown]() # option dropdown izin

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else None
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    page.overlay.append(pick_files_dialog)

    # izin tab bagian text dan text area
    t = ft.Text(color="black")
    konfirmasi_btn = ft.ElevatedButton("Konfirmasi")
    box_area = ft.TextField(height=100,visible=False,width=10000,min_lines=3,max_lines=3,max_length=50)
    fileDispen = ft.Row([
        ft.ElevatedButton(
                        "Pick files",
                        icon=ft.icons.UPLOAD_FILE,
                        on_click=lambda _: pick_files_dialog.pick_files(
                            allow_multiple=True
                        ),
                    ),selected_files
    ],visible=False)

    def dropdown_changed(e):
        if opt.current.value == "Izin" or opt.current.value == "Sakit":
            fileDispen.visible = False
            box_area.visible = True
            t.value = "Keterangan"
            page.update()
        elif opt.current.value == "Dispen":
            box_area.visible = False
            fileDispen.visible = True
            t.value = "File"
            page.update()


    absent_tab = ft.Tabs(
        selected_index=0,
        animation_duration=200,
        tabs=[
            ft.Tab(
                tab_content=ft.Text("Hadir",color="blue"),
                content=ft.Column([
                    ft.Row([
                        ft.Text("Absensi sekarang: ",color="#00BAE9"),
                    ],alignment="center"),
                    ft.Row([
                        ft.Text("Pengantar Rekayasa Perangkat Lunak",color="#00BAE9"),
                    ],alignment = "center"),
                    ft.Row([
                        ft.Text("Batas Absen",color="#00BAE9"),
                    ],alignment = "center"),
                    ft.Row([
                        ft.Text("12:15 ",color="#00BAE9"),
                    ],alignment = "center",),
                    ft.Row([
                        ft.ElevatedButton(
                            content= ft.Icon(name=ft.icons.FINGERPRINT,color="white",size=150),
                            bgcolor="#00BAE9",
                            style=ft.ButtonStyle(
                                padding=0
                            )
                        ),
                    ],alignment="center"),
                    ft.Row([
                        ft.Text("Absen kehadiranmu",color="#00BAE9")
                    ],alignment="center")
                ],width=1000)
            ),
            ft.Tab(
                tab_content=ft.Text("Izin",color="blue"),
                content=ft.Column([
                    ft.Text("Keterangan: ",weight=ft.FontWeight.BOLD,color="black"),
                    ft.Dropdown(
                        ref = opt,
                        width = 10000,
                        options=[
                            ft.dropdown.Option("Dispen"),
                            ft.dropdown.Option("Sakit"),
                            ft.dropdown.Option("Izin"),
                        ],
                        color="#00BAE9",
                        focused_bgcolor="94D3E4",
                        hint_text="Pilih Keterangan Anda",
                        border_radius=10,
                        on_change=dropdown_changed
                    ),
                    t,
                    box_area,
                    fileDispen,
                    ft.Stack([
                        ft.Container(
                            content= konfirmasi_btn, #belum ditambahin fungsionalitas
                            bottom=10,
                            right=10
                        )
                    ],
                    expand=True,
                    width=10000,
                    )
                ]),
            )
        ],
        scrollable=True,
        expand=True,
        width=10000,
    )

    def changetab(e):
        my_index = e.control.selected_index
        history.visible = True if my_index == 0 else False
        homepage.visible = True if my_index == 1 else False
        profile.visible = True if my_index == 2 else False
        page.update()

    page.navigation_bar = ft.NavigationBar(
        selected_index=1,
        on_change=changetab,
        bgcolor="white",
        destinations=[
            ft.NavigationDestination(icon=ft.icons.LOCATION_HISTORY_ROUNDED),
            ft.NavigationDestination(icon=ft.icons.HOME_ROUNDED),
            ft.NavigationDestination(icon=ft.icons.TAG_FACES_ROUNDED),
        ],
        height=60,
    )


    homepage =ft.Stack(
                [
                    ft.Container(
                        content=ft.Text(f"{hari}, {tanggal} {bulan} {tahun}",text_align="center",size=20,color="white"),
                        right=50,
                        left=50,
                        top = 40
                    ),
                    ft.Container(
                        content=ft.Row(
                                [
                                ft.Text(f"{jam} : {menit}",color="white",size=40,weight=ft.FontWeight.BOLD)
                                ],alignment="center"),
                        width= page.width,
                        right = 50,
                        left=50,
                        top=75
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Row([
                                ft.Text("Pilih Kehadiran",weight=ft.FontWeight.BOLD,size=20,color="black",text_align="center")
                            ],alignment="center"),
                            ft.Container(
                                content=absent_tab,
                                height=400,
                                width=10000
                            )
                        ],),
                        width=700,
                        left=50,
                        right=50,
                        top= 150,
                        bgcolor="white",
                        border_radius=25,
                        padding=10
                    )
                ],
                expand=True,
                width=10000,
            )
    homepage.visible = True

    history = ft.Stack(
                [
                    ft.Text("history")
                ],
                expand=True,
                width=10000
            )
    
    history.visible = False
    
    profile = ft.Stack(
                [
                    ft.Text("profile")
                ],
                expand=True,
                width=10000
            )
    profile.visible = False

    page.add(
        ft.Container(
            content= ft.Stack(
                [
                        history,
                        homepage,
                        profile
                ],
                expand=True,
                width=10000
            ),
            gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=['#00A7D2', "#94D3E4"],
                    ),
            width=14000,
            expand=True,
        )
    )


ft.app(target=main)