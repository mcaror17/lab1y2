UyC = {"Usuarios": ["Juan1223","Maria2345",
                     "Pablo1459 ","Ana3456"], 
                     "Contraseñas": ["J12an*.","M23a*.",
                                     "P14o*.","A34a*."]}
for i in range (0,3):
    u = str(input("Ingrese el usuario: "))
    c = str(input("Ingrese la contraseña: "))
    Acceso = False
    for i in range (len(UyC["Usuarios"])):
        if (UyC["Usuarios"][i] == u and UyC["Contraseñas"][i] == c):
            print("Acceso permitido")
            Acceso = True
            break
    if (Acceso == True):
        break
    if (Acceso == False):
        print("Datos incorrectos")
if (Acceso == False):
    print("Lo siento, su acceso no es permitido")

