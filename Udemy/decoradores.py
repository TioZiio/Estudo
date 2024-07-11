
def funcao():
    def decoradora(func):
        print('---------Decorando---------')
        def aninhada(*args, **kwargs):
            print('Valores: ', *args)
            x, operador, z = [*args]
            if operador == '+':
                resultado = x + z
            elif operador == '-':
                resultado = x - z
            elif operador == '*':
                resultado = x * z
            elif operador == '/':
                resultado = x / z
            else:
                raise ValueError("Operador inválido")
            return resultado
        return aninhada

    @decoradora
    def soma(x=0, y='+', z=0): return (x, y, z)

    x_mais_y = [(10,'-',5),(15,'*',2),(10,'/',2), (5,'+',1)]
    for n in x_mais_y:
        rest = soma(n[0], n[1], n[2])
        print('\n\t', rest, '\n')


def classes():

    def meu_repr(self):
            class_name = self.__class__.__name__
            class_dict = self.__dict__
            class_repr = f'{class_name} - {class_dict}'
            return class_repr

    def adiciona_repr(cls):
        cls.__repr__ = meu_repr
        return cls

    @adiciona_repr
    class Nome:
        def __init__(self, nome):
            self.nome = nome
        
    @adiciona_repr
    class Rpg:
        def __init__(self, classe):
            self.classe = classe

    tio = Nome('TioZiio')
    zara = Nome('Zarathrusta')
    mago = Rpg('Mago-Runico')
    merc = Rpg('Mercador')

    print(f'{tio.nome} - {mago.classe};\n{zara.nome} - {merc.classe};')

classes()
