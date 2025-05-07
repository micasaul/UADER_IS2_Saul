class valor:

    def __init__(self, num):
        self._num = num
    
    def render(self):
        return self._num

class suma(valor):

    def __init__(self, cuenta):
        self._cuenta = cuenta

    def render(self):
        return self._cuenta.render() + 2
    
class multiplicacion(valor):

    def __init__(self, cuenta):
        self._cuenta = cuenta
    
    def render(self):
        return self._cuenta.render() * 2

class division(valor):
    
    def __init__(self, cuenta):
        self._cuenta = cuenta
    
    def render(self):
        return self._cuenta.render() / 3
    
antes = valor(16)
despues = division(multiplicacion(suma(antes)))

print(f"Antes de decorator el valor era {antes.render()}")
print(f"Con decorator el valor queda {despues.render()}")