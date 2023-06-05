

class Controlador:
    __instancia = None

    def __init__(self, qualquer):
        self.atributo_qualquer = qualquer

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not Controlador.__instancia:
            Controlador.__instancia = object.__new__(cls)
        return Controlador.__instancia

    @classmethod
    def metodo_classe(cls):
        print("metodo zumbi")

Controlador.metodo_classe()

inst_controlador = Controlador('Atributo 1')

print(inst_controlador, inst_controlador.atributo_qualquer)

inst_controlador2 = Controlador('Atributo 2')


print(inst_controlador2, inst_controlador2.atributo_qualquer)