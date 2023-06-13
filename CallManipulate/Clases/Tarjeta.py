class Tarjeta:
    def __init__(self, numero):
        self.numero = numero

    def ValidarTarjeta(self):
        tarjetaInvertida = ""
        # Se invierte el string tarjeta
        for x in self.numero:
            tarjetaInvertida = x + tarjetaInvertida

        InvertidoMultiplicado = ""
        #Multiplicar x2 salteando una vez por iteracion un elemento del string
        for i in range(0, len(tarjetaInvertida), 2):
            par = tarjetaInvertida[i:i+2]
            try:
                numeroMultiplicado = int(par[1]) * 2
            except IndexError:
                numeroMultiplicado = 0
        
        # str numeroMultiplicado convierte en una cadena de texto
        # int digito convierte cada valor de esta cadena en un entero
        if numeroMultiplicado > 9:
            numeroMultiplicado = sum(int(digito) for digito in str(numeroMultiplicado))

        InvertidoMultiplicado += str(par[0]) + str(numeroMultiplicado)

        valorAValidar = 0
        for x in InvertidoMultiplicado:
            valorAValidar += int(x)

        if valorAValidar % 10 == 0:
            return "Tarjeta valida."
        else:
            return "Tarjeta no valida."
    



