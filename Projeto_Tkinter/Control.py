from View import Create_visual
from View import View_Login
from View import View_Vendas
from View import View_Cadastro
import Model
import tkinter as tk
from tkinter import ttk

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
        dados = []
        for n in self.entrys:
            dados.append(n.get().upper().strip())
        return dados

    def Func_Validar_user(self):
        dados = self.Puxa_dados()
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
        from datetime import datetime
        data = datetime.now().strftime('%d/%m')
        return data

    def Limpar_entrys(self):
        import tkinter as tk
        # Limpa as Entrys da Tela Cadastro.
        for entry in self.entrys:
            entry.delete(0, tk.END)

    def Limpa_label5(self):
        variavel_local = self.Transform_frames(frame='.!frame2')
        for n in range(5,25):
            try: 
                if f'!label{n}' in variavel_local.children:
                    variavel_local = self.Transform_frames(f'.!frame2.!label{n}')
                    variavel_local.destroy()
                    break
                else:
                    break
            except Exception as error:
                print(f'Erro: {error}')
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
            self.frame_lista = self.cadastro.verificador_treeview(value='frame')
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

    def Processamento_dados(self):
        dados_1 = self.Puxa_dados()
        variavel_cod_venda = dados_1[0]
        dados_1.pop(0)
        if len(dados_1) == 3:
            if ',' in dados_1[1]:
                    alt = dados_1[1].replace(",", ".").strip()
                    dados_1[1] = alt
            if dados_1[0] == '' or dados_1[2] == '' or int(dados_1[0]) > 6:
                return [0, 0]
            if dados_1[1] == '':
                dados_1[1] = '0'
            return [dados_1, variavel_cod_venda]
        elif len(dados_1) == 4:
            if dados_1[0] == '' or dados_1[1] == '':
                return [0, 0]
            else:
                return [dados_1, variavel_cod_venda]
        else:
            print('Deu erro no process 1')   

    def Processamento_dados_venda(self, tipoFunc):
        dados_2, variavel_cod_venda = self.Processamento_dados()
        if dados_2 == 0 and variavel_cod_venda == 0:
            return [False, 0]
        else:
            dados_2.insert(1, self.vendas.Info_Cod_Produto(dados_2[0]))
            variavel_local = self.banco.Puxa_nome(dados_2[3])
            if variavel_local == False:
                return [False, 0]
            else:
                dados_2.append(self.banco.Puxa_nome(dados_2[3]))
                dados_2.append(self.Data())
                self.Limpa_label5()
                if tipoFunc == "add":
                    return [True, dados_2]
                elif tipoFunc == "alt" or tipoFunc == "del":
                    dados_2.append([variavel_cod_venda])
                    return [True, dados_2]

    def Processamento_dados_cadastro(self, tipoFunc):
        dados_2, variavel_cod_venda = self.Processamento_dados()
        if dados_2 == 0 and variavel_cod_venda == 0:
            return [False, 0]
        else:
            self.Limpa_label5
            if tipoFunc == "add":
                return [True, dados_2]
            elif tipoFunc == "alt" or tipoFunc == "del":
                dados_2.append([variavel_cod_venda])
                return [True, dados_2]

    def Atualiza_db_vendas(self, value):
        dados_v, dados = self.Processamento_dados_venda(value)
        treeview = '!frame3.!treeview'
        if dados_v == True:
            if value == 'add':
                self.banco.Adicionar_db_vendas(dados)
                self.Atualiza_TreeView(typTela='vendas', frame=treeview)
                self.Limpar_entrys()
            elif value == 'alt':
                self.banco.Alterar_db_vendas(dados)
                self.Atualiza_TreeView(typTela='vendas', frame=treeview)
                self.Limpar_entrys()
            elif value == 'del':
                self.banco.Apagar_db_vendas(dados)
                self.Atualiza_TreeView(typTela='vendas', frame=treeview)
                self.Limpar_entrys()
        else:
            self.create.Func_Erro_Dados(self.root, frase='Cod Produto ou cliente não Cadastrado')

    def Atualiza_db_cadastro(self, value):
        dados_v, dados = self.Processamento_dados_cadastro(value)
        treeview = self.cadastro.recebe_treeview()
        if dados_v == True:
            if value == 'add':
                self.banco.Adicionar_db_cadastro(dados)
                self.Atualiza_TreeView(frame=treeview)
                self.Limpar_entrys()
            elif value == 'alt':
                self.banco.Alterar_db_cadastro(dados)
                self.Atualiza_TreeView(frame=treeview)
                self.Limpar_entrys()
            elif value == 'del':
                self.banco.Apagar_db_cadastro(dados)
                self.Atualiza_TreeView(frame=treeview)
                self.Limpar_entrys()
        else:
            self.create.Func_Erro_Dados(self.root, frase='Cod Produto ou cliente não Cadastrado')

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
                  