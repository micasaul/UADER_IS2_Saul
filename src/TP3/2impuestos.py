class Impuestos:
    _instance= None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Impuestos, cls).__new__(cls)
        return cls._instance
    
    def calcular (self, base):
        if base < 0:
            raise ValueError("La base imponible no puede ser negativa")
        
        iva = base * 0.21
        iibb = base * 0.05
        contribuciones = base * 0.012

        total_impuestos = iva + iibb + contribuciones
        base_con_impuestos = base + total_impuestos

        return base_con_impuestos