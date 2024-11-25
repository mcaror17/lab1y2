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
        return (f"{usr.nombre} {usr.id} {usr.fecha_nacimiento} {usr.ciudad_nacimiento} {usr.tel} {usr.email} {usr.dir}")

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
            usuarioi = Usuario(nombre=i[0],id=i[1],fecha_nacimiento=fechai.formatof(),ciudad_nacimiento=i[5],tel=i[6],email=i[7],dir=direccioni.formatod())
            agei.agregar(usuarioi)
        return agei
    
fcha1 = Fecha(15,10,2003)
dir1 = Direccion(calle="cll15", nomenclatura="CD-10", edificio="Nuevo-Milenio", apto=1510)
usr1 = Usuario(nombre="Mateo-Giraldo", id=77, fecha_nacimiento=fcha1.formatof(),ciudad_nacimiento="Bello", tel=60045, email="mateo@gmail.com", dir=dir1.formatod())
age2 = Agenda(0)
age2 = age2.importar()
#for i in range (0,len(age2.registro)):
    #print(age2.registro[i].formatou())
age2.eliminar("1075689")
age2.agregar(usr1)
age2.toFile()
            
