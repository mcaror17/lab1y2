UyC = {"Usuarios": ["Juan1223","Maria2345",
                     "Pablo1459 ","Ana3456"], 
                     "Contraseñas": ["J12an*.","M23a*.",
                                     "P14o*.","A34a*."]}
try: 
  for i in range (0,3):
    try: 
      u = str(input("Ingrese el usuario: "))
      c = str(input("Ingrese la contraseña: ")) 
    except ValueError: 
      print("Intente nuevamente")
    
    Acceso = False
    for i in range (len(UyC["Usuarios"])):
        if (UyC["Usuarios"][i] == u and UyC["Contraseñas"][i] == c):
            print("Acceso permitido")
            Acceso = True
            break
    if (Acceso == True):
        break
    elif (Acceso == False):
        print("Datos incorrectos")
except:
    print("Lo siento, su acceso no es permitido")

