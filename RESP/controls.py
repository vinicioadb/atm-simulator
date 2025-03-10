
import flet
import datetime, locale
from flet import *

from os import remove, rename

locale.setlocale(locale.LC_ALL, "")
fecha_actual = datetime.datetime.now()
form_dia = str(fecha_actual.strftime('%a %#d de %b %Y'))


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


menEdt = AlertDialog(
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
                                icons.NUMBERS, size=30, color="white"
                            ),

                            Text(
                                "Edicion Exitosa !", size=20, color="white"
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


""" P1 """

tW = Text(
    "Bienvenido !",
    font_family="aesthetica",
    size=60,
    weight=FontWeight.BOLD
)

us = TextField(
    label="Cedula", suffix_icon=icons.PERSON,
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

bLogi = IconButton(

    width=230,
    content=Text(
        "Ingresar", weight="bold",
        color="black"
    ),

    style=ButtonStyle(
        bgcolor="#bbc191",
        shape=RoundedRectangleBorder(radius=8)
    ),
)


""" REGISTRO """

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

usA = TextField(
    label="Usuario", suffix_icon=icons.PERSON,
    suffix_style=TextStyle(color="green"),
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
    on_submit=lambda e: psA.focus(), autofocus=True,
)

psA = TextField(
    label="Contraseña", password=True,
    can_reveal_password=True,
    filled=True, border_color="transparent",
)

cReg = AlertDialog(
    actions_padding=0,
    shape=RoundedRectangleBorder(radius=8),
    actions=[
        Container(
            padding=17, bgcolor="#faf4ea", border_radius=8,

            content=Column(
                [
                    Icon(
                        icons.DASHBOARD_CUSTOMIZE, size=55, color="#1c110a"
                    ),

                    Text(
                        "Registrate", size=25, weight="bold"
                    ),

                    Text(
                        "Siga las instrucciones", size=15, weight=FontWeight.W_400
                    ),

                    Divider(),

                    usA, psA,

                    Divider(), 
                    
                    bRegi,
                ],

                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),

            alignment=alignment.center
        ),
    ],

    # on_dismiss=lambda e: cReg.open(e) = False
)


""" Pagina USUARIO = P2 """

cUsu = Container(
    shape=BoxShape.CIRCLE, bgcolor="#bbc191",
    width=110, height=110, 
    alignment=alignment.center, ink=True,
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
        overlay_color="#001219",
    ),
)


# bCon = FloatingActionButton(
#     width=130, height=130, bgcolor="#2d728f",
    
#     content=IconButton(
        
#         width=130, height=130,
#         content=Image(
#             src="./Prueba APP 1/icons/consu1.png", height=80
#         ),

#         style=ButtonStyle(
#             shape=RoundedRectangleBorder(radius=16),
#             overlay_color="#001219",
#         ),
#     )
# )


# bCon = IconButton(

#     width=130, height=130,

#     content=Image(
#         src="./Prueba APP 1/icons/consu1.png", height=80
#     ),

#     style=ButtonStyle(
#         bgcolor="#677423", overlay_color="#002626",
#         # shape=RoundedRectangleBorder(radius=10),
#     ),
# )

# bCon = FloatingActionButton(

#     content=Image(
#         src="./Prueba APP 1/icons/consu1.png", height=80
#     ),

#     width=130, height=130, bgcolor="#677423",
#     # sty
#     # bgcolor="#002626",
#     # on_click=opciones
# )

bRet = FloatingActionButton(

    content=Image(
        src="./Prueba APP 1/icons/reti1.png", height=80
    ),

    width=130, height=130, bgcolor="#2d728f"
)

bEdt = FloatingActionButton(

    content=Image(
        src="./Prueba APP 1/icons/edit1.png", height=80
    ),

    width=130, height=130, bgcolor="#0e4749"
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

menCon = BottomSheet(
    # open=True,
    content=Container(
        bgcolor="#faf4ea", 
        content=Column(
            height=250,
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

menRet10 = BottomSheet(
    content=Container(
        bgcolor="#faf4ea", 
        content=Column(
            height=250,
            controls=[
                Text(
                    "Desea imprimir su comprobante por $ 0.35\n¿Deseas continuar?",
                    text_align=TextAlign.CENTER, size=20
                ),

                Row(
                    [
                        siRet10,
                        noRet10,
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

menRet20 = BottomSheet(
    content=Container(
        bgcolor="#faf4ea", 
        content=Column(
            height=250,
            controls=[
                Text(
                    "Dese imprimir su comprobante por $ 0.35\n¿Deseas continuar?",
                    text_align=TextAlign.CENTER, size=20
                ),

                Row(
                    [
                        siRet20,
                        noRet20,
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

menRet30 = BottomSheet(
    content=Container(
        bgcolor="#faf4ea", 
        content=Column(
            height=250,
            controls=[
                Text(
                    "Dese imprimir su comprobante por $ 0.35\n¿Deseas continuar?",
                    text_align=TextAlign.CENTER, size=20
                ),

                Row(
                    [
                        siRet30,
                        noRet30,
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

menRet40 = BottomSheet(
    content=Container(
        bgcolor="#faf4ea", 
        content=Column(
            height=250,
            controls=[
                Text(
                    "Dese imprimir su comprobante por $ 0.35\n¿Deseas continuar?",
                    text_align=TextAlign.CENTER, size=20
                ),

                Row(
                    [
                        siRet40,
                        noRet40,
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

menRet50 = BottomSheet(
    content=Container(
        bgcolor="#faf4ea", 
        content=Column(
            height=250,
            controls=[
                Text(
                    "Dese imprimir su comprobante por $ 0.35\n¿Deseas continuar?",
                    text_align=TextAlign.CENTER, size=20
                ),

                Row(
                    [
                        siRet50,
                        noRet50,
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

menRetO = BottomSheet(
    content=Container(
        bgcolor="#faf4ea", 
        content=Column(
            height=250,
            controls=[
                Text(
                    "Dese imprimir su comprobante por $ 0.35\n¿Deseas continuar?",
                    text_align=TextAlign.CENTER, size=20
                ),

                Row(
                    [
                        siRetO,
                        noRetO,
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

cCon = AlertDialog(
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
                                    "Mi Balance Actual", size=20, weight="bold"
                                ),

                                Text(
                                    "mie, 25 enero 2023", size=17, weight=FontWeight.W_400
                                ),
                            ],
                        ),

                        border_radius=8, border=border.all(0.5, "black"), padding=17, 
                    ),

                    IconButton(

                        height=95,
                        content=Text(
                            "$ 290.98", weight=FontWeight.W_300, 
                            color="white", size=20
                        ),

                        style=ButtonStyle(
                            shape=RoundedRectangleBorder(radius=8), bgcolor="#1c110a"
                        ),
                    ),

                ],

                alignment=MainAxisAlignment.CENTER
            ),

            alignment=alignment.center
        ),
    ],
)

cTfr = AlertDialog(
    actions_padding=0,
    shape=RoundedRectangleBorder(radius=8),
    # on_dismiss=retorno,
    actions=[
        Container(
            width=635, height=430,
            padding=17, bgcolor="#faf4ea", border_radius=8,

            content=Row(
                [
                    Card(
                        content=Container(
                            padding=20,
                            border_radius=8, bgcolor="#f1ece2",
                            content=Column(
                                [
                                    Text(
                                        "Ingrese el monto\na transferir", size=17,
                                        weight="w400", text_align="center"
                                    ),

                                    TextField(
                                        hint_text="0.0", filled=True, prefix_text="$",
                                        border_color="transparent", text_align="center",
                                    ),

                                    Container(
                                        width=300,
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

                                        border_radius=8, border=border.all(0.5, "black"), padding=17,
                                    ),
                                ],
                                
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER
                            ),
                            
                            # alignment=alignment.center

                            # alignment=alignment.
                        ),

                        height=300
                    ),

                    # Column(
                    #     [
                    #         Text(
                    #             "Ingrese el monto\na transferir", size=17,
                    #             weight="w400", text_align="center"
                    #         ),

                    #         TextField(
                    #             hint_text="0.0", filled=True, prefix_text="$",
                    #             border_color="transparent", text_align="center",
                    #         ),

                    #         Container(
                    #             width=240,
                    #             content=Column(
                    #                 [
                    #                     Text(
                    #                         "Desde Mi Cuenta", size=15, weight="bold"
                    #                     ),

                    #                     Text(
                    #                         "Nr. 20000", size=10, weight=FontWeight.W_400
                    #                     ),
                    #                 ],

                    #                 alignment=MainAxisAlignment.CENTER
                    #             ),

                    #             border_radius=8, border=border.all(0.5, "black"), padding=17,
                    #         ),
                    #     ],
                        
                    #     horizontal_alignment=CrossAxisAlignment.CENTER
                    # ),



                #     Divider(),

                #     Text(
                #         "Numero de cuenta\ndel beneficiario", size=17, 
                #         weight="w400", text_align="center"
                #     ),

                #     TextField(
                #         border_color="transparent", text_align="center",
                #         hint_text="21234", filled=True, prefix_icon=icons.PERSON_ADD,
                #     ),

                #     Divider(),

                #     bTafi,

                ],

                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER
            ),

            alignment=alignment.center
        ),
    ],
)

tUsu = DataTable(
    data_text_style=TextStyle(weight="bold", color="black"),

    columns=[
        DataColumn(Text("Usuario")),
        DataColumn(Text("Contraseña")),
        DataColumn(Text("Nr. Cuenta")),
        
        # DataColumn(Text("Permisos")),
    ],

    # rows=[
    #     DataRow(
    #         cells=[
    #             DataCell(Text(f"{tabla[0]}"), on_tap=lambda e: print("Editar User")),
    #             DataCell(Text(f"{tabla[1]}"), on_tap=lambda e: print("Editar Pasg")),
    #             DataCell(Text(f"{tabla[2]}")),
    #             # DataCell(Text(f"{tabla[3]}"), on_tap=lambda e: print("Editar ")),
    #         ],
    #     ),
    # ],
)

cEdt = AlertDialog(
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

                    tUsu,
                    # tUsu,
                ],

                horizontal_alignment=CrossAxisAlignment.CENTER, 
            ),

            alignment=alignment.center
        ),
    ],
)
 

""" PAGINA ADMINISTRADOR = P3 """

cAdm = Container(
    shape=BoxShape.CIRCLE, bgcolor="white",
    width=100, height=100, alignment=alignment.center, 
    content=Row(
        controls=[
            Icon(
                icons.SYSTEM_SECURITY_UPDATE , color="black", size=55
            ),
        ],

        alignment=MainAxisAlignment.CENTER,
        vertical_alignment=CrossAxisAlignment.CENTER,
    )
)

bAdm = FloatingActionButton(

    content=Image(
        src="./Prueba APP 1/icons/adm.png", height=80
    ),

    width=130, height=130, bgcolor="#023859",
    # on_click=opciones
)

bReg = FloatingActionButton(

    content=Icon(
        icons.PERSON_ADD, size=80, color="#f1ece2"
    ),

    width=130, height=130, bgcolor="#023859",
)

tfced = TextField(
    label="Cedula", width=310,
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
    on_submit=lambda e: tfnom.focus(),
    text_align="center"
)

tfnom = TextField(
    label="Nombre", width=150,
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
    on_submit=lambda e: tfape.focus(),
    text_align="center"
)

tfape = TextField(
    label="Apellido", width=150,
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
    on_submit=lambda e: tfpsg.focus(),
    text_align="center"
)

tfpsg = TextField(
    label="PIN", width=310,
    filled=True, border_color="transparent",
    capitalization=TextCapitalization.CHARACTERS,
    text_align="center"
)

tfA = Checkbox(
    label="Administrador", label_position=LabelPosition.LEFT
)

tfU = Checkbox(
    label="Usuario", label_position=LabelPosition.LEFT
)



cRegA = AlertDialog(
    actions_padding=0,
    shape=RoundedRectangleBorder(radius=8),
    actions=[
        Container(
            padding=17, bgcolor="#faf4ea", border_radius=8,

            content=Column(
                [
                    Icon(
                        icons.DASHBOARD_CUSTOMIZE, size=55, color="#1c110a"
                    ),

                    Text(
                        "Registrate", size=25, weight="bold"
                    ),

                    Text(
                        "Siga las instrucciones", size=15, weight=FontWeight.W_400
                    ),

                    Divider(),

                    usA, psA,

                    Divider(), 
                    
                    bRegi,
                ],

                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),

            alignment=alignment.center
        ),
    ],
)





bAbs = FloatingActionButton(

    content=Image(
        src="./Prueba APP 1/icons/abst.png", height=80
    ),

    width=130, height=130, bgcolor="#e9b44c"
)

bRegA = FloatingActionButton(

    content=Image(
        src="./Prueba APP 1/icons/regis.png", height=80
    ),

    width=130, height=130, bgcolor="#9b2915"
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
