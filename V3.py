
""" CAJERO AUTOMATICO V3 """


from os import system, remove, rename

import flet
from flet import *
from controls_V3 import *
import datetime, locale
import itertools as it
from time import sleep


""" PROCESOS INICIALES """

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


""" Funciones del Cajero """


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


def edicion(nuevo: str, cedula: str, columna: int):

    with open("usuarios.txt", "r+") as f, open("temp.txt", "w+") as ree:

        for line in f.readlines():
            editUS = line.strip().split(" ")

            if cedula in editUS:
                
                editUS[columna] = nuevo
                ree.write(" ".join(editUS)+"\n")

            else:
                ree.write(" ".join(editUS)+"\n")
                                             
    remove("usuarios.txt")
    rename("temp.txt", "usuarios.txt")


def eliminacion(cedula: str):

    compr = True

    with open("usuarios.txt", "r") as lee, open("temp.txt", "w") as ree:
                
        for dato in lee.readlines():
            usuarioElm = dato.strip().strip(" ")
                
            if cedula in usuarioElm: compr = True

            else: ree.writelines(f"{usuarioElm}\n")
                
    remove("usuarios.txt")
    rename("temp.txt", "usuarios.txt")


def saldoCJR(cargo: float, accion: str):

    match accion:

        case "-":

            with open("saldoCJR.txt", "r+") as f, open("temp.txt", "w+") as ree:

                for linea in f.readlines():
                    
                    saldoAC = linea.strip().split(" ")

                    carg = round(((float(saldoAC[0]) - cargo)), 2)
                    saldoAC[0] = str(carg)
                    ree.write(" ".join(saldoAC)+"\n")
                                                    
            remove("saldoCJR.txt")
            rename("temp.txt", "saldoCJR.txt")
        
        case "+":

            with open("saldoCJR.txt", "r+") as f, open("temp.txt", "w+") as ree:

                for linea in f.readlines():
                    
                    saldoAC = linea.strip().split(" ")

                    carg = round(((float(saldoAC[0]) + cargo)), 2)
                    saldoAC[0] = str(carg)
                    ree.write(" ".join(saldoAC)+"\n")
                                                    
            remove("saldoCJR.txt")
            rename("temp.txt", "saldoCJR.txt")


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


""" Constructores de Ventanas """


class Regresiva(UserControl):
    def __init__(self, segundos: int):
        self.segs = segundos
        super().__init__()
    
    def vent(self):
        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    padding=50, bgcolor="#faf4ea",
                    border_radius=8,
                    content=Row(
                        [
                            Column(
                                [
                                        Row(
                                            [
                                                Image(
                                                    src="./Prueba APP 1/icons/exito.png", height=32
                                                ),

                                                Text(
                                                    "Edicion Exitosa", size=20, color="green", weight="bold"
                                                ),
                                            ]
                                        ),

                                    Text(
                                            "Estas a punto de Cerrar Sesión", size=13, weight="bold"
                                        ),


                                ],

                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER
                            ),

                            Countdown(self.segs),
                        ],

                        alignment=MainAxisAlignment.CENTER
                    )
                )
            ],
        )


class ventana(UserControl):
    def __init__(self, btSi: TextButton, btNo: TextButton, btCn: TextButton):
        self.si = btSi
        self.no = btNo
        self.cn = btCn
        super().__init__()

    def Consulta():
        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    padding=50, bgcolor="#faf4ea", 
                    border_radius=8,
                    content=Column(
                        [
                            Text(
                                "Ésta acción tiene un costo de $ 0.35\n¿Desea continuar?",
                                text_align="center", size=20
                            ),

                            Row(
                                [
                                    siCon, noCon
                                ],

                                alignment=MainAxisAlignment.CENTER
                            ),

                        ],

                        alignment=MainAxisAlignment.CENTER
                    )
                )
            ],

            modal=True
        )


    def Retiro(self):

        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    padding=50, bgcolor="#faf4ea", 
                    border_radius=8,
                    content=Column(
                        [
                            Text(
                                "Imprimir su comprobante por $ 0.35\n¿Deseas continuar?",
                                text_align="center", size=20
                            ),
                            Row(
                                [
                                    self.si, self.no, self.cn
                                ],

                                alignment=MainAxisAlignment.CENTER
                            ),
                        ],

                        alignment=MainAxisAlignment.CENTER
                    )
                )
            ],

            modal=True
        )     
    

    def Abastecer(self):

        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    padding=50, bgcolor="#faf4ea", 
                    border_radius=8,
                    content=Column(
                        [
                            Text(
                                "Confirmar Acción",
                                text_align="center", size=20
                            ),
                            Row(
                                [
                                    self.si, self.cn
                                ],

                                alignment=MainAxisAlignment.CENTER
                            ),
                        ],

                        alignment=MainAxisAlignment.CENTER
                    )
                )
            ],

            modal=True
        ) 


class comprob(UserControl):
    def __init__(self, usuario: list, monto: str):
        self.ct = usuario
        self.mn = monto
        super().__init__()
    

    def CONS(self):

        saldo = f"""
--------------------------------

Saldo:   $ {self.ct[6]}
Fecha:   {form_dia}
Cuenta:  XXX{self.ct[0][3:]}
Lugar:   Quito, EC

--------------------------------
        """

        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    image_src="./Prueba APP 1/comprobante.png",                
                    width=655, height=450, border_radius=8,
                    padding=17, bgcolor="#faf4ea",
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
                                f"{saldo}"
                            )
                        ],

                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                    
                    alignment=alignment.center
                )
            ]
        )
    
    
    def RETI(self):

        saldo = f"""
--------------------------------

Monto:   $ {self.mn}
Fecha:   {form_dia}
Cuenta:  XXX{self.ct[0][3:]}
Lugar:   Quito, EC

--------------------------------
        """

        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    image_src="./Prueba APP 1/comprobante.png",                
                    width=655, height=450, border_radius=8,
                    padding=17, bgcolor="#faf4ea",
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
                                f"{saldo}"
                            )
                        ],

                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                    
                    alignment=alignment.center
                )
            ]
        )


    def ABS(self):

        saldo = f"""
--------------------------------
         
Nombre:   {self.ct[3]} {self.ct[2][0]}.
Cédula:   {self.ct[1]}
Fecha:    {form_dia}
Cantidad: $ {self.mn}
Cuenta:   XXX{self.ct[0][3:]}
Lugar:    Quito, EC

--------------------------------
        """

        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    image_src="./Prueba APP 1/comprobante.png",                
                    width=655, height=450, border_radius=8,
                    padding=17, bgcolor="#faf4ea",
                    content=Column(
                        [
                            Text(
                                "COOP. Coordillera", size=20, weight="bold",
                            ),

                            Text(
                                "Comprobante", size=15, weight="bold",
                            ),

                            Text(
                                "Abastecimiento", size=15, weight="bold",
                            ),

                            Text(
                                f"{saldo}"
                            )
                        ],

                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                    
                    alignment=alignment.center
                )
            ]
        )


class nuevaCta(UserControl):
    def __init__(self, usuario: list):
        self.us = usuario
        super().__init__()
    
    def ventana(self):
        return AlertDialog(
            actions_padding=0,
            shape=RoundedRectangleBorder(radius=8),
            actions=[
                Container(
                    padding=50, bgcolor="#faf4ea", border_radius=8,
                    content=Row(
                        [
                            Image(
                                src="./Prueba APP 1/welco.png", height=256
                            ),


                            Card(
                                content=Container(
                                    # width=350,
                                    padding=20,
                                    bgcolor="#faf4ea",
                                    border_radius=8, 
                                    alignment=alignment.center,
                                    content=Column(
                                        [
                                            Text(
                                                "Gracias !", weight="bold", font_family="Aesthetica", size=50
                                            ),

                                            Text(
                                                "Registro Exitoso", weight="bold", size=18
                                            ),

                                            Divider(visible=True),

                                            Column(
                                                [
                                                    Row(
                                                        [
                                                            Text(
                                                                f"Cédula:  ", weight="bold", size=16
                                                            ),
                                                            
                                                            Text(
                                                                f"{self.us[1]}", size=16
                                                            )
                                                        ],

                                                        alignment=MainAxisAlignment.SPACE_EVENLY
                                                    ),

                                                    Row(
                                                        [
                                                            Text(
                                                                f"Nombre:  ", weight="bold", size=16
                                                            ),
                                                            
                                                            Text(
                                                                f"{self.us[2]}", size=16
                                                            )
                                                        ],

                                                        alignment=MainAxisAlignment.SPACE_EVENLY
                                                    ),

                                                    Row(
                                                        [
                                                            Text(
                                                                f"Apellido:  ", weight="bold", size=16
                                                            ),
                                                            
                                                            Text(
                                                                f"{self.us[3]}", size=16
                                                            )
                                                        ],

                                                        alignment=MainAxisAlignment.SPACE_EVENLY
                                                    ),
                                                    
                                                    Row(
                                                        [
                                                            Text(
                                                                f"Cuenta:  ", weight="bold", size=16
                                                            ),
                                                            
                                                            Text(
                                                                f"{self.us[0]}", size=16
                                                            )
                                                        ],

                                                        alignment=MainAxisAlignment.SPACE_EVENLY
                                                    ),

                                                ],

                                                alignment=MainAxisAlignment.CENTER
                                            ),

                                        ], 

                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER
                                    )
                                ),

                                elevation=20
                            ),
                        ],

                        spacing=40,
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER
                    )
                )
            ],

        )



def main(page: Page):

    class openDG(UserControl):
        def __init__(self, ventana: AlertDialog):
            self.dg = ventana
            super().__init__()
           
        def __call__(self, e, *args, **kwargs):
            page.dialog = self.dg
            self.dg.open = True
            page.update()

    class closeDG(UserControl):
        def __init__(self, ventana: AlertDialog):
            self.dlg = ventana
            super().__init__()

        def __call__(self, e, *args, **kwargs):
            self.dlg.open = False
            page.update()

    page.fonts = {
        "Josefina": "./Prueba APP 1/fonts/JosefinSans.ttf",
        "Aesthetica": "./Prueba APP 1/fonts/aesthetica.ttf",
        "Consolas": "./Prueba APP 1/fonts/Consola.ttf"
    }

    page.window_width = 960
    page.window_height = 540
    page.theme_mode = "light"
    page.window_focused = True
    page.window_frameless = True
    page.window_resizable = False
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True

    page.theme = Theme(font_family = "Consolas")

    close = Row(
        [
            WindowDragArea(Container(Text(), bgcolor="transparent", padding=10), expand=True),
            IconButton(icons.CLOSE_ROUNDED, icon_color="black", on_click=lambda _: page.window_close()),
        ]
    )

    btBack = IconButton(
        style=ButtonStyle(bgcolor="#bbc191", overlay_color="red", shape=RoundedRectangleBorder(radius=8)),
        content=Text("Cerrar Sesión", weight="bold", color="black", size=12), on_click=lambda _: page.go("/login")
    )

    back = Row(
        [
            WindowDragArea(Container(Text(), bgcolor="transparent", padding=10), expand=True), btBack
        ]
    )

    bkUs = Row(
        [
            WindowDragArea(Container(Text(), bgcolor="transparent", padding=10), expand=True),
            IconButton(icons.HOME_ROUNDED, icon_color="black", tooltip="Menu Principal", on_click=lambda _: page.go("/user")) 
        ]
    )

    bkAm = Row(
        [
            WindowDragArea(Container(Text(), bgcolor="transparent", padding=10), expand=True),
            IconButton(icons.HOME_ROUNDED, icon_color="black", tooltip="Menu Principal", on_click=lambda _: page.go("/admin")) 
        ]
    )


    """ Variables """

    temp = ""
    usAc = ["" for x in range(7)]
    info = ["" for x in range(7)]
    usBq = []
    cont = band = canti = 0
    indi = False


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

            if temp != usAc[1]: cont = 1
            
            ps.focus()
            ps.value = ""
            ps.error_text = f"Contraseña incorrecta\nTiene {3-cont} intentos"

            if cont == 3:

                page.dialog = intentosAgot
                intentosAgot.open = True
                page.update()

                sleep(3)
                page.window_close()

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


    """ P2 = Pagina de Usuario """


    class Retiro(UserControl):
        
        def __init__(self, mn: float, us: list, cl: AlertDialog, op: str):
            self.mn = mn
            self.us = us
            self.cl = cl
            self.op = op
            super().__init__()
        
        def __call__(self, e):
            
            self.cl.open = False
            page.update()

            sleep(1)

            match self.op:

                case "S":

                    self.mn += 0.35
            
                    if float(self.us[6]) >= self.mn:

                        recargo(self.mn, self.us)
                        saldoCJR(self.mn, "-")

                        comprobanteRet = comprob(self.us, self.mn).RETI()

                        page.dialog = comprobanteRet
                        comprobanteRet.open = True
                        page.update()
                    
                    else:

                        page.dialog = saldoIN
                        saldoIN.open = True
                        page.update()
                
                case "N":
                    
                    if float(self.us[6]) >= self.mn:

                        recargo(self.mn, self.us)
                        saldoCJR(self.mn, "-")

                        page.dialog = retiDN
                        retiDN.open = True
                        page.update()
                    
                    else:

                        page.dialog = saldoIN
                        saldoIN.open = True
                        page.update()

    
    class Abastecer(UserControl):
        
        def __init__(self, mn: float, us: list, cl: AlertDialog):
            self.mn = mn
            self.us = us
            self.cl = cl
            super().__init__()
        
        def __call__(self, e):
            
            self.cl.open = False
            page.update()

            sleep(1)


            saldoCJR(self.mn, "+")

            comprobanteAbs = comprob(self.us, self.mn).ABS()

            page.dialog = comprobanteAbs
            comprobanteAbs.open = True
            page.update()
    

    menCons = ventana.Consulta()

    menRt10 = ventana(siRet10, noRet10, bCn10).Retiro()
    menRt20 = ventana(siRet20, noRet20, bCn20).Retiro()
    menRt30 = ventana(siRet30, noRet30, bCn30).Retiro()
    menRt40 = ventana(siRet40, noRet40, bCn40).Retiro()
    menRt50 = ventana(siRet50, noRet50, bCn50).Retiro()
    menRtO = ventana(siRetO, noRetO, bCnO).Retiro()

    menAbs = ventana(siAbs, None, bCnAbs).Abastecer()
    

    def CJRConsulta(e):

        nonlocal usAc

        if float(usAc[6]) >= 0.35:

            recargo(0.35, usAc)
            usAc = actual(usAc[1])

            comprobanteCon = comprob(usAc, "").CONS()

            menCons.open = False
            page.update()

            sleep(0.5)

            page.dialog = comprobanteCon
            comprobanteCon.open = True
            page.update()
        
        else:
            menCons.open = False
            page.update()

            sleep(0.5)

            page.dialog = saldoIN
            saldoIN.open = True
            page.update()


    def validRet(e):

        if (tfRetO.value.isnumeric() and int(tfRetO.value) >= 10 and (int(tfRetO.value) % 10 == 0) and int(tfRetO.value) <= 500) == False:

            tfRetO.focus()
            tfRetO.error_text = "Monto Inválido"
            tfRetO.value = ""

        else:
            
            tfRetO.border_color = "green"

            siRetO.on_click = Retiro(float(tfRetO.value), usAc, menRtO, "S")
            noRetO.on_click = Retiro(float(tfRetO.value), usAc, menRtO, "N")

            page.dialog = menRtO
            menRtO.open = True
            page.update()
        
        page.update()

        sleep(2)

        tfRetO.border_color = "transparent"
        tfRetO.error_text = tfRetO.value = None
        page.update()


    def validEdt(e):

        nonlocal usAc

        if (tfPIN.value.isnumeric() and len(tfPIN.value) == 4) == False:

            tfPIN.focus()
            tfPIN.error_text = "PIN Inválido"
            tfPIN.value = ""

        else:

            menEdt = Regresiva(5).vent()

            page.dialog = menEdt
            menEdt.open = True
            page.update()

            sleep(5)

            # page.controls.remove(menEdt)
            page.dialog = None
            page.update()

            edicion(tfPIN.value, usAc[1], 4)

            # menEdt.open = False
            # page.update()
            
            page.go("/login")
        

        page.update()

        sleep(2)

        tfPIN.error_text = tfPIN.value = None
        tfPIN.border_color = "transparent"
        page.update()

    
    def validReg(e):

        nonlocal usAc, canti, indi, info

        canti = 0
        indi = False

        info = ["" for x in range(7)]

        if (tfced.value.isnumeric() and len(tfced.value) == 10):
            
            with open("usuarios.txt", "r+") as f:

                for linea in f.readlines():
                    cedulas = linea.strip().split(" ")
                    
                    if tfced.value in cedulas:

                        indi = True

                        tfced.value = ""
                        tfced.focus()
                        tfced.error_text = "Cédula Ya Rgistrada"
                    
            if indi == False: canti += 1
        
        else:
            tfced.value = ""
            tfced.focus()
            tfced.error_text = "Cédula Inválida"
        
        if (tfnom.value.isalpha()) == False:

            tfnom.value = ""
            tfnom.error_text = "Nombre Inválido"

        else:
            tfnom.value = "".join(tfnom.value.split())
            canti += 1

        if (tfape.value.isalpha()) == False:

            tfape.value = ""
            tfape.error_text = "Apellido Inválido"
        
        else:
            tfape.value = "".join(tfape.value.split())
            canti += 1

        if (tfpsg.value.isnumeric() and len(tfpsg.value) == 4) == False:

            tfpsg.value = ""
            tfpsg.error_text = "PIN Inválido"

        else: canti += 1

        if tfP.value == None:
            tfP.error_text = "Escoja un Opcion"
        
        else: canti += 1

        # canti += 1

        if canti == 5:

            info[0] = generarCTA()
            info[1] = tfced.value
            info[2] = tfnom.value
            info[3] = tfape.value
            info[4] = tfpsg.value
            
            if tfP.value == "Usuario": info[5] = "U"
            else: info[5] = "A"

            info[6] = "10.0"

            cadeInf = " ".join(map(str, info))

            with open("usuarios.txt", "a+") as f:
                f.write(cadeInf + "\n")

            venComp = nuevaCta(info).ventana()
            
            page.dialog = venComp
            venComp.open = True
            page.update()

            sleep(2)

            tfced.value = tfnom.value = tfape.value = tfpsg.value = tfP.value = ""
            page.update()

        page.update()
        
        sleep(2)
        tfced.error_text = tfnom.error_text = tfape.error_text = tfpsg.error_text = tfP.error_text = None
        tfced.border_color = tfnom.border_color = tfape.border_color = tfpsg.border_color = tfP.border_color = "transparent"

        page.update()
    
    
    def validCed(e):
        
        try:

            suma = 0
            for i in range(len(tfced.value) - 1):
                    
                x = int(tfced.value[i])

                if (i % 2 == 0):
                    x = x * 2
                    
                    if x > 9: x = x -9

                suma += x

            ulti = int(tfced.value[9])

            if suma % 10 != 0:
                result = (10 - (suma % 10))

                if ulti == result:
                    tfced.border_color = "green"
                    tfced.helper_text = "Cedula Ecuatorina"
                        
                else:
                    tfced.border_color = "orange"
                    tfced.helper_text = "Cedula No Ecuatorina"
                
            else:
                tfced.border_color = "green"
                tfced.helper_text = "Cedula Ecuatorina"
            
        except IndexError:
            tfced.error_text = "Cédula Inválida"
            
        
        page.update()

        sleep(2)

        tfced.border_color = tfced.helper_text = tfced.error_text = None
        tfced.border_color = "transparent"
        page.update()

    
    def validAbs(e):

        if (tfAbs.value.isnumeric() and int(tfAbs.value) >= 1000 and (int(tfAbs.value) % 1000 == 0) and int(tfAbs.value) <= 10000) == False:

            tfAbs.focus()
            tfAbs.error_text = "Monto Inválido"
            tfAbs.value = ""

        else:
            
            tfAbs.border_color = "green"

            siAbs.on_click = Abastecer(float(tfAbs.value), usAc, menAbs)

            page.dialog = menAbs
            menAbs.open = True
            page.update()
        
        page.update()

        sleep(2)

        tfAbs.border_color = "transparent"
        tfAbs.error_text = tfAbs.value = None
        page.update()


    def CJRTabla(e):
        
        nonlocal indi, usBq

        indi = False
        usBq = []

        Tabla.rows.clear()

        with open("usuarios.txt", "r+") as f:

            for linea in f.readlines():
                usBq = linea.strip().split(" ")

                if usBq[5] == "U": permisoUs = "Usuario"
                if usBq[5] == "A": permisoUs = "Administrador"

                if tfBq.value in usBq:

                    indi = True

                    Tabla.rows.append(
                        DataRow(
                            cells=[
                                DataCell(Text(f"{usBq[0]}")),
                                DataCell(Text(f"{usBq[1]}")),
                                DataCell(Text(f"{usBq[2]}"), on_tap=lambda e: page.go("/edtNom")),
                                DataCell(Text(f"{usBq[3]}"), on_tap=lambda e: page.go("/edtApe")),
                                DataCell(Text(f"{usBq[4]}"), on_tap=lambda e: page.go("/edtPIN")),
                                DataCell(Text(f"{permisoUs}")),
                                DataCell(Text(f"$ {usBq[6]}"))
                            ]
                        )
                    )

                    break
        
        if indi == False: 
            tfBq.error_text = "Cédula No Registrada"
            tfBq.focus()

        page.update()

        sleep(2)
        tfBq.value = tfBq.error_text = None
        
        page.update()
    

    def CJRTablaElm(e):
        
        nonlocal indi, usBq

        indi = False
        usBq = []

        TablaElm.rows.clear()

        with open("usuarios.txt", "r+") as f:

            for linea in f.readlines():
                usBq = linea.strip().split(" ")

                if usBq[5] == "U": permisoUs = "Usuario"
                if usBq[5] == "A": permisoUs = "Administrador"

                if tfBq.value in usBq:

                    indi = True

                    TablaElm.rows.append(
                        DataRow(
                            cells=[
                                DataCell(Text(f"{usBq[0]}")),
                                DataCell(Text(f"{usBq[1]}")),
                                DataCell(Text(f"{usBq[2]}")),
                                DataCell(Text(f"{usBq[3]}")),
                                DataCell(Text(f"{usBq[4]}")),
                                DataCell(Text(f"{permisoUs}", col=colors.RED)),
                                DataCell(Text(f"$ {usBq[6]}"))
                            ]
                        )
                    )

                    break
        
        if indi == False: 
            
            tfBq.error_text = "Cédula No Registrada"
            tfBq.focus()
        
        else: 
            
            bEli.autofocus = True
            bEli.visible = True

        page.update()

        sleep(2)
        tfBq.error_text = None
        
        page.update()


    def validENom(e):

        nonlocal usBq

        if tfEdtNom.value.isalpha() == False:
            
            tfEdtNom.error_text = "Nombre Inválido"
            tfEdtNom.focus()

        else:
            edicion(tfEdtNom.value, usBq[1], 2)
            
            tfEdtNom.border_color = "green"
            tfEdtNom.helper_style = TextStyle(weight="bold", size=16, color="black")
            tfEdtNom.helper_text = f"Edicion Exitosa ! Regresando {Countdown(3)}"
            
            page.update()

            sleep(3)

            page.go("/admin")

        page.update()

        sleep(2)
        tfEdtNom.border_color = "transparent"
        tfEdtNom.error_text = tfEdtNom.helper_text = tfEdtNom.value = None

        page.update()


    def validEApe(e):

        nonlocal usBq

        if tfEdtApe.value.isalpha() == False:
            
            tfEdtApe.error_text = "Apellido Inválido"
            tfEdtApe.focus()

        else:
            edicion(tfEdtApe.value, usBq[1], 3)
            
            tfEdtApe.border_color = "green"
            tfEdtApe.helper_style = TextStyle(weight="bold", size=16, color="black")
            tfEdtApe.helper_text = f"Edicion Exitosa ! Regresando {Countdown(3)}"
            
            page.update()

            sleep(3)

            page.go("/admin")

        page.update()

        sleep(2)
        tfEdtApe.border_color = "transparent"
        tfEdtApe.error_text = tfEdtApe.helper_text = tfEdtApe.value = None

        page.update()


    def validEPIN(e):

        nonlocal usBq

        if (tfEdtPIN.value.isnumeric() and len(tfEdtPIN.value) == 4) == False:
            
            tfEdtPIN.error_text = "PIN Inválido"
            tfEdtPIN.focus()

        else:
            edicion(tfEdtPIN.value, usBq[1], 4)
            
            tfEdtPIN.border_color = "green"
            tfEdtPIN.helper_style = TextStyle(weight="bold", size=16, color="black")
            tfEdtPIN.helper_text = f"Edicion Exitosa ! Regresando {Countdown(3)}"
            
            page.update()

            sleep(3)

            page.go("/admin")

        page.update()

        sleep(2)
        tfEdtPIN.border_color = "transparent"
        tfEdtPIN.error_text = tfEdtPIN.helper_text = tfEdtPIN.value = None

        page.update()

    
    def eliminarUS(e):
        
        nonlocal usBq

        eliminacion(usBq[1])
            
        tfBq.helper_style = TextStyle(weight="bold", size=14)
        tfBq.helper_text = "Usuario Eliminado Exitosamente .."
        tfBq.border_color = "green"

        page.update()

        sleep(2)

        tfBq.border_color = "transaparent"
        tfBq.helper_text = tfBq.value = None
        bEli.visible = False
        page.update()

        page.go("/admin")
        


    """ Escoger Perfiles (P1, P2, P3) """

    def perfiles(route):

        nonlocal usAc, band, cont

        """"""
        # Consulta
        bCon.on_click = openDG(menCons)
        siCon.on_click = CJRConsulta
        noCon.on_click = closeDG(menCons)

        # Retiro
        Reti10.on_click = openDG(menRt10)
        siRet10.on_click = Retiro(10, usAc, menRt10, "S")
        noRet10.on_click = Retiro(10, usAc, menRt10, "N")
        bCn10.on_click = closeDG(menRt10)

        Reti20.on_click = openDG(menRt20)
        siRet20.on_click = Retiro(20, usAc, menRt20, "S")
        noRet20.on_click = Retiro(20, usAc, menRt20, "N")
        bCn20.on_click = closeDG(menRt20)

        Reti30.on_click = openDG(menRt30)
        siRet30.on_click = Retiro(30, usAc, menRt30, "S")
        noRet30.on_click = Retiro(30, usAc, menRt30, "N")
        bCn30.on_click = closeDG(menRt30)

        Reti40.on_click = openDG(menRt40)
        siRet40.on_click = Retiro(40, usAc, menRt40, "S")
        noRet40.on_click = Retiro(40, usAc, menRt40, "N")
        bCn40.on_click = closeDG(menRt40)

        Reti50.on_click = openDG(menRt50)
        siRet50.on_click = Retiro(50, usAc, menRt50, "S")
        noRet50.on_click = Retiro(50, usAc, menRt50, "N")
        bCn50.on_click = closeDG(menRt50)

        bReti.on_click = validRet
        bCnO.on_click = closeDG(menRtO)

        # Editar
        bEdi.on_click = validEdt

        # Registrar
        bRegi.on_click = validReg
        bVali.on_click = validCed

        # Abastecer
        bAbi.on_click = validAbs
        bCnAbs.on_click = closeDG(menAbs)

        # Editar
        bBusqi.on_click = CJRTabla
        # tfBq.on_change = CJRTabla

        # Eliminar
        bEli.on_click = eliminarUS

        # Visualizar


        """"""

        def accionBAct(_):
            Tabla.rows.clear()
            page.go("/editarUS")
        
        def accionBElm(_):
            TablaElm.rows.clear()
            page.go("/eliminar")

        def accionBVis(_):
            TablaCmp.rows.clear()

            nonlocal indi, usBq

            indi = False
            usBq = []

            TablaCmp.rows.clear()

            with open("usuarios.txt", "r+") as f:

                for linea in f.readlines():
                    usBq = linea.strip().split(" ")

                    if usBq[5] == "U": permisoUs = "Usuario"
                    if usBq[5] == "A": permisoUs = "Administrador"

                    TablaCmp.rows.append(
                        DataRow(
                            cells=[
                                DataCell(Text(f"{usBq[0]}")),
                                DataCell(Text(f"{usBq[1]}")),
                                DataCell(Text(f"{usBq[2]}")),
                                DataCell(Text(f"{usBq[3]}")),
                                DataCell(Text(f"{usBq[4]}")),
                                DataCell(Text(f"{permisoUs}")),
                                DataCell(Text(f"$ {usBq[6]}"))
                            ]
                        )
                    )

            page.go("/ver")


        bRet.on_click = lambda _: page.go("/retiro")
        OtroMon.on_click = lambda _: page.go("/RetO")
        bEdt.on_click = lambda _: page.go("/editarPIN")
        bReg.on_click = lambda _: page.go("/registro") 
        bAbs.on_click = lambda _: page.go("/abastecer")
        bAdm.on_click = lambda _: page.go("/manteni")
        # bAct.on_click = lambda _: page.go("/editarUS")
        bAct.on_click = accionBAct
        bElm.on_click = accionBElm
        bVis.on_click = accionBVis

        """"""

        P1 = View(
            route="/ingreso", bgcolor="#f1ece2",
            controls=[
                close,
                Container(
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
            ]
        )

        page.views.clear()
        page.views.append(P1)

        if page.route == "/user":
            
            cont = 0

            P2 = View(
                route="/user", bgcolor="#f1ece2",
                controls=[
                    close,
                    Container(
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
                                                width=130,
                                            ),

                                            cUsu,

                                            VerticalDivider(),

                                            Text(
                                                f"Hey! {usAc[2]} {usAc[3][0]}.\nCta. XXX{usAc[0][3:]}",
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
                                                        FloatingActionButton(
                                                            width=130, height=130, bgcolor="#2d728f", content=bCon
                                                        ),

                                                        Text(
                                                            "Consultar", text_align="center"
                                                        )
                                                    ],

                                                    alignment=MainAxisAlignment.CENTER,
                                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                                ),

                                                Column(
                                                    [
                                                        FloatingActionButton(
                                                            width=130, height=130, bgcolor="#2d728f", content=bRet
                                                        ),

                                                        Text(
                                                            "Retirar", text_align="center"
                                                        )
                                                    ],

                                                    alignment=MainAxisAlignment.CENTER,
                                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                                ),

                                                Column(
                                                    [
                                                        FloatingActionButton(
                                                            width=130, height=130, bgcolor="#2d728f", content=bEdt
                                                        ),

                                                        Text(
                                                            "Editar PIN", text_align="center"
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
                    ),

                    back,
                ],

                horizontal_alignment=CrossAxisAlignment.CENTER,
                vertical_alignment=MainAxisAlignment.CENTER
            )
            
            page.views.clear()
            page.views.append(P2)

        if page.route == "/admin":
            
            cont = 0

            P3 = View(
                route="/admin", bgcolor="#f1ece2",
                controls=[
                    close,
                    Container(
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
                                                width=130,
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
                                                        f"Hey! {usAc[2]} {usAc[3][0]}.\nCta. XXX{usAc[0][3:]}",
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
                                                        FloatingActionButton(
                                                            width=130, height=130, bgcolor="#2d728f", content=bAbs
                                                        ),

                                                        Text(
                                                            "Abastecer", text_align="center"
                                                        )
                                                    ],

                                                    alignment=MainAxisAlignment.CENTER,
                                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                                ),

                                                Column(
                                                    [
                                                        FloatingActionButton(
                                                            width=130, height=130, bgcolor="#2d728f", content=bReg
                                                        ),

                                                        Text(
                                                            "Registrar", text_align="center"
                                                        )
                                                    ],

                                                    alignment=MainAxisAlignment.CENTER,
                                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                                ),

                                                Column(
                                                    [
                                                        FloatingActionButton(
                                                            width=130, height=130, bgcolor="#2d728f", content=bAdm
                                                        ),

                                                        Text(
                                                            "Mantenimiento", text_align="center"
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
                    ),

                    back,
                ],

                horizontal_alignment=CrossAxisAlignment.CENTER,
                vertical_alignment=MainAxisAlignment.CENTER
            )

            page.views.clear()
            page.views.append(P3)

        
        """ Retiro y Edicion = P2 """

        if page.route == "/retiro":

            P2Ret = View(
                route="/retiro", bgcolor="#f1ece2",
                controls=[
                    close,
                    
                    Container(
                        expand=True, 
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

                    bkUs
                ]
            )

            page.views.clear()
            page.views.append(P2Ret)
        
        if page.route == "/RetO":

            P2RetO = View(
                route="/RetO", bgcolor="#f1ece2",
                controls=[
                    close,
                    Container(
                        padding=17, expand=True,
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
                                    "Valores multiplos de 10\nMonto menor a $ 500", 
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

                    bkUs,
                ]
            )

            page.views.clear()
            page.views.append(P2RetO)
    
        if page.route == "/editarPIN":
            
            P2Edt = View(
                route="/editarPIN", bgcolor="#f1ece2",
                controls=[
                    close,

                    Container(
                        padding=17, expand=True,
                        # border_radius=8,
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

                    bkUs
                ]
            )

            page.views.clear()
            page.views.append(P2Edt)



        """ Abastecer, Registro y Administrar = P3 """

        if page.route == "/registro":
            
            P3Reg = View(
                route="/registro", bgcolor="#f1ece2",
                controls=[
                    close,

                    Container(
                        padding=17, expand=True,
                        alignment=alignment.center,
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

                                Row(
                                    [
                                        tfced,
                                        bVali,
                                    ],

                                    alignment=MainAxisAlignment.CENTER,
                                    vertical_alignment=CrossAxisAlignment.CENTER
                                ),

                                Row(
                                    [
                                        tfnom,
                                        tfape,
                                    ],

                                    alignment=MainAxisAlignment.CENTER,
                                    vertical_alignment=CrossAxisAlignment.CENTER
                                ),

                                tfpsg,

                                tfP,

                                bRegi,
                            ],
                            
                            scroll=ScrollMode.AUTO,
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        ),
                    ),

                    bkAm,
                ]
            )

            page.views.clear()
            page.views.append(P3Reg)

        if page.route == "/abastecer":

            P3Abs = View(
                route="/abastecer", bgcolor="#f1ece2",
                controls=[
                    close,

                    Container(
                        padding=17, expand=True,
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
                                        content=Column(
                                            [
                                                Row(
                                                    [
                                                        Icon(
                                                            icons.ATM_ROUNDED, size=30
                                                        ),

                                                        Text(
                                                            "Abastecer", size=20
                                                        ),
                                                    ],

                                                    alignment=MainAxisAlignment.CENTER
                                                ),

                                                Text(
                                                    "Ingrese un monto"
                                                ),

                                                Text(
                                                    "Valores multiplos de 1000\nMonto menor a $ 10000", 
                                                    color="green", text_align="center"
                                                ),
                                            ],

                                            alignment=MainAxisAlignment.CENTER,
                                            horizontal_alignment=CrossAxisAlignment.CENTER
                                        )
                                    ),
                                ),

                                Divider(),

                                tfAbs,

                                bAbi,
                            ],

                            spacing=30,
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        ),
                    ),

                    bkAm,
                ]
            )

            page.views.clear()
            page.views.append(P3Abs)

        if page.route == "/manteni":
            
            P3Mnt = View(
                route="/manteni", bgcolor="#f1ece2",
                controls=[
                    close,

                    Container(
                        padding=17, expand=True,
                        border_radius=8,
                        alignment=alignment.center,
                        content=Column(
                            [
                                Container(
                                    content=Row(
                                        [
                                            Image(
                                                src="./Prueba APP 1/cover1.png",
                                                width=130,
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
                                                        f"Hey! {usAc[2]} {usAc[3][0]}.\nCta. XXX{usAc[0][3:]}",
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

                                Card(
                                    elevation=20,
                                    content=Container(
                                        width=580,
                                        padding=20,
                                        border_radius=8, 
                                        bgcolor="#faf4ea",
                                        content=Row(
                                            [
                                                bAct, bElm, bVis
                                            ],

                                            spacing=40,
                                            alignment=MainAxisAlignment.CENTER,
                                            vertical_alignment=CrossAxisAlignment.CENTER
                                        ),
                                    )
                                ),
                            ],

                            spacing=25,
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER
                        )
                    ),

                    bkAm,
                ]
            )

            page.views.clear()
            page.views.append(P3Mnt)

        if page.route == "/editarUS":

            P3Act = View(
                route="/editarUS", bgcolor="#f1ece2",
                controls=[
                    close,
                    
                    Container(
                        expand=True, alignment=alignment.center,
                        content=Column(
                            [   
                                Card(
                                    elevation=20,
                                    content=Container(
                                        width=680,
                                        padding=20,
                                        bgcolor="#faf4ea",
                                        border_radius=8, 
                                        alignment=alignment.center,
                                        content=Column(
                                            [
                                                Text(
                                                    "Administración | Editar", size=16, weight="bold"
                                                ),

                                                Divider(),

                                                Row(
                                                    [
                                                        tfBq, bBusqi
                                                    ],

                                                    alignment=MainAxisAlignment.CENTER,
                                                    vertical_alignment=CrossAxisAlignment.CENTER
                                                ),

                                                # Tabla,
                                                
                                            ],

                                            alignment=MainAxisAlignment.CENTER,
                                            horizontal_alignment=CrossAxisAlignment.CENTER
                                        )
                                    )
                                ),
                                
                                Tabla,
                            ],

                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER
                        )
                    ),

                    bkAm
                ]
            )

            page.views.clear()
            page.views.append(P3Act)

        if page.route == "/edtNom":

            edtNom = View(
                route="/edtNom", bgcolor="#f1ece2",
                controls=[
                    close,
                    
                    Container(
                        expand=True, alignment=alignment.center,
                        content=Column(
                            [
                                Card(
                                    elevation=20,
                                    content=Container(
                                        width=680,
                                        padding=20,
                                        bgcolor="#faf4ea",
                                        border_radius=8, 
                                        alignment=alignment.center,
                                        content=Column(
                                            [
                                                Text(
                                                    "Administración | Editar", size=16, weight="bold"
                                                ),

                                                Divider(),

                                                Text(
                                                    "Ingrese un Nuevo Nombre", color="green", size=14, weight="bold"
                                                ),

                                                Row(
                                                    [
                                                        tfEdtNom,

                                                        IconButton(
                                                            width=230, height=60,
                                                            content=Text(
                                                                "Editar\nNombre", weight="bold",
                                                                color="black"
                                                            ),

                                                            style=ButtonStyle(
                                                                bgcolor="#bbc191",
                                                                shape=RoundedRectangleBorder(radius=8)
                                                            ),

                                                            on_click=validENom
                                                        )

                                                    ],

                                                    alignment=MainAxisAlignment.CENTER,
                                                    vertical_alignment=CrossAxisAlignment.CENTER
                                                )
                                            ],

                                            spacing=35,
                                            alignment=MainAxisAlignment.CENTER, 
                                            horizontal_alignment=CrossAxisAlignment.CENTER
                                        )
                                    )
                                ),
                                
                            ],

                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER
                        )
                    ),

                    bkAm,
                ]
            ) 

            page.views.clear()
            page.views.append(edtNom)

        if page.route == "/edtApe":

            edtApe = View(
                route="/edtApe", bgcolor="#f1ece2",
                controls=[
                    close,
                    Container(
                        expand=True, alignment=alignment.center,
                        content=Column(
                            [
                                Card(
                                    elevation=20,
                                    content=Container(
                                        width=680,
                                        padding=20,
                                        bgcolor="#faf4ea",
                                        border_radius=8, 
                                        alignment=alignment.center,
                                        content=Column(
                                            [
                                                Text(
                                                    "Administración | Editar", size=16, weight="bold"
                                                ),

                                                Divider(),

                                                Text(
                                                    "Ingrese un Nuevo Apellido", color="green", size=14, weight="bold"
                                                ),

                                                Row(
                                                    [
                                                        tfEdtApe,

                                                        IconButton(
                                                            width=230, height=60,
                                                            content=Text(
                                                                "Editar\nApellido", weight="bold",
                                                                color="black"
                                                            ),

                                                            style=ButtonStyle(
                                                                bgcolor="#bbc191",
                                                                shape=RoundedRectangleBorder(radius=8)
                                                            ),

                                                            on_click=validEApe
                                                        )

                                                    ],

                                                    alignment=MainAxisAlignment.CENTER,
                                                    vertical_alignment=CrossAxisAlignment.CENTER
                                                )
                                            ],

                                            spacing=35,
                                            alignment=MainAxisAlignment.CENTER, 
                                            horizontal_alignment=CrossAxisAlignment.CENTER
                                        )
                                    )
                                ),
                                
                            ],

                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER
                        )
                    ),

                    bkAm,
                ]
            ) 

            page.views.clear()
            page.views.append(edtApe)
        
        if page.route == "/edtPIN":

            edtPIN = View(
                route="/edtPIN", bgcolor="#f1ece2",
                controls=[
                    close,
                    Container(
                        expand=True, alignment=alignment.center,
                        content=Column(
                            [
                                Card(
                                    elevation=20,
                                    content=Container(
                                        width=680,
                                        padding=20,
                                        bgcolor="#faf4ea",
                                        border_radius=8, 
                                        alignment=alignment.center,
                                        content=Column(
                                            [
                                                Text(
                                                    "Administración | Editar", size=16, weight="bold"
                                                ),

                                                Divider(),

                                                Text(
                                                    "Ingrese un Nuevo PIN", color="green", size=14, weight="bold"
                                                ),

                                                Row(
                                                    [
                                                        tfEdtPIN,

                                                        IconButton(
                                                            width=230, height=60,
                                                            content=Text(
                                                                "Editar\nPIN", weight="bold",
                                                                color="black"
                                                            ),

                                                            style=ButtonStyle(
                                                                bgcolor="#bbc191",
                                                                shape=RoundedRectangleBorder(radius=8)
                                                            ),

                                                            on_click=validEPIN
                                                        )

                                                    ],

                                                    alignment=MainAxisAlignment.CENTER,
                                                    vertical_alignment=CrossAxisAlignment.CENTER
                                                )
                                            ],

                                            spacing=35,
                                            alignment=MainAxisAlignment.CENTER, 
                                            horizontal_alignment=CrossAxisAlignment.CENTER
                                        )
                                    )
                                ),
                                
                            ],

                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER
                        )
                    ),

                    bkAm,
                ]
            ) 

            page.views.clear()
            page.views.append(edtPIN)
        
        if page.route == "/eliminar":

            P3Elm = View(
                route="/eliminar", bgcolor="#f1ece2",
                controls=[
                    close,
                    Container(
                        expand=True, alignment=alignment.center,
                        content=Column(
                            [   
                                Card(
                                    elevation=20,
                                    content=Container(
                                        width=680,
                                        padding=20,
                                        bgcolor="#faf4ea",
                                        border_radius=8, 
                                        alignment=alignment.center,
                                        content=Column(
                                            [
                                                Text(
                                                    "Administración | Eliminar", size=16, weight="bold"
                                                ),

                                                Divider(),

                                                Row(
                                                    [
                                                        tfBq, 

                                                        IconButton(
                                                            width=230, height=60,
                                                            
                                                            content=Text(
                                                                "Buscar", weight="bold",
                                                                color="black"
                                                            ),

                                                            style=ButtonStyle(
                                                                bgcolor="#bbc191",
                                                                shape=RoundedRectangleBorder(radius=8)
                                                            ),

                                                            on_click=CJRTablaElm
                                                        ),

                                                        bEli,
                                                    ],

                                                    alignment=MainAxisAlignment.CENTER,
                                                    vertical_alignment=CrossAxisAlignment.CENTER
                                                ),

                                            ],

                                            alignment=MainAxisAlignment.CENTER,
                                            horizontal_alignment=CrossAxisAlignment.CENTER
                                        )
                                    )
                                ),
                                
                                TablaElm,
                            ],

                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER
                        )
                    ),

                    bkAm
                ]
            )

            page.views.clear()
            page.views.append(P3Elm)

        if page.route == "/ver":

            P3Ver = View(
                route="/ver", bgcolor="#f1ece2",
                controls=[
                    close,
                    Container(
                        expand=True, alignment=alignment.center,
                        content=Card(
                            elevation=20,
                            content=Container(
                                # width=680,
                                padding=20,
                                bgcolor="#faf4ea",
                                border_radius=8, 
                                alignment=alignment.center,
                                content=TablaCmp
                            )
                        )
                    ),

                    bkAm
                ]
            )

            page.views.clear()
            page.views.append(P3Ver)


        page.update()


    def matchPerfiles(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = perfiles
    page.on_view_pop = matchPerfiles
    page.go(page.route)


if __name__ == "__main__":
    flet.app(target = main, assets_dir = "Prueba APP 1")
