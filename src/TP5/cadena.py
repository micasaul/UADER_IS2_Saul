def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

class Handler:
    def __init__(self, next=None):
        self.next = next

    def handle(self, request):
        handled = self.processRequest(request)
        if not handled:
            self.next.handle(request)

    def processRequest(self, request):
        raise NotImplementedError('First implement it !')

class ParesHandler(Handler):
    def processRequest(self, num):
        if num % 2 == 0:
            print(f"{num} fue consumido por ParesHandler.")
            return True

class PrimosHandler(Handler):
    def processRequest(self, num):
        if es_primo(num):
            print(f"{num} fue consumido por PrimosHandler.")
            return True

class DefaultHandler(Handler):
    def processRequest(self, num):
        print("Este numero no puede ser consumido.")
        return True
    
class User:
    def __init__(self):
        initial = None
        self.handler = PrimosHandler(ParesHandler(DefaultHandler(initial)))

    def agent(self, user_request):
        self.handler.handle(user_request)

user = User()

for i in range(1, 101):
    user.agent(i)
