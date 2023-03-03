import os
import random
import smtplib

def enviar_correo(usuario, email):
    mensaje= (f"{usuario}, esto es un correo automatico usando python")
    
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    
    s.login("juantonioramos26@gmail.com", "fjcihvbyzfrjnsmz")
    s.sendmail("juantonioramos26@gmail.com", email, mensaje)
    print(f"Mensaje enviado a {usuario}")

enviar_correo("Briones", "20630241@itocotlan.com")

"""
correos = [["Antonio Ramos", "20630271@itocotlan.com"], ["Martin", "juanmglezrazo@gmail.com"], ["Danca", "dancarrodoce@gmail.com"], ["Benja", "benjamin3455rg16@gmail.com"]]

for correo in correos:
    enviar_correo(correo[0], correo[1])
"""