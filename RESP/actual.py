
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
        "Consola": "./Prueba APP 1/fonts/CONSOLA.ttf"
    }
    
    page.theme = Theme(font_family = "Consola")
    page.bgcolor = "#f1ece2"
    page.window_width = 550
    page.window_height = 550
    page.theme_mode = "light"
    page.window_focused = True
    page.window_resizable = False
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True

    page.theme = Theme(font_family = "Consola")


    class openDLG(UserControl):
        def __init__(self, ventana: AlertDialog):
            self.dlg = ventana
            super().__init__()
           
        def __call__(self, e, *args, **kwargs):
            page.dialog = self.dlg
            self.dlg.open = True
            page.update()


    class openBS(UserControl):
        def __init__(self, mensaje: BottomSheet):
            self.bs = mensaje
            super().__init__()
           
        def __call__(self, e, *args, **kwargs):
            page.add(self.bs)
            self.bs.open = True
            self.bs.update()
    

    class closeBS(UserControl):
        def __init__(self, mensaje: BottomSheet):
            self.bs = mensaje
            super().__init__()
           
        def __call__(self, e, *args, **kwargs):
            self.bs.open = False
            self.bs.update()


    class doble(UserControl):
        def __init__(self, ventana: AlertDialog, mensaje: BottomSheet):
            self.dlg = ventana
            self.bs = mensaje
            super().__init__()
           
        def __call__(self, e, *args, **kwargs):
            page.dialog = self.dlg
            self.dlg.open = True
            page.update()
            
            self.bs.open = False
            self.bs.update()


    class CR(UserControl):
        def __init__(self):
            super().__init__()
        

        def abrirP1():
            P1 = Container(
                expand=True,
                content=Card(
                    elevation=15,
                    content=btAbrir,
                ),

                alignment=alignment.center
            )

            page.clean()

            page.add(close)
            page.add(P1)
            page.update()

    
        def abrirP2():
            P2 = Container(
                expand=True,
                content=Card(
                    elevation=15,
                    content=Text(
                        f"""
    Usuario: {usAc[1]} {usAc[2][0]}.
    SALDO: $ {usAc[6]}
                        """,
                        weight="bold"
                    ),
                ),

                alignment=alignment.center
            )

            # page.clean()

            page.add(close)
            page.add(P2)
            page.update()

         

    """ SIMULAR LOGIN """

    usAc = actual("1724727621")

    
    """ BOTONES """
    
    siCon = TextButton(
        content=Text(
            "Si", color="black", weight="bold"
        ),
    )

    noCon = TextButton(
        content=Text(
            "No", color="black", weight="bold"
        ),
    )

    menCon = BottomSheet(
        content=Container(
            bgcolor="#faf4ea", 
            content=Column(
                height=200,
                controls=[
                    Text(
                        "Esta accion tiene un costo de $ 0.35\n¿Deseas continuar?",
                        text_align=TextAlign.CENTER, size=20
                    ),

                    Row(
                        [
                            siCon,
                            noCon,
                        ],

                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER
                    )
                ],

                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            )
        )
    )

    btAbrir = OutlinedButton(

        content=Text(
            "ACTULIZAR", color="black"
        ),

        style=ButtonStyle(
            shape=RoundedRectangleBorder(radius=8)
        ),

        on_click=openBS(menCon)
    )


    # siCon.on_click = CR.abrirP2()

    if usAc[5] == "U":
        
        CR.abrirP1()
        


if __name__ == "__main__":
    flet.app(target = main, assets_dir = "Prueba APP 1")

