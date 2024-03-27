from View import Create_visual
from View import View_Login
from View import View_Vendas
from View import View_Cadastro
import Model
import tkinter as tk
from tkinter import ttk
from datetime import datetime

class Control():
    def __init__(self, root, entrys):
        self.root = root
        self.create = Create_visual.Create(self.root)
        self.vendas = View_Vendas.Infos_Vendas(self.root)
        self.banco = Model.Main_db(self.root)
        self.cadastro = View_Cadastro.Infos_Cadastro(self.root)
        self.entrys = entrys

    def Transform_frames(self, frame):
        frame = self.root.nametowidget(frame)
        return frame

    def Puxa_dados(self):
        dados = {}
        if len(self.entrys) == 4:
            dados = {
                'Cod Venda': self.entrys[0].get().upper().strip(),
                'Cod Produto': self.entrys[1].get().upper().strip(),
                'Valor' : self.entrys[2].get().upper().strip(),
                "Cod Cliente": self.entrys[3].get().upper().strip()
            }
        if len(self.entrys) == 5:
            dados = {
                'codigo': self.entrys[0].get().upper().strip(),
                'nome': self.entrys[1].get().upper().strip(),
                'telefone': self.entrys[2].get().upper().strip(),
                'endereco': self.entrys[3].get().upper().strip(),
                'cidade': self.entrys[4].get().upper().strip()
            }
        return dados

    def Func_Validar_user(self):
        dados = [[],[]]
        dados[0] = 'david'; dados[1] = '123'
        if not dados[0] and not dados[1]:
            self.create.Info_Labls_Login_Erro()
        else:
            if dados[0] == 'david' and dados[1] == '123':
                self.Transform_frames('!frame').destroy()
                self.vendas.Organiza_Funcs_Vendas()
            else:
                self.create.Info_Labls_Login_Erro()

    def Data(self):
        data = datetime.now().strftime('%d/%m')
        return data

    def Limpar_entrys(self):
        # Limpa as Entrys da Tela Cadastro.
        for entry in self.entrys:
            entry.delete(0, tk.END)

    def Limpa_label5(self, typlabel='.!frame2.!label'):
        valores = ['6','7','8','9','10']
        for n in valores:
            try:
                x = label + n
                frame = self.Transform_frames(x)
                if frame.winfo_exists():
                    frame.destroy()
                    break
                else:
                    break
            except Exception as err:
                print(f'Log: Label {err} já destruida')
                pass

    def Func_Criar_Treeview(self, typTela=''):
        # Funçao responsavel pela criação da lista e scroll.
        if typTela == 'vendas':
            self.frame_lista = self.Transform_frames(frame='.!frame3')
            self.Lista_Treeview = ttk.Treeview(
                self.frame_lista, height=3, column=(
                    "Cod PROD", "PRODUTO", "Qt PROD", "VALOR", "Cod CLIENTE", "NOME", "DATA"
                )
            )
        else:
            self.frame_lista = self.cadastro.verificador_treeview(typFrame='frame')
            self.Lista_Treeview = ttk.Treeview(
                self.frame_lista, height=3, column=("Cod CLIENTE", "NOME", "TELEFONE", "EENDEREÇO", "CIDADE")
            )
        self.scroolLista = tk.Scrollbar(self.frame_lista, orient="vertical")
        self.scroolLista.place(relx=0.97, rely=0.01, relwidth=0.016, relheight=0.96)
        self.Lista_Treeview.configure(yscroll=self.scroolLista.set)
        self.Lista_Treeview.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.96)
        self.Lista_Treeview.bind("<Double-1>", self.Func_Double_Click)

    def Func_Double_Click(self, event=None):
        selection = self.Lista_Treeview.selection()
        item = self.Lista_Treeview.item(selection[0], "values")
        if len(item) == 7:
            lista = []
            for info in item:
                lista.append(info)
            lista.pop(2); lista.pop(); lista.pop()
            if 'R$ ' in lista[2]:
                alt = lista[2].replace('R$ ', ' ').strip()
                lista[2] = alt
            for entry, value in zip(self.entrys, lista):
                entry.insert(tk.END, value)
        else:
            lista = []
            for info in item:
                lista.append(info)
            for entry, value in zip(self.entrys, lista):
                entry.insert(tk.END, value)

    def Atualiza_TreeView(self, frame, typTela=''):
        # Atualiza a lista
        self.Lista_Treeview = self.Transform_frames(frame)
        self.Lista_Treeview.delete(*self.Lista_Treeview.get_children())
        for row in self.banco.Func_Select_Lista(typTela):
            if typTela == 'vendas':
                self.Lista_Treeview.insert(
                    "", tk.END, values=(row[0],f"{row[1]:0>3}",row[2],
                            (f"R$ {row[3]:.2f}"),row[4], row[5],row[6])
                )
            else:
                self.Lista_Treeview.insert(
                "", tk.END, values=(row[0], row[1], row[2], row[3], row[4])
                )

    def Processamento_dados_venda(self):
        try:    
            dados_vendas = self.Puxa_dados()
            if dados_vendas['Valor'] == '':
                dados_vendas['Valor'] = '0'
            if ',' in dados_vendas['Valor']:
                alt = dados_vendas['Valor'].replace(',', '.').strip()
                dados_vendas['Valor'] = alt
            if dados_vendas['Cod Produto'] == '' or int(dados_vendas['Cod Produto']) > 6:
                return [False, 0]
            if dados_vendas['Cod Cliente'] == '':
                return [False, 0]
            dados_vendas['Nome Produto'] = self.vendas.Info_Cod_Produto(dados_vendas['Cod Produto'])
            if bool(self.banco.Puxa_nome(dados_vendas['Cod Cliente'])):
                dados_vendas['Nome Cliente'] = self.banco.Puxa_nome(dados_vendas['Cod Cliente'])
            else:
                return [False, 0]
            dados_vendas['Data'] = self.Data()
            return [True, dados_vendas]
        except Exception as err:
            print(f'Log: erro no Processamento de dados\n{err}')

    def Processamento_dados_cadastro(self):
        dados_cadastro = self.Puxa_dados()
        if dados_cadastro['nome'] == '' and dados_cadastro['telefone'] == '':
            return [False, 0]
        if dados_cadastro['endereco'] == '':
            dados_cadastro['endereco'] = 'ENDEREÇO NÃO INSERIDO'
        if dados_cadastro['cidade'] == '':
            dados_cadastro['cidade'] = 'CIDADE NÃO INSERIDA'
        return [True, dados_cadastro]

    def buscar_cadastro(self):
        self.Lista_Treeview.delete(*self.Lista_Treeview.get_children())
        buscar_dados = self.Puxa_dados()
        coluna = '' ; pesquisa = 'nome'
        for info in buscar_dados.keys():
            if buscar_dados[info] != '':
                coluna = info
                pesquisa = f'{buscar_dados[info]}%'
        dados = self.banco.buscar_db_cadastro(coluna=coluna, pesquisa=pesquisa)
        print(dados)

    def Atualiza_db_vendas(self, typFunc):
        verificador, dados = self.Processamento_dados_venda()
        treeview = '!frame3.!treeview'
        if verificador == True:
            if typFunc == 'add':
                self.banco.Adicionar_db_vendas(dados)
                self.Atualiza_TreeView(typTela='vendas', frame=treeview)
                self.Limpar_entrys()
            elif typFunc == 'alt':
                self.banco.Alterar_db_vendas(dados)
                self.Atualiza_TreeView(typTela='vendas', frame=treeview)
                self.Limpar_entrys()
            elif typFunc == 'del':
                self.banco.Apagar_db_vendas(dados)
                self.Atualiza_TreeView(typTela='vendas', frame=treeview)
                self.Limpar_entrys()
        else:
            self.create.Func_Erro_Dados(self.root, frase='Cod Produto ou cliente não Cadastrado')

    def Atualiza_db_cadastro(self, typFunc):
        dados_v, dados = self.Processamento_dados_cadastro()
        treeview = self.cadastro.recebe_treeview()
        if dados_v == True:
            if typFunc == 'add':
                self.banco.Adicionar_db_cadastro(dados)
                self.Atualiza_TreeView(frame=treeview)
                self.Limpar_entrys()
                self.Limpa_label5(typlabel='!.toplevel.!frame.!label')
            elif typFunc == 'alt':
                self.banco.Alterar_db_cadastro(dados)
                self.Atualiza_TreeView(frame=treeview)
                self.Limpar_entrys()
                self.Limpa_label5(typlabel='!.toplevel.!frame.!label')
            elif typFunc == 'del':
                self.banco.Apagar_db_cadastro(dados)
                self.Atualiza_TreeView(frame=treeview)
                self.Limpar_entrys()
                self.Limpa_label5(typlabel='!.toplevel.!frame.!label')
        else:
            self.create.Func_Erro_Dados(
                self.root, frame='.!toplevel.!frame',frase='Cod Produto ou cliente não Cadastrado'
            )

    def vizualizador_widget(self):
        print('----------------------------------------------')
        def listar_widgets_ativos(root):
            for widget in root.winfo_children():
                print(f"Widget: {widget}")
                print(f"Ativo: {widget.winfo_exists()}")
                print("-----------")
                if widget.winfo_children():
                    listar_widgets_ativos(widget)
        listar_widgets_ativos(self.root)
                  