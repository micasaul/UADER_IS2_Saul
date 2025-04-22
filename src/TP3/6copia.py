class Documento:

    def __init__(self, contenido):
        self.contenido = contenido
    
    def get(self):
        return self.contenido
    
    def clone(self):
        return Documento(self.contenido)