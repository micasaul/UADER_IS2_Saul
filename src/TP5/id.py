class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, id_code):
        print(f"Emitiendo ID: {id_code}")
        for observer in self.observers:
            observer.update(id_code)

class Observer:
    def __init__(self, id):
        self.id = id

    def update(self, emitted_id):
        if self.id == emitted_id:
            print(f"Recibió su ID ({self.id})")

subject = Subject()
subject.attach(Observer("AB12"))
subject.attach(Observer("CD34"))
subject.attach(Observer("EF56"))
subject.attach(Observer("GH78"))

ids_emitidos = ["ZZ99", "AB12", "XY01", "CD34", "EF56", "00ZZ", "GH78", "A1B2"]
for id in ids_emitidos:
    subject.notify(id)
