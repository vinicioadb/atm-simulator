
import flet
import datetime, locale
from flet import *
import time, threading

from os import remove, rename

locale.setlocale(locale.LC_ALL, "")
fecha_actual = datetime.datetime.now()
form_dia = str(fecha_actual.strftime('%a %#d de %b %Y'))

class Countdown(UserControl):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.seconds and self.running:
            secs = self.seconds
            self.countdown.value = "{:2d}".format(secs)
            self.update()
            time.sleep(1)
            self.seconds -= 1

    def build(self):
        self.countdown = Text(size=30)
        return self.countdown


"""" MENSAJES CAJERO """

saldoIN = AlertDialog(
    actions_padding=0,
    shape=RoundedRectangleBorder(radius=8),
    actions=[
        Container(
            padding=17, bgcolor="#faf4ea", 
            border_radius=8,
            content=Card(
                elevation=20,
                content=Container(
                    height=100, 
                    padding=20,
                    border_radius=8, 
                    bgcolor="red",
                    content=Row(
                        [
                            Icon(
                                icons.ERROR, size=30, color="white"
                            ),

                            Text(
                                "Saldo Insufuciente", size=20, color="white"
                            )
                        ]
                    )
                ),
            )
        ),
    ],
)


retiDN = AlertDialog(
    actions_padding=0,
    shape=RoundedRectangleBorder(radius=8),
    actions=[
        Container(
            padding=17, bgcolor="#faf4ea", 
            border_radius=8,
            content=Card(
                elevation=20,
                content=Container(
                    height=100, 
                    padding=20,
                    border_radius=8, 
                    bgcolor="green",
                    content=Row(
                        [
                            Icon(
                                icons.WALLET, size=30, color="white"
                            ),

                            Text(
                                "Retire su Dinero", size=20, color="white"
                            )
                        ]
                    )
                ),
            )
        ),
    ],
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


""" Pagina INGRESO = P1 """

tW = Text(
    "Bienvenido !", font_family="aesthetica", size=60, weight="bold"
)

us = TextField(
    label="Cédula", suffix_icon=icons.PERSON,
    suffix_style=TextStyle(color="green"),
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
    on_submit=lambda e: ps.focus(), autofocus=True,
    text_align="center"
)

ps = TextField(
    label="PIN", password=True,
    can_reveal_password=True, 
    filled=True, border_color="transparent",
    text_align="center",
)


""" Pagina USUARIO = P2 """

cUsu = Container(
    shape=BoxShape.CIRCLE, bgcolor="#bbc191",
    width=110, height=110, 
    alignment=alignment.center,
    content=Row(
        controls=[
            Icon(
                icons.PERSON_ROUNDED, color="black", size=60
            ),
        ],

        alignment=MainAxisAlignment.CENTER,
        vertical_alignment=CrossAxisAlignment.CENTER,
    )
)

bCon = IconButton(
    width=130, height=130,
    content=Image(
        src="./Prueba APP 1/icons/consu1.png", height=80
    ),

    style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=16),
        overlay_color="#001219", bgcolor="#2d728f"
    ),
)

bRet = IconButton(
    width=130, height=130,
    content=Image(
        src="./Prueba APP 1/icons/reti1.png", height=80
    ),

    style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=16),
        overlay_color="#001219",
    ),
)

bEdt = IconButton(
    width=130, height=130,
    content=Image(
        src="./Prueba APP 1/icons/edit1.png", height=80
    ),

    style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=16),
        overlay_color="#001219",
    ),
)

#   ________________

#   Botones de Accion

bEdi = IconButton(

    width=230,
    content=Text(
        "Editar", weight="bold",
        color="black"
    ),

    style=ButtonStyle(
        bgcolor="#bbc191",
        shape=RoundedRectangleBorder(radius=8)
    ),
)

bReti = IconButton(

    width=230,
    content=Text(
        "Retirar", weight="bold",
        color="black"
    ),

    style=ButtonStyle(
        bgcolor="#bbc191",
        shape=RoundedRectangleBorder(radius=8)
    ),
)

Reti10 = IconButton(
    
    width=130, height=50,
    content=Text(
        "$ 10", size=20,
        weight="bold",
        color="black"
    ),

    style=ButtonStyle(
        bgcolor="#bbc191",
        shape=RoundedRectangleBorder(radius=8)
    ),
)

Reti20 = IconButton(
    width=130, height=50,
    content=Text(
        "$ 20", size=20,
        weight="bold",
        color="black"
    ),

    style=ButtonStyle(
        bgcolor="#bbc191",
        shape=RoundedRectangleBorder(
            radius=8)
    ),
)

Reti30 =IconButton(
    width=130, height=50,
    content=Text(
        "$ 30", size=20,
        weight="bold",
        color="black"
    ),

    style=ButtonStyle(
        bgcolor="#bbc191",
        shape=RoundedRectangleBorder(
            radius=8)
    ),
)

Reti40 = IconButton(
    width=130, height=50,
    content=Text(
        "$ 40", size=20,
        weight="bold",
        color="black"
    ),

    style=ButtonStyle(
        bgcolor="#bbc191",
        shape=RoundedRectangleBorder(
            radius=8)
    ),
)

Reti50 = IconButton(
    width=130, height=50,
    content=Text(
        "$ 50", size=20,
        weight="bold",
        color="black"
    ),

    style=ButtonStyle(
        bgcolor="#bbc191",
        shape=RoundedRectangleBorder(
            radius=8)
    ),
)

OtroMon = TextButton(
    width=130, height=50,
    content=Text(
        "Otro", size=20, color="black"
    ),
)

#   ________________

siCon = TextButton(
    content=Text(
        "Si", color="black", weight="bold"
    )  
)

noCon = TextButton(
    content=Text(
        "No", color="black", weight="bold"
    )  
)

siRet10 = TextButton(
    content=Text(
        "Si", color="black", weight="bold"
    )  
)

noRet10 = TextButton(
    content=Text(
        "No", color="black", weight="bold"
    )  
)

bCn10 = TextButton(
    content=Text(
        "Cancelar", color="red", weight="bold"
    )
)

siRet20 = TextButton(
    content=Text(
        "Si", color="black", weight="bold"
    )  
)

noRet20 = TextButton(
    content=Text(
        "No", color="black", weight="bold"
    )  
)

bCn20 = TextButton(
    content=Text(
        "Cancelar", color="red", weight="bold"
    )
)

siRet30 = TextButton(
    content=Text(
        "Si", color="black", weight="bold"
    )  
)

noRet30 = TextButton(
    content=Text(
        "No", color="black", weight="bold"
    )  
)

bCn30 = TextButton(
    content=Text(
        "Cancelar", color="red", weight="bold"
    )
)

siRet40 = TextButton(
    content=Text(
        "Si", color="black", weight="bold"
    )  
)

noRet40 = TextButton(
    content=Text(
        "No", color="black", weight="bold"
    )  
)

bCn40 = TextButton(
    content=Text(
        "Cancelar", color="red", weight="bold"
    )
)

siRet50 = TextButton(
    content=Text(
        "Si", color="black", weight="bold"
    )  
)

noRet50 = TextButton(
    content=Text(
        "No", color="black", weight="bold"
    )  
)

bCn50 = TextButton(
    content=Text(
        "Cancelar", color="red", weight="bold"
    )
)

siRetO = TextButton(
    content=Text(
        "Si", color="black", weight="bold"
    )  
)

noRetO = TextButton(
    content=Text(
        "No", color="black", weight="bold"
    )  
)

bCnO = TextButton(
    content=Text(
        "Cancelar", color="red", weight="bold"
    )
)

tfRetO = TextField(
    hint_text="0.0", filled=True, prefix_text="$",
    border_color="transparent", text_align="center",
    width=170
)

tfPIN = TextField(
    border_color="transparent", text_align="center",
    hint_text="1234", filled=True, width=170,
    password=True, can_reveal_password=True,
)


""" Pagina ADMINISTRADOR = P3 """

bVali = IconButton(

    width=150,
    content=Text(
        "Verificar\nCed. Ecuatoriana", weight="bold",
        color="black", text_align="center"
    ),

    style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=8)
    ),
)


bRegi = IconButton(

    width=230,
    content=Text(
        "Registrar", weight="bold",
        color="black"
    ),

    style=ButtonStyle(
        bgcolor="#bbc191",
        shape=RoundedRectangleBorder(radius=8)
    ),
)


cAdm = Container(
    shape=BoxShape.CIRCLE, bgcolor="white",
    width=110, height=110, 
    # alignment=alignment.center, 
    content=Row(
        controls=[
            Icon(
                icons.PERSON ,color="black", size=60
            ),
        ],

        alignment=MainAxisAlignment.CENTER,
        vertical_alignment=CrossAxisAlignment.CENTER,
    )
)

bAdm = IconButton(
    width=130, height=130,
    content=Image(
        src="./Prueba APP 1/icons/adm.png", height=80
    ),

    style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=16),
        overlay_color="#001219", bgcolor="#2d728f"
    ),
)

bReg = IconButton(
    width=130, height=130,
    content=Image(
        src="./Prueba APP 1/icons/regis.png", height=80
    ),

    style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=16),
        overlay_color="#001219", bgcolor="#2d728f"
    ),
)

tfced = TextField(
    label="Cédula", width=350, 
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
    on_submit=lambda e: tfnom.focus(),
    text_align="center"
)

tfnom = TextField(
    label="Nombre", width=250,
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
    on_submit=lambda e: tfape.focus(),
    text_align="center"
)

tfape = TextField(
    label="Apellido", width=250,
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
    on_submit=lambda e: tfpsg.focus(),
    text_align="center"
)

tfpsg = TextField(
    label="PIN", width=510, password=True,
    can_reveal_password=True,
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
    text_align="center", on_submit= lambda e: tfP.focus()
)

tfP = Dropdown(
    width=510, label="Permisos", filled=True,
    border_color=colors.TRANSPARENT,
    options=[
        dropdown.Option("Usuario"),
        dropdown.Option("Administrador")
    ]
)

bAbs = IconButton(
    width=130, height=130,
    content=Image(
        src="./Prueba APP 1/icons/abst.png", height=80
    ),

    style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=16),
        overlay_color="#001219", bgcolor="#2d728f"
    ),
)

tfAbs = TextField(
    hint_text="0.0", filled=True, prefix_text="$",
    border_color="transparent", text_align="center",
    width=170
)

#   ________________

#   Botones de Accion

bAbi = IconButton(

    width=230,
    content=Text(
        "Abastecer", weight="bold",
        color="black"
    ),

    style=ButtonStyle(
        bgcolor="#bbc191",
        shape=RoundedRectangleBorder(radius=8)
    ),
)

siAbs = TextButton(
    content=Text(
        "Si", color="black", weight="bold"
    )  
)

bCnAbs = TextButton(
    content=Text(
        "Cancelar", color="red", weight="bold"
    )
)

bAct = OutlinedButton(
    width=130, height=130,
    content=Text(
        "Editar", weight="bold", size=20, color="black"
    ),

    style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=16),
        overlay_color="#ffecd1",
    ),
)

bElm = OutlinedButton(
    width=130, height=130,
    content=Text(
        "Eliminar", weight="bold", size=20, color="black"
    ),

    style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=16),
        overlay_color="#ffecd1",
    ),
)

bVis = OutlinedButton(
    width=130, height=130,
    content=Text(
        "Visualizar", weight="bold", size=20, color="black"
    ),

    style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=16),
        overlay_color="#ffecd1",
    ),

    tooltip="Ver Usuarios y Administradores"
)

tfBq = TextField(
    label="Cédula", 
    # width=510, 
    suffix_icon=icons.SEARCH,
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
    text_align="center",
)

bBusqi = IconButton(
    width=230, height=60,
    content=Text(
        "Buscar", weight="bold",
        color="black"
    ),

    style=ButtonStyle(
        bgcolor="#bbc191",
        shape=RoundedRectangleBorder(radius=8)
    ),
)

Tabla = DataTable(
    columns=[
        DataColumn(Text("Cuenta", weight="bold")),
        DataColumn(Text("Cedula", weight="bold")),
        DataColumn(Text("Nombre", weight="bold")),
        DataColumn(Text("Apellido", weight="bold")),
        DataColumn(Text("PIN", weight="bold")),
        DataColumn(Text("Permisos", weight="bold")),
        DataColumn(Text("Saldo", weight="bold")),
    ]
)

TablaElm = DataTable(
    columns=[
        DataColumn(Text("Cuenta", weight="bold")),
        DataColumn(Text("Cédula", weight="bold")),
        DataColumn(Text("Nombre", weight="bold")),
        DataColumn(Text("Apellido", weight="bold")),
        DataColumn(Text("PIN", weight="bold")),
        DataColumn(Text("Permisos", weight="bold")),
        DataColumn(Text("Saldo", weight="bold")),
    ]
)

TablaCmp = DataTable(
    columns=[
        DataColumn(Text("Cuenta", weight="bold")),
        DataColumn(Text("Cédula", weight="bold")),
        DataColumn(Text("Nombre", weight="bold")),
        DataColumn(Text("Apellido", weight="bold")),
        DataColumn(Text("PIN", weight="bold")),
        DataColumn(Text("Permisos", weight="bold")),
        DataColumn(Text("Saldo", weight="bold")),
    ]
)

bEli = IconButton(
    icon=icons.REMOVE_CIRCLE_ROUNDED, icon_color="red", 
    icon_size=40, tooltip="Eliminar Usuario", visible=False
)

tfEdtNom = TextField(
    label="Nombre", text_align="center",
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
)

tfEdtApe = TextField(
    label="Apellido", text_align="center",
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
)

tfEdtPIN = TextField(
    label="PIN", text_align="center",
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
)


#   ________________

tAdmU = DataTable(
    data_text_style=TextStyle(weight="bold", color="black"),

    columns=[
        DataColumn(Text("Usuario")),
        DataColumn(Text("Contraseña")),
        DataColumn(Text("Nr. Cuenta")),
        DataColumn(Text("Permisos")),
    ],

    # rows=[
    #     DataRow(
    #         cells=[
    #             DataCell(Text(f"{tabla[0]}"), on_tap=lambda e: print("Editar User")),
    #             DataCell(Text(f"{tabla[1]}"), on_tap=lambda e: print("Editar Pasg")),
    #             DataCell(Text(f"{tabla[2]}")),
    #             DataCell(Text(f"{tabla[3]}"), on_tap=lambda e: print("Editar Perm")),
    #         ],
    #     ),
    # ],
)

cEdA = AlertDialog(
    actions_padding=0,
    shape=RoundedRectangleBorder(radius=8),
    actions=[
        Container(
            width=635, height=430,
            padding=17, bgcolor="#faf4ea", border_radius=8,

            content=Column(
                controls=[

                    Card(
                        content=Container(
                                border_radius=8, padding=17,
                                content=Text(
                                    "Administrar mi Usuario", weight="bold"
                                ),
                        ),
                    ),

                    tAdmU,
                ],

                horizontal_alignment=CrossAxisAlignment.CENTER, 
            ),

            alignment=alignment.center
        ),
    ]
)

cAbs = AlertDialog(
    actions_padding=0,
    shape=RoundedRectangleBorder(radius=8),

    actions=[
        Container(
            width=635, height=430,
            padding=17, bgcolor="#faf4ea", border_radius=8,

            content=Column(
                [

                    Text(
                        "Ingrese el monto\na retirar", size=17,
                        weight="w400", text_align="center"
                    ),

                    TextField(
                        hint_text="0.0", filled=True, prefix_text="$",
                        border_color="transparent", text_align="center",
                    ),

                    Container(
                        width=240,
                        content=Column(
                            [
                                Text(
                                    "Desde Mi Cuenta", size=15, weight="bold"
                                ),

                                Text(
                                    "Nr. 20000", size=10, weight=FontWeight.W_400
                                ),
                            ],

                            alignment=MainAxisAlignment.CENTER
                        ),
                        # expand=True,
                        border_radius=8, border=border.all(0.5, "black"), padding=17,
                    ),

                    Row(
                        [
                            TextButton(
                                "$1000"
                            ),

                            TextButton(
                                "$2000"
                            ),

                            TextButton(
                                "$3000"
                            ),
                        ],

                        alignment=MainAxisAlignment.CENTER
                    ),

                    Divider(),

                    bAbi,

                ],

                horizontal_alignment=CrossAxisAlignment.CENTER, 
            ),

            alignment=alignment.center
        ),
    ],
)

comTafi = AlertDialog(
    actions_padding=0,
    shape=RoundedRectangleBorder(radius=8),

    actions=[
        Container(
            width=635, height=430,
            padding=17, bgcolor="#faf4ea", border_radius=8,

            content=Column(
                [
                    Icon(
                        icons.VERIFIED
                    )
                ]
            )
        )
    ],
)
