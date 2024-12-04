import requests

class Pessoa:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.data = False
        
    def get_data(self):
        resposta = requests.get('https://jsonplaceholder.typicode.com/users/1')
        
        if resposta.ok:
            self.data = True
            return 'CONECTADO'
        else:
            self.data = False
            return 'ERRO 404'

