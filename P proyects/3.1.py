class Fecha:
    def __init__(fcha, dd=None, mm=None, aa=None):
        fcha.dd = dd
        fcha.mm = mm
        fcha.aa = aa
    
    def set_dia(fcha,ndd):
        fcha.dd = ndd
    def set_mes(fcha,nmm):
        fcha.mm = nmm
    def set_año(fcha,naa):
        fcha.aa = naa
    def get_dia(fcha):
        return fcha.dd 
    def get_mes(fcha):
        return fcha.mm 
    def get_año(fcha):
        return fcha.aa
    def formatof(fcha):
        return (f"{fcha.dd} {fcha.mm} {fcha.aa}")
    
class Direccion:
    def __init__(dir, calle=None , nomenclatura=None, barrio=None, ciudad=None, edificio=None, apto=None):
        dir.calle = calle
        dir.nomenclatura = nomenclatura
        dir.barrio = barrio
        dir.ciudad = ciudad
        dir.edificio = edificio
        dir.apto = apto
    
    def set_calle(dir,ncalle):
        dir.calle = ncalle
    def set_nomenclatura(dir,nnomenclatura):
        dir.nomenclatura = nnomenclatura
    def set_barrio(dir,nbarrio):
        dir.barrio = nbarrio
    def set_ciudad(dir,nciudad):
        dir.ciudad = nciudad
    def set_edificio(dir,nedificio):
        dir.edificio = nedificio
    def set_apto(dir,napto):
        dir.apto = napto
    
    def get_calle(dir):
        return dir.calle
    def get_nomenclatura(dir):
        return dir.nomenclatura
    def get_barrio(dir):
        return dir.barrio
    def get_ciudad(dir):
        return dir.ciudad
    def get_edificio(dir):
        return dir.edificio
    def get_apto(dir):
        return dir.apto
    def formatod(dir):
        return (f"{dir.calle} {dir.nomenclatura} {dir.barrio} {dir.ciudad} {dir.edificio} {dir.apto}")
    
class Usuario:
    def __init__(usr, nombre=None, id=None, fecha_nacimiento=None, ciudad_nacimiento=None, tel=None, email=None, dir=None):
        usr.nombre = nombre
        usr.id = id
        usr.fecha_nacimiento = fecha_nacimiento
        usr.ciudad_nacimiento = ciudad_nacimiento
        usr.tel = tel
        usr.email = email
        usr.dir = dir

    def set_nombre(usr,nnombre):
        usr.nombre = nnombre
    def set_id(usr,nid):
        usr.id = nid
    def set_fecha_nacimiento(usr,nfecha_nacimiento):
        usr.fecha_nacimiento = nfecha_nacimiento
    def set_tel(usr,ntel):
        usr.tel = ntel
    def set_dir(usr,ndir):
        usr.dir = ndir

    def get_nombre(usr):
        return usr.nombre
    def get_id(usr):
        return usr.id
    def get_fecha_nacimiento(usr):
        return usr.fecha_nacimiento
    def get_tel(usr):
        return usr.tel
    def get_dir(usr):
        return usr.dir
    def formatou(usr):
        return (f"{usr.nombre} {usr.id} {usr.fecha_nacimiento.formatof()} {usr.ciudad_nacimiento} {usr.tel} {usr.email} {usr.dir.formatod()}")

class Agenda:
    def __init__(age, capacidad):
        age.registro = [None]*capacidad
        age.no_registro = 0

    def agregar(age, usr):
        if(age.buscar(usr.get_id()) != -1):
            return False
        elif(age.no_registro<len(age.registro)):
            age.no_registro += 1
            age.registro[age.no_registro-1]=usr
            return True
        
    def buscar(age, id):
        for i in range (0, len(age.registro)): 
            if age.registro[i] is not None and age.registro[i].get_id() == id:
                return i
        return -1 
    
    def eliminar(age, id):
        if(age.buscar(id) == -1):
            return False
        else:
            iborrado = age.buscar(id)
            age.registro[iborrado]=None
            for i in range (iborrado, len(age.registro)-1):
                age.registro[i] = age.registro[i+1]
            age.registro[-1] = None
            age.no_registro -= 1
            return True
        
    def toFile(age):
        agenda = open('agenda.txt', 'w')
        for i in age.registro:
            if (i is not None):
                agenda.write(f"{i.formatou()}\n")
        agenda.close()
        
    def importar(age):
        agenda = open('agenda.txt','r')
        a = agenda.readlines()
        agei = Agenda(len(a))
        for j in a:
            i = j.split()
            if len(i)<14:
                continue
            fechai = Fecha(dd=int(i[2]),mm=int(i[3]),aa=int(i[4]))
            direccioni = Direccion(calle=i[8],nomenclatura=i[9],barrio=i[10],ciudad=i[11],edificio=i[12],apto=i[13])
            usuarioi = Usuario(nombre=i[0],id=int(i[1]),fecha_nacimiento=fechai,ciudad_nacimiento=i[5],tel=int(i[6]),email=i[7],dir=direccioni)
            agei.agregar(usuarioi)
        agenda.close()
        return agei

fcha1 = Fecha(15,8,2000)
fcha2 = Fecha(9,10,2003)
fcha3 = Fecha(24,12,1999)
fcha4 = Fecha(30,1,2005)
fcha5 = Fecha(5,7,2002)
dir1 = Direccion(calle="Cll40", nomenclatura="C-15", barrio="Candelaria", ciudad="Medellin", edificio="Bosque-de-viento", apto= 1218)
dir2 = Direccion(calle="Cll10", nomenclatura="B3", barrio="Santafe", ciudad="Bogota", edificio="Manzana-10", apto= 121)
dir3 = Direccion(calle="Av40", nomenclatura="A-20", barrio="Prado", ciudad="Medellin", edificio="Altos-del-bosque", apto= 1817)
dir4 = Direccion(calle="Cll8", nomenclatura="TO-15", barrio="Poblado", ciudad="Medellin", edificio="Bosque-Tropical", apto= 909)
dir5 = Direccion(calle="Cll53", nomenclatura="D-10H", barrio="Niquia", ciudad="Bello", edificio="Nuevo-Amanecer", apto=151)
usr1 = Usuario(nombre="Sofia-Martinez", id= 1982, fecha_nacimiento=fcha1, ciudad_nacimiento="Cartagena", tel=7000457, email="sofim@gmail.com", dir=dir1)
usr2 = Usuario(nombre="Andra-Garcia", id= 4768, fecha_nacimiento=fcha2, ciudad_nacimiento="Medellin", tel=4000978, email="andreita123@gmail.com", dir=dir2)
usr3 = Usuario(nombre="Maria-Lopez", id= 9944, fecha_nacimiento=fcha3, ciudad_nacimiento="Medellin", tel=8000465, email="marial@gmail.com", dir=dir3)
usr4 = Usuario(nombre="Juan-Gomez", id= 5656, fecha_nacimiento=fcha4, ciudad_nacimiento="Bogota", tel=3000365, email="juang@gmail.com", dir=dir4)
usr5 = Usuario(nombre="Mateo-Giraldo", id= 7777, fecha_nacimiento=fcha5, ciudad_nacimiento="Medellin", tel=3000576, email="mateog@gmail.com", dir=dir5)
age1 = Agenda(5)
age1.agregar(usr1)
age1.agregar(usr2)
age1.agregar(usr3)
age1.agregar(usr4)
age1.agregar(usr5)
print(age1.buscar(7777)
age1.toFile()
