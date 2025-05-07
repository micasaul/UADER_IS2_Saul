class lamina:

    def __init__(self, tren):
        self.espesor = 0.5
        self.ancho = 1.5
        self.alto = None
        self.tren = tren

    def generar(self):
        self.tren.generar(self)

class tren5:

    def generar(self, lamina):
        lamina.alto = 5
        print(f"Lamina de {lamina.alto} metros generada.")
        print(f"Espesor: {lamina.espesor} pulgadas, Ancho: {lamina.ancho} metros")

class tren10:
    
    def generar(self, lamina):
        lamina.alto = 10
        print(f"Lamina de {lamina.alto} metros generada.")
        print(f"Espesor: {lamina.espesor} pulgadas, Ancho: {lamina.ancho} metros")

#Prueba de 5 metros
lamina_5 = lamina(tren5())
lamina_5.generar()

#Prueba de 10 metros
lamina_10 = lamina(tren10())
lamina_10.generar()
