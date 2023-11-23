from random import choice, shuffle

class Jogador:
    def __init__(self, name, classe_Fav):
        """
        Forma de jogar:
        Ex:
        people = Jogador('David', 'Guerreiro')
        people.escolha_classe()
        people.jogar()
        Neste exemplo o people e apenas uma varialvel para acessar o jogo.
        """
        self.name = name
        self.classe_Fav = classe_Fav
 
    def dados(self):
        self.lista = {
    'mago': ['É frágil em combate físico', 'Usa cajado ou varinha', 'Tem alta inteligência e sabedoria', 'Usa magia', 'Começa com M'],

    'guerreiro': ['Usa armadura e armas pesadas', 'Possui alta resistência e vigor', 'É forte em combate físico', 'Tem habilidades de defesa e bloqueio', 'Tem baixa habilidade em magia'],
    
    'ladrao': ['É ágil e rápido', 'Usa adagas ou balestra', 'Tem habilidades de furtividade', 'Tem alta habilidade em abrir fechaduras', 'É fraco em combate corpo a corpo'],
    
    'paladino': ['Tem alta resistência e vigor', 'Tem habilidades de cura e proteção', 'Usa armadura pesada e armas divinas', 'É forte contra mortos-vivos/demonios', 'Imagem assemelha a um anjo'],
    
    'necromante': ['É frágil em combate físico', 'Usa magia negra', 'Pode controlar mortos-vivos', 'Geralmente do Mal', 'Nao é apenas um Mago'],
    
    'clerigo': ['Usa magia divina', 'Geralmente usa equipamentos de Ouro', 'É forte contra mortos-vivos/demonios', 'Possui alta resistência mágica', 'Figura lembra Padres/Pastores'],
    
    'barbaro': ['Usa armas brutais', 'Pode entrar em estado de fúria em combate', 'É forte em luta corpo a corpo', 'É fraco em combate à distância', 'Adora desafois de luta ate a morte'],
    
    'arqueiro': ['Usa arco/balestra,crosbow', 'Possui alta habilidade em acerto de precisão', 'Geralmente ligado a figura elfica', 'É frágil em combate corpo a corpo', 'Quase nao usa magia'],
    
    'cavaleiro': ['Possui habilidades de equitação', 'Geralmente utiliza escudo', 'Pode ter habilidades de cura e proteção', 'Otimo FrontLine', 'Possui alta resistência física'],
    
    'assassino': ['Usa armas leves para atacar furtivamente', 'Possui habilidades de disfarce', 'Figura ligada aos ladroes', 'Gosta de ver brigas e sangue', 'Tendem a andar em grupos'],
    
    'druida': ['Geralmente vivem mais de 100 anos', 'Pode transformar-se em animais', 'Usa magia da natureza', 'Tem alta inteligência', 'Tem afinidade com animais'],
    
    'pirata': ['Usa armas de longo alcance', 'É ágil e rápido', 'Tem habilidades de navegação', 'Adora um Rum', 'Figura lembra um marinheiro'],
    
    'samurai': ['É habilidoso com armas de corte', 'Possui alta habilidade em artes marciais', 'Tem alta resistência física', 'Geralmente segue um código de honra', 'Figura lembra um guerreiro japonês'],
    
    'vampiro': ['Possui habilidades sobrenaturais', 'Pode controlar a mente de outras pessoas', 'Usa habilidades de sangue', 'É frágil contra luz solar e objetos sagrados', 'Possui mais de 1000 anos em sua grande maioria'],
    
    'artesao': ['Tem habilidades de criação e reparo', 'Pode criar objetos mágicos', 'Geralmente é habilidoso em usar ferramentas', 'Tem alta inteligência', 'Lembrado por fazer esculturas magicas'],
    
    'arcanista': ['Utiliza runas e o proprio ser como base para atacar', 'Utiliza habilidades Arcanas', 'Geralmente é frágil fisicamente', 'Tem alta inteligência', 'Figura lembra um estudioso ou erudito'],
    
    'caçador': ['Usa armas de longo alcance', 'É habilidoso em rastrear', 'Pode ter habilidades de armadilhas', 'Tam altas habilidades em sobrevivencia', 'Otimo guia para florestas'],
    
    'alquimista': ['Tem habilidades de criação de poções e elixires', 'Pode ter habilidades de transmutação de objetos', 'Geralmente é inteligente e excêntrico', 'Pode usar armas químicas em combate', 'Figura lembra um cientista'],
    
    'monge': ['Possui habilidades avançadas em artes marciais', 'Geralmente é pacífico e meditativo', 'Tem alta resistência física', 'Pode ter habilidades de cura', 'Todos tem uma doutrina religiosa'],
    
    'ninja': ['Usa armas leves para atacar furtivamente', 'Tem habilidades de disfarce e de infiltrar-se em locais', 'Tem um foco muito grande em missoes', 'Tem alta habilidade em artes marciais', 'Figura lembra um assassino silencioso'],
    
    'bardo': ['Conhecido pelas suas musicas', 'Dado como um figura brincalhona', 'Geralmente utiliza instrumentos musicas como arma', 'Utiliza magia', 'Adora tavernas']
    
    }
        return self.lista

    def escolha_classe(self):
        """
        Funçao apenas escolhe alguma das classes na Funçao dados().
        self.escolha_classe = Seleciona aleatorio uma classe na Funçao dados().
        """
        self.escolha_classe = choice([n for n in self.dados().keys()])
        return self.escolha_classe

    def random_dica(self):
        """
        Funçao para randomizar as dicas, para nao se reptirem e terem a mesma ordem sempre.
        dicas = Lista com quantidade de dicas.
        todas_dicas = Lista com as dicas referente a Funçao escolha_classe, todas as dicas ramdomizadas.
        """
        dicas = [0, 1, 2, 3, 4]
        todas_dicas = []
        shuffle(dicas)
        for n in dicas:
            todas_dicas.append(self.dados()[self.escolha_classe][n])
        return todas_dicas

    def ler_letras(self):
        self.ler_letras = len(self.escolha_classe)
        return self.ler_letras

    def jogar(self):
        """
        Funçao principal do jogo.
        cont = Contagem das Dicas.
        cont_T = Contagem de Tentativas.
        dica_not_usadas = Sao todas as dicas refernte a Funçao dados() apor passar na Funçao random_dica().
        perg = Faz a Pergunta ao Jogador.
        """
        cont = cont_T = 0
        dica_not_usadas = self.random_dica()
        print(f'A Classe de RPG tem {self.ler_letras()} letras')
        while True:
            try:
                perg = str(input(f'Qual e a classe de RPG: ')).strip().lower()
                if perg == self.escolha_classe:
                    print(f'\033[1;31mParabens Carai...Voce acertou, a classe é \033[1;36m{(self.escolha_classe).upper()}\033[m')
                    break
                else:
                    print('Errou...')
                    dica = str(input('\nQuer uma Dica: [S/N] ')).upper()[0].strip()
                    if dica == 'S' and cont <= 4 :
                        print(f'\033[1;35m{dica_not_usadas[cont]}\033[m')
                        cont += 1
                        cont_T += 1
                    elif dica == 'S' and cont > 4:
                        print('\033[1;35mSuas dicas acabaram...\033[m')
                        cont_T += 1
                    elif dica == 'N':
                        print('Beleza, Boa sorte...')
                        cont_T += 1
                    if cont_T == 8:
                        print(f'\033[1;31mSuas chances acabaram, a classe era \033[1;36m{self.escolha_classe}\033[m')
                        break
            except (ValueError, TypeError):
                Interrupçao(x='', y=True)
                continue
            except (KeyboardInterrupt):
                Interrupaçao()
                break
