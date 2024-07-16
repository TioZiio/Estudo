import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
        
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade


    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{atributos}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta : contas.Conta | None = None


if __name__=='__main__':
    cl1 = Cliente('David', 23)
    cl1.conta = contas.Poupanca(111,20,100)
    print(cl1)
    print(cl1.conta)
    print(32 * '#')

    cl2 = Cliente('Gaby', 21)
    cl2.conta = contas.Corrente(115, 20, 200, 50)
    print(cl2)
    print(cl2.conta)
    cl2.conta.sacar(50)
    print(32 * '#')