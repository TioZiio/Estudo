import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, n_conta: int, saldo:float = 0):
        self.agencia = agencia
        self.n_conta = n_conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'\tDepositado: {valor:.2f}')

    def detalhes(self, msg=''):
        print(32*'-')
        print(f'{msg}\nValor em conta: \t{self.saldo:.2f}')
    
    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.agencia!r}, {self.n_conta!r}, {self.saldo!r})'
        return f'{class_name}{atributos}'


class Poupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'\tSacando: {valor:.2f}')
            return self.saldo
        
        self.detalhes(f'\tSaque negado {valor:.2f}')

class Corrente(Conta):
    def __init__(self, agencia: int, n_conta: int, saldo: float = 0, limite: float = -100):
        super().__init__(agencia, n_conta, saldo)
        self.limite = limite
    
    def sacar(self, valor: int):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
        
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'\tSacando: {valor:.2f}')
            return self.saldo
        
        self.detalhes(f'\tSaque negado {valor:.2f}')

    
    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.agencia!r}, {self.n_conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{atributos}'


if __name__ == '__main__':
    infs = ['Agencia', 'Conta', 'Saldo']
    perfil = [int(input(f'Digite a {infs[i]}: ')) for i in range(3)]

    david = Poupanca(*perfil)
    david.sacar(20)
    david.depositar(10)

    print(10*'%')

    infs = ['Agencia', 'Conta', 'Saldo', 'limite']
    perfil = [int(input(f'Digite a {infs[i]}: ')) for i in range(len(infs))]

    gaby = Corrente(*perfil)
    gaby.sacar(100)
    gaby.depositar(10)

