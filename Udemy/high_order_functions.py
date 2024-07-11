"""
Crie uma função que dupliquem, tripliquem e quadripliquem o número recebido como parametro
"""

# def mult(valor, *args):
# 	return [valor * n for n in args[0]]
# x = int(input('Valor: '))
# print(mult(x,[2,3,4]))

def mult(func):
	def calc(valor):
		return func * valor
	return calc
x = int(input('VAlor: '))

v = {
	'dup': mult(2),
	'trip': mult(3),
	'quad': mult(4)
}
x = [print(v[n](x)) for n in v.keys()]