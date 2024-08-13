
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
