from Clases.Tarjeta import Tarjeta

# Definicion de la clase Persona
class Persona:
    def __init__(self, numero_cliente, nombre, telefono, documento, tarjetas):
        self.numero_cliente = numero_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.documento = documento
        self.visa = ""
        self.validateVisa = ""
        self.master = ""
        self.validateMaster = ""
        self.amex = ""
        self.validateAmex = ""
        self.discover = ""
        self.validateDiscover = ""


        for tarjeta in tarjetas:
            if tarjeta.startswith("4"):
                self.visa = tarjeta
                self.validateVisa = Tarjeta(str(self.visa)).ValidarTarjeta()

            elif tarjeta.startswith("5"):
                self.master = tarjeta
                self.validateMaster = Tarjeta(str(self.master)).ValidarTarjeta()
               
            elif tarjeta.startswith("3"):
                self.amex = tarjeta
                self.validateAmex = Tarjeta(str(self.amex)).ValidarTarjeta()            
            
            elif tarjeta.startswith("6"):
                self.discover = tarjeta
                self.validateDiscover = Tarjeta(str(self.discover)).ValidarTarjeta()              
    



