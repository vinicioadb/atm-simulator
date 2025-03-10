
from os import system, remove, rename

import flet
from flet import *
from controls import *
import datetime, locale
import itertools as it

locale.setlocale(locale.LC_ALL, "")
fecha_actual = datetime.datetime.now()
form_dia = str(fecha_actual.strftime('%a %#d de %b %Y'))

acc = []
ct = ""


prmp = it.product(range(10), repeat=4)
ctas = list("".join(map(str, x)) for x in list(prmp))

with open("usuarios.txt", "r+") as f:
    for line in f.readlines():
        cta, ced, nom, ape, ctr, per, sld = line.strip().split(" ")
        acc.append(cta[1:])


class CR(UserControl):
    def __init__(self, usuario: list, monto: str):
        self.user = usuario
        self.mont = monto
        super().__init__()


    def PCon(self):
        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    width=655, height=450,
                    padding=17, bgcolor="#faf4ea", 
                    border_radius=8,
                    content=Row(
                        [
                            Container(
                                content=Column(
                                    [
                                            
                                        Text(
                                            "COOP. Coordillera", size=20, weight="bold",
                                        ),

                                        Text(
                                            "Comprobante", size=15, weight="bold",
                                        ),

                                        Text(
                                            "Consulta", size=15, weight="bold",
                                        ),

                                        Text(
                                            f"""
        --------------------------------

        Saldo:   $ {self.user[6]}
        Fecha:   {form_dia}
        Cuenta:  XXX{self.user[0][3:]}
        Lugar:   Quito, EC

        --------------------------------
                                            """,
                                            size=15
            
                                        ),

                                    ],
                                        
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER
                                ),
                                    
                                alignment=alignment.center, height=350, bgcolor=colors.WHITE38,
                                border=border.all(0.5, "black"), padding=17, 
                            ),

                        ],

                        alignment=MainAxisAlignment.CENTER
                    ),

                    alignment=alignment.center
                ),
            ],
        )


    def PRet():
        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    width=635, height=450,
                    padding=17, bgcolor="#faf4ea", 
                    border_radius=8,
                    content=Column(
                        [   
                            Card(
                                elevation=20,
                                content=Container(
                                    width=350,
                                    padding=20,
                                    bgcolor="#faf4ea",
                                    border_radius=8, 
                                    alignment=alignment.center,
                                    content=Row(
                                        [
                                            Icon(
                                                icons.CONFIRMATION_NUMBER, size=30
                                            ),

                                            Text(
                                                "Retirar", size=20
                                            ),
                                        ],

                                        alignment=MainAxisAlignment.CENTER
                                    )
                                )
                            ),

                            Text(
                                "Montos Sugeridos"
                            ),

                            Divider(),

                            Row(
                                [
                                    Column(
                                        controls=[
                                            Reti10, 
                                            Reti20, 
                                            Reti30,
                                        ],

                                        alignment=MainAxisAlignment.CENTER
                                    ),

                                    Column(
                                        controls=[
                                            Reti40, 
                                            Reti50, 
                                            OtroMon,
                                        ],

                                        alignment=MainAxisAlignment.CENTER
                                    )
                                ],

                                spacing=40,
                                alignment=MainAxisAlignment.CENTER
                            ),
                        ],
                        
                        spacing=30,
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                ),
            ],
        ) 

    
    def PRetO():
        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    width=435, height=490,
                    padding=17, bgcolor="#faf4ea", 
                    border_radius=8,
                    content=Column(
                        [   
                            Card(
                                elevation=20,
                                content=Container(
                                    width=350,
                                    padding=20,
                                    bgcolor="#faf4ea",
                                    border_radius=8, 
                                    alignment=alignment.center,
                                    content=Row(
                                        [
                                            Icon(
                                                icons.CONFIRMATION_NUMBER, size=30
                                            ),

                                            Text(
                                                "Retirar", size=20
                                            ),
                                        ],

                                        alignment=MainAxisAlignment.CENTER
                                    )
                                ),
                            ),

                            Text(
                                "Ingrese un monto"
                            ),

                            Text(
                                "Valores multiplos de 10\nMonto menor a $500", 
                                color="green", text_align="center"
                            ),

                            Divider(),

                            tfRetO,

                            bReti,
                        ],

                        spacing=30,
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                ),
            ],
        )
         
    
    def PEdit():
        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    width=435, height=490,
                    padding=17, bgcolor="#faf4ea", 
                    border_radius=8,
                    content=Column(
                        [   
                            Card(
                                elevation=20,
                                content=Container(
                                    width=350,
                                    padding=20,
                                    bgcolor="#faf4ea",
                                    border_radius=8, 
                                    alignment=alignment.center,
                                    content=Row(
                                        [
                                            Icon(
                                                icons.PASSWORD, size=30
                                            ),

                                            Text(
                                                "Editar", size=20
                                            ),
                                        ],

                                        alignment=MainAxisAlignment.CENTER
                                    )
                                ),
                            ),

                            Text(
                                "Ingrese el Nuevo PIN"
                            ),

                            Divider(),

                            tfPIN,

                            bEdi,
                        ],

                        spacing=30,
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                ),
            ],
        )     


    def PRegC(self):
        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    width=655, height=450,
                    padding=17, bgcolor="#faf4ea", 
                    border_radius=8,
                    content=Row(
                        [
                            Container(
                                content=Column(
                                    [
                                            
                                        Text(
                                            "Bienvenido", size=20, weight="bold",
                                            font_family="Aesthetica"
                                        ),

                                        Text(
                                            "Nuevo Usuario", size=15, weight="bold",
                                        ),

                                        Text(
                                            f"""
        --------------------------------

        Cedula:  {self.user[1]}
        Cuenta:  {self.user[0]}

        --------------------------------
                                            """,
                                            size=15
            
                                        ),

                                    ],
                                        
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER
                                ),
                                    
                                alignment=alignment.center, height=350, bgcolor=colors.WHITE38,
                                border=border.all(0.5, "black"), padding=17, 
                            ),

                        ],

                        alignment=MainAxisAlignment.CENTER
                    ),

                    alignment=alignment.center
                ),
            ],
        )


    def PEditC(self):
        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    width=655, height=450,
                    padding=17, bgcolor="#faf4ea", 
                    border_radius=8,
                    content=Row(
                        [
                            Container(
                                content=Column(
                                    [
                                            
                                        Text(
                                            "COOP. Coordillera", size=20, weight="bold",
                                        ),

                                        Text(
                                            "Comprobante", size=15, weight="bold",
                                        ),

                                        Text(
                                            "Edicion de Pin", size=15, weight="bold",
                                        ),

                                        Text(
                                            f"""
        --------------------------------

        Fecha:   {form_dia}
        Cuenta:  XXX{self.user[0][3:]}
        Lugar:   Quito, EC

        --------------------------------
                                            """,
                                            size=15
            
                                        ),

                                    ],
                                        
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER
                                ),
                                    
                                alignment=alignment.center, height=350, bgcolor=colors.WHITE38,
                                border=border.all(0.5, "black"), padding=17, 
                            ),

                        ],

                        alignment=MainAxisAlignment.CENTER
                    ),

                    alignment=alignment.center
                ),
            ],
        )


    def PReg():
        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    width=435, height=490,
                    padding=17, bgcolor="#faf4ea", 
                    border_radius=8,
                    content=Column(
                        [   
                            Card(
                                elevation=20,
                                content=Container(
                                    width=350,
                                    padding=20,
                                    bgcolor="#faf4ea",
                                    border_radius=8, 
                                    alignment=alignment.center,
                                    content=Row(
                                        [
                                            Icon(
                                                icons.ADD, size=30
                                            ),

                                            Text(
                                                "Registrar", size=20
                                            ),
                                        ],

                                        alignment=MainAxisAlignment.CENTER
                                    )
                                ),
                            ),

                            Text(
                                "Siga las instrucciones"
                            ),

                            Divider(),

                            tfced,

                            Row(
                                [
                                    tfnom,
                                    tfape,
                                ],

                                alignment=MainAxisAlignment.CENTER,
                                vertical_alignment=CrossAxisAlignment.CENTER
                            ),

                            tfpsg,

                            Row(
                                [
                                    Row(
                                        [tfA],

                                        alignment=MainAxisAlignment.CENTER,
                                        vertical_alignment=CrossAxisAlignment.CENTER
                                    ),

                                    Row(
                                        [tfU],

                                        alignment=MainAxisAlignment.CENTER,
                                        vertical_alignment=CrossAxisAlignment.CENTER
                                    ),
                                ],

                                alignment=MainAxisAlignment.CENTER,
                                vertical_alignment=CrossAxisAlignment.CENTER
                            ),

                            bRegi,
                        ],

                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                ),
            ],
        )


    def comprobante(self):
        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    width=655, height=450,
                    padding=17, bgcolor="#faf4ea", 
                    border_radius=8,
                    content=Row(
                        [
                            Container(
                                content=Column(
                                    [
                                            
                                        Text(
                                            "COOP. Coordillera", size=20, weight="bold",
                                        ),

                                        Text(
                                            "Comprobante", size=15, weight="bold",
                                        ),

                                        Text(
                                            "Retiro", size=15, weight="bold",
                                        ),

                                        Text(
                                            f"""
        --------------------------------

        Monto:   $ {self.mont}
        Fecha:   {form_dia}
        Cuenta:  XXX{self.user[0][3:]}
        Lugar:   Quito, EC

        --------------------------------
                                            """,
                                            size=15
            
                                        ),

                                    ],
                                        
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER
                                ),
                                    
                                alignment=alignment.center, height=350, bgcolor=colors.WHITE38,
                                border=border.all(0.5, "black"), padding=17, 
                            ),

                        ],

                        alignment=MainAxisAlignment.CENTER
                    ),

                    alignment=alignment.center
                ),
            ],
        )



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


def edicionPIN(newPIN: str, cedula: str):

    with open("usuarios.txt", "r+") as f, open("temp.txt", "w+") as ree:

        for line in f.readlines():
            editUS = line.strip().split(" ")

            if cedula in editUS:
                
                editUS[4] = newPIN
                ree.write(" ".join(editUS)+"\n")

            else:
                ree.write(" ".join(editUS)+"\n")
                                             
    remove("usuarios.txt")
    rename("temp.txt", "usuarios.txt")


def generarCTA():

    global ct, revCt

    for cuentas, regist in zip(ctas, acc):

        if cuentas != regist:
            ct = cuentas
            break

        else: ct = ctas[ctas.index(cuentas) + 1]

        acc.append(ct)

        revCt = f"2{ct}"
    
    return revCt



def main(page: Page):


    page.fonts = {
        "Josefina": "./Prueba APP 1/fonts/JosefinSans.ttf",
        "Aesthetica": "./Prueba APP 1/fonts/aesthetica.ttf",
        "Consolas": "./Prueba APP 1/fonts/Consola.ttf"
    }

    page.window_width = 960
    page.window_height = 540
    page.theme_mode = "light"
    page.window_focused = True
    page.window_resizable = False
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.bgcolor = "#f1ece2"

    page.theme = Theme(font_family = "Consolas")

    close = Row(
        [
            WindowDragArea(Container(Text(), bgcolor="#f1ece2",padding=10), expand=True),
            IconButton(icons.CLOSE_ROUNDED, icon_color="black",on_click=lambda _: page.window_close()),
        ]
    )


    class openBS(UserControl):
        def __init__(self, mensaje: BottomSheet):
            self.bs = mensaje
            super().__init__()
           
        def __call__(self, e):
            page.add(self.bs)
            self.bs.open = True
            self.bs.update()
            # page.update()
    

    class closBS(UserControl):
        def __init__(self, mensaje: BottomSheet):
            self.bs = mensaje
            super().__init__()
           
        def __call__(self, e):
            self.bs.open = False
            self.bs.update()
            page.update()


    class openDLG(UserControl):
        def __init__(self, ventana: AlertDialog):
            self.dg = ventana
            super().__init__()
           
        def __call__(self, e, *args, **kwargs):
            page.dialog = self.dg
            self.dg.open = True
            page.update()

    
    class closeDLG(UserControl):
        def __init__(self, ventana: AlertDialog):
            self.dlg = ventana
            super().__init__()

        def __call__(self, e, *args, **kwargs):
            self.dlg.open = False
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
        
    
    class dobleDLG(UserControl):
        def __init__(self, venN1: AlertDialog, venN2: AlertDialog):
            self.venN1 = venN1
            self.venN2 = venN2
            super().__init__()
        
        def __call__(self, e,*args, **kwargs):
            
            page.dialog = self.venN1
            self.venN1.open = False
            page.update()

            sleep(1)
            
            page.dialog = self.venN2
            self.venN2.open = True
            page.update()


            # return super().__call__(*args, **kwds)
    

    """ P1 """

    compr = False
    
    temp = ""
    monto = ""
    cont = band = canti = 0

    inf = ["" for x in range(7)]
    usAc = ["" for x in range(7)]


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


    P1 = Container(
        expand=True,
        alignment=alignment.center,
        content=Row(
            alignment=MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Image(
                    src="./Prueba APP 1/dirt.png",
                    width=300,
                ),

                Card(
                    elevation=20,
                    content=Container(
                        height=400, 
                        padding=20,
                        border_radius=8, 
                        bgcolor="#faf4ea",
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

                                IconButton(
                                    width=230,
                                    content=Text(
                                        "Ingresar", weight="bold",
                                        color="black"
                                    ),

                                    style=ButtonStyle(
                                        bgcolor="#bbc191",
                                        shape=RoundedRectangleBorder(radius=8)
                                    ),

                                    on_click=ingresar
                                ),
                                
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

    page.update()

    page.add(close)
    page.add(P1)
    page.update()

    
    while True:

        if band == 1 or cont == 3:
            
            page.add(ProgressBar(color="#677423", bgcolor="#bbc191"))
            
            sleep(2.3)
            break
    
    
    print(f"Usuario Actual: {usAc[2]}, $ {usAc[6]}")

    
    """ CONSULTAR """

    def CJRConsulta(e):

        nonlocal usAc

        if float(usAc[6]) >= 0.35:

            recargo(0.35, usAc)
            usAc = actual(usAc[1])

            ventanaCON = CR(usAc, "").PCon()

            page.dialog = ventanaCON
            ventanaCON.open = True
            page.update()

            menCon.open = False
            menCon.update()
            page.update()
        
        else:

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()

            menCon.open = False
            menCon.update()
            page.update()


    """ RETIRAR """

    def Retiro10Comp(e):
        
        nonlocal usAc, monto
        monto = 10.35

        if float(usAc[6]) >= 10.35:

            recargo(10.35, usAc)
            usAc = actual(usAc[1])

            R10 = CR(usAc, "10.35").comprobante()

            # page.dialog = venRet
            venRet.open = False
            menRet10.open = False
            
            menRet10.update()
            page.update()

            sleep(1)

            page.dialog = R10
            R10.open = True
            page.update()
        
        else:

            # page.dialog = venRet
            venRet.open = False
            menRet10.open = False

            menRet10.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()

    def Retiro10SN(e):
        
        nonlocal usAc, monto
        monto = 10

        if float(usAc[6]) >= 10:

            recargo(10, usAc)
            usAc = actual(usAc[1])

            # page.dialog = venRet
            venRet.open = False
            menRet10.open = False
            
            menRet10.update()
            page.update()

            sleep(1)

            page.dialog = retiDN
            retiDN.open = True
            page.update()
        
        else:

            # page.dialog = venRet
            venRet.open = False
            menRet10.open = False

            menRet10.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()

    def Retiro20Comp(e):
        
        nonlocal usAc, monto
        monto = 20.35

        if float(usAc[6]) >= 20.35:

            recargo(20.35, usAc)
            usAc = actual(usAc[1])

            R20 = CR(usAc, "20.35").comprobante()

            # page.dialog = venRet
            venRet.open = False
            menRet20.open = False
            
            menRet20.update()
            page.update()

            sleep(1)

            page.dialog = R20
            R20.open = True
            page.update()
        
        else:

            # page.dialog = venRet
            venRet.open = False
            menRet20.open = False

            menRet20.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()

    def Retiro20SN(e):
        
        nonlocal usAc, monto
        monto = 20

        if float(usAc[6]) >= 20:

            recargo(20, usAc)
            usAc = actual(usAc[1])

            # page.dialog = venRet
            venRet.open = False
            menRet20.open = False
            
            menRet20.update()
            page.update()

            sleep(1)

            page.dialog = retiDN
            retiDN.open = True
            page.update()
        
        else:

            # page.dialog = venRet
            venRet.open = False
            menRet20.open = False

            menRet20.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()

    def Retiro30Comp(e):
        
        nonlocal usAc, monto
        monto = 30.35

        if float(usAc[6]) >= 30.35:

            recargo(30.35, usAc)
            usAc = actual(usAc[1])

            R30 = CR(usAc, "30.35").comprobante()

            # page.dialog = venRet
            venRet.open = False
            menRet30.open = False
            
            menRet30.update()
            page.update()

            sleep(1)

            page.dialog = R30
            R30.open = True
            page.update()
        
        else:

            # page.dialog = venRet
            venRet.open = False
            menRet30.open = False

            menRet30.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()

    def Retiro30SN(e):
        
        nonlocal usAc, monto
        monto = 30

        if float(usAc[6]) >= 30:

            recargo(30, usAc)
            usAc = actual(usAc[1])

            # page.dialog = venRet
            venRet.open = False
            menRet30.open = False
            
            menRet30.update()
            page.update()

            sleep(1)

            page.dialog = retiDN
            retiDN.open = True
            page.update()
        
        else:

            # page.dialog = venRet
            venRet.open = False
            menRet30.open = False

            menRet30.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()
    
    def Retiro40Comp(e):
        
        nonlocal usAc, monto
        monto = 40.35

        if float(usAc[6]) >= 40.35:

            recargo(40.35, usAc)
            usAc = actual(usAc[1])

            R40 = CR(usAc, "40.35").comprobante()

            # page.dialog = venRet
            venRet.open = False
            menRet40.open = False
            
            menRet40.update()
            page.update()

            sleep(1)

            page.dialog = R40
            R40.open = True
            page.update()
        
        else:

            # page.dialog = venRet
            venRet.open = False
            menRet40.open = False

            menRet40.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()

    def Retiro40SN(e):
        
        nonlocal usAc, monto
        monto = 40

        if float(usAc[6]) >= 40:

            recargo(40, usAc)
            usAc = actual(usAc[1])

            # page.dialog = venRet
            venRet.open = False
            menRet40.open = False
            
            menRet40.update()
            page.update()

            sleep(1)

            page.dialog = retiDN
            retiDN.open = True
            page.update()
        
        else:

            # page.dialog = venRet
            venRet.open = False
            menRet40.open = False

            menRet40.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()

    def Retiro50Comp(e):
        
        nonlocal usAc, monto
        monto = 50.35

        if float(usAc[6]) >= 50.35:

            recargo(50.35, usAc)
            usAc = actual(usAc[1])

            R50 = CR(usAc, "30.35").comprobante()

            # page.dialog = venRet
            venRet.open = False
            menRet50.open = False
            
            menRet50.update()
            page.update()

            sleep(1)

            page.dialog = R50
            R50.open = True
            page.update()
        
        else:

            # page.dialog = venRet
            venRet.open = False
            menRet50.open = False

            menRet50.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()

    def Retiro50SN(e):
        
        nonlocal usAc, monto
        monto = 50

        if float(usAc[6]) >= 50:

            recargo(50, usAc)
            usAc = actual(usAc[1])

            # page.dialog = venRet
            venRet.open = False
            menRet50.open = False
            
            menRet50.update()
            page.update()

            sleep(1)

            page.dialog = retiDN
            retiDN.open = True
            page.update()
        
        else:

            # page.dialog = venRet
            venRet.open = False
            menRet50.open = False

            menRet50.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()

    def validRet(e):

        # nonlocal compr

        if (tfRetO.value.isnumeric() and (int(tfRetO.value) % 10 == 0) and int(tfRetO.value) <= 500) == False:

            tfRetO.focus()
            tfRetO.error_text = "Monto Invalido"
            tfRetO.value = ""

        else:
            # compr = True
            tfRetO.border_color = "green"

            page.add(menRetO)
            menRetO.open = True
            menRetO.update()


        tfRetO.update()

        sleep(2)
        tfRetO.error_text = None
        tfRetO.border_color = "transparent"

        page.update()

    def RetiroOComp(e):

        nonlocal usAc, monto
        
        monto = int(tfRetO.value) + 0.35

        if float(usAc[6]) >= monto:

            recargo(monto, usAc)
            usAc = actual(usAc[1])

            RO = CR(usAc, str(monto)).comprobante()

            # page.dialog = venRetO
            venRetO.open = False
            menRetO.open = False
            
            menRetO.update()
            page.update()

            sleep(1)

            page.dialog = RO
            RO.open = True
            page.update()
        
        else:

            # page.dialog = venRetO
            venRetO.open = False
            menRetO.open = False

            menRetO.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()
    
    def RetiroOSN(e):

        nonlocal usAc, monto
        
        monto = int(tfRetO.value)

        if float(usAc[6]) >= monto:

            recargo(monto, usAc)
            usAc = actual(usAc[1])

            page.dialog = venRetO
            venRetO.open = False
            menRetO.open = False
            
            menRetO.update()
            page.update()

            sleep(1)

            page.dialog = retiDN
            retiDN.open = True
            page.update()
        
        else:

            page.dialog = venRetO
            venRetO.open = False
            menRetO.open = False

            menRetO.update()
            page.update()

            sleep(1)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()

    
    """ EDITAR """

    def validEdt(e):

        nonlocal usAc

        if (tfPIN.value.isnumeric() and len(tfPIN.value) == 4) == False:

            tfPIN.focus()
            tfPIN.error_text = "PIN Invalido"
            tfPIN.value = ""

        else:

            edicionPIN(tfPIN.value, usAc[0])

            page.dialog = venEdt
            venEdt.open = False
            page.update()

            sleep(1)

            ventanaEDT = CR(usAc, "").PEditC()

            page.dialog = ventanaEDT
            ventanaEDT.open = True
            page.update()


        tfPIN.update()

        sleep(2)
        tfPIN.value = ""
        tfPIN.error_text = None
        tfPIN.border_color = "transparent"

        page.update()

    
    """ REGISTRAR """

    def validReg(e):

        nonlocal usAc, canti 

        canti = 0

        if (tfced.value.isnumeric() and len(tfced.value) == 10):
            
            with open("usuarios.txt", "r+") as f:

                for linea in f.readlines():
                    cedulas = linea.strip().split(" ")

                    if tfced.value in cedulas:

                        tfced.value = ""
                        tfced.focus()
                        tfced.error_text = "Cedula Ya Rgistrada"
                    
                    else: canti += 1
        
        else:
            tfced.value = ""
            tfced.focus()
            tfced.error_text = "Cedula Invalida"
        
        if (tfnom.value.isalpha()) == False:

            tfnom.value = ""
            tfnom.error_text = "Nombre Invalido"

        else: canti += 1

        if (tfape.value.isalpha()) == False:

            tfape.value = ""
            tfape.error_text = "Apellido Invalido"

        if (tfpsg.value.isnumeric() and len(tfpsg.value) == 4) == False:

            tfpsg.value = ""
            tfpsg.error_text = "PIN Invalido"

        else: canti += 1

        tfced.update()
        tfnom.update()
        tfape.update()
        tfpsg.update()
        
        sleep(2)
        tfced.error_text = tfnom.error_text = tfape.error_text = tfpsg.error_text = None
        tfced.border_color = tfnom.border_color = tfape.border_color = tfpsg.border_color = "transparent"
        page.update()

        canti -= 1

        print(canti)

        if canti == 4:

            inf[0] = generarCTA()
            inf[1] = tfced.value
            inf[2] = tfnom.value
            inf[3] = tfape.value
            inf[4] = tfpsg.value
            tfA.on_change = inf[5] = "A"
            tfU.on_change = inf[5] = "U"
            inf[6] = "10.0"

            cadeInf = " ".join(map(str, inf))

            with open("usuarios.txt", "a+") as f:
                f.write(cadeInf + "\n")
        
            page.dialog = venReg
            venReg.open = False
            page.update()

            sleep(1)

            ventanaREG = CR(inf, "").PRegC()

            page.dialog = ventanaREG
            ventanaREG.open = True
            page.update()
        

    # """ P2 """

    if band == 1 and usAc[5] == "U":

        band = cont = 0

        """"""

        bCon.on_click = openBS(menCon)
        siCon.on_click = CJRConsulta
        noCon.on_click = closBS(menCon)
        
        """"""

        venRet = CR.PRet()
        bRet.on_click = openDLG(venRet)
                
        Reti10.on_click = openBS(menRet10)
        siRet10.on_click = Retiro10Comp
        noRet10.on_click =  Retiro10SN

        Reti20.on_click = openBS(menRet20)
        siRet20.on_click = Retiro20Comp
        noRet20.on_click =  Retiro20SN
        
        Reti30.on_click = openBS(menRet30)
        siRet30.on_click = Retiro30Comp
        noRet30.on_click =  Retiro30SN
        
        Reti40.on_click = openBS(menRet40)
        siRet40.on_click = Retiro40Comp
        noRet40.on_click =  Retiro40SN
        
        Reti50.on_click = openBS(menRet50)
        siRet50.on_click = Retiro50Comp
        noRet50.on_click =  Retiro50SN

        venRetO = CR.PRetO()
        OtroMon.on_click = dobleDLG(venRet, venRetO)
        bReti.on_click = validRet
        siRetO.on_click = RetiroOComp
        noRetO.on_click = RetiroOSN
        
        """"""

        venEdt = CR.PEdit()
        bEdt.on_click = openDLG(venEdt)
        bEdi.on_click = validEdt

        page.update()

        P2 = Container(
            expand=True,
            alignment=alignment.center,
            content=Column(
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
                                    f"Hey! {usAc[2]} {usAc[3][0]}.\nCta. {usAc[0]}",
                                    weight=FontWeight.W_100, text_align=TextAlign.CENTER,
                                    selectable=True
                                ),
                            ],

                            alignment=MainAxisAlignment.SPACE_EVENLY,
                        ),

                        bgcolor="#efe7da",
                        width=580, height=160,
                        border_radius=15, border=border.all(0.5, "black"),
                    ),

                    # ________

                    Card(
                        elevation=20,
                        content=Container(
                            width=580,
                            # height=400, 
                            padding=20,
                            border_radius=8, 
                            bgcolor="#faf4ea",
                            content=Row(
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
                                                "Editar\nPIN de Ingreso", text_align="center"
                                            )
                                        ],

                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                    ),
                                    
                                ],

                                spacing=40,
                                alignment=MainAxisAlignment.CENTER,
                                vertical_alignment=CrossAxisAlignment.CENTER
                            ),
                        )
                    ),
                ],

                spacing=35,
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            )
        )

        page.clean()
        page.add(close)
        page.add(P2)
        page.update()

    
    # """ P3 """

    elif band == 1 and usAc[5] == "A":

        band = cont = 0

        """"""
        
        venReg = CR.PReg()
        bReg.on_click = openDLG(venReg)
        bRegi.on_click = validReg
        
        page.update()

        P3 = Container(
            expand=True,
            alignment=alignment.center,
            content=Column(
                expand=True,
                controls=[
                    Container(
                        content=Row(
                            [
                                Image(
                                    src="./Prueba APP 1/cover1.png",
                                    width=150,
                                ),

                                cAdm,

                                VerticalDivider(),

                                Column(
                                    [
                                        Text(
                                            "Administrador",
                                            weight=FontWeight.W_100, text_align=TextAlign.CENTER,
                                            selectable=True, color="white"
                                        ),

                                        Text(
                                            f"Hey! {usAc[2]} {usAc[3][0]}.\nCta. {usAc[0]}",
                                            weight=FontWeight.W_100, text_align=TextAlign.CENTER,
                                            selectable=True, color="white"
                                        ),
                                    ],

                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER
                                ),

                            ],

                            alignment=MainAxisAlignment.SPACE_EVENLY,
                        ),

                        bgcolor="#252627",
                        width=580, height=160,
                        border_radius=15, border=border.all(0.5, "black"),
                    ),

                    # ________

                    Card(
                        elevation=20,
                        content=Container(
                            width=580,
                            padding=20,
                            border_radius=8, 
                            bgcolor="#faf4ea",
                            content=Row(
                                [
                                    Column(
                                        [
                                            bReg,

                                            Text(
                                                "Registrar", text_align="center"
                                            )
                                        ],

                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                    ),

                                    Column(
                                        [
                                            bAdm,

                                            Text(
                                                "Mantenimiento\nde Usuarios", text_align="center"
                                            )
                                        ],

                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                    ),
                                ],

                                spacing=40,
                                alignment=MainAxisAlignment.CENTER,
                                vertical_alignment=CrossAxisAlignment.CENTER
                            ),
                        )
                    ),
                ],

                spacing=35,
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            )
        )

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



if __name__ == "__main__":
    flet.app(target = main, assets_dir = "Prueba APP 1")
