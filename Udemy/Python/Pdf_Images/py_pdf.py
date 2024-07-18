

from pathlib import Path
from PyPDF2 import PdfReader


pasta_raiz = Path(__file__).parent
concursos_nova = pasta_raiz / 'Novacap.pdf'
concursos_brb = pasta_raiz / 'BRB.pdf'
arquivos_novos = pasta_raiz


reader = PdfReader(concursos_nova)
reader_brb = PdfReader(concursos_brb)

pages = reader.pages[44:46]
pages_brb = reader_brb.pages
cb = {}

for n, page in enumerate(pages_brb, start=1):
    paginas = page.extract_text()
    if 'CONHECIMENTOS GERAIS' in paginas:
        cb[f'pag{n}'] = paginas

print(cb)
