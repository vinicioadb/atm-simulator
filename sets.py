
# def validCed(cedula: str):

#     suma = 0

#     for i in range(len(cedula) - 1):
        
#         x = int(cedula[i])

#         if (i % 2 == 0):
#             x = x * 2
        
#             if x > 9: x = x -9

#         suma += x

#     ulti = int(cedula[9])

#     if suma % 10 != 0:
#         result = (10 - (suma % 10))

#         if ulti == result:
#             return 1
#         else:
#             return 0
    
#     else: return 1

# print(validCed("1755084140"))

muestra = "DE LA TORRE"
muestra = "".join(muestra.split())
print(muestra)


""" TABLA """

# import flet
# from flet import *

# def main(page: Page):

#     page.bgcolor = "#faf4ea"
#     page.fonts = {"Consolas": "./Prueba APP 1/fonts/Consola.ttf"}
#     page.theme = Theme(font_family="Consolas")
#     page.window_width = 960
#     page.window_height = 200
#     page.vertical_alignment = MainAxisAlignment.CENTER
#     page.horizontal_alignment = CrossAxisAlignment.CENTER

#     Tabla = DataTable(
#         columns=[
#             DataColumn(Text("Cuenta", weight="bold")),
#             DataColumn(Text("Cedula", weight="bold")),
#             DataColumn(Text("Nombre", weight="bold")),
#             DataColumn(Text("Apellido", weight="bold")),
#             DataColumn(Text("PIN", weight="bold")),
#             DataColumn(Text("Permisos", weight="bold")),
#             DataColumn(Text("Saldo", weight="bold")),
#         ]
#     )

#     with open("usuarios.txt", "r+") as f:

#         for linea in f.readlines():
#             usuarios = linea.strip().split(" ")

#             if usuarios[5] == "U": permisoUs = "Usuario"
#             if usuarios[5] == "A": permisoUs = "Administrador"

#             if "1724727621" in usuarios:

#                 Tabla.rows.append(
#                     DataRow(
#                         cells=[
#                             DataCell(Text(f"{usuarios[0]}"), on_tap=lambda e: print(usuarios[0])),
#                             DataCell(Text(f"{usuarios[1]}"), on_tap=lambda e: print(usuarios[1])),
#                             DataCell(Text(f"{usuarios[2]}"), on_tap=lambda e: print(usuarios[2])),
#                             DataCell(Text(f"{usuarios[3]}"), on_tap=lambda e: print(usuarios[3])),
#                             DataCell(Text(f"{usuarios[4]}"), on_tap=lambda e: print(usuarios[4])),
#                             DataCell(Text(f"{permisoUs}")),
#                             DataCell(Text(f"$ {usuarios[6]}"))
#                         ]
#                     )
#                 )

#                 break

#     page.add(Tabla)
#     page.update()

# flet.app(target=main, assets_dir="./Prueba APP 1")

""" CUENTA REGRESIVA """

# import flet
# from flet import *
# import time, threading


# class Countdown(UserControl):
#     def __init__(self, seconds):
#         super().__init__()
#         self.seconds = seconds

#     def did_mount(self):
#         self.running = True
#         self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
#         self.th.start()

#     def will_unmount(self):
#         self.running = False

#     def update_timer(self):
#         while self.seconds and self.running:
#             secs = self.seconds
#             self.countdown.value = "{:2d}".format(secs)
#             self.update()
#             time.sleep(1)
#             self.seconds -= 1

#     def build(self):
#         self.countdown = Text(size=30)
#         return self.countdown



# def main(page: Page):
    
#     # page.bgcolor = "#faf4ea"
#     page.fonts = {"Consolas": "./Prueba APP 1/fonts/Consola.ttf"}
#     page.theme = Theme(font_family="Consolas")
#     page.window_width = 460
#     page.window_height = 300
#     page.vertical_alignment = MainAxisAlignment.CENTER
#     page.horizontal_alignment = CrossAxisAlignment.CENTER
    
#     dg = AlertDialog(
#         actions_padding=0,
#         shape=RoundedRectangleBorder(radius=8),
#         actions=[
#             Container(
#                 padding=50, bgcolor="#faf4ea", 
#                 border_radius=8,
#                 content=Row(
#                     [   
#                         Column(
#                             [
#                                 Row(
#                                     [
#                                         Image(
#                                             src="./Prueba APP 1/icons/exito.png", height=32
#                                         ),

#                                         Text(   
#                                             "Edicion Exitosa", size=20, color="green", weight="bold"
#                                         ),
#                                     ]
#                                 ),

#                                 Text(
#                                     "Estas a punto de Cerrar Sesión", size=13, weight="bold"
#                                 ),

                                
#                             ],

#                             alignment=MainAxisAlignment.CENTER,
#                             horizontal_alignment=CrossAxisAlignment.CENTER
#                         ),

#                         Countdown(5),
#                     ],

#                     alignment=MainAxisAlignment.CENTER
#                 )
#             )
#         ],
#     )


#     def abrirCR(e):
        
#         page.dialog = dg
#         dg.open = True
#         page.update()

#         sleep(5)

#         page.window_close()


#     page.add(
#         Card(
#             content=IconButton(
#                 width=230,
#                 content=Text(
#                     "Ingresar", weight="bold",
#                     color="black"
#                 ),

#                 style=ButtonStyle(
#                     bgcolor="#bbc191",
#                     shape=RoundedRectangleBorder(
#                         radius=8)
#                 ),

#                 on_click=abrirCR
#             )
#         )
#     )


# flet.app(target=main, assets_dir="./Prueba APP 1")

""" VAlidar Cedula """

# def vcedula(texto):
#     # sin ceros a la izquierda
#     nocero = texto.strip("0")
    
#     cedula = int(nocero,0)
#     verificador = cedula%10
#     numero = cedula//10
    
#     # mientras tenga números
#     suma = 0
#     while (numero > 0):
        
#         # posición impar
#         posimpar = numero%10
#         numero   = numero//10
#         posimpar = 2*posimpar
#         if (posimpar  > 9):
#             posimpar = posimpar-9
        
#         # posición par
#         pospar = numero%10
#         numero = numero//10
        
#         suma = suma + posimpar + pospar
    
#     decenasup = suma//10 + 1
#     calculado = decenasup*10 - suma
    
#     if (calculado  >= 10):
#         calculado = calculado - 10

#     if (calculado == verificador):
#         validado = 1
#     else:
#         validado = 0
        
#     return (validado)

# print(vcedula("1234567890"))