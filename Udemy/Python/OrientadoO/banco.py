import contas
import pessoas


class Banco:
    def __init__(
        self, 
        agencias: list[int] | None = None ,
        clientes: list[pessoas.Pessoa] | None = None,
        todas_contas: list[contas.Conta] | None = None
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.todas_contas = todas_contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.todas_contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_se_conta_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_cliente', True)
            return True
        print('_checa_se_conta_cliente', False)
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.agencias!r}, {self.clientes!r}, {self.todas_contas!r})'
        return f'{class_name}{atributos}'
        

if __name__=='__main__':
    cl1 = pessoas.Cliente('David', 23)
    cpl1 = contas.Poupanca(111,20,100)
    cl1.conta = cpl1

    cl2 = pessoas.Cliente('Gaby', 21)
    ccl2 = contas.Corrente(115, 20, 200, 50)
    cl2.conta = ccl2

    banco = Banco()
    banco.clientes.extend([cl1, cl2])
    banco.todas_contas.extend([cpl1, ccl2])
    banco.agencias.extend([111, 115])


    if banco.autenticar(cl1, cpl1):
        cpl1.sacar(150)

    # print(banco)
    # print(32 *'#')
    # print(banco.autenticar(cl1, ccl2))
    # print(32 *'#')
    # print(banco.autenticar(cl2, ccl2))