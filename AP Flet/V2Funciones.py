
import flet
from flet import *

def main(page: Page):

    cont = band = 0
    temp = ""
    usAc = ["" for x in range(7)]

    class func(UserControl):
        
        def __init__(self, ced: TextField, pin: TextField):
            self.cedula = ced
            self.contra = pin
            super().__init__()

        def ingresar(self, e):

            nonlocal temp, cont, band, usAc

            with open("usuarios.txt", "r+") as f:      
                
                for linea in f.readlines():
                    datos = linea.strip().split(" ")

                    if self.cedula.value == datos[1]: 
                        usAc = datos
                        break

                    else: usAc = datos


            if self.cedula.value == usAc[1] and self.contra.value == usAc[4]:
                self.cedula.border_color = self.contra.border_color = "green"
                band = 1
            
            elif self.cedula.value == usAc[1] and self.contra.value != usAc[4]:

                cont += 1

                if temp != usAc[1]:
                    cont = 1
                
                self.contra.value = ""
                self.contra.focus()
                self.contra.error_text = f"Contraseña incorrecta\nTiene {3-cont} intentos"

            elif self.cedula.value != usAc[1]:

                self.cedula.value = ""

                self.cedula.focus()
                self.cedula.value = self.contra.value = ""
                self.cedula.error_text = "Usuario no registrado"
            
            temp = usAc[1]

            self.cedula.update()
            self.contra.update()

            sleep(2)
            self.cedula.error_text = self.contra.error_text = None
            self.cedula.border_color = self.contra.border_color = "transparent"
            
            page.update()