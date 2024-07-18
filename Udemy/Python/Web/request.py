
import requests


url = 'http://localhost:12000/'

#           Metodos
# GET - POST - PUT - PATCH - DELETE
# HEAD - OPTIONS - TRACE - CONNECT 

response = requests.get(url)

print(response.status_code)
# print(response.headers)  # Puxa o cabeçario da pagina;
# print(response.content)  # Puxa o conteudo do arquivo;
print(response.text)

