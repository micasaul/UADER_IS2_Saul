class Factorial: 
    _instance= None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Factorial, cls).__new__(cls)
        return cls._instance
    
    def calcular (self, n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado