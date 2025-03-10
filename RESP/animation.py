
import flet
from flet import *
from controls import *

from os import system
from time import sleep
import itertools as it


""" Variables CAJERO """

compr = False
usuario = []


""" CAJEROS """

def actualizar(lista: list):

    with open("datos.txt", "r+") as f:

        for linea in f.readlines():
            actual = linea.strip().split(" ")

            if lista[0] in actual: break

    return actual


def cargo(cargo: float):

    global compr, usuario

    with open("datos.txt", "r+") as f, open("temp.txt", "w+") as ree:

        for linea in f.readlines():

            listaUs = linea.strip().split(" ")

            if usuario[0] in listaUs and float(usuario[6]) >= cargo:

                compr = True

                carg = round(((float(listaUs[6]) - cargo)), 2)
                listaUs[6] = str(carg)
                ree.write(" ".join(listaUs)+"\n")

            else:
                ree.write(" ".join(listaUs)+"\n")
                                     
    remove("datos.txt")
    rename("temp.txt", "datos.txt")


def main(page: Page):

    global actualizar, cargo, usuario

    page.fonts = {
        "Josefina": "./Prueba APP 1/fonts/JosefinSans.ttf",
        "Aesthetica": "./Prueba APP 1/fonts/aesthetica.ttf",
        "Consolas": "./Prueba APP 1/fonts/Consola.ttf"
    }

    page.theme = Theme(font_family = "Consolas")
    page.window_width = 850
    page.window_height = 530
    page.theme_mode = "light"
    page.window_focused = True
    page.window_resizable = False
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.bgcolor = "#f1ece2"

    close = Row(
        [
            WindowDragArea(Container(Text(), bgcolor="#f1ece2", padding=10), expand=True),
            IconButton(icons.CLOSE_ROUNDED, icon_color="black", on_click=lambda _: page.window_close()),
        ]
    )

    #   Variables

    cont = band = 0
    usAc = acc = []
    temp = ct = ""

    #   Procesos iniciales

    """ Permutacion que asigna los numeros de cunta """

    prmp = it.product(range(10), repeat=4)
    ctas = list("".join(map(str, x)) for x in list(prmp))

    with open("datos.txt", "r+") as f:
        for line in f.readlines():
            ct, c, n, a, p, pm, s = line.strip().split(" ")
            acc.append(ct[1:])


    """ Clase que abre las Ventans emergentes """

    class openDLG(UserControl):
        def __init__(self, ventana: AlertDialog):
            self.dlg = ventana
            super().__init__()
           
        def __call__(self, e, *args, **kwargs):
            page.dialog = self.dlg
            self.dlg.open = True
            page.update()
    

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


    class closeDLG(UserControl):
        def __init__(self, ventana: AlertDialog):
            self.dlg = ventana
            super().__init__()

        def __call__(self, e, *args, **kwargs):
            self.dlg.open = False
            page.update()


    """ Clase que abre los Mensajes emergentes """

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


    #   Funciones

    def ingresar(e):

        nonlocal temp, cont, band, usAc

        with open("datos.txt", "r+") as f:      
            
            for linea in f.readlines():
                datos = linea.strip().split(" ")

                if us.value == datos[1]: 
                    usAc = datos
                    break

                else: usAc = datos


        if us.value == usAc[1] and ps.value == usAc[4]:

            us.border_color = ps.border_color = "green"
            band = 1
        
        elif us.value == usAc[1] and ps.value != usAc[4]:

            cont += 1

            if temp != usAc[1]:
                cont = 1
            
            ps.value = ""
            ps.focus()
            ps.error_text = f"Contraseña incorrecta\nTiene {3-cont} intentos"

        elif us.value != usAc[1]:

            us.value = ""

            us.focus()
            us.value = ps.value = ""
            us.error_text = "Usuario no registrado"
        
        
        temp = usAc[1]

        us.update()
        ps.update()

        sleep(2)
        us.error_text = ps.error_text = None
        us.border_color = ps.border_color = "transparent"
        
        page.update()

    
    """ Boton de Ingresar """

    bLogi.on_click = ingresar
    

    # def registrar(e):

    #     nonlocal acc, aux, ct

    #     aux = ""

    #     with open("datos.txt", "r+") as f:

    #         for line in f.readlines():
    #             u, p, a, t = line.strip().split(" ")

    #             if usA.value == u:
    #                 aux = u

    #     if aux == usA.value:
            
    #         usA.focus()
    #         psA.error_text = ""
    #         usA.error_text = "Nombre de usuario ya en uso"

    #         cReg.update()

    #     elif aux != usA.value:
            
    #         usA.border_color = psA.border_color = colors.GREEN
    #         acc.sort()
            
    #         for i, j in zip(ctas, acc):

    #             if i != j:
    #                 ct = i
    #                 break
    #             else:
    #                 ct = ctas[ctas.index(i) + 1]

    #         acc.append(ct)
    #         ct = "".join(("2", "".join(map(str, ct))))

    #         with open("datos.txt", "a+") as f:
    #             f.write(f"\n{usA.value} {psA.value} {ct} U")

    #         # print("Registros nuevos:  ", acc)
        

    #     # usA.update(), psA.update()
    #     # cReg.update()

    #     sleep(2)
    #     usA.error_text = psA.error_text = None
    #     usA.border_color = psA.border_color = "transparent"
    #     cReg.update()

    
    """ Boton de Registrar """

    # bRegi.on_click = registrar

    # def transferir(e):

    #     cTfr.actions.append(
    #         ProgressBar(
    #             color="#677423", bgcolor="#bbc191"
    #         )
    #     )

    #     cTfr.update()

    #     sleep(2)

    #     cTfr.actions.clear()

    #     cTfr.actions_padding = 0
    #     cTfr.shape=RoundedRectangleBorder(radius=8)

    #     cTfr.actions.append(
    #         Container(
    #             width=635, height=430,
    #             padding=17, bgcolor="#faf4ea", border_radius=8,
    #             content=Text(
    #                 "Hola mundo"
    #             ),

    #             alignment=alignment.center
    #         )
    #     )

        

    #     # cTfr.update()
    #     # sleep(3)

    #     cTfr.update()


    # bTafi.on_click = transferir


    """ Asignar funcion al boton de Abrir VENTANA (Dialogos) """

    bReg.on_click = openDLG(cReg)
    bTfr.on_click = openDLG(cTfr)
    bRet.on_click = openDLG(cRet)
    bEdt.on_click = openDLG(cEdt)
    bAdm.on_click = openDLG(cEdA)
    bAbs.on_click = openDLG(cAbs)
    bRegA.on_click = openDLG(cRegA)
    

    """ P1 = Login, Registro y Depositos """

    P1 = Container(
        alignment=alignment.center,
        expand=True,
        content=Row(
            alignment=MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[

                Image(
                    src="./Prueba APP 1/dirt.png",
                    width=300,
                ),

                VerticalDivider(color="black"),

                Card(
                    elevation=20, height=500,
                    content=Container(
                        # expand=True, 
                        border_radius=8, bgcolor="#faf4ea",
                        padding=20,
                        content=Column(
                            alignment=MainAxisAlignment.SPACE_EVENLY,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[

                                tW,

                                Column(
                                    controls=[
                                        us, ps,
                                    ],
                                ),

                                bLogi, 

                                Text(
                                    "® 2023 ITSCO        |        DSW", size=9,
                                )
                            ],
                        ),
                    ),
                ),
            ],
        ),
    )
    
    page.add(close)
    page.add(P1)
    page.update()
    
    while True:

        if band == 1 or cont == 3:

            page.add(
                ProgressBar(
                    color="#677423", bgcolor="#bbc191"
                )
            )

            sleep(2.3)
            break
    
    
    usuario = usAc
    print(usuario)
    

    """ Clase que contruye las Ventanas emergentes """

    class cr(UserControl):
        def __init__(self):
            super().__init__()

        def cCon():

            # global usAc
            nonlocal usAc
            
            usAc = actualizar(usAc)

            return AlertDialog(
                actions_padding=0,
                shape=RoundedRectangleBorder(radius=8),
                actions=[
                    Container(
                        width=635, height=430,
                        padding=17, bgcolor="#faf4ea", border_radius=8,
                        content=Row(
                            [
                                Container(
                                    content=Column(
                                        [
                                            
                                            Text(
                                                "Cooperativa Coordillera", size=20, weight="bold",
                                                font_family="Consola"
                                            ),

                                            Text(
                                                "Comprobante", size=15, weight="bold",
                                                font_family="Consola"
                                            ),

                                            # vert,
                                            Divider(color="black"),

                                            Text(
                                                f"Saldo:  $ {usAc[6]}", size=15, 
                                                font_family="Consola"
                                            ),

                                            Text(
                                                f"Fecha:  {form_dia}", size=15, 
                                                font_family="Consola"
                                            ),

                                            Text(
                                                f"Cuenta:  XXX{usAc[0][3:]}", size=15, 
                                                font_family="Consola"
                                            ),

                                            Text(
                                                f"Lugar:  Quito, EC", size=15, 
                                                font_family="Consola"
                                            ),
                                        ],
                                        
                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER
                                    ),
                                    
                                    alignment=alignment.center, height=250, bgcolor=colors.WHITE,
                                    border_radius=8, border=border.all(0.5, "black"), padding=17, 
                                ),

                            ],

                            alignment=MainAxisAlignment.CENTER
                        ),

                        alignment=alignment.center
                    ),
                ],
            )
    

    def accionConsulta(e):

        global usuario

        if float(usuario[6]) >= 0.35:

            cargo(0.35)
            usuario = actualizar(usuario)

            siCon.on_click = doble(cr.cCon(), menCon)

            # page.update()
        
        else:

            saldoIns = AlertDialog(
                actions_padding=0,
                shape=RoundedRectangleBorder(radius=8),
                actions=[
                    Container(
                        width=635, height=430,
                        padding=17, bgcolor="#faf4ea", border_radius=8,
                        content=Text(
                            "Saldo Insuficiente"
                        )
                    )
                ],
            )

            siCon.on_click = doble(cr.cCon(), saldoIns)




    bCon.on_click = openBS(menCon)
    noCon.on_click = closeBS(menCon)
    # siCon.on_click = doble(cr.cCon(), menCon),

    siCon.on_click = accionConsulta



    """ P2 = [USUARIO], Consultar, Retirar, Transferir, Editar """

    P2 = (
        Column(
            expand=True,
            controls=[

                Container(
                    content=Row(
                        [
                            Image(
                                src="./Prueba APP 1/cover.png",
                                width=150,
                            ),

                            cUsu,

                            VerticalDivider(),

                            Text(
                                f"Hey! {usAc[2]}\nCta. {usAc[0]}",
                                weight=FontWeight.W_100, text_align=TextAlign.CENTER,
                                selectable=True
                            ),
                        ],

                        alignment=MainAxisAlignment.SPACE_EVENLY,
                        # horizontal_alignment=CrossAxisAlignment.CENTER
                    ),

                    bgcolor="#efe7da",
                    width=580, height=160,
                    border_radius=15, border=border.all(0.5, "black"),
                ),

                # Divider(),

                # ________

                Row(
                    [
                        Column(
                            [
                                bCon,

                                Text(
                                    "Consultar", text_align="center"
                                )
                            ],

                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        ),

                        Column(
                            [
                                bRet,

                                Text(
                                    "Retirar", text_align="center"
                                )
                            ],

                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        ),

                        Column(
                            [
                                bEdt,

                                Text(
                                    "Editar Mi Usuario", text_align="center"
                                )
                            ],

                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        ),
                    
                    ], 

                    spacing=40,
                    alignment=MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER
                )                
            ],

            spacing=35,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )
    
    """ P3 = [ADMIN], Administrar, Registrar Adm, Abastecer, ... """

    P3 = (
        Row(
            expand=True,
            controls=[

                Container(
                    content=Column(
                        [
                            Image(
                                src="./Prueba APP 1/cover1.png",
                                width=150,
                            ),

                            cAdm,

                            Divider(),

                            Text(
                                f"Hey! {usAc[0]}\nAdministrador",
                                weight=FontWeight.W_100, text_align=TextAlign.CENTER,
                                selectable=True, color="#efe7da"
                            ),
                        ],

                        alignment=MainAxisAlignment.SPACE_EVENLY,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    ),

                    bgcolor="#1c110a",
                    width=230, height=380,
                    border_radius=15, border=border.all(0.5, "white"),
                ),

                Divider(),

                # ________

                Column(
                    [
                        Column(
                            [
                                bAdm,

                                Text(
                                    "Administrar", text_align="center"
                                )
                            ],

                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            animate_offset=animation.Animation(3000, AnimationCurve.DECELERATE),
                        ),

                        Column(
                            [
                                bAbs,

                                Text(
                                    "Abastecer", text_align="center"
                                )
                            ],

                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            animate_offset=animation.Animation(3000, AnimationCurve.DECELERATE),
                        ),
                    ],

                    spacing=40,
                    alignment=MainAxisAlignment.CENTER,
                ),

                Column(
                    [
                        Column(
                            [
                                bRegA,

                                Text(
                                    "Registrar Admin", text_align="center"
                                )
                            ],

                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            animate_offset=animation.Animation(3000, AnimationCurve.DECELERATE),
                        ),

                        # Column(
                        #     [
                        #         bEdt,

                        #         Text(
                        #             "Editar Mi Usuario", text_align="center"
                        #         )
                        #     ],

                        #     alignment=MainAxisAlignment.CENTER,
                        #     horizontal_alignment=CrossAxisAlignment.CENTER,
                        #     animate_offset=animation.Animation(3000, AnimationCurve.DECELERATE),
                        # ),
                    ],

                    spacing=40,
                    alignment=MainAxisAlignment.CENTER,
                ),

                # VerticalDivider(),                
            ],

            spacing=35,
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER
        )
    )

    """ Ingrese a los menus, segun el tipo de usuario """

    if band == 1 and usAc[5] == "U":

        band = cont = 0

        page.clean()

        page.add(close)
        page.add(P2)

        page.update()

    elif band == 1 and usAc[5] == "A":

        band = cont = 0

        page.clean()

        page.add(close)
        page.add(P3)

        page.update()

    elif cont == 3:
        page.clean()

        page.add(close)
        page.add(
            AlertDialog(
                actions=[
                    Text(
                        "Agotaste tu numero de intentos\nIntentalo mas tarde",
                        size=35, weight="bold", text_align=TextAlign.CENTER
                    ),

                    ProgressBar(color="#677423", bgcolor="#bbc191")
                ],

                open=True, modal=True
            ),
        )

        sleep(3)
        page.window_close()
        

""" BUILDER """

if __name__ == "__main__":
    flet.app(target = main, assets_dir = "Prueba APP 1")

