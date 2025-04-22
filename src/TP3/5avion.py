class Avion:

    def __init__(self):
        self.body = None
        self.turbinas = []
        self.alas = []
        self.tren_aterrizaje = None
    
    def build(self):
        return Avion(self.body, self.turbinas, self.alas, self.tren_aterrizaje)
    