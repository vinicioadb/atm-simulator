
import flet
from flet import *
from os import system, remove, rename


def actual(cedula: str):

    with open("usuarios.txt", "r+") as archivo:

        for linea in archivo.readlines():
            dato = linea.strip().split(" ")

            if cedula in dato: break

    return dato

def recargo(monto: float, usuario: list):

    with open("usuarios.txt", "r+") as f, open("temp.txt", "w+") as ree:

        for linea in f.readlines():
            listaUs = linea.strip().split(" ")

            if usuario[0] in listaUs:

                listaUs[6] = str(round(((float(listaUs[6]) - monto)), 2))
                ree.write(" ".join(listaUs)+"\n")

            else:

                ree.write(" ".join(listaUs)+"\n")
                                     
    remove("usuarios.txt")
    rename("temp.txt", "usuarios.txt")


def main(page: Page):

    close = Row(
        [
            WindowDragArea(Container(Text(), bgcolor="#f1ece2",padding=10), expand=True),
            IconButton(icons.CLOSE_ROUNDED, icon_color="black",on_click=lambda _: page.window_close()),
        ]
    )

    page.fonts = {
        "Josefina": "./Prueba APP 1/fonts/JosefinSans.ttf",
        "Aesthetica": "./Prueba APP 1/fonts/aesthetica.ttf",
        "Consolas": "./Prueba APP 1/fonts/Consola.ttf"
    }

    page.window_width = 530
    page.window_height = 530
    page.theme_mode = "light"
    page.window_focused = True
    page.window_resizable = False
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.bgcolor = "#f1ece2"

    page.theme = Theme(font_family = "Consolas")

    class CR(UserControl):
        
        def __init__(self, funcion):
            self.funcion = funcion
            super().__init__()

    
        def P1(self):
            return Container(
                expand=True,
                alignment=alignment.center,
                content=Column(
                    [
                        OutlinedButton(

                            content=Text(
                                "ENTRAR A P2", color="black"
                            ),

                            style=ButtonStyle(
                                shape=RoundedRectangleBorder(radius=8)
                            ),

                            on_click=self.funcion
                        )
                    ], 

                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )


        def P2(self):
            return Container(
                expand=True,
                alignment=alignment.center,
                content=Column(
                    [
                        Text(
                            f"""
        USER: {usAc[2]} {usAc[3][0]}.
        MONT: $ {usAc[6]}
                            """
                        ),

                        OutlinedButton(

                            content=Text(
                                "ACTULIZAR", color="black"
                            ),

                            style=ButtonStyle(
                                shape=RoundedRectangleBorder(radius=8)
                            ),

                            on_click=self.funcion
                        )
                    ], 

                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )


    """ SIMULAR LOGIN """
    
    usAc = actual("1724727621")

    
    def openP1(e):

        page.clean()

        page.add(close)
        page.add(CR(openP2).P1())
        page.update()

    def openP2(e):

        page.clean()

        page.add(close)
        page.add(CR(actulizarSaldo).P2())
        page.add(
            OutlinedButton(

                content=Text(
                    "REGREAR", color="black"
                ),

                style=ButtonStyle(
                    shape=RoundedRectangleBorder(radius=8)
                ),

                on_click=openP1
            )
        )

        page.update()

    def actulizarSaldo(e):

        nonlocal usAc

        if float(usAc[6]) >= 10:

            recargo(10, usAc)
            usAc = actual(usAc[1])

            page.clean()

            page.add(close)
            page.add(CR(actulizarSaldo).P2())
            page.add(
                OutlinedButton(

                    content=Text(
                        "REGREAR", color="black"
                    ),

                    style=ButtonStyle(
                        shape=RoundedRectangleBorder(radius=8)
                    ),

                    on_click=openP1
                )
            )
            page.update()
        
        else:

            page.clean()

            page.add(close)
            page.add(
                Text(
                    "SALDO INSUFICIENTE"
                )
            )
            page.add(
                OutlinedButton(

                    content=Text(
                        "REGREAR", color="black"
                    ),

                    style=ButtonStyle(
                        shape=RoundedRectangleBorder(radius=8)
                    ),

                    on_click=openP1
                )
            )
            page.update()


    if usAc[5] == "U":
        
        page.clean()
        page.add(close)
        page.add(CR(openP2).P1())
        page.update()


if __name__ == "__main__":
    flet.app(target = main, assets_dir = "Prueba APP 1")
