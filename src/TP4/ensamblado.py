class LeafElement:

    def __init__(self, *args):
        self.position = args[0]

    def showDetails(self):
        print("\t", end ="")
        print("%s {Child}" % (self.position))


class CompositeElement:
    
    def __init__(self, *args):
        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        print("%s {Composed}" % (self.position))
        for child in self.children:
            print("\t", end ="")
            child.showDetails()

topLevelMenu = CompositeElement("ProductoPrincipal")
subMenuItem1 = CompositeElement("Sub-conjunto1")
subMenuItem2 = CompositeElement("Sub-conjunto2")
subMenuItem3 = CompositeElement("Sub-conjunto3")
subMenuItem11 = LeafElement("Pieza11")
subMenuItem12 = LeafElement("Pieza12")
subMenuItem13 = LeafElement("Pieza13")
subMenuItem14 = LeafElement("Pieza14")
subMenuItem1.add(subMenuItem11)
subMenuItem1.add(subMenuItem12)
subMenuItem1.add(subMenuItem13)
subMenuItem1.add(subMenuItem14)
subMenuItem21 = LeafElement("Pieza21")
subMenuItem22 = LeafElement("Pieza22")
subMenuItem23 = LeafElement("Pieza23")
subMenuItem24 = LeafElement("Pieza24")
subMenuItem2.add(subMenuItem21)
subMenuItem2.add(subMenuItem22)
subMenuItem2.add(subMenuItem23)
subMenuItem2.add(subMenuItem24)
subMenuItem31 = LeafElement("Pieza31")
subMenuItem32 = LeafElement("Pieza32")
subMenuItem33 = LeafElement("Pieza33")
subMenuItem34 = LeafElement("Pieza34")
subMenuItem3.add(subMenuItem31)
subMenuItem3.add(subMenuItem32)
subMenuItem3.add(subMenuItem33)
subMenuItem3.add(subMenuItem34)
topLevelMenu.add(subMenuItem1)
topLevelMenu.add(subMenuItem2)
topLevelMenu.add(subMenuItem3)

#Sub-conjunto adicional
subMenuItem4 = CompositeElement("Sub-conjunto4")
subMenuItem41 = LeafElement("Pieza41")
subMenuItem42 = LeafElement("Pieza42")
subMenuItem43 = LeafElement("Pieza43")
subMenuItem44 = LeafElement("Pieza44")
subMenuItem4.add(subMenuItem41)
subMenuItem4.add(subMenuItem42)
subMenuItem4.add(subMenuItem43)
subMenuItem4.add(subMenuItem44)

resp=input("Quisiera agregar un sub-conjunto adicional? S/N ")
if resp == "S":
    topLevelMenu.add(subMenuItem4)
    topLevelMenu.showDetails()
else:
    topLevelMenu.showDetails()
