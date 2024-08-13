
# yield funciona como um checkpoint..., que precisa ser acionado novamente para iniciar de onde parou
def test(inicio=0, fim=10):
    while True:
        yield inicio
        n = input("Quer continuar?")
        if n[0] == 'n':
            break
        inicio += 1
        if inicio == 10:
            break

"""
# É possivel chamar cada checkpoint com o comando next()
generator = test()
print(next(generator)) # cada next chama até o próximo checkpoint.
"""
generator = test()
for n in generator:
    print(n)