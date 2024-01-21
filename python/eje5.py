# Debe devolver el total de la compra
class ListaDeCompras:
    def __init__(self):
        self.compras = []

    def agregar_item(self, item):
        self.compras.append(item)

    def calcular_total(self, precios):
        total = 0
        for item in self.compras:
            if item in precios:
                total += precios[item]
            else:
                total += 0
            return total 

        
            
mi_lista = ListaDeCompras()


mi_lista.agregar_item('manzanas')
mi_lista.agregar_item('peras')
mi_lista.agregar_item('almendras')

precios = {'manzanas': 2.0, 'peras': 2.5}

total = mi_lista.calcular_total(precios)
print(f'Total de la compra: ${total}')
