class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificaciones(self):
        raise NotADirectoryError
    

class NotificadorEmail(Notificador):
    def __init__(self,usuario,mensaje,email):
        super().__init__(usuario,mensaje)
        self.email = email

    def notificaciones(self):
        print(f"Enviando mensaje {self.mensaje} a {self.usuario} al correo {self.email}")

class NotificadorSMS(Notificador):
    def __init__(self,usuario,mensaje,telefono):
        super().__init__(usuario,mensaje)
        self.telefono = telefono

    def notificaciones(self):
        print(f"Enviando mensaje {self.mensaje} a {self.usuario} al telefono {self.telefono}")

class NotificadorWhatsapp(Notificador):
    def __init__(self,usuario,mensaje,numero):
        super().__init__(usuario,mensaje)
        self.numero = numero

    def notificaciones(self):
        print(f"Enviando mensaje {self.mensaje} a {self.usuario} al numero {self.numero}")