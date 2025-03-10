
from time import sleep

import flet
from flet import *


def main(page: Page):
        
    close = Row(
        [
            WindowDragArea(Container(Text(), bgcolor="#f1ece2", padding=10), expand=True),
            IconButton(icons.CLOSE_ROUNDED, icon_color="black", on_click=lambda _: page.window_close()),
        ]
    )

    # back = IconButton(
    #     icons.LOGOUT_OUTLINED, icon_color="black", tooltip="Cerrar Sesion"
    # )
    back = IconButton(
        content=Text("Cerrar Sesion", weight="bold", color="black", size=12),
        style=ButtonStyle(bgcolor="#bbc191", overlay_color="red", shape=RoundedRectangleBorder(radius=8)),
    )

    loggout = Row(
        [
            WindowDragArea(Container(Text(), bgcolor="transparent", padding=10), expand=True), back
        ]
    )

    page.fonts = {"Consola": "./Prueba APP 1/fonts/CONSOLA.ttf"}
    
    page.window_width = 850
    page.window_height = 530
    page.theme_mode = "light"
    page.window_focused = True
    page.window_resizable = False
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True

    page.theme = Theme(font_family = "Consola")

    usAc = []
    temp = ""
    band = cont = 0

    us = TextField(label="Cedula", filled=True, border_color="transparent", autofocus=True, on_submit=lambda e: ps.focus())
    ps = TextField(label="PIN", password=True, filled=True, border_color="transparent")
    al = AlertDialog(
        content=Column(
            [
                Text("ALADASDA")
            ]
        )
    )

    op = IconButton(
        width=230,
        content=Text(
            "DIALOGO", weight="bold",
            color="black"
        ),

        style=ButtonStyle(
            bgcolor="#bbc191",
            shape=RoundedRectangleBorder(radius=8)
        ),
    )

    intentosAgot = AlertDialog(
        actions=[
            Text(
                "Agotaste tu numero de intentos\nIntentalo mas tarde",
                size=35, weight="bold", text_align=TextAlign.CENTER
            ),

            ProgressBar(color="#677423", bgcolor="#bbc191")
        ],

        modal=True
    )

    
    def ingresar(e):

        nonlocal temp, cont, band, usAc

        with open("usuarios.txt", "r+") as f:      
            for linea in f.readlines():
                datos = linea.strip().split(" ")

                if us.value == datos[1]: 
                    usAc = datos
                    break

                else: usAc = datos

        if us.value == usAc[1] and ps.value == usAc[4]:
            us.value = ps.value = None

            if usAc[5] == "U": page.go("/user")
            if usAc[5] == "A": page.go("/admin")

        elif us.value == usAc[1] and ps.value != usAc[4]:

            cont += 1

            if temp != usAc[1]: 
                cont = 1
            
            if cont == 3:

                page.dialog = intentosAgot
                intentosAgot.open = True
                page.update()

                sleep(3)
                page.window_close()

            ps.focus()
            ps.value = ""
            ps.error_text = f"Contraseña incorrecta\nTiene {3-cont} intentos"

        elif us.value != usAc[1]:

            us.value = ""

            us.focus()
            us.value = ps.value = ""
            us.error_text = "Usuario no registrado"
        
        temp = usAc[1]

        page.update(), sleep(2)

        us.error_text = ps.error_text = None
        us.border_color = ps.border_color = "transparent"
        
        page.update()

    
    P1 = View(
        
        route="/ingreso", bgcolor="#f1ece2",
        controls=[
            
            close,

            Container(
                expand=True, 
                content=Column(
                    
                    [
                        us, ps,

                        IconButton(
                            width=230,

                            content=Text(
                                "Ingresar", weight="bold", color="black"
                            ),

                            style=ButtonStyle(
                                bgcolor="#bbc191",
                                shape=RoundedRectangleBorder(radius=8),
                            ),

                            # si,

                            on_click=ingresar
                        )
                    ],

                    width=400,
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            ),

        ],

        horizontal_alignment=CrossAxisAlignment.CENTER,
        vertical_alignment=MainAxisAlignment.CENTER
    )

    back.on_click = lambda _: page.go("/ingreso")

    P2 = View(
        route="/user", bgcolor="#f1ece2",
        controls=[
            close,
            Container(
                expand=True,
                content=Column(
                    [
                        Text(
                            "Usuario"
                        ),
                    ],

                    width=400,
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            ),

            loggout,
        ],

        horizontal_alignment=CrossAxisAlignment.CENTER,
        vertical_alignment=MainAxisAlignment.CENTER
    )

    P3 = View(
        route="/admin", bgcolor="#f1ece2",
        controls=[
            close,
            Container(
                expand=True,
                content=Column(
                    [
                        Text(
                            "Administrador"
                        ),
                    ],

                    width=400,
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            ),

            loggout,
        ],

        horizontal_alignment=CrossAxisAlignment.CENTER,
        vertical_alignment=MainAxisAlignment.CENTER
    )


    def route_change(route):

        nonlocal usAc, band, cont

        page.views.clear()
        page.views.append(P1)
        
        if page.route == "/user":
            cont = 0
            # page.go("/ingreso")
            # usAc = ["" for x in range(7)] 
            page.views.clear()
            page.views.append(P2)

        if page.route == "/admin":
            cont = 0
            # page.go("/ingreso")
            # usAc = ["" for x in range(7)] 
            page.views.clear()
            page.views.append(P3)

        page.update()


    def view_pop(view):

        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == "__main__":
    flet.app(target = main, assets_dir = "Prueba APP 1")
