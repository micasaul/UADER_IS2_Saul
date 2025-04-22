class Factura:

    def __init__(self, importe):
        self.importe = importe
    
class Responsable(Factura):
    def mostrar(self):
        base = self.importe
        iva = base * 0.21
        total = base + iva
        print("Factura - IVA Responsable Inscripto")
        print(f"Total: {total}")

class NoInscripto(Factura):
    def mostrar(self):
        base = self.importe
        print("Factura - IVA No Inscripto")
        print(f"Total: {base}")

class Exento(Factura):
    def mostrar(self):
        base = self.importe
        print("Factura - IVA Exento")
        print(f"Total: {base}")

class facturaFactory:
    def crear_factura(condicion, importe):
        if condicion == "responsable":
            return Responsable(importe)
        elif condicion == "no inscripto":
            return NoInscripto(importe)
        elif condicion == "exento":
            return Exento(importe)
        else:
            raise ValueError("Condición impositiva no válida. Las condiciones validas son responsable, no inscripto o exento.")