

import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		
		self.file = file
		self.content = content


class FileWriterUtility:

	def __init__(self, file):

		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string


	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:

	def __init__(self):
		self.saved = []

	def save(self, writer):
		self.obj = writer.save()
		if len(self.saved) < 4:
			self.saved.append(self.obj)
		else:
			self.saved.pop(0)
			self.saved.append(self.obj)

	def undo(self, writer, index=0):
		writer.undo(self.saved[-(index+1)])


if __name__ == '__main__':

	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar");
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional II")
	writer.write("Material adicional de la clase de patrones II\n")
	print(writer.content + "\n\n")


	print("se invoca al <undo>")
	caretaker.undo(writer)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

	print("se invoca al <undo>")
	caretaker.undo(writer, 1)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")


