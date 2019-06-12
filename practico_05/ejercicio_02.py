# Implementar los metodos de la capa de datos de socios.


from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio, engine, reset_tabla



class DatosSocio(object):

    def __init__(self):

        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
    
    def cerrar(self):
        self.session.close()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        usuario = self.session.query(Socio).filter(Socio.id==id_socio).first()
        if usuario is None:
            return False
        else:
            return usuario
 

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        usuario = self.session.query(Socio).filter(Socio.dni==dni_socio).first()
        if usuario is None:
            return False
        else:
            return usuario

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        usuario = []
        buscar=(self.session.query(Socio).all())
        for i in buscar:
            usuario.append(i)    
        return usuario

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        usuario = []
        buscar=(self.session.query(Socio).all())
        for i in buscar:
            usuario.append(i)
        if usuario is None:
            return False
        else:
            self.session.query(Socio).delete()
            
            return True

    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        self.session.add(socio)
        self.session.commit()
        return socio

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        usuario = self.buscar(id_socio)
        if usuario is None :
            return False
        else:
            self.session.delete(usuario)
            self.session.commit()
            return True
       

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """
        actualizar = update(Socio).where(Socio.id == socio.id).values(nombre=socio.nombre,apellido=socio.apellido,dni=socio.dni)
        self.session.execute(actualizar)
        self.session.commit()
        return socio

@reset_tabla
def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0
    print("Assert 1 ", socio.id)
    # baja
    assert datos.baja(socio.id) == True
    print("Assert 2 ", socio.id)
    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2
    print("Assert 3 ", datos.buscar(socio_2.id))

    # buscar dni
    # socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar_dni(socio_2.dni) == socio_2
    print("Assert 4 ", datos.buscar(socio_2.dni))
    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587
    print ("Assert 5 ", socio_3_modificado.id, socio_3_modificado.nombre, socio_3_modificado.apellido, socio_3_modificado.dni)

    # todos
    assert len(datos.todos()) == 2
    print ("Assert 6 ", len(datos.todos()))
    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0
    print ("Assert 7 ", len(datos.todos()))
    #cerrar sesion
    datos.cerrar()

    

if __name__ == '__main__':
    pruebas()
    
