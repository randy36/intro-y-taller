class invertir:
    def __init__(self):
        pass

    def invertir1(self,lista):
        if isinstance (lista,list):
            return self.invertir_lista(lista)
        else: return "Error, la lista ingresada no es valida"

    def invertir_lista(self,lista):
        if lista == []:
            return []
        else: return [lista[-1]] + self.invertir_lista(lista [:-1])
