from datetime import date, datetime

class Rol:
    def __init__(self, sueldo, horario, tipo_rol):
        self.sueldo = sueldo
        self.horario = horario
        self.tipo_rol = tipo_rol

    def presentar_rol(self):
        print("Rol: ",self.tipo_rol,"\nHorario: ",self.horario,"\nSueldo: " ,self.sueldo)

class Usuario(Rol):
    def __init__(self,sueldo,horario,tipo_rol,nombre,cedula,telefono,correo):
        super().__init__(sueldo,horario,tipo_rol)
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
        
    def presentar_usuario(self):
        print("\nNombre: ",self.nombre,"\nCédula: ",self.cedula,"\nTeléfono: ",self.telefono,"\nCorreo: ",self.correo,"\nRol: ",self.tipo_rol)

class Opciones_Sis(Usuario):
    def __init__(self,sueldo,horario,tipo_rol,nombre,cedula,telefono,correo,nombre_opcion,accion_realizar):
        super().__init__(sueldo, horario, tipo_rol, nombre, cedula, telefono, correo)
        self.nombre_opcion = nombre_opcion
        self.accion_realizar = accion_realizar

    def presentar_opcion(self):
        print("\nOpción: ",self.nombre_opcion,"\nAcción: ",self.accion_realizar,"\nRol: ",self.tipo_rol)

class Operaciones:
    def __init__(self,nombre_operaciones,horas_activo,operaciones_realizadas):
        self.nombre_operaciones = nombre_operaciones
        self.horas_activo = horas_activo
        self.operaciones_realizadas = operaciones_realizadas

    def presentar_operaciones(self):
        print("\nOperación: ",self.nombre_operaciones,"\nHoras Activo: ", self.horas_activo,"\nOperaciones realizadas: ", self.operaciones_realizadas)

class Modulo_Seguridad:
    def operaciones(self):
        pass

rol = Rol(425.50,datetime.today(),"Gerente")
rol.presentar_rol()

user = Usuario(425,datetime.today,"Gerente","Andrés", "0929472397", "0984479305", "wtrujillov")
user.presentar_usuario()

opciones = Opciones_Sis(425,date.today,"Gerente","Andrés", "0929472397", "0984479305", "wtrujillov","Admin","Controlar")
opciones.presentar_opcion()

operacion = Operaciones("Supervisar a sus subordinados",10,20)
operacion.presentar_operaciones()