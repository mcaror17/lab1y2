class Fecha:
    def __init__(fcha, dd, mm, aa):
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
        return (f"{fcha.dd} - {fcha.mm} - {fcha.aa}")
    
class Direccion:
    def __init__(dir, calle, nomenclatura, barrio, ciudad, edificio, apto):
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
        return (f"Calle: {dir.calle} - {dir.nomenclatura} - Barrio: {dir.barrio} - Ciudad: {dir.ciudad} - Edificio: {dir.edificio} - Apto: {dir.apto}")
    
class Usuario:
    def __init__(usr, nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir):
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
        return (f"Nombre: {usr.nombre} - ID: {usr.id} - Fecha nacimiento: {usr.fecha_nacimiento} - Telefono: {usr.tel} - Direccion: {usr.dir}")

