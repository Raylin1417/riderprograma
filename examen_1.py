print("Calculemos los segundos de un tiempo determinado\n")
tiempo=input("Cual es tu tiempo ")
print(f"Tu tiempo para calcular los segundos es : {tiempo} ")
hora=int(input("Dame la hora de tu tiempo elegido "))
minutos=int(input("Dame los minutos de tu hora "))
segundos=int(input("Dame los segundos de tu hora "))
segundos_totales=hora*3600+ minutos*60 + segundos
print(f"Hola los segundos totales de el tiempo que colocaste es de : {segundos_totales}")
