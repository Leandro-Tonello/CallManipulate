import re

# Definicion de la clase Persona
class Persona:
    def __init__(self, numero_cliente, nombre, telefono, documento, tarjetas):
        self.numero_cliente = numero_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.documento = documento
        self.tarjetas = tarjetas

texto = """
1
 Nombre   : GIOFFRE, LUCAS DANIEL                    Doc.    : DU    36.901.296
 Act.Ppal : OTRAS ACTIVIDADES                                                  
 Direccion: AIZPURUA BENITO 2575 2 40                Fe.Alta : 22-06-2017      
            (C1431ERC) CIUDAD AUTONOMA BUENOS AI     Fe.Nac. : 03-10-1993      
            CAPITAL FEDERAL, ARGENTINA               Cod.Post.: (1431)         
 Telefono : (11)>3163-5365 Int.:              Tlx.:         Fax:               
 . Tipo            Mo Cuenta                Fecha  Saldo Deudor  Saldo Acreed. 
 . VISA ORO           4546420024951918                                         

2
 Nombre   : GIORGIUTTI, MARIA CECILIA                Doc.    : DU    17.713.125
 Act.Ppal : HOTELES Y/O RESTAURANTES                                           
 Direccion: MONSENOR LARUMBE 1115                    Fe.Alta : 02-08-2004      
            (1640) MARTINEZ                          Fe.Nac. : 12-04-1966      
            BUENOS AIRES, ARGENTINA                                            
 Telefono : (11)>4144-8799 Int.:              Tlx.:         Fax:               
 . Tipo            Mo Cuenta                Fecha  Saldo Deudor  Saldo Acreed. 
 . TODO SUMA          0001732753                                               
 . ELECTRON                                                                    
 . FILTRAR            020953388                                                
 . CAJA DE AHORRO   $ 4004362-1 142-1      ACTUAL                      9.222,52
 . DEB.AUTOMATICO                                                              
 . OPERACION DE ME                                                             
 . NOSIS              004034773                                                
 . MENSAJES           0003461779                                               
 . SERV. PREFER                                                                
 . -VISA PLATINUM     4338300009675678                                         
 . -MASTER PLA        5239372783200707                                         

3
 Nombre   : GIOVANELLI, JUAN                         Doc.    : DU    33.079.910
 Act.Ppal : SERVICIOS PARA EMPRESAS                                            
 Direccion: DON BOSCO 1499 3 25 B                    Fe.Alta : 25-08-2014      
            (B1642FEE) SAN ISIDRO                    Fe.Nac. : 26-06-1987      
            BUENOS AIRES, ARGENTINA                  Cod.Post.: (1642)         
 Telefono : (11)>6885-3093 Int.:              Tlx.:         Fax:               
 . Tipo            Mo Cuenta                Fecha  Saldo Deudor  Saldo Acreed. 
 . VISA BUSINESS      4937028000412826                                         
 . EMINENT DEBITO                                                              
 . RADOC            $  803974-3 209-7      NODISP                              
 . FILTRAR            033902570                                                
 . VERAZ EXP.         035720795                                                
 . OPERACION DE ME                                                             
 . MENSAJES           0009542785                                               
 . SV.EMINENT CONV                                                             
 . -EMP.ASOCIADA                                                               
 . -VISA SIGNATURE    4593540005400551                                         
 . -MASTER BLK        5505684430500546                                         

4
 Nombre   : GIRALT, ESTEBAN ADOLFO ANDRES            Doc.    : DU    24.529.714
 Act.Ppal : SERVICIOS DE ASESORIA                                              
 Direccion: MEXICO 1036                              Fe.Alta : 19-09-2007      
            (B1640DLF) MARTINEZ                      Fe.Nac. : 01-01-1975      
            BUENOS AIRES, ARGENTINA                  Cod.Post.: (1640)         
 Telefono : (11)>5327-4985 Int.:              Tlx.:         Fax:               
 . Tipo            Mo Cuenta                Fecha  Saldo Deudor  Saldo Acreed. 
 . ELECTRON                                                                    
 . FILTRAR            033208719                                                
 . SOLICITUD ADIC     00000020747699                                           
 . VERAZ EXP.         035898241                                                
 . OPERACION DE ME                                                             
 . MENSAJES           0011431491                                               
 . SERV. PREFER                                                                
 . -VISA ORO          4546420029162289                                         
 . -MASTER.ORO        5456524205615567                                         

5
 Nombre   : GIRALT, MARIA MERCEDES                   Doc.    : DU    30.495.380
 Act.Ppal : ENSENANZA                                                          
 Direccion: AMEGHINO FLORENTINO 355                  Fe.Alta : 21-09-2007      
            (B1643DTE) BECCAR                        Fe.Nac. : 14-09-1983      
            BUENOS AIRES, ARGENTINA                  Cod.Post.: (1643)         
 Telefono : (11)>3588-0367 Int.:              Tlx.:         Fax:               
 . Tipo            Mo Cuenta                Fecha  Saldo Deudor  Saldo Acreed. 
 . MASTER.ORO         5456520317547789                                         

6
  Nombre   : GIRARDI, MARIA EMILIA                    Doc.    : DU    31.722.224
  Act.Ppal : OTRAS ACTIVIDADES                                                  
  Direccion: ELCANO SEBASTIAN 490                     Fe.Alta : 10-09-2008      
             (B1641AYB) ACASSUSO                      Fe.Nac. : 18-07-1985      
             BUENOS AIRES, ARGENTINA                  Cod.Post.: (1640)         
  Telefono : (11)>5616-5024 Int.:              Tlx.:         Fax:               
  . Tipo            Mo Cuenta                Fecha  Saldo Deudor  Saldo Acreed. 
  . VISA PLATINUM      4338300007752834                                         
  . VISA INTERNAC.     4546400067353818                                         
  . VISA ORO           4546420004919018                                         
  . AMEX PLATINUM      377797004554552                                          

7
  Nombre   : GIUNTI, LARA MARIEL                      Doc.    : DU    36.914.785
  Act.Ppal : OTRAS ACTIVIDADES                                                  
  Direccion: AVENIDA MARIA 1155                       Fe.Alta : 04-05-2015      
             (1611) DON TORCUATO                      Fe.Nac. : 21-10-1992      
             BUENOS AIRES, ARGENTINA                                            
  Telefono : (11)>5991-6240 Int.:              Tlx.:         Fax:               
  . Tipo            Mo Cuenta                Fecha  Saldo Deudor  Saldo Acreed. 
  . VISA INTERNAC.     4546400074989125                                         
  . VISA ORO           4546420028099508                                         
  . AMEX ORO           377796011953864                                          
                                      
"""

# Patrones de expresiones regulares
patron_persona = r"\n(\d+)\n\s+Nombre\s+:\s+([^:\n]+)\s+Doc\.\s+:\s+DU\s+([^:\n]+)([\s\S]+?)(?=\n\d+\n|\Z)"
patron_telefono = r"Telefono\s+:\s+([^:\n]+)"
patron_tarjeta = r"\b\d{15,16}\b"

# Extraccion de informacion de todas las personas
personas = []
matches_personas = re.finditer(patron_persona, texto, re.MULTILINE)
for match_persona in matches_personas:
    numero_cliente = match_persona.group(1).strip()
    nombre = match_persona.group(2).strip()
    documento = match_persona.group(3).strip()
    bloque_persona = match_persona.group(4)

    telefono = re.search(patron_telefono, bloque_persona).group(1).strip().replace(" Int.", "")
    tarjetas = re.findall(patron_tarjeta, bloque_persona)

    persona = Persona(numero_cliente, nombre, telefono, documento, tarjetas)
    personas.append(persona)


# Mostrar informacion por pantalla para cada persona
for persona in personas:
    print("Numero de cliente:", persona.numero_cliente)
    print("Nombre:", persona.nombre)
    print("Telefono:", persona.telefono)
    print("Documento:", persona.documento)
    for i, tarjeta in enumerate(persona.tarjetas, start=1):
        print("Tarjeta", i, ":", tarjeta)
    print()  # Separador entre personas